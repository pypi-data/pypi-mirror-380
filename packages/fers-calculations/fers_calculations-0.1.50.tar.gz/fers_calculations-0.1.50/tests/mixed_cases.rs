#[path = "test_support/mod.rs"]
mod test_support;

use fers_calculations::models::supports::supportconditiontype::SupportConditionType;
use test_support::formulas::*;
use test_support::helpers::*;
use test_support::*;

#[test]
fn test_041_rigid_member_end_load() {
    let mut model = make_fers();

    let mat_id = add_material_s235(&mut model, 1);
    let sec_id = add_section_ipe180_like(&mut model, 1, mat_id, SECOND_MOMENT_STRONG_AXIS_IN_M4);

    // Fixed at node 1
    model.nodal_supports.push(make_fixed_support(1));

    let length_elastic = 5.0_f64;
    let length_rigid = 5.0_f64;
    let force_newton = 1000.0_f64;
    let r_x = length_rigid;

    let n1 = make_node(1, 0.0, 0.0, 0.0, Some(1));
    let n2 = make_node(2, length_elastic, 0.0, 0.0, None);
    let n3 = make_node(3, length_elastic + length_rigid, 0.0, 0.0, None);

    let m_el = make_beam_member(1, &n1, &n2, sec_id);
    let m_rg = make_rigid_member(2, &n2, &n3);
    add_member_set(&mut model, 1, vec![m_el, m_rg]);

    let lc_id = add_load_case(&mut model, 1, "End Load");
    add_nodal_load(&mut model, 1, lc_id, 2, force_newton, (0.0, -1.0, 0.0));

    model.solve_for_load_case(lc_id).expect("Analysis failed");

    let res = model
        .results
        .as_ref()
        .unwrap()
        .loadcases
        .get("End Load")
        .unwrap();

    let dy_2 = res.displacement_nodes.get(&2).unwrap().dy;
    let dy_3 = res.displacement_nodes.get(&3).unwrap().dy;
    let rz_2 = res.displacement_nodes.get(&2).unwrap().rz;
    let rz_3 = res.displacement_nodes.get(&3).unwrap().rz;
    let mz_1 = res.reaction_nodes.get(&1).unwrap().nodal_forces.mz;

    let steel_e = 210.0e9_f64;
    let dy_expected = cantilever_end_point_load_deflection_at_free_end(
        force_newton,
        length_elastic,
        steel_e,
        SECOND_MOMENT_STRONG_AXIS_IN_M4,
    );
    let mz_expected =
        cantilever_end_point_load_fixed_end_moment_magnitude(force_newton, length_elastic);
    let rz_expected =
        -force_newton * length_elastic.powi(2) / (2.0 * steel_e * SECOND_MOMENT_STRONG_AXIS_IN_M4);

    assert_close(dy_2, dy_expected, TOL_ABSOLUTE_DISPLACEMENT_IN_METER);
    assert_close(mz_1.abs(), mz_expected, TOL_ABSOLUTE_MOMENT_IN_NEWTON_METER);

    assert!((rz_2 - rz_3).abs() < TOL_ABSOLUTE_ROTATION_IN_RADIAN);
    assert!((rz_2 - rz_expected).abs() < TOL_ABSOLUTE_ROTATION_IN_RADIAN);

    assert_close(dy_3, dy_2 + rz_2 * r_x, TOL_ABSOLUTE_DISPLACEMENT_IN_METER);
}

#[test]
fn test_061_two_colinear_tension_only_members_with_mid_load() {
    let mut model = make_fers();

    let mat_id = add_material_s235(&mut model, 1);
    let sec_id = add_section_ipe180_like(&mut model, 1, mat_id, SECOND_MOMENT_STRONG_AXIS_IN_M4);

    // Node 1 fixed, Node 3 fixed, Node 2: X free, Y fixed, Z fixed; rotations all fixed for safety.
    model.nodal_supports.push(make_fixed_support(1));
    model.nodal_supports.push(make_support_custom(
        2,
        SupportConditionType::Free,  // Ux
        SupportConditionType::Fixed, // Uy
        SupportConditionType::Fixed, // Uz
        SupportConditionType::Fixed, // Rx
        SupportConditionType::Fixed, // Ry
        SupportConditionType::Fixed, // Rz
    ));
    model.nodal_supports.push(make_fixed_support(3));

    let member_length = 2.5_f64;
    let n1 = make_node(1, 0.0, 0.0, 0.0, Some(1));
    let n2 = make_node(2, member_length, 0.0, 0.0, Some(2));
    let n3 = make_node(3, 2.0 * member_length, 0.0, 0.0, Some(3));

    let m_left = make_tension_only_member(1, &n1, &n2, sec_id);
    let m_right = make_tension_only_member(2, &n2, &n3, sec_id);
    add_member_set(&mut model, 1, vec![m_left, m_right]);

    let lc_id = add_load_case(&mut model, 1, "Mid Load");
    add_nodal_load(&mut model, 1, lc_id, 2, 1.0_f64, (1.0, 0.0, 0.0));

    model.solve_for_load_case(lc_id).expect("Analysis failed");

    let res = model
        .results
        .as_ref()
        .unwrap()
        .loadcases
        .get("Mid Load")
        .unwrap();

    let dx_2 = res.displacement_nodes.get(&2).unwrap().dx;
    let fx_1 = res.reaction_nodes.get(&1).unwrap().nodal_forces.fx;
    let fx_3 = res.reaction_nodes.get(&3).unwrap().nodal_forces.fx;

    let e = 210.0e9_f64;
    let area = 26.2e-4_f64;
    let expected_dx_2 = 1.0_f64 * member_length / (area * e);

    assert_close(dx_2, expected_dx_2, TOL_ABSOLUTE_DISPLACEMENT_IN_METER);
    assert!((fx_1 - (-1.0_f64)).abs() < TOL_ABSOLUTE_FORCE_IN_NEWTON);
    assert!(fx_3.abs() < TOL_ABSOLUTE_FORCE_IN_NEWTON);
}
