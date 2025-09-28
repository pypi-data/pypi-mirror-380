use std::collections::{BTreeMap, HashMap, HashSet};

use nalgebra::DMatrix;

use crate::models::fers::fers::FERS;
use crate::models::members::enums::MemberType;
use crate::models::results::forces::NodeForces;
use crate::models::results::reaction::{NodeLocation, ReactionNodeResult};
use crate::models::results::results::ResultType;
use crate::models::supports::nodalsupport::NodalSupport;
use crate::models::supports::supportconditiontype::SupportConditionType;

// -------------------------------------------------------------------------------------------------
// Public API
// -------------------------------------------------------------------------------------------------

/// Build reactions keyed by node_id. This handles multiple nodes sharing the same support_id.
pub fn extract_reaction_nodes(
    fers: &FERS,
    global_reaction_vector: &DMatrix<f64>,
) -> BTreeMap<u32, ReactionNodeResult> {
    let mut out: BTreeMap<u32, ReactionNodeResult> = BTreeMap::new();

    for ms in &fers.member_sets {
        for m in &ms.members {
            for n in [&m.start_node, &m.end_node] {
                if let Some(support_id) = n.nodal_support {
                    let node_id = n.id;
                    let dof0 = dof_index(node_id, 0);

                    let nodal_forces = NodeForces {
                        fx: global_reaction_vector[(dof0 + 0, 0)],
                        fy: global_reaction_vector[(dof0 + 1, 0)],
                        fz: global_reaction_vector[(dof0 + 2, 0)],
                        mx: global_reaction_vector[(dof0 + 3, 0)],
                        my: global_reaction_vector[(dof0 + 4, 0)],
                        mz: global_reaction_vector[(dof0 + 5, 0)],
                    };

                    out.insert(
                        node_id,
                        ReactionNodeResult {
                            nodal_forces,
                            location: node_location(fers, node_id),
                            support_id,
                        },
                    );
                }
            }
        }
    }

    out
}

/// Compose support reactions by **equilibrium per node**, not from residuals.
///
/// Algorithm:
/// 1) Sum deformable member end **forces and moments** into their end nodes.
/// 2) Add applied **nodal** loads and **nodal** moments (for the active result).
/// 3) Roll up wrenches along **rigid links**:
///        F_master += F_slave
///        M_master += M_slave + r × F_slave   with r = x_slave − x_master
/// 4) For each support DOF:
///        Fixed         → reaction = −(net node wrench component)
///        Spring        → reaction = k * value
///        Free          → 0
///        PositiveOnly  → clamp ≥ 0
///        NegativeOnly  → clamp ≤ 0
pub fn compose_support_reaction_vector_equilibrium(
    fers: &FERS,
    result_type: &ResultType,
    displacement_vector_full: &DMatrix<f64>,
    active_map: Option<&std::collections::HashMap<u32, bool>>,
) -> Result<DMatrix<f64>, String> {
    // 1) Deformable member end wrenches → nodes
    let deformable = deformable_member_ids(fers, active_map);
    let ends = member_end_node_map(fers);

    let member_results = crate::functions::results::compute_member_results_from_displacement(
        fers,
        result_type,
        displacement_vector_full,
        active_map,
    );

    let mut node_wrench: HashMap<u32, NodeWrench> = HashMap::new();
    for (mid, mr) in &member_results {
        if !deformable.contains(mid) {
            continue;
        }
        let Some(&(n_start, n_end)) = ends.get(mid) else {
            continue;
        };

        // Start end
        {
            let entry = node_wrench.entry(n_start).or_default();
            entry.add_force(
                -mr.start_node_forces.fx,
                -mr.start_node_forces.fy,
                -mr.start_node_forces.fz,
            );
            entry.add_moment(
                -mr.start_node_forces.mx,
                -mr.start_node_forces.my,
                -mr.start_node_forces.mz,
            );
        }
        // End end
        {
            let entry = node_wrench.entry(n_end).or_default();
            entry.add_force(
                -mr.end_node_forces.fx,
                -mr.end_node_forces.fy,
                -mr.end_node_forces.fz,
            );
            entry.add_moment(
                -mr.end_node_forces.mx,
                -mr.end_node_forces.my,
                -mr.end_node_forces.mz,
            );
        }
    }

    // 2) Applied **nodal** loads and moments
    let external_nodal = gather_external_nodal_wrenches_for_result_type(fers, result_type);
    for (nid, w) in external_nodal {
        node_wrench.entry(nid).or_default().add_wrench(&w);
    }

    // 3) Roll-up over rigid links
    roll_up_wrenches_via_rigid_links(fers, &mut node_wrench);

    // 4) Compose reactions per support DOF
    let total_dofs = compute_num_dofs(fers);
    let mut reaction_vector_full = DMatrix::<f64>::zeros(total_dofs, 1);

    // Spring contributions (k·u) computed explicitly here
    let spring_reaction_vector_full =
        compute_support_spring_reaction_vector_verbose(fers, displacement_vector_full)?;

    visit_unique_supported_nodes(fers, |node_id, base_index, support| {
        let w = node_wrench.get(&node_id).copied().unwrap_or_default();

        // Translations: X=0, Y=1, Z=2
        for (axis_label, local_dof) in [("X", 0usize), ("Y", 1usize), ("Z", 2usize)] {
            let comp_equil = -get_wrench_component(&w, local_dof);
            let value = match get_condition_type_case_insensitive(
                &support.displacement_conditions,
                axis_label,
            ) {
                Some(SupportConditionType::Free) => 0.0,
                Some(SupportConditionType::Spring) => {
                    spring_reaction_vector_full[(base_index + local_dof, 0)]
                }
                Some(SupportConditionType::PositiveOnly) => comp_equil.max(0.0),
                Some(SupportConditionType::NegativeOnly) => comp_equil.min(0.0),
                None | Some(SupportConditionType::Fixed) => comp_equil,
            };
            reaction_vector_full[(base_index + local_dof, 0)] = value;
        }

        // Rotations: RX=3, RY=4, RZ=5
        for (axis_label, local_dof) in [("X", 3usize), ("Y", 4usize), ("Z", 5usize)] {
            let comp_equil = -get_wrench_component(&w, local_dof);
            let value =
                match get_condition_type_case_insensitive(&support.rotation_conditions, axis_label)
                {
                    Some(SupportConditionType::Free) => 0.0,
                    Some(SupportConditionType::Spring) => {
                        spring_reaction_vector_full[(base_index + local_dof, 0)]
                    }
                    Some(SupportConditionType::PositiveOnly) => comp_equil.max(0.0),
                    Some(SupportConditionType::NegativeOnly) => comp_equil.min(0.0),
                    None | Some(SupportConditionType::Fixed) => comp_equil,
                };
            reaction_vector_full[(base_index + local_dof, 0)] = value;
        }

        Ok(())
    })?;

    Ok(reaction_vector_full)
}

// -------------------------------------------------------------------------------------------------
// Internal helpers (module-private)
// -------------------------------------------------------------------------------------------------

/// Simple wrench container for per-node force and moment
#[derive(Clone, Copy, Debug, Default)]
struct NodeWrench {
    fx: f64,
    fy: f64,
    fz: f64,
    mx: f64,
    my: f64,
    mz: f64,
}

impl NodeWrench {
    fn add_force(&mut self, fx: f64, fy: f64, fz: f64) {
        self.fx += fx;
        self.fy += fy;
        self.fz += fz;
    }
    fn add_moment(&mut self, mx: f64, my: f64, mz: f64) {
        self.mx += mx;
        self.my += my;
        self.mz += mz;
    }
    fn add_wrench(&mut self, other: &NodeWrench) {
        self.fx += other.fx;
        self.fy += other.fy;
        self.fz += other.fz;
        self.mx += other.mx;
        self.my += other.my;
        self.mz += other.mz;
    }
}

fn get_wrench_component(w: &NodeWrench, local_dof: usize) -> f64 {
    match local_dof {
        0 => w.fx,
        1 => w.fy,
        2 => w.fz,
        3 => w.mx,
        4 => w.my,
        5 => w.mz,
        _ => 0.0,
    }
}

fn cross_r_x_f(rx: f64, ry: f64, rz: f64, fx: f64, fy: f64, fz: f64) -> (f64, f64, f64) {
    // r × F
    let mx = ry * fz - rz * fy;
    let my = rz * fx - rx * fz;
    let mz = rx * fy - ry * fx;
    (mx, my, mz)
}

fn dof_index(node_id: u32, local_dof: usize) -> usize {
    (node_id as usize - 1) * 6 + local_dof
}

fn compute_num_dofs(fers: &FERS) -> usize {
    let max_node = fers
        .member_sets
        .iter()
        .flat_map(|ms| ms.members.iter())
        .flat_map(|m| [m.start_node.id, m.end_node.id])
        .max()
        .unwrap_or(0) as usize;
    max_node * 6
}

fn node_location(fers: &FERS, node_id: u32) -> NodeLocation {
    for ms in &fers.member_sets {
        for m in &ms.members {
            if m.start_node.id == node_id {
                return NodeLocation {
                    X: m.start_node.X,
                    Y: m.start_node.Y,
                    Z: m.start_node.Z,
                };
            }
            if m.end_node.id == node_id {
                return NodeLocation {
                    X: m.end_node.X,
                    Y: m.end_node.Y,
                    Z: m.end_node.Z,
                };
            }
        }
    }
    NodeLocation {
        X: 0.0,
        Y: 0.0,
        Z: 0.0,
    }
}

fn deformable_member_ids(
    fers: &FERS,
    active_map: Option<&std::collections::HashMap<u32, bool>>,
) -> std::collections::HashSet<u32> {
    use crate::models::members::enums::MemberType;
    let mut ids = std::collections::HashSet::new();
    for ms in &fers.member_sets {
        for m in &ms.members {
            match m.member_type {
                MemberType::Rigid => {} // never deformable
                MemberType::Tension | MemberType::Compression => {
                    // include only if active (tie/strut logic)
                    if active_map
                        .and_then(|mmap| mmap.get(&m.id))
                        .copied()
                        .unwrap_or(true)
                    {
                        ids.insert(m.id);
                    }
                }
                _ => {
                    ids.insert(m.id);
                }
            }
        }
    }
    ids
}

fn member_end_node_map(fers: &FERS) -> HashMap<u32, (u32, u32)> {
    let mut map = HashMap::new();
    for ms in &fers.member_sets {
        for m in &ms.members {
            map.insert(m.id, (m.start_node.id, m.end_node.id));
        }
    }
    map
}

/// Gather applied nodal loads and nodal moments for the active ResultType.
/// Distributed loads are already represented through member end forces.
fn gather_external_nodal_wrenches_for_result_type(
    fers: &FERS,
    result_type: &ResultType,
) -> HashMap<u32, NodeWrench> {
    let mut out: HashMap<u32, NodeWrench> = HashMap::new();

    // Helper to add a single case with factor
    let mut add_case = |case_id: u32, factor: f64| {
        if let Some(lc) = fers.load_cases.iter().find(|c| c.id == case_id) {
            // nodal loads → forces
            for nl in &lc.nodal_loads {
                let e = out.entry(nl.node).or_default();
                e.add_force(
                    factor * nl.direction.0 as f64 * nl.magnitude,
                    factor * nl.direction.1 as f64 * nl.magnitude,
                    factor * nl.direction.2 as f64 * nl.magnitude,
                );
            }
            // nodal moments → moments
            for nm in &lc.nodal_moments {
                let e = out.entry(nm.node).or_default();
                e.add_moment(
                    factor * nm.direction.0 as f64 * nm.magnitude,
                    factor * nm.direction.1 as f64 * nm.magnitude,
                    factor * nm.direction.2 as f64 * nm.magnitude,
                );
            }
        }
    };

    match result_type {
        ResultType::Loadcase(id) => add_case(*id, 1.0),
        ResultType::Loadcombination(cid) => {
            if let Some(combo) = fers
                .load_combinations
                .iter()
                .find(|lc| lc.load_combination_id == *cid)
            {
                for (case_id, factor) in &combo.load_cases_factors {
                    add_case(*case_id, *factor);
                }
            }
        }
    }

    out
}

/// Look up a condition case-insensitively in a per-axis map like `displacement_conditions`.
fn get_condition_type_case_insensitive(
    map: &BTreeMap<String, crate::models::supports::supportcondition::SupportCondition>,
    axis: &str,
) -> Option<SupportConditionType> {
    if let Some(c) = map.get(axis) {
        return Some(c.condition_type.clone());
    }
    let lower = axis.to_ascii_lowercase();
    map.get(&lower).map(|c| c.condition_type.clone())
}

/// Compute spring reactions vector (k · dof_value) at support DOFs only.
fn compute_support_spring_reaction_vector_verbose(
    fers: &FERS,
    displacement_vector_full: &DMatrix<f64>,
) -> Result<DMatrix<f64>, String> {
    let total_dofs = compute_num_dofs(fers);
    let mut spring_vec = DMatrix::<f64>::zeros(total_dofs, 1);

    visit_unique_supported_nodes(fers, |_node_id, base_index, support| {
        // Translational springs
        for (axis_label, local_dof) in [("X", 0usize), ("Y", 1usize), ("Z", 2usize)] {
            if let Some(typ) =
                get_condition_type_case_insensitive(&support.displacement_conditions, axis_label)
            {
                if let SupportConditionType::Spring = typ {
                    let k = spring_stiffness_or_error(
                        support,
                        axis_label,
                        "displacement",
                        support
                            .displacement_conditions
                            .get(axis_label)
                            .or_else(|| {
                                support
                                    .displacement_conditions
                                    .get(&axis_label.to_ascii_lowercase())
                            })
                            .and_then(|c| c.stiffness),
                    )?;
                    let u = displacement_vector_full[(base_index + local_dof, 0)];
                    spring_vec[(base_index + local_dof, 0)] += k * u;
                }
            }
        }
        // Rotational springs
        for (axis_label, local_dof) in [("X", 3usize), ("Y", 4usize), ("Z", 5usize)] {
            if let Some(typ) =
                get_condition_type_case_insensitive(&support.rotation_conditions, axis_label)
            {
                if let SupportConditionType::Spring = typ {
                    let k = spring_stiffness_or_error(
                        support,
                        axis_label,
                        "rotation",
                        support
                            .rotation_conditions
                            .get(axis_label)
                            .or_else(|| {
                                support
                                    .rotation_conditions
                                    .get(&axis_label.to_ascii_lowercase())
                            })
                            .and_then(|c| c.stiffness),
                    )?;
                    let r = displacement_vector_full[(base_index + local_dof, 0)];
                    spring_vec[(base_index + local_dof, 0)] += k * r;
                }
            }
        }
        Ok(())
    })?;

    Ok(spring_vec)
}

/// Iterate each **unique supported node** once, yielding (node_id, base_dof_index, &NodalSupport)
fn visit_unique_supported_nodes<F>(fers: &FERS, mut visitor: F) -> Result<(), String>
where
    F: FnMut(u32, usize, &NodalSupport) -> Result<(), String>,
{
    let support_by_id: HashMap<u32, &NodalSupport> =
        fers.nodal_supports.iter().map(|s| (s.id, s)).collect();

    let mut seen: HashSet<u32> = HashSet::new();

    for member_set in &fers.member_sets {
        for member in &member_set.members {
            for node in [&member.start_node, &member.end_node] {
                if !seen.insert(node.id) {
                    continue;
                }
                if let Some(support_id) = node.nodal_support {
                    if let Some(support) = support_by_id.get(&support_id) {
                        let base_index = dof_index(node.id, 0);
                        visitor(node.id, base_index, *support)?;
                    }
                }
            }
        }
    }
    Ok(())
}

fn spring_stiffness_or_error(
    support: &NodalSupport,
    axis_label: &str,
    kind_label: &str,
    stiffness: Option<f64>,
) -> Result<f64, String> {
    let k = stiffness.ok_or_else(|| {
        format!(
            "Support {} {} {} is Spring but stiffness is missing.",
            support.id, kind_label, axis_label
        )
    })?;
    if k <= 0.0 {
        return Err(format!(
            "Support {} {} {} Spring stiffness must be positive.",
            support.id, kind_label, axis_label
        ));
    }
    Ok(k)
}

/// Roll wrenches up rigid links: move child (slave) node wrench to master:
/// F_master += F_slave ; M_master += M_slave + r × F_slave
fn roll_up_wrenches_via_rigid_links(fers: &FERS, node_wrench: &mut HashMap<u32, NodeWrench>) {
    // slave -> (master, r = x_b − x_a)
    let mut parent: HashMap<u32, (u32, (f64, f64, f64))> = HashMap::new();
    let mut edges: Vec<(u32, u32, (f64, f64, f64))> = Vec::new();

    for ms in &fers.member_sets {
        for m in &ms.members {
            if !matches!(m.member_type, MemberType::Rigid) {
                continue;
            }
            let a = m.start_node.id;
            let b = m.end_node.id;
            let r = (
                m.end_node.X - m.start_node.X,
                m.end_node.Y - m.start_node.Y,
                m.end_node.Z - m.start_node.Z,
            );
            parent.insert(b, (a, r));
            edges.push((a, b, r));
        }
    }

    fn depth_of(node: u32, parent: &HashMap<u32, (u32, (f64, f64, f64))>) -> usize {
        let mut d = 0usize;
        let mut p = node;
        while let Some(&(pp, _)) = parent.get(&p) {
            d += 1;
            p = pp;
        }
        d
    }

    // Process deepest slaves first so we fold chains correctly
    edges.sort_by_key(|&(_a, b, _)| std::cmp::Reverse(depth_of(b, &parent)));

    for (a, b, (rx, ry, rz)) in edges {
        let wb = node_wrench.remove(&b).unwrap_or_default();
        if wb.fx == 0.0
            && wb.fy == 0.0
            && wb.fz == 0.0
            && wb.mx == 0.0
            && wb.my == 0.0
            && wb.mz == 0.0
        {
            continue;
        }
        let (d_mx, d_my, d_mz) = cross_r_x_f(rx, ry, rz, wb.fx, wb.fy, wb.fz);
        let wa = node_wrench.entry(a).or_default();
        wa.add_force(wb.fx, wb.fy, wb.fz);
        wa.add_moment(wb.mx + d_mx, wb.my + d_my, wb.mz + d_mz);
    }
}
