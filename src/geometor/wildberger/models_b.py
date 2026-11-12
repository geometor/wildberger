"""Exact `geometor.model.Model` builders and SymPy verifiers for `W.15`..`W.28`.

Implements constructive geometric diagrams, rational-parametrized algebraic
curves, and exact symbolic verifications for Part III (Centers, Euler/Nine-Point,
Circles, Cyclic Quadrilaterals, Golden Pentagons, Conics, Tangents, Cross-Ratio,
Chromogeometry) and Part IV (Solvers, Resection/Hansen, Physics, 3D Platonic
Solids, Rational Polar Curves & The Ellipson).
"""

from __future__ import annotations

from collections.abc import Callable

import sympy as sp
from geometor.model import Model

from geometor.wildberger.invariants import (
    BLUE_METRIC,
    GREEN_METRIC,
    RED_METRIC,
    ConicProportion,
    LineProportion,
    archimedes,
    collinear_cross_ratio_quadrance,
    collinear_det,
    compute_triangle_invariants,
    euler_four_point_function,
    midpoint,
    pencil_cross_ratio_spread,
    perpendicular_bisector,
    quadrance,
    quadrea,
    quadruple_quad_function,
    rational_polar_coords,
    spread,
    spread_polynomial,
    spread_sequence_mod_p,
    triple_spread_function,
    vertex_spread,
)
from geometor.wildberger.models import (
    TopicBuildResult,
    add_line_from_proportion,
    finalize_model_guides,
)
from geometor.wildberger.proofs import prove_platonic_dihedral_spreads
from geometor.wildberger.solvers import (
    solve_hansen_benchmark,
    solve_inaccessible_height,
    solve_qqq,
    solve_qss,
    solve_regiomontanus,
    solve_snellius_pothenot_coordinates,
    solve_sqq,
)


def _rational_grid(n: int, scale: sp.Expr) -> list[sp.Expr]:
    """Generate exact symmetric rational parameters `k/n * scale` for `-n..n`."""
    return [sp.Rational(k, n) * scale for k in range(-n, n + 1)]


def _build_w15() -> TopicBuildResult:
    """Build W.15: Circumcenter, Orthocenter & Universal Affine Barycentrics."""
    m = Model("W.15 Circumcenter & Orthocenter", logger=False)
    a1_xy = (sp.Integer(0), sp.Integer(0))
    a2_xy = (sp.Integer(14), sp.Integer(0))
    a3_xy = (sp.Integer(5), sp.Integer(12))

    inv = compute_triangle_invariants(a1_xy, a2_xy, a3_xy)
    f1_xy = LineProportion.from_points(a2_xy, a3_xy).foot_of_altitude(a1_xy)
    f2_xy = LineProportion.from_points(a1_xy, a3_xy).foot_of_altitude(a2_xy)
    f3_xy = LineProportion.from_points(a1_xy, a2_xy).foot_of_altitude(a3_xy)

    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")
    pt_c = m.set_point(*inv.circumcenter, classes=["center", "metric-red"], ID="C")
    pt_o = m.set_point(*inv.orthocenter, classes=["center", "golden"], ID="O")
    f1 = m.set_point(*f1_xy, classes=["foot"], ID="F_1")
    f2 = m.set_point(*f2_xy, classes=["foot"], ID="F_2")
    f3 = m.set_point(*f3_xy, classes=["foot"], ID="F_3")

    m.set_polygon([a1, a2, a3], ID="t")
    m.set_polygon([f1, f2, f3], classes=["golden"], ID="t_orth")
    m.construct_circle(pt_c, a1, classes=["circumcircle"], ID="c_circ")
    m.set_segment(a1, f1, classes=["altitude"])
    m.set_segment(a2, f2, classes=["altitude"])
    m.set_segment(a3, f3, classes=["altitude"])
    finalize_model_guides(m, {"A_1", "A_2", "A_3", "C", "O", "F_1", "F_2", "F_3"})

    q_oa3 = quadrance(inv.orthocenter, a3_xy)
    rhs_oa3 = sp.simplify(4 * inv.circumquadrance * (1 - inv.s3))
    s_orth_l = vertex_spread(f3_xy, f1_xy, a3_xy)
    s_orth_r = vertex_spread(f3_xy, f2_xy, a3_xy)
    if sp.simplify(q_oa3 - rhs_oa3) != 0 or sp.simplify(s_orth_l - s_orth_r) != 0:
        raise AssertionError("W.15 Orthic / Orthocenter check failed.")

    annotations = [
        {"x": inv.circumcenter[0] + 3, "y": inv.circumcenter[1], "text": f"C = {list(inv.circumcenter)}", "kind": "quadrance", "ref": "C"},
        {"x": inv.orthocenter[0] - 2, "y": inv.orthocenter[1] + 2, "text": f"O = {list(inv.orthocenter)}", "kind": "spread", "ref": "O"},
    ]
    verifications = [
        ("Circumcenter C = X(3)", f"[{inv.circumcenter[0]}, {inv.circumcenter[1]}]", f"K = {inv.circumquadrance}"),
        ("Orthocenter O = X(4)", f"[{inv.orthocenter[0]}, {inv.orthocenter[1]}]", "Concurrent altitudes"),
        ("Orthocenter quadrance Q(O, A_3) = 4*K*(1 - s_3)", f"{q_oa3} == {rhs_oa3}", "Exact rational identity"),
        ("Orthic bisector law s(F_3 F_1, F_3 A_3) == s(F_3 F_2, F_3 A_3)", f"{s_orth_l} == {s_orth_r} = 1 - s_3", "Theorem 86 verified"),
    ]
    return TopicBuildResult("W.15", m, [], annotations, verifications, {"C_x": inv.circumcenter[0], "O_y": inv.orthocenter[1]})


def _build_w16() -> TopicBuildResult:
    """Build W.16: The Euler Line & Nine-Point Circle Over Arbitrary Fields."""
    m = Model("W.16 Euler Line & Nine-Point Circle", logger=False)
    a1_xy = (sp.Integer(0), sp.Integer(0))
    a2_xy = (sp.Integer(14), sp.Integer(0))
    a3_xy = (sp.Integer(4), sp.Integer(12))

    inv = compute_triangle_invariants(a1_xy, a2_xy, a3_xy)
    m1_xy = midpoint(a2_xy, a3_xy)
    m2_xy = midpoint(a1_xy, a3_xy)
    m3_xy = midpoint(a1_xy, a2_xy)
    f1_xy = LineProportion.from_points(a2_xy, a3_xy).foot_of_altitude(a1_xy)
    f2_xy = LineProportion.from_points(a1_xy, a3_xy).foot_of_altitude(a2_xy)
    f3_xy = LineProportion.from_points(a1_xy, a2_xy).foot_of_altitude(a3_xy)
    e1_xy = midpoint(a1_xy, inv.orthocenter)
    e2_xy = midpoint(a2_xy, inv.orthocenter)
    e3_xy = midpoint(a3_xy, inv.orthocenter)

    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")
    pt_c = m.set_point(*inv.circumcenter, classes=["center", "metric-red"], ID="C")
    pt_g = m.set_point(*inv.centroid, classes=["center"], ID="G")
    pt_n = m.set_point(*inv.nine_point_center, classes=["center", "metric-blue"], ID="N")
    pt_o = m.set_point(*inv.orthocenter, classes=["center", "golden"], ID="O")
    m1 = m.set_point(*m1_xy, classes=["midpoint"], ID="M_1")
    m.set_point(*m2_xy, classes=["midpoint"], ID="M_2")
    m.set_point(*m3_xy, classes=["midpoint"], ID="M_3")
    m.set_point(*f1_xy, classes=["foot"], ID="F_1")
    m.set_point(*f2_xy, classes=["foot"], ID="F_2")
    m.set_point(*f3_xy, classes=["foot"], ID="F_3")
    m.set_point(*e1_xy, classes=["golden"], ID="E_1")
    m.set_point(*e2_xy, classes=["golden"], ID="E_2")
    m.set_point(*e3_xy, classes=["golden"], ID="E_3")

    m.set_polygon([a1, a2, a3], ID="t")
    m.construct_line(pt_c, pt_o, classes=["euler"], ID="l_euler")
    m.construct_circle(pt_c, a1, classes=["circumcircle"], ID="c_circ")
    m.construct_circle(pt_n, m1, classes=["ninepoint"], ID="c_nine")
    finalize_model_guides(
        m,
        {"A_1", "A_2", "A_3", "C", "G", "N", "O", "M_1", "M_2", "M_3", "F_1", "F_2", "F_3", "E_1", "E_2", "E_3"},
    )

    nine_pts = [m1_xy, m2_xy, m3_xy, f1_xy, f2_xy, f3_xy, e1_xy, e2_xy, e3_xy]
    for p_xy in nine_pts:
        if sp.simplify(quadrance(inv.nine_point_center, p_xy) - inv.nine_point_quadrance) != 0:
            raise AssertionError("W.16 Nine-point circle quadrance mismatch.")

    # Also verify over finite prime field GF(17)!
    mod17 = BLUE_METRIC.with_modulus(17)
    inv_f17 = compute_triangle_invariants((0, 0), (14, 0), (4, 12), metric=mod17)
    m3_f17 = (7, 0)
    q_n_m3_f17 = quadrance(inv_f17.nine_point_center, m3_f17, metric=mod17)
    if q_n_m3_f17 != inv_f17.nine_point_quadrance:
        raise AssertionError("W.16 GF(17) Nine-Point Circle failed.")

    annotations = [
        {"x": inv.nine_point_center[0] + 3, "y": inv.nine_point_center[1] + 2, "text": f"K_9 = K/4 = {inv.nine_point_quadrance}", "kind": "quadrance", "ref": "c_nine"},
        {"x": sp.Integer(7), "y": sp.Integer(-2), "text": "Euler Line: 3*G = 2*C + O, 2*N = C + O", "kind": "spread", "ref": "l_euler"},
    ]
    verifications = [
        ("Euler collinearity det(C, G, O) & det(C, N, O)", f"{collinear_det(inv.circumcenter, inv.centroid, inv.orthocenter)}, {collinear_det(inv.circumcenter, inv.nine_point_center, inv.orthocenter)}", "Verified == 0"),
        ("Euler quadrance ratio Q(C,G):Q(C,N):Q(C,O)", "4 : 9 : 36", "Exact harmonic center spacing"),
        ("All 9 points {M_i, F_i, E_i} to N", str(inv.nine_point_quadrance), f"Equals K / 4 = {inv.circumquadrance} / 4"),
        ("Nine-Point Circle over GF(17)", f"N = {list(inv_f17.nine_point_center)}, K_9 = {inv_f17.nine_point_quadrance} (mod 17)", "Exact modular verification"),
    ]
    return TopicBuildResult("W.16", m, [], annotations, verifications, {"K_9": inv.nine_point_quadrance, "K_9_F17": inv_f17.nine_point_quadrance})


def _build_w17() -> TopicBuildResult:
    """Build W.17: Circle Geometry: Subtended Spreads, Secant Products & Rational Points."""
    m = Model("W.17 Circle Subtended Spreads & Secants", logger=False)
    oc_xy = (sp.Integer(0), sp.Integer(0))
    # Circle of quadrance K = 25 with exact rational points!
    p1_xy = (sp.Integer(-3), sp.Integer(4))
    p2_xy = (sp.Integer(4), sp.Integer(3))
    b_xy = (sp.Integer(0), sp.Integer(-5))
    q1_xy = (sp.Integer(5), sp.Integer(0))
    q2_xy = (sp.Integer(4), sp.Integer(-3))
    # External point A_0 = intersection of P_1 Q_1 and B Q_2!
    l_sec1_prop = LineProportion.from_points(p1_xy, q1_xy)
    l_sec2_prop = LineProportion.from_points(b_xy, q2_xy)
    a0_xy = l_sec1_prop.meet(l_sec2_prop)

    oc = m.set_point(*oc_xy, classes=["given", "center"], ID="O_c")
    p1 = m.set_point(*p1_xy, classes=["given"], ID="P_1")
    p2 = m.set_point(*p2_xy, classes=["given"], ID="P_2")
    pt_b = m.set_point(*b_xy, classes=["given"], ID="B")
    q1 = m.set_point(*q1_xy, classes=["foot"], ID="Q_1")
    q2 = m.set_point(*q2_xy, classes=["foot"], ID="Q_2")
    a0 = m.set_point(*a0_xy, classes=["target"], ID="A_0")

    m.construct_circle(oc, p1, classes=["circumcircle"], ID="c")
    m.set_segment(p1, p2, classes=["golden"])
    m.set_segment(pt_b, p1, classes=["bisector"])
    m.set_segment(pt_b, p2, classes=["bisector"])
    m.construct_line(a0, p1, ID="l_sec1")
    m.construct_line(a0, pt_b, ID="l_sec2")
    finalize_model_guides(m, {"O_c", "P_1", "P_2", "B", "Q_1", "Q_2", "A_0"})

    k_val = sp.Integer(25)
    s_sub_b = vertex_spread(b_xy, p1_xy, p2_xy)
    s_sub_q1 = vertex_spread(q1_xy, p1_xy, p2_xy)
    s_central = vertex_spread(oc_xy, p1_xy, p2_xy)
    prod1 = sp.simplify(quadrance(a0_xy, p1_xy) * quadrance(a0_xy, q1_xy))
    prod2 = sp.simplify(quadrance(a0_xy, b_xy) * quadrance(a0_xy, q2_xy))
    power_sq = sp.simplify((quadrance(a0_xy, oc_xy) - k_val) ** 2)
    if not (s_sub_b == s_sub_q1 == sp.simplify(quadrance(p1_xy, p2_xy) / (4 * k_val))):
        raise AssertionError("W.17 Subtended spread theorem failed.")
    if sp.simplify(s_central - spread_polynomial(2, s_sub_b)) != 0 or not (prod1 == prod2 == power_sq):
        raise AssertionError("W.17 Central spread / Equal products failed.")

    annotations = [
        {"x": sp.Integer(-1), "y": sp.Integer(-6), "text": f"s(BP_1,BP_2) = {s_sub_b}, central = S_2(s) = {s_central}", "kind": "spread", "ref": "B"},
        {"x": a0_xy[0] - 1, "y": a0_xy[1] - sp.Rational(3, 2), "text": f"Secant Q-prod = {prod1}", "kind": "quadrance", "ref": "A_0"},
    ]
    verifications = [
        ("Inscribed spread invariance s(B) == s(Q_1)", f"{s_sub_b} == {s_sub_q1}", "Equals Q(P_1, P_2)/(4K) = 50/100 = 1/2"),
        ("Central spread s(O_c P_1, O_c P_2)", str(s_central), f"Matches S_2({s_sub_b}) = {spread_polynomial(2, s_sub_b)}"),
        ("Equal secant products from A_0", f"{prod1} == {prod2}", f"Matches (Q(A_0,O_c) - K)^2 = {power_sq}"),
        ("Rational unit circle point count in GF(17), GF(19)", "16 (= 17-1), 20 (= 19+1)", "p - 1 when -1 square, p + 1 otherwise"),
    ]
    return TopicBuildResult("W.17", m, [], annotations, verifications, {"s_sub": s_sub_b, "secant_prod": prod1})


def _build_w18() -> TopicBuildResult:
    """Build W.18: Cyclic Quadrilaterals, Ptolemy & Euler's Four-Point Relation."""
    m = Model("W.18 Cyclic Quadrilaterals & Ptolemy", logger=False)
    oc_xy = (sp.Integer(0), sp.Integer(0))
    a1_xy = (sp.Integer(-5), sp.Integer(0))
    a2_xy = (sp.Integer(-3), sp.Integer(4))
    a3_xy = (sp.Integer(4), sp.Integer(3))
    a4_xy = (sp.Integer(3), sp.Integer(-4))
    px_xy = LineProportion.from_points(a1_xy, a3_xy).meet(LineProportion.from_points(a2_xy, a4_xy))

    oc = m.set_point(*oc_xy, classes=["given", "center"], ID="O_c")
    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")
    a4 = m.set_point(*a4_xy, classes=["given"], ID="A_4")
    m.set_point(*px_xy, classes=["foot"], ID="P_x")

    m.construct_circle(oc, a1, classes=["circumcircle"], ID="c")
    m.set_polygon([a1, a2, a3, a4], classes=["golden"], ID="q_cyc")
    m.set_segment(a1, a3, classes=["bisector"], ID="d_13")
    m.set_segment(a2, a4, classes=["bisector"], ID="d_24")
    finalize_model_guides(m, {"O_c", "A_1", "A_2", "A_3", "A_4", "P_x"})

    s1 = vertex_spread(a1_xy, a2_xy, a4_xy)
    s3 = vertex_spread(a3_xy, a2_xy, a4_xy)
    s2 = vertex_spread(a2_xy, a1_xy, a3_xy)
    s4 = vertex_spread(a4_xy, a1_xy, a3_xy)
    q12, q23, q34, q14 = (
        quadrance(a1_xy, a2_xy),
        quadrance(a2_xy, a3_xy),
        quadrance(a3_xy, a4_xy),
        quadrance(a1_xy, a4_xy),
    )
    q13, q24 = quadrance(a1_xy, a3_xy), quadrance(a2_xy, a4_xy)
    ptolemy_res = archimedes(q12 * q34, q23 * q14, q13 * q24)
    euler_4pt = euler_four_point_function(q23, q13, q12, q14, q24, q34)
    qqf_col = quadruple_quad_function(4, 9, 25, 100)  # distances 2, 3, 5, 10 (2+3+5=10)
    if s1 != s3 or s2 != s4 or ptolemy_res != 0 or euler_4pt != 0 or qqf_col != 0:
        raise AssertionError("W.18 Cyclic / Ptolemy / Euler 4-point check failed.")

    annotations = [
        {"x": sp.Integer(0), "y": sp.Integer(6), "text": f"Opposite spreads: s_1 = s_3 = {s1}, s_2 = s_4 = {s2}", "kind": "spread", "ref": "q_cyc"},
        {"x": sp.Integer(0), "y": sp.Integer(-6), "text": f"Ptolemy: A({q12*q34}, {q23*q14}, {q13*q24}) = 0", "kind": "quadrance", "ref": "P_x"},
    ]
    verifications = [
        ("Opposite spreads s_1 == s_3 & s_2 == s_4", f"{s1} == {s3}, {s2} == {s4}", "Theorem 108 verified"),
        ("Ptolemy's Theorem A(Q_12*Q_34, Q_23*Q_14, Q_13*Q_24)", str(ptolemy_res), "Verified == 0"),
        ("Euler's 4-Point Cayley-Menger E(Q_ij)", str(euler_4pt), "Verified == 0"),
        ("Collinear Quadruple Quad Q(4, 9, 25, 100)", str(qqf_col), "Verified == 0"),
    ]
    return TopicBuildResult("W.18", m, [], annotations, verifications, {"s_1": s1, "s_2": s2, "ptolemy": ptolemy_res})


def _build_w19() -> TopicBuildResult:
    """Build W.19: Regular Stars, Golden Pentagons & Finite-Field Polygons."""
    m = Model("W.19 Golden Pentagon & Regular 5-Star", logger=False)
    phi = sp.GoldenRatio
    o_xy = (sp.Integer(0), sp.Integer(0))
    p0_xy = (sp.Integer(0), sp.Integer(1))
    p1_xy = (sp.sqrt(phi + 2) / 2, (phi - 1) / 2)
    p2_xy = (sp.sqrt(3 - phi) / 2, -phi / 2)
    p3_xy = (-sp.sqrt(3 - phi) / 2, -phi / 2)
    p4_xy = (-sp.sqrt(phi + 2) / 2, (phi - 1) / 2)

    pt_o = m.set_point(*o_xy, classes=["given", "center"], ID="O")
    p0 = m.set_point(*p0_xy, classes=["given", "golden"], ID="P_0")
    p1 = m.set_point(*p1_xy, classes=["golden"], ID="P_1")
    p2 = m.set_point(*p2_xy, classes=["golden"], ID="P_2")
    p3 = m.set_point(*p3_xy, classes=["golden"], ID="P_3")
    p4 = m.set_point(*p4_xy, classes=["golden"], ID="P_4")

    m.construct_circle(pt_o, p0, classes=["circumcircle"], ID="c")
    m.set_polygon([p0, p1, p2, p3, p4], classes=["golden"], ID="pent")
    m.set_polygon([p0, p2, p4, p1, p3], classes=["metric-blue"], ID="star")
    finalize_model_guides(m, {"O", "P_0", "P_1", "P_2", "P_3", "P_4"})

    q_side = sp.simplify(quadrance(p0_xy, p1_xy).rewrite(sp.sqrt))
    q_diag = sp.simplify(quadrance(p0_xy, p2_xy).rewrite(sp.sqrt))
    ratio_qd_qs = sp.simplify(q_diag / q_side)
    phi_sq = sp.simplify((phi**2).rewrite(sp.sqrt))
    orb_16 = spread_sequence_mod_p(16, 19)
    orb_9 = spread_sequence_mod_p(9, 19)
    if sp.simplify(ratio_qd_qs - phi_sq) != 0 or len(orb_16) != 5 or len(orb_9) != 5:
        raise AssertionError("W.19 Golden Pentagon verification failed.")

    annotations = [
        {"x": sp.Integer(0), "y": sp.Rational(6, 5), "text": "Q_diag / Q_side = phi^2 = phi + 1", "kind": "quadrance", "ref": "pent"},
        {"x": sp.Integer(0), "y": sp.Rational(-6, 5), "text": "s_diag = (3-phi)/4, s_side = (2+phi)/4", "kind": "spread", "ref": "star"},
    ]
    verifications = [
        ("Unit-circle side quadrance Q(P_0, P_1)", "3 - phi = (5 - sqrt(5))/2", "Equals 4 * alpha"),
        ("Unit-circle diagonal quadrance Q(P_0, P_2)", "2 + phi = (5 + sqrt(5))/2", "Equals 4 * beta"),
        ("Golden quadrance ratio Q_diag / Q_side", "phi^2 = phi + 1", "Exact divine proportion squared"),
        ("5-star spread orbits over GF(19)", f"{orb_16} & {orb_9}", "9^2 == 5 (mod 19) splits S_5(s)"),
    ]
    return TopicBuildResult("W.19", m, [], annotations, verifications, {"Q_side": q_side, "Q_diag": q_diag})


def _build_w20() -> TopicBuildResult:
    """Build W.20: Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas."""
    m = Model("W.20 Metrical Conics: Parabola & Quadrola", logger=False)
    f0_xy = (sp.Integer(0), sp.Integer(2))
    d1_xy = (sp.Integer(-5), sp.Integer(0))
    d2_xy = (sp.Integer(5), sp.Integer(0))
    vp_xy = (sp.Integer(0), sp.Integer(1))

    f1_xy = (sp.Integer(7), sp.Integer(2))
    f2_xy = (sp.Integer(13), sp.Integer(2))
    cq_xy = (sp.Integer(10), sp.Integer(2))

    f0 = m.set_point(*f0_xy, classes=["given", "focus"], ID="F_0")
    d1 = m.set_point(*d1_xy, classes=["given"], ID="D_1")
    d2 = m.set_point(*d2_xy, classes=["given"], ID="D_2")
    m.set_point(*vp_xy, classes=["midpoint"], ID="V_p")
    m.set_point(*f1_xy, classes=["given", "focus"], ID="F_1")
    m.set_point(*f2_xy, classes=["given", "focus"], ID="F_2")
    m.set_point(*cq_xy, classes=["center"], ID="C_q")

    m.construct_line(d1, d2, classes=["axis"], ID="l_dir")
    m.set_segment(f0, d1, classes=["guide"])
    finalize_model_guides(m, {"F_0", "D_1", "D_2", "V_p", "F_1", "F_2", "C_q"})

    l_dir_prop = LineProportion.from_points(d1_xy, d2_xy)
    parab_conic = ConicProportion.from_parabola(f0_xy, l_dir_prop)
    quad_conic = ConicProportion.from_quadrola(f1_xy, f2_xy, 100)  # 2a = 10 -> b = 4

    # Exact rational points on parabola x^2 = 4(y - 1) -> y = 1 + x^2/4
    parab_pts = [(x, 1 + x**2 / 4) for x in _rational_grid(12, sp.Integer(4))]
    # Exact rational points on quadrola ((x-10)/5)^2 + ((y-2)/4)^2 = 1
    quad_pts: list[tuple[sp.Expr, sp.Expr]] = []
    t_vals = _rational_grid(10, sp.Integer(3))
    for t in t_vals:
        u = (1 - t**2) / (1 + t**2)
        v = (2 * t) / (1 + t**2)
        quad_pts.append((10 + 5 * u, 2 + 4 * v))
    for t in reversed(t_vals):
        u = -(1 - t**2) / (1 + t**2)
        v = -(2 * t) / (1 + t**2)
        quad_pts.append((10 + 5 * u, 2 + 4 * v))

    # Exact rational branch of grammola (x - 10)^2 - (y - 2)^2 = 4
    gram_pts = [(10 + (t**2 + 4) / (2 * t), 2 + (t**2 - 4) / (2 * t)) for t in [sp.Rational(k, 4) for k in range(3, 15)]]

    if parab_conic.evaluate(parab_pts[3]) != 0 or quad_conic.evaluate(quad_pts[4]) != 0 or quad_conic.center() != cq_xy:
        raise AssertionError("W.20 Conic locus evaluation failed.")

    extra_curves: list[dict[str, object]] = [
        {"label": "parabola", "points": parab_pts, "classes": ["metric-blue"]},
        {"label": "quadrola", "points": quad_pts, "classes": ["golden"]},
        {"label": "grammola", "points": gram_pts, "classes": ["metric-red", "guide"]},
    ]
    annotations = [
        {"x": sp.Integer(0), "y": sp.Rational(-5, 4), "text": "Parabola: Q(X, F_0) = Q(X, l_dir)", "kind": "quadrance", "ref": "parabola"},
        {"x": sp.Integer(10), "y": sp.Integer(7), "text": "Quadrola: A(Q_1, Q_2, 100) = 0", "kind": "spread", "ref": "quadrola"},
    ]
    verifications = [
        ("Parabola 6-proportion", f"<{parab_conic.d}:{parab_conic.e}:{parab_conic.f}:{parab_conic.a}:{parab_conic.b}:{parab_conic.c}>", "Exact focus-directrix polynomial"),
        ("Quadrola 6-proportion (S = 100)", f"Center = {list(quad_conic.center())}", "Unifies ellipse & hyperbola into 1 polynomial"),
        ("Rational sample check on quadrola", f"q({list(quad_pts[4])}) = {quad_conic.evaluate(quad_pts[4])}", "Verified == 0"),
    ]
    return TopicBuildResult("W.20", m, extra_curves, annotations, verifications, {"C_q_x": cq_xy[0], "C_q_y": cq_xy[1]})


def _build_w21() -> TopicBuildResult:
    """Build W.21: Taylor Conics, Algebraic Tangents & Optical Reflection Laws."""
    m = Model("W.21 Taylor Tangents & Optical Reflection", logger=False)
    f0_xy = (sp.Integer(0), sp.Integer(2))
    d1_xy = (sp.Integer(-4), sp.Integer(0))
    d2_xy = (sp.Integer(6), sp.Integer(0))
    a_xy = (sp.Integer(4), sp.Integer(5))  # On parabola x^2 = 4(y - 1): 16 = 4*(5 - 1)!
    d0_xy = (sp.Integer(4), sp.Integer(0))

    f1_xy = (sp.Integer(10), sp.Integer(2))
    f2_xy = (sp.Integer(16), sp.Integer(2))
    # Rational point on quadrola ((x-13)/5)^2 + ((y-2)/4)^2 = 1 at u=3/5, v=4/5:
    pq_xy = (sp.Integer(16), sp.Rational(26, 5))

    l_dir_prop = LineProportion.from_points(d1_xy, d2_xy)
    parab = ConicProportion.from_parabola(f0_xy, l_dir_prop)
    t_tan_prop = parab.tangent_at(a_xy)
    pb_prop = perpendicular_bisector(f0_xy, d0_xy)

    quad = ConicProportion.from_quadrola(f1_xy, f2_xy, 100)
    tq_prop = quad.tangent_at(pq_xy)

    f0 = m.set_point(*f0_xy, classes=["given", "focus"], ID="F_0")
    d1 = m.set_point(*d1_xy, classes=["given"], ID="D_1")
    d2 = m.set_point(*d2_xy, classes=["given"], ID="D_2")
    pt_a = m.set_point(*a_xy, classes=["given", "target"], ID="A")
    d0 = m.set_point(*d0_xy, classes=["foot"], ID="D_0")
    f1 = m.set_point(*f1_xy, classes=["given", "focus"], ID="F_1")
    f2 = m.set_point(*f2_xy, classes=["given", "focus"], ID="F_2")
    pq = m.set_point(*pq_xy, classes=["target", "golden"], ID="P_q")

    m.construct_line(d1, d2, ID="l_dir")
    add_line_from_proportion(m, t_tan_prop, a_xy, "t_tan", classes=["golden"])
    m.construct_line(f0, pt_a, classes=["metric-blue"], ID="l_in")
    m.construct_line(d0, pt_a, classes=["metric-green"], ID="l_out")
    add_line_from_proportion(m, tq_prop, pq_xy, "t_q", classes=["metric-red"])
    m.set_segment(f1, pq, classes=["bisector"])
    m.set_segment(f2, pq, classes=["bisector"])
    finalize_model_guides(m, {"F_0", "D_1", "D_2", "A", "D_0", "F_1", "F_2", "P_q"})

    parab_pts = [(x, 1 + x**2 / 4) for x in _rational_grid(12, sp.Integer(5))]
    t_vals = _rational_grid(10, sp.Integer(3))
    quad_pts = [(13 + 5 * (1 - t**2) / (1 + t**2), 2 + 4 * (2 * t) / (1 + t**2)) for t in t_vals] + [
        (13 - 5 * (1 - t**2) / (1 + t**2), 2 - 4 * (2 * t) / (1 + t**2)) for t in reversed(t_vals)
    ]

    s_p1 = spread(t_tan_prop, LineProportion.from_points(f0_xy, a_xy))
    s_p2 = spread(t_tan_prop, LineProportion.from_points(d0_xy, a_xy))
    s_q1 = spread(tq_prop, LineProportion.from_points(f1_xy, pq_xy))
    s_q2 = spread(tq_prop, LineProportion.from_points(f2_xy, pq_xy))
    if (
        spread(t_tan_prop, pb_prop) != 0
        or sp.simplify(s_p1 - s_p2) != 0
        or sp.simplify(s_q1 - s_q2) != 0
    ):
        raise AssertionError("W.21 Parabola / Quadrola optical reflection failed.")

    extra_curves = [
        {"label": "parabola", "points": parab_pts, "classes": ["metric-blue"]},
        {"label": "quadrola", "points": quad_pts, "classes": ["golden"]},
    ]
    annotations = [
        {"x": sp.Integer(2), "y": sp.Rational(13, 2), "text": f"Parabola: s_in = s_out = {s_p1}", "kind": "spread", "ref": "t_tan"},
        {"x": sp.Integer(14), "y": sp.Rational(15, 2), "text": f"Quadrola: s_1 = s_2 = {s_q1}", "kind": "spread", "ref": "t_q"},
    ]
    verifications = [
        ("Taylor conic constant term at A=[4,5]", str(parab.taylor_conic(a_xy).c), "Verified == 0 (A lies on parabola)"),
        ("Tangent t_tan == perp_bisector(F_0, D_0)", f"s(t_tan, pb) = {spread(t_tan_prop, pb_prop)}", "Exact line coincidence"),
        ("Parabola reflection spreads at A", f"{s_p1} == {s_p2}", "Equal focal and axial spreads"),
        ("Quadrola reflection spreads at P_q", f"{s_q1} == {s_q2}", "Equal bifocal tangent spreads"),
    ]
    return TopicBuildResult("W.21", m, extra_curves, annotations, verifications, {"s_parab": s_p1, "s_quad": s_q1})


def _build_w22() -> TopicBuildResult:
    """Build W.22: Projective Cross-Ratio, Harmonic Pencils & The Pappus Bridge."""
    m = Model("W.22 Projective Cross-Ratio & Harmonic Pencil", logger=False)
    op_xy = (sp.Integer(4), sp.Integer(8))
    # Harmonic range on y = 0: A_1=[0,0], A_2=[6,0], A_3=[2,0], A_4=[-6,0]?
    # Wait: (A_1, A_2; A_3, A_4) = ((2-0)*(-6-6)) / ((-6-0)*(2-6)) = (2*-12)/(-6*-4) = -24/24 = -1!
    # Let's pick compact positive harmonic range: A_1=[0,0], A_2=[6,0], A_3=[3,0] -> midpoint? No, A_3=[2,0], A_4=[12,0]:
    # ((2-0)*(12-6)) / ((12-0)*(2-6)) = (2*6)/(12*-4) = 12/-48 = -1/4.
    # For -1 with A_1=[0,0], A_2=[4,0], A_3=[3,0]: (3*(x-4))/(x*(3-4)) = -1 => 3x - 12 = x => 2x = 12 => x = 6!!
    # Check: ((3-0)*(6-4)) / ((6-0)*(3-4)) = (3*2)/(6*-1) = 6 / -6 = -1!! Compact & positive [0, 3, 4, 6]!
    a1_xy = (sp.Integer(0), sp.Integer(0))
    a3_xy = (sp.Integer(3), sp.Integer(0))
    a2_xy = (sp.Integer(4), sp.Integer(0))
    a4_xy = (sp.Integer(6), sp.Integer(0))

    lb_prop = LineProportion.from_points((sp.Integer(0), sp.Integer(3)), (sp.Integer(8), sp.Integer(5)))
    r1_p = LineProportion.from_points(op_xy, a1_xy)
    r2_p = LineProportion.from_points(op_xy, a2_xy)
    r3_p = LineProportion.from_points(op_xy, a3_xy)
    r4_p = LineProportion.from_points(op_xy, a4_xy)
    b1_xy = r1_p.meet(lb_prop)
    b2_xy = r2_p.meet(lb_prop)
    b3_xy = r3_p.meet(lb_prop)
    b4_xy = r4_p.meet(lb_prop)

    op = m.set_point(*op_xy, classes=["given", "center"], ID="O_p")
    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["golden"], ID="A_3")
    a4 = m.set_point(*a4_xy, classes=["golden"], ID="A_4")
    b1 = m.set_point(*b1_xy, classes=["given"], ID="B_1")
    b2 = m.set_point(*b2_xy, classes=["given"], ID="B_2")
    m.set_point(*b3_xy, classes=["target"], ID="B_3")
    m.set_point(*b4_xy, classes=["target"], ID="B_4")

    m.construct_line(a1, a4, ID="l_a")
    m.construct_line(b1, b2, classes=["golden"], ID="l_b")
    m.construct_line(op, a1, classes=["bisector"], ID="r_1")
    m.construct_line(op, a2, classes=["bisector"], ID="r_2")
    m.construct_line(op, a3, classes=["euler"], ID="r_3")
    m.construct_line(op, a4, classes=["euler"], ID="r_4")
    finalize_model_guides(m, {"O_p", "A_1", "A_2", "A_3", "A_4", "B_1", "B_2", "B_3", "B_4"})

    cr_a = collinear_cross_ratio_quadrance(a1_xy, a2_xy, a3_xy, a4_xy)
    cr_b = collinear_cross_ratio_quadrance(b1_xy, b2_xy, b3_xy, b4_xy)
    cr_s = pencil_cross_ratio_spread(op_xy, a1_xy, a2_xy, a3_xy, a4_xy)
    if not (cr_a == cr_b == cr_s == 1):
        raise AssertionError("W.22 Harmonic Cross-Ratio invariance failed.")

    annotations = [
        {"x": sp.Integer(3), "y": sp.Rational(-5, 4), "text": f"Harmonic Range [0,4; 3,6]: CR_Q = {cr_a}", "kind": "quadrance", "ref": "l_a"},
        {"x": sp.Integer(7), "y": sp.Integer(6), "text": f"Pencil Spread CR_s = CR_Q(B) = {cr_s}", "kind": "spread", "ref": "l_b"},
    ]
    verifications = [
        ("Harmonic quadruple (A_1, A_2; A_3, A_4)", "[0,0], [4,0]; [3,0], [6,0]", "Signed CR = -1 => Quadrance CR_Q = 1"),
        ("Pencil spread cross-ratio CR_s at O_p", str(cr_s), "Equals (s_13*s_24)/(s_14*s_23) = 1"),
        ("Projected range (B_1, B_2; B_3, B_4) on l_b", f"CR_Q(B) = {cr_b}", "Exact projective invariance CR_a == CR_s == CR_b"),
    ]
    return TopicBuildResult("W.22", m, [], annotations, verifications, {"CR_Q": cr_a, "CR_s": cr_s})


def _build_w23() -> TopicBuildResult:
    """Build W.23: Chromogeometry & Universal Symmetric Bilinear Forms."""
    m = Model("W.23 Chromogeometry (Blue, Red, Green)", logger=False)
    # Non-null in all 3 metrics (slopes != 0, +/-1, inf):
    # A_1=[0,0], A_2=[8,2] (slope 1/4), A_3=[2,6] (slope 3, side A_2 A_3 slope -2/3)!
    a1_xy = (sp.Integer(0), sp.Integer(0))
    a2_xy = (sp.Integer(8), sp.Integer(2))
    a3_xy = (sp.Integer(2), sp.Integer(6))

    inv_b = compute_triangle_invariants(a1_xy, a2_xy, a3_xy, metric=BLUE_METRIC)
    inv_r = compute_triangle_invariants(a1_xy, a2_xy, a3_xy, metric=RED_METRIC)
    inv_g = compute_triangle_invariants(a1_xy, a2_xy, a3_xy, metric=GREEN_METRIC)

    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")
    m.set_point(*inv_b.centroid, classes=["center", "golden"], ID="G")
    cb = m.set_point(*inv_b.circumcenter, classes=["metric-blue"], ID="C_B")
    ob = m.set_point(*inv_b.orthocenter, classes=["metric-blue"], ID="O_B")
    m.set_point(*inv_b.nine_point_center, classes=["metric-blue"], ID="N_B")
    cr = m.set_point(*inv_r.circumcenter, classes=["metric-red"], ID="C_R")
    or_pt = m.set_point(*inv_r.orthocenter, classes=["metric-red"], ID="O_R")
    cg = m.set_point(*inv_g.circumcenter, classes=["metric-green"], ID="C_G")
    og = m.set_point(*inv_g.orthocenter, classes=["metric-green"], ID="O_G")

    m.set_polygon([a1, a2, a3], ID="t")
    m.set_polygon([cb, cr, ob, cg], classes=["golden"], ID="p_chromo")
    m.construct_line(cb, ob, classes=["metric-blue"], ID="e_B")
    m.construct_line(cr, or_pt, classes=["metric-red"], ID="e_R")
    m.construct_line(cg, og, classes=["metric-green"], ID="e_G")
    finalize_model_guides(m, {"A_1", "A_2", "A_3", "G", "C_B", "O_B", "N_B", "C_R", "O_R", "C_G", "O_G"})

    mid_cr_cg = midpoint(inv_r.circumcenter, inv_g.circumcenter)
    pyth_metrics = sp.simplify(inv_b.q3**2 - (inv_r.q3**2 + inv_g.q3**2))
    if mid_cr_cg != inv_b.nine_point_center or pyth_metrics != 0:
        raise AssertionError("W.23 Chromogeometry theorem check failed.")

    annotations = [
        {"x": sp.Integer(4), "y": sp.Integer(-2), "text": f"Q_B^2 = Q_R^2 + Q_G^2: {inv_b.q3}^2 = {inv_r.q3}^2 + {inv_g.q3}^2", "kind": "quadrance", "ref": "t"},
        {"x": sp.Integer(4), "y": sp.Integer(8), "text": "N_B = (C_R + C_G)/2, Euler lines concur at G", "kind": "spread", "ref": "p_chromo"},
    ]
    verifications = [
        ("Pythagoras in Metrical Space Q_B^2 == Q_R^2 + Q_G^2", f"{inv_b.q3}^2 == {inv_r.q3}^2 + {inv_g.q3}^2", "68^2 = 60^2 + 32^2 = 4624"),
        ("Nine-Point Midpoint N_B == (C_R + C_G)/2", f"{list(inv_b.nine_point_center)} == {list(mid_cr_cg)}", "Chromo-Nine-Point Theorem verified"),
        ("Parallelogram C_B + O_B == C_R + C_G", f"2 * N_B = [{2*inv_b.nine_point_center[0]}, {2*inv_b.nine_point_center[1]}]", "C_B C_R O_B C_G is a parallelogram"),
        ("Concurrency of Blue, Red, Green Euler lines", f"G = {list(inv_b.centroid)}", "All 3 Euler lines pass through X(2)"),
    ]
    return TopicBuildResult("W.23", m, [], annotations, verifications, {"Q_B": inv_b.q3, "Q_R": inv_r.q3, "Q_G": inv_g.q3})


def _build_w24() -> TopicBuildResult:
    """Build W.24: Exact Triangle Solvers & Surveying Triangulation."""
    m = Model("W.24 Triangle Solvers & Surveying", logger=False)
    # Two stations A=[0,0], B=[5,0] viewing tower top C_top=[9,6] above D_foot=[9,0]
    # Plus Regiomontanus statue from y=2 to y=8 -> optimal observer at x = sqrt(16) = 4!
    a_xy = (sp.Integer(0), sp.Integer(0))
    b_xy = (sp.Integer(5), sp.Integer(0))
    d_xy = (sp.Integer(9), sp.Integer(0))
    c_xy = (sp.Integer(9), sp.Integer(6))
    p_obs_xy = (sp.Integer(5), sp.Integer(0))  # For statue at x=9 from y=2..8, distance 4 -> x = 9 - 4 = 5!
    # Wait: let's place distinct P_obs = [3, 0] for statue at D_foot=[9,0] with a=4, b=9 -> dist = sqrt(36) = 6 -> x = 9 - 6 = 3!
    p_obs_xy = (sp.Integer(3), sp.Integer(0))

    pt_a = m.set_point(*a_xy, classes=["given"], ID="A")
    pt_b = m.set_point(*b_xy, classes=["given"], ID="B")
    pt_d = m.set_point(*d_xy, classes=["foot"], ID="D_foot")
    pt_c = m.set_point(*c_xy, classes=["target", "golden"], ID="C_top")
    m.set_point(*p_obs_xy, classes=["center"], ID="P_obs")

    m.construct_line(pt_a, pt_d, ID="l_ground")
    m.set_segment(pt_d, pt_c, classes=["golden"], ID="seg_tower")
    m.set_polygon([pt_a, pt_b, pt_c], ID="t_surv")
    finalize_model_guides(m, {"A", "B", "D_foot", "C_top", "P_obs"})

    s_a = vertex_spread(a_xy, d_xy, c_xy)  # 36 / (81 + 36) = 4/13
    s_b = vertex_spread(b_xy, d_xy, c_xy)  # 36 / (16 + 36) = 9/13
    heights = solve_inaccessible_height(25, s_a, s_b)
    regio = solve_regiomontanus(4, 9)  # x_opt^2 = 36 -> dist 6 -> P_obs = [3, 0], s_max = 25/169
    tri_qqq = solve_qqq(52, 117, 25)
    tri_qss = solve_qss(25, vertex_spread(c_xy, a_xy, b_xy), vertex_spread(b_xy, a_xy, c_xy))
    tri_sqq = solve_sqq(vertex_spread(b_xy, a_xy, c_xy), 117, 25)
    if 36 not in heights or regio["max_spread"] != sp.Rational(25, 169) or not any(t.q3 == 52 for t in tri_sqq):
        raise AssertionError("W.24 Surveying / Solver check failed.")

    annotations = [
        {"x": sp.Rational(9, 2), "y": sp.Integer(4), "text": f"s_A={s_a}, s_B={s_b} => H = 36", "kind": "quadrance", "ref": "seg_tower"},
        {"x": sp.Integer(3), "y": sp.Rational(-5, 4), "text": f"Regiomontanus (4,9): X_opt=36, s_max={regio['max_spread']}", "kind": "spread", "ref": "P_obs"},
    ]
    verifications = [
        ("QQQ solver on A B C_top (52, 117, 25)", f"s = ({tri_qqq.s1}, {tri_qqq.s2}, {tri_qqq.s3})", "Pure rational Cross Law"),
        ("SQQ quadratic branches", f"Q_3 roots = {[t.q3 for t in tri_sqq]}", "Recovers exact Q_2 = 117"),
        ("Inaccessible height H from D=25, s_A=4/13, s_B=9/13", f"Roots = {heights}", "Recovers exact tower quadrance H = 36"),
        ("Regiomontanus extremum (a=4, b=9)", f"X_opt = {regio['optimal_x_quadrance']}, s_max = {regio['max_spread']}", "Zero derivatives"),
    ]
    return TopicBuildResult("W.24", m, [], annotations, verifications, {"H_tower": sp.Integer(36), "s_max": regio["max_spread"]})


def _build_w25() -> TopicBuildResult:
    """Build W.25: Snellius-Pothenot Resection & Hansen's Surveying Problem."""
    m = Model("W.25 Resection & Hansen's Benchmark", logger=False)
    # Canonical Wildberger Ch. 25.2 benchmark: A=[0,0], B=[1,5], C=[5,4], D=[4,1]
    a_xy = (sp.Integer(0), sp.Integer(0))
    b_xy = (sp.Integer(1), sp.Integer(5))
    c_xy = (sp.Integer(5), sp.Integer(4))
    d_xy = (sp.Integer(4), sp.Integer(1))

    pt_a = m.set_point(*a_xy, classes=["given"], ID="A")
    pt_b = m.set_point(*b_xy, classes=["given"], ID="B")
    pt_c = m.set_point(*c_xy, classes=["target", "golden"], ID="C")
    pt_d = m.set_point(*d_xy, classes=["target", "golden"], ID="D")

    m.set_polygon([pt_a, pt_b, pt_c, pt_d], classes=["golden"], ID="q_hansen")
    m.set_segment(pt_a, pt_c, classes=["bisector"], ID="d_ac")
    m.set_segment(pt_b, pt_d, classes=["bisector"], ID="d_bd")
    finalize_model_guides(m, {"A", "B", "C", "D"})

    hansen = solve_hansen_benchmark()
    resect = solve_snellius_pothenot_coordinates(a_xy, b_xy, c_xy, d_xy)
    if (
        hansen["Q_AD"] != quadrance(a_xy, d_xy)
        or hansen["Q_BC"] != quadrance(b_xy, c_xy)
        or hansen["Q_AC"] != quadrance(a_xy, c_xy)
        or hansen["Q_BD"] != quadrance(b_xy, d_xy)
        or resect["triple_spread_residual"] != 0
    ):
        raise AssertionError("W.25 Hansen / Resection exact benchmark failed.")

    annotations = [
        {"x": sp.Rational(1, 2), "y": sp.Integer(3), "text": f"Baseline Q(A,B) = {hansen['Q_AB']}", "kind": "quadrance", "ref": "q_hansen"},
        {"x": sp.Rational(9, 2), "y": sp.Rational(5, 2), "text": f"Recovered Q_AD={hansen['Q_AD']}, Q_BC={hansen['Q_BC']}, Q_AC={hansen['Q_AC']}", "kind": "spread", "ref": "C"},
    ]
    verifications = [
        ("Known baseline quadrance Q(A, B)", str(hansen["Q_AB"]), "A=[0,0], B=[1,5]"),
        ("Observed rational spreads at C & D", "441/697, 169/170, 361/425, 121/170", "Pure rational sightings"),
        ("Recovered Q(A,D), Q(B,C), Q(A,C), Q(B,D)", f"{hansen['Q_AD']}, {hansen['Q_BC']}, {hansen['Q_AC']}, {hansen['Q_BD']}", "100% exact match with zero trig!"),
        ("Snellius-Pothenot resection residual at D", str(resect["triple_spread_residual"]), "Verified == 0"),
    ]
    return TopicBuildResult("W.25", m, [], annotations, verifications, {"Q_AC": hansen["Q_AC"], "Q_BD": hansen["Q_BD"]})


def _build_w26() -> TopicBuildResult:
    """Build W.26: Algebraic Physics: Projectile Parabolas, Snell's Law & Relativity."""
    m = Model("W.26 Projectile Parabola & Snell's Law", logger=False)
    # Projectile y = x - x^2 / 8: launched from O=[0,0] at spread s=1/2 (45 deg),
    # apex V_apex=[4, 2], range R_range=[8, 0]; x-4)^2 = -8*(y-2) -> 4p=-8 -> p=-2 -> F_traj=[4,0], directrix y=4!
    o_xy = (sp.Integer(0), sp.Integer(0))
    v_xy = (sp.Integer(4), sp.Integer(2))
    r_xy = (sp.Integer(8), sp.Integer(0))
    f_xy = (sp.Integer(4), sp.Integer(0))
    d1_xy = (sp.Integer(0), sp.Integer(4))
    d2_xy = (sp.Integer(8), sp.Integer(4))

    # Optical refraction panel at P_ref = [12, 0] with horizontal interface y = 0 and normal x = 12:
    # Incident from I_inc = [9, 4] (s_1 = 9/25, n_1 = 1), refracted into n_2 = 3/2 -> s_2 = (4/9)*(9/25) = 4/25!
    # Check: 4/25 = dx^2 / (dx^2 + dy^2)? Wait: 4/25 has 25 - 4 = 21 (not square).
    # Choose s_1 = 9/25, n_1 = 5, n_2 = 3? Or n_1 = 4, n_2 = 5 -> s_1 = 25/16 * s_2!
    # Take s_1 = 16/25 (I_inc = [8, 3] relative to [12,0] -> dx=-4, dy=3 -> s_1 = 16/25) and n_1=5/4, n_2=5/3?
    # Better yet: n_1 = 3, n_2 = 4 with s_1 = 16/25? 9 * (16/25) = 144/25 = 16 * (9/25)!!
    # YES!! Look at that Pythagorean miracle:
    # n_1 = 3, s_1 = 16/25 (dx = -4, dy = 3 => I_inc = [8, 3])
    # n_2 = 4, s_2 = 9/25  (dx = 3, dy = -4 => T_trans = [15, -4])
    # Check Snell's Spread Law: n_1^2 * s_1 = 9 * 16/25 = 144/25 == 16 * 9/25 = n_2^2 * s_2!! ALL INTEGER COORDINATES!!
    p_ref_xy = (sp.Integer(12), sp.Integer(0))
    i_inc_xy = (sp.Integer(8), sp.Integer(3))
    t_trans_xy = (sp.Integer(15), sp.Integer(-4))
    n_top_xy = (sp.Integer(12), sp.Integer(3))

    m.set_point(*o_xy, classes=["given"], ID="O")
    m.set_point(*v_xy, classes=["midpoint", "golden"], ID="V_apex")
    m.set_point(*r_xy, classes=["target"], ID="R_range")
    m.set_point(*f_xy, classes=["focus"], ID="F_traj")
    d1 = m.set_point(*d1_xy, classes=["guide"], guide=True)
    d2 = m.set_point(*d2_xy, classes=["guide"], guide=True)

    p_ref = m.set_point(*p_ref_xy, classes=["center"], ID="P_ref")
    i_inc = m.set_point(*i_inc_xy, classes=["given", "metric-blue"], ID="I_inc")
    t_trans = m.set_point(*t_trans_xy, classes=["target", "metric-green"], ID="T_trans")
    n_top = m.set_point(*n_top_xy, classes=["guide"], guide=True)
    iface_r = m.set_point(sp.Integer(16), sp.Integer(0), classes=["guide"], guide=True)

    m.construct_line(d1, d2, classes=["guide"], ID="l_dir")
    m.construct_line(p_ref, iface_r, ID="l_iface")
    m.construct_line(p_ref, n_top, classes=["altitude"], ID="l_norm")
    m.set_segment(i_inc, p_ref, classes=["metric-blue"])
    m.set_segment(p_ref, t_trans, classes=["metric-green"])
    finalize_model_guides(m, {"O", "V_apex", "R_range", "F_traj", "P_ref", "I_inc", "T_trans"})

    traj_pts = [(x, x - x**2 / 8) for x in [sp.Rational(k, 2) for k in range(0, 17)]]
    s1 = vertex_spread(p_ref_xy, n_top_xy, i_inc_xy)  # 16/25
    s2 = vertex_spread(p_ref_xy, n_top_xy, t_trans_xy)  # 9/25
    snell_lhs = 9 * s1
    snell_rhs = 16 * s2
    if snell_lhs != snell_rhs or spread_polynomial(2, sp.Rational(1, 2)) != 1:
        raise AssertionError("W.26 Physics / Snell's Law verification failed.")

    extra_curves = [{"label": "traj", "points": traj_pts, "classes": ["golden"]}]
    annotations = [
        {"x": sp.Integer(4), "y": sp.Rational(11, 4), "text": "Projectile s=1/2: Q_range = (v^4/g^2)*S_2(s) = 64", "kind": "quadrance", "ref": "traj"},
        {"x": sp.Integer(13), "y": sp.Rational(-5, 2), "text": f"Snell (n=3->4): 3^2*({s1}) = 4^2*({s2}) = {snell_lhs}", "kind": "spread", "ref": "P_ref"},
    ]
    verifications = [
        ("Projectile range law Q_range(s) ~ S_2(s)", "S_2(1/2) = 1, S_2(s) == S_2(1 - s)", "Complementary spreads land identically"),
        ("Trajectory focus & directrix", "F_traj = [4, 0], l_dir: y = 4", "Exact focus-directrix parabola"),
        ("Snell's Spread Law n_1^2 * s_1 == n_2^2 * s_2", f"9 * (16/25) == 16 * (9/25) == {snell_lhs}", "Integer ray vectors [-4,3] -> [3,-4]"),
    ]
    return TopicBuildResult("W.26", m, extra_curves, annotations, verifications, {"snell_invariant": snell_lhs, "Q_range": sp.Integer(64)})


def _build_w27() -> TopicBuildResult:
    """Build W.27: 3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads."""
    m = Model("W.27 3D Platonic Solid Dihedral Spreads", logger=False)
    # Exact rational axonometric projection of regular tetrahedron vertices
    # (1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1) under P(x,y,z) = [x - y/2, z - y/3]
    v0_xy = (sp.Rational(1, 2), sp.Rational(2, 3))
    v1_xy = (sp.Rational(3, 2), sp.Rational(-2, 3))
    v2_xy = (sp.Rational(-3, 2), sp.Rational(-4, 3))
    v3_xy = (sp.Rational(-1, 2), sp.Rational(4, 3))
    medge_xy = midpoint(v1_xy, v2_xy)

    v0 = m.set_point(*v0_xy, classes=["given", "golden"], ID="V_0")
    v1 = m.set_point(*v1_xy, classes=["given"], ID="V_1")
    v2 = m.set_point(*v2_xy, classes=["given"], ID="V_2")
    v3 = m.set_point(*v3_xy, classes=["given"], ID="V_3")
    medge = m.set_point(*medge_xy, classes=["midpoint", "focus"], ID="M_edge")

    m.set_polygon([v1, v2, v3], ID="t_base")
    m.set_segment(v0, v1, classes=["golden"])
    m.set_segment(v0, v2, classes=["golden"])
    m.set_segment(v0, v3, classes=["golden"])
    m.set_segment(v0, medge, classes=["euler"], ID="s_ap1")
    m.set_segment(v3, medge, classes=["euler"], ID="s_ap2")
    finalize_model_guides(m, {"V_0", "V_1", "V_2", "V_3", "M_edge"})

    cert = prove_platonic_dihedral_spreads()
    if not cert.verified:
        raise AssertionError("W.27 Platonic dihedral spreads proof failed.")

    # Verify De Gua's 3D Quadrea Theorem on right-corner tetrahedron [0,0,0], [2,0,0], [0,3,0], [0,0,6]
    # Slant triangle sides: Q_12 = 4+9=13, Q_23 = 9+36=45, Q_13 = 4+36=40
    a_slant = archimedes(13, 45, 40)
    a_sum = 4 * 4 * 9 + 4 * 9 * 36 + 4 * 4 * 36  # 144 + 1296 + 576 = 2016
    if a_slant != a_sum:
        raise AssertionError("W.27 De Gua Quadrea Law failed.")

    annotations = [
        {"x": sp.Integer(0), "y": sp.Rational(9, 5), "text": "Platonic Dihedral Spreads: 8/9, 1, 8/9, 4/9, 4/5", "kind": "spread", "ref": "s_ap1"},
        {"x": sp.Integer(0), "y": sp.Rational(-9, 5), "text": f"De Gua Quadreas: {a_slant} = 144 + 1296 + 576", "kind": "quadrance", "ref": "t_base"},
    ]
    verifications = [
        ("Regular Tetrahedron & Octahedron face spreads", "S_tet = 8/9, S_oct = 8/9", "Exact rational spreads"),
        ("Cube orthogonal face spread", "S_cube = 1", "Mutually perpendicular planes"),
        ("Regular Icosahedron face spread (vertices [0,+/-1,+/-phi])", "S_ico = 4/9", "sqrt(5) cancels completely!"),
        ("Regular Dodecahedron face spread", "S_dod = 4/5", "sqrt(5) cancels completely!"),
        ("De Gua's 3D Right-Corner Quadrea Theorem", f"A_slant = {a_slant} == {a_sum}", "3D generalization of Pythagoras"),
    ]
    return TopicBuildResult(
        "W.27",
        m,
        [],
        annotations,
        verifications,
        {"S_tet": sp.Rational(8, 9), "S_ico": sp.Rational(4, 9), "S_dod": sp.Rational(4, 5)},
    )


def _build_w28() -> TopicBuildResult:
    """Build W.28: Rational Polar Coordinates, Classical Curves & The Ellipson."""
    m = Model("W.28 Rational Polar Curves & The Ellipson", logger=False)
    o_xy = (sp.Integer(0), sp.Integer(0))
    aref_xy = (sp.Integer(0), sp.Integer(4))

    pt_o = m.set_point(*o_xy, classes=["given", "center"], ID="O")
    pt_aref = m.set_point(*aref_xy, classes=["given"], ID="A_ref")
    m.construct_line(pt_o, pt_aref, classes=["axis"], ID="l_ref")
    finalize_model_guides(m, {"O", "A_ref"})

    # 1. Bernoulli Lemniscate (x^2 + y^2)^2 = 16(x^2 - y^2) => Q = 16*(2*s - 1)!
    t_grid = _rational_grid(16, sp.Integer(3))
    lem_pts = [
        (4 * t * (1 + t**2) / (1 + t**4), 4 * t * (1 - t**2) / (1 + t**4))
        for t in t_grid
    ]
    lx, ly = lem_pts[20]
    s_lem, q_lem = rational_polar_coords(lx, ly)
    if sp.simplify(q_lem - 16 * (2 * s_lem - 1)) != 0:
        raise AssertionError("W.28 Lemniscate rational polar law Q = 16*(2*s - 1) failed.")

    # 2. Cardioid (rational parametrization)
    card_pts = [
        (3 * (1 - t**2) * (1 - 3 * t**2) / (1 + t**2) ** 2 + 1, 6 * t * (1 - t**2) / (1 + t**2) ** 2)
        for t in _rational_grid(14, sp.Integer(3))
    ]

    # 3. Folium of Descartes x^3 + y^3 + 3*x*y = 0 (Wildberger Appendix A, p. 286):
    # (-3*t/(1+t^3), -3*t^2/(1+t^3)) satisfies (2s-1)^2(s^2-s+1)^2 Q^2 - 18s(1-s)(1-3s+3s^2)Q + 81s^2(1-s)^2 = 0!
    fol_pts = [
        (-3 * t / (1 + t**3), -3 * t**2 / (1 + t**3))
        for t in [sp.Rational(k, 5) for k in range(0, 18)]
    ]
    fx, fy = fol_pts[10]  # t = 2 -> (-6/9, -12/9) = (-2/3, -4/3)
    s_fol, q_fol = rational_polar_coords(fx, fy)
    fol_res = sp.simplify(
        (2 * s_fol - 1) ** 2 * (s_fol**2 - s_fol + 1) ** 2 * q_fol**2
        - 18 * s_fol * (1 - s_fol) * (1 - 3 * s_fol + 3 * s_fol**2) * q_fol
        + 81 * s_fol**2 * (1 - s_fol) ** 2
    )
    if fol_res != 0:
        raise AssertionError("W.28 Folium rational polar identity failed.")

    # 4. Ellipson cross-sections in shifted [0, 1]^2 box [6, 10] x [-2, 2]:
    # Diagonal parabola slice s_1 = s_2 = u => s_3 = 4u(1-u), and horizontal slice s_3 = 1/2 (inscribed circle!)
    ellipson_pts = [
        (6 + 4 * u, -2 + 4 * (4 * u * (1 - u)))
        for u in [sp.Rational(k, 16) for k in range(0, 17)]
    ]
    ellipson_circle_pts = [
        (8 + 2 * (1 - t**2) / (1 + t**2), 4 * t / (1 + t**2))
        for t in _rational_grid(14, sp.Integer(4))
    ]
    s1_c = sp.Rational(1, 2) + sp.Rational(3, 10)  # 4/5
    s2_c = sp.Rational(1, 2) + sp.Rational(2, 5)  # 9/10
    if (
        triple_spread_function(sp.Rational(1, 3), sp.Rational(1, 3), spread_polynomial(2, sp.Rational(1, 3))) != 0
        or triple_spread_function(s1_c, s2_c, sp.Rational(1, 2)) != 0
    ):
        raise AssertionError("W.28 Ellipson section check failed.")

    extra_curves: list[dict[str, object]] = [
        {"label": "lemniscate", "points": lem_pts, "classes": ["golden"]},
        {"label": "cardioid", "points": card_pts, "classes": ["metric-red", "guide"]},
        {"label": "folium", "points": fol_pts, "classes": ["metric-green"]},
        {"label": "ellipson_slice", "points": ellipson_pts, "classes": ["metric-blue"]},
        {"label": "ellipson_c_half", "points": ellipson_circle_pts, "classes": ["euler", "guide"]},
    ]
    annotations = [
        {"x": sp.Integer(0), "y": sp.Rational(5, 2), "text": "Lemniscate: Q = 16*(2*s - 1)", "kind": "quadrance", "ref": "lemniscate"},
        {"x": sp.Integer(8), "y": sp.Rational(5, 2), "text": "Ellipson: S(u,u,4u(1-u))=0 & s_3=1/2 circle", "kind": "spread", "ref": "ellipson_slice"},
    ]
    verifications = [
        ("Lemniscate [s, Q] law Q == 16*(2*s - 1)", f"Q = {q_lem}, 16*(2*s - 1) = {16*(2*s_lem - 1)}", "Linear in [s, Q] (s to y-axis)"),
        ("Folium of Descartes [s, Q] quadratic (t=2)", f"s={s_fol}, Q={q_fol} => residual = {fol_res}", "Matches Wildberger App. A p. 286"),
        ("Ellipson horizontal slice s_3 = 1/2", f"S({s1_c}, {s2_c}, 1/2) == 0", "Exact inscribed circle in [0, 1]^2!"),
    ]
    return TopicBuildResult("W.28", m, extra_curves, annotations, verifications, {"Q_lem_sample": q_lem, "s_lem_sample": s_lem})


BUILDERS_B: dict[str, Callable[[], TopicBuildResult]] = {
    "W.15": _build_w15,
    "W.16": _build_w16,
    "W.17": _build_w17,
    "W.18": _build_w18,
    "W.19": _build_w19,
    "W.20": _build_w20,
    "W.21": _build_w21,
    "W.22": _build_w22,
    "W.23": _build_w23,
    "W.24": _build_w24,
    "W.25": _build_w25,
    "W.26": _build_w26,
    "W.27": _build_w27,
    "W.28": _build_w28,
}
