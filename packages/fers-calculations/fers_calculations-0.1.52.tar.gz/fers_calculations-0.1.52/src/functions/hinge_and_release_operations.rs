use crate::models::members::memberhinge::{AxisMode, MemberHinge};
use nalgebra::DMatrix;

fn submatrix_by_indices(k: &DMatrix<f64>, rows: &[usize], cols: &[usize]) -> DMatrix<f64> {
    let mut out = DMatrix::<f64>::zeros(rows.len(), cols.len());
    for (i_out, &i_in) in rows.iter().enumerate() {
        for (j_out, &j_in) in cols.iter().enumerate() {
            out[(i_out, j_out)] = k[(i_in, j_in)];
        }
    }
    out
}

/// Utility: selection/embedding matrix P (size: n_full × n_keep)
fn selection_matrix(n_full: usize, keep: &[usize]) -> DMatrix<f64> {
    let mut p = DMatrix::<f64>::zeros(n_full, keep.len());
    for (j, &i_full) in keep.iter().enumerate() {
        p[(i_full, j)] = 1.0;
    }
    p
}

/// Local 12-DOF index helper.
/// Local ordering: [uX,uY,uZ,thX,thY,thZ]_A, then [uX,uY,uZ,thX,thY,thZ]_B
fn local_dof_index(is_end_b: bool, is_rot: bool, axis: usize) -> usize {
    let base = if is_end_b { 6 } else { 0 };
    if is_rot {
        base + 3 + axis
    } else {
        base + axis
    }
}

/// Convert Option<f64> to AxisMode (Rigid / Release / Spring(k))
pub fn axis_mode_from_option(value: Option<f64>) -> AxisMode {
    match value {
        None => AxisMode::Rigid,
        Some(k) if k > 0.0 => AxisMode::Spring(k),
        Some(_) => AxisMode::Release,
    }
}

/// Per-end modes (LOCAL axes) directly from hinges.
/// Returns (A_trans, A_rot, B_trans, B_rot).
pub fn modes_from_single_ends(
    a: Option<&MemberHinge>,
    b: Option<&MemberHinge>,
) -> ([AxisMode; 3], [AxisMode; 3], [AxisMode; 3], [AxisMode; 3]) {
    let (vx_a, vy_a, vz_a, mx_a, my_a, mz_a) = a
        .map(|h| {
            (
                h.translational_release_vx,
                h.translational_release_vy,
                h.translational_release_vz,
                h.rotational_release_mx,
                h.rotational_release_my,
                h.rotational_release_mz,
            )
        })
        .unwrap_or((None, None, None, None, None, None));

    let (vx_b, vy_b, vz_b, mx_b, my_b, mz_b) = b
        .map(|h| {
            (
                h.translational_release_vx,
                h.translational_release_vy,
                h.translational_release_vz,
                h.rotational_release_mx,
                h.rotational_release_my,
                h.rotational_release_mz,
            )
        })
        .unwrap_or((None, None, None, None, None, None));

    let a_trans = [
        axis_mode_from_option(vx_a),
        axis_mode_from_option(vy_a),
        axis_mode_from_option(vz_a),
    ];
    let a_rot = [
        axis_mode_from_option(mx_a),
        axis_mode_from_option(my_a),
        axis_mode_from_option(mz_a),
    ];
    let b_trans = [
        axis_mode_from_option(vx_b),
        axis_mode_from_option(vy_b),
        axis_mode_from_option(vz_b),
    ];
    let b_rot = [
        axis_mode_from_option(mx_b),
        axis_mode_from_option(my_b),
        axis_mode_from_option(mz_b),
    ];

    (a_trans, a_rot, b_trans, b_rot)
}

/// Apply end releases and semi-rigid springs to a LOCAL 12x12 beam stiffness.
/// Static condensation on the released DOFs (with optional node-to-ground spring).
pub fn apply_end_releases_to_local_beam_k(
    k_local_in: &DMatrix<f64>, // 12x12
    a_trans: [AxisMode; 3],
    a_rot: [AxisMode; 3],
    b_trans: [AxisMode; 3],
    b_rot: [AxisMode; 3],
) -> Result<DMatrix<f64>, String> {
    if k_local_in.nrows() != 12 || k_local_in.ncols() != 12 {
        return Err("apply_end_releases_to_local_beam_k: matrix must be 12x12".to_string());
    }

    // Collect all non-rigid interface DOFs (Release -> k=0, Spring(k) -> k>0)
    let mut elim_idx: Vec<usize> = Vec::new();
    let mut kdiag: Vec<f64> = Vec::new();

    let mut consider = |is_end_b: bool, is_rot: bool, modes: [AxisMode; 3]| {
        for (axis, mode) in modes.iter().enumerate() {
            let idx = local_dof_index(is_end_b, is_rot, axis);
            match *mode {
                AxisMode::Rigid => { /* keep */ }
                AxisMode::Release => {
                    elim_idx.push(idx);
                    kdiag.push(0.0);
                }
                AxisMode::Spring(kval) => {
                    elim_idx.push(idx);
                    kdiag.push(kval.max(0.0));
                }
            }
        }
    };

    consider(false, false, a_trans);
    consider(false, true, a_rot);
    consider(true, false, b_trans);
    consider(true, true, b_rot);

    if elim_idx.is_empty() {
        return Ok(k_local_in.clone());
    }

    use std::collections::HashSet;
    let elim_set: HashSet<usize> = elim_idx.iter().copied().collect();
    let keep_idx: Vec<usize> = (0..12).filter(|i| !elim_set.contains(i)).collect();

    let k_kk = submatrix_by_indices(k_local_in, &keep_idx, &keep_idx);
    let k_kr = submatrix_by_indices(k_local_in, &keep_idx, &elim_idx);
    let k_rk = submatrix_by_indices(k_local_in, &elim_idx, &keep_idx);
    let mut k_rr = submatrix_by_indices(k_local_in, &elim_idx, &elim_idx);

    // interface spring on eliminated block
    for i in 0..k_rr.nrows() {
        k_rr[(i, i)] += kdiag[i];
    }

    // K_eff = K_kk − K_kr (K_rr)^{-1} K_rk
    let x = k_rr.clone().lu().solve(&k_rk).ok_or_else(|| {
        "apply_end_releases_to_local_beam_k: (K_rr + diag(k)) is singular".to_string()
    })?;
    let k_eff = &k_kk - &(k_kr * x);

    let p = selection_matrix(12, &keep_idx);
    Ok(&p * k_eff * p.transpose())
}

/// LOCAL 12x12 matrix for node-to-ground translational springs at ends A and B (trusses).
/// Only translations are considered; rotations are ignored.
pub fn build_local_truss_translational_spring_k(
    a_trans: [AxisMode; 3],
    b_trans: [AxisMode; 3],
) -> DMatrix<f64> {
    let mut k = DMatrix::<f64>::zeros(12, 12);

    for (axis, mode) in a_trans.iter().enumerate() {
        if let AxisMode::Spring(ka) = *mode {
            let i = local_dof_index(false, false, axis);
            k[(i, i)] += ka.max(0.0);
        }
    }

    for (axis, mode) in b_trans.iter().enumerate() {
        if let AxisMode::Spring(kb) = *mode {
            let i = local_dof_index(true, false, axis);
            k[(i, i)] += kb.max(0.0);
        }
    }

    k
}
