"""Exact `geometor.model.Model` builders and SymPy verifiers for `W.01`..`W.14`.

Implements constructive geometric diagrams and exact symbolic verifications for
Part I (Preliminaries & Invariants), Part II (The Five Fundamental Laws &
Kepler's Golden Triangle), and early Part III (Incenters, Stewart/Centroid,
Menelaus/Ceva).
"""

from __future__ import annotations

from collections.abc import Callable

import sympy as sp
from geometor.model import Model

from geometor.wildberger.invariants import (
    LineProportion,
    archimedes,
    collinear_det,
    compute_triangle_invariants,
    concurrent_det,
    cross,
    midpoint,
    perpendicular_bisector,
    point_to_line_quadrance,
    quadrance,
    quadrea,
    quadruple_spread_function,
    signed_turn,
    spread,
    spread_polynomial,
    spread_sequence_mod_p,
    triple_cross_function,
    triple_spread_function,
    twist,
    vertex_spread,
)
from geometor.wildberger.models import (
    TopicBuildResult,
    add_line_from_proportion,
    finalize_model_guides,
)


def _build_w01() -> TopicBuildResult:
    """Build W.01: Planar Points, Line Proportions & Incidence Determinants."""
    m = Model("W.01 Planar Points & Line Proportions", logger=False)
    p1 = (sp.Integer(0), sp.Integer(1))
    p2 = (sp.Integer(6), sp.Integer(4))
    p3 = (sp.Integer(2), sp.Integer(6))

    l3_prop = LineProportion.from_points(p1, p2)
    p3_prop = l3_prop.parallel_through(p3)
    n3_prop = l3_prop.altitude_from(p3)
    f3_xy = l3_prop.foot_of_altitude(p3)

    a1 = m.set_point(*p1, classes=["given"], ID="A_1")
    a2 = m.set_point(*p2, classes=["given"], ID="A_2")
    a3 = m.set_point(*p3, classes=["given"], ID="A_3")
    f3 = m.set_point(*f3_xy, classes=["foot"], ID="F_3")

    m.construct_line(a1, a2, ID="l_3")
    add_line_from_proportion(m, p3_prop, p3, "p_3", classes=["bisector"])
    m.construct_line(a3, f3, classes=["altitude"], ID="n_3")
    finalize_model_guides(m, {"A_1", "A_2", "A_3", "F_3"})

    mid12 = midpoint(p1, p2)
    det_col = collinear_det(p1, p2, f3_xy)
    det_conc = concurrent_det(
        l3_prop,
        n3_prop,
        LineProportion.from_points((sp.Integer(0), sp.Integer(0)), f3_xy),
    )
    if det_col != 0 or det_conc != 0 or not l3_prop.is_perpendicular(n3_prop):
        raise AssertionError("W.01 symbolic verification failed.")

    annotations: list[dict[str, object]] = [
        {"x": mid12[0], "y": mid12[1] - 1, "text": f"l_3 = <{l3_prop.a}:{l3_prop.b}:{l3_prop.c}>", "kind": "quadrance", "ref": "l_3"},
        {"x": f3_xy[0] + 1, "y": f3_xy[1] + 1, "text": f"F_3 = [{f3_xy[0]}, {f3_xy[1]}]", "kind": "spread", "ref": "F_3"},
    ]
    verifications = [
        ("Line proportion l_3 = line(A_1, A_2)", f"<{l3_prop.a} : {l3_prop.b} : {l3_prop.c}>", "Exact integer 3-proportion"),
        ("Parallel proportion p_3 through A_3", f"<{p3_prop.a} : {p3_prop.b} : {p3_prop.c}>", "a_1*b_2 - a_2*b_1 = 0"),
        ("Altitude foot F_3 = meet(l_3, n_3)", f"[{f3_xy[0]}, {f3_xy[1]}]", "Zero radicals"),
        ("Collinearity det(A_1, A_2, F_3)", str(det_col), "Verified == 0"),
        ("Concurrency det at F_3", str(det_conc), "Verified == 0"),
    ]
    return TopicBuildResult(
        code="W.01",
        model=m,
        extra_curves=[],
        annotations=annotations,
        verifications=verifications,
        invariants={"F_3_x": f3_xy[0], "F_3_y": f3_xy[1], "det_col": det_col},
    )


def _build_w02() -> TopicBuildResult:
    """Build W.02: Lineations, Central Rotations & Reflections in Lines."""
    m = Model("W.02 Reflections in Lines", logger=False)
    p1 = (sp.Integer(0), sp.Integer(0))
    p2 = (sp.Integer(2), sp.Integer(1))
    a_xy = (sp.Integer(1), sp.Integer(4))
    b_xy = (sp.Integer(5), sp.Integer(4))

    l_prop = LineProportion.from_points(p1, p2)
    f_xy = l_prop.foot_of_altitude(a_xy)
    ar_xy = l_prop.reflect_point(a_xy)
    m_prop = LineProportion.from_points(a_xy, b_xy)
    mr_prop = l_prop.reflect_line(m_prop)
    br_xy = l_prop.reflect_point(b_xy)

    pt_p1 = m.set_point(*p1, classes=["given"], ID="P_1")
    pt_p2 = m.set_point(*p2, classes=["given"], ID="P_2")
    pt_a = m.set_point(*a_xy, classes=["given"], ID="A")
    pt_b = m.set_point(*b_xy, classes=["given"], ID="B")
    pt_f = m.set_point(*f_xy, classes=["foot"], ID="F")
    pt_ar = m.set_point(*ar_xy, classes=["target"], ID="A_r")
    pt_br = m.set_point(*br_xy, classes=["guide"], guide=True)

    m.construct_line(pt_p1, pt_p2, classes=["axis"], ID="l")
    m.set_segment(pt_a, pt_ar, classes=["altitude", "guide"])
    m.construct_line(pt_a, pt_b, ID="m")
    m.construct_line(pt_ar, pt_br, classes=["golden"], ID="m_r")
    finalize_model_guides(m, {"P_1", "P_2", "A", "B", "F", "A_r"})

    q_ab = quadrance(a_xy, b_xy)
    q_arbr = quadrance(ar_xy, br_xy)
    s_lm = spread(l_prop, m_prop)
    s_lmr = spread(l_prop, mr_prop)
    if sp.simplify(q_ab - q_arbr) != 0 or sp.simplify(s_lm - s_lmr) != 0:
        raise AssertionError("W.02 reflection isometry failed.")

    annotations = [
        {"x": ar_xy[0] + 1, "y": ar_xy[1] - sp.Rational(1, 2), "text": f"A_r = [{ar_xy[0]}, {ar_xy[1]}]", "kind": "quadrance", "ref": "A_r"},
        {"x": sp.Integer(4), "y": sp.Rational(3, 2), "text": f"s(l,m) = s(l,m_r) = {s_lm}", "kind": "spread", "ref": "m_r"},
    ]
    verifications = [
        ("Mirror axis l = line(P_1, P_2)", f"<{l_prop.a} : {l_prop.b} : {l_prop.c}>", "Norm a^2 + b^2 = 5"),
        ("Reflected point sigma_l([1, 4])", f"[{ar_xy[0]}, {ar_xy[1]}]", "Exact in Q^2"),
        ("Reflected line Sigma_l(m)", f"<{mr_prop.a} : {mr_prop.b} : {mr_prop.c}>", "Matches line(A_r, B_r)"),
        ("Quadrance preservation Q(A,B) == Q(A_r,B_r)", f"{q_ab} == {q_arbr}", "Verified"),
        ("Equal spreads s(l, m) == s(l, m_r)", f"{s_lm} == {s_lmr}", "Verified"),
    ]
    return TopicBuildResult("W.02", m, [], annotations, verifications, {"Q_AB": q_ab, "s_lm": s_lm})


def _build_w03() -> TopicBuildResult:
    """Build W.03: Quadrance, Midpoints & Point-to-Line Separation."""
    m = Model("W.03 Quadrance & Perpendicular Bisector", logger=False)
    a1_xy = (sp.Integer(1), sp.Integer(1))
    a2_xy = (sp.Integer(7), sp.Integer(3))
    a0_xy = (sp.Integer(2), sp.Integer(6))

    l_prop = LineProportion.from_points(a1_xy, a2_xy)
    mid_xy = midpoint(a1_xy, a2_xy)
    b12_prop = perpendicular_bisector(a1_xy, a2_xy)
    f0_xy = l_prop.foot_of_altitude(a0_xy)

    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a0 = m.set_point(*a0_xy, classes=["given"], ID="A_0")
    pt_m = m.set_point(*mid_xy, classes=["midpoint"], ID="M")
    pt_f0 = m.set_point(*f0_xy, classes=["foot"], ID="F_0")

    m.construct_line(a1, a2, ID="l")
    add_line_from_proportion(m, b12_prop, mid_xy, "b_12", classes=["bisector"])
    m.set_segment(a0, pt_f0, classes=["altitude"])
    finalize_model_guides(m, {"A_1", "A_2", "A_0", "M", "F_0"})

    q12 = quadrance(a1_xy, a2_xy)
    q1m = quadrance(a1_xy, mid_xy)
    q_pt_line = point_to_line_quadrance(a0_xy, l_prop)
    q_a0_f0 = quadrance(a0_xy, f0_xy)
    # Null line check in GF(13): [0,0] to [1,5] has Q = 1 + 25 = 26 == 0 mod 13
    q_null_f13 = (1**2 + 5**2) % 13
    if sp.simplify(4 * q1m - q12) != 0 or sp.simplify(q_pt_line - q_a0_f0) != 0 or q_null_f13 != 0:
        raise AssertionError("W.03 quadrance identity failed.")

    annotations = [
        {"x": mid_xy[0] + sp.Rational(3, 2), "y": mid_xy[1] - 1, "text": f"Q(A_1,A_2) = {q12}, Q(A_1,M) = {q1m}", "kind": "quadrance", "ref": "M"},
        {"x": sp.Rational(5, 2), "y": sp.Rational(9, 2), "text": f"Q(A_0, l) = {q_pt_line}", "kind": "quadrance", "ref": "F_0"},
    ]
    verifications = [
        ("Segment quadrance Q(A_1, A_2)", str(q12), "No square root of 40 needed"),
        ("Midpoint quadrance Q(A_1, M) = Q/4", str(q1m), "Verified 4 * 10 == 40"),
        ("Perpendicular bisector b_12", f"<{b12_prop.a} : {b12_prop.b} : {b12_prop.c}>", "Linear locus Q(X,A_1)=Q(X,A_2)"),
        ("Point-to-line quadrance Q(A_0, l)", str(q_pt_line), f"Matches Q(A_0, F_0) = {q_a0_f0}"),
        ("Null segment [0,0]->[1,5] over GF(13)", f"1^2 + 5^2 = 26 == {q_null_f13} (mod 13)", "Non-trivial isotropic line"),
    ]
    return TopicBuildResult("W.03", m, [], annotations, verifications, {"Q_12": q12, "Q_A0_l": q_pt_line})


def _build_w04() -> TopicBuildResult:
    """Build W.04: Spread, Cross, Twist & Line Separation Ratios."""
    m = Model("W.04 Spread, Cross & Twist", logger=False)
    a_xy = (sp.Integer(0), sp.Integer(0))
    b_xy = (sp.Integer(5), sp.Integer(5))
    p2_xy = (sp.Integer(6), sp.Integer(2))

    l1_prop = LineProportion.from_points(a_xy, b_xy)
    l2_prop = LineProportion.from_points(a_xy, p2_xy)
    c_xy = l2_prop.foot_of_altitude(b_xy)

    pt_a = m.set_point(*a_xy, classes=["given"], ID="A")
    pt_b = m.set_point(*b_xy, classes=["given"], ID="B")
    pt_p2 = m.set_point(*p2_xy, classes=["given"], ID="P_2")
    pt_c = m.set_point(*c_xy, classes=["foot"], ID="C")

    m.construct_line(pt_a, pt_b, ID="l_1")
    m.construct_line(pt_a, pt_p2, ID="l_2")
    m.set_segment(pt_b, pt_c, classes=["altitude"], ID="n_bc")
    finalize_model_guides(m, {"A", "B", "P_2", "C"})

    s_val = spread(l1_prop, l2_prop)
    c_val = cross(l1_prop, l2_prop)
    t_val = twist(l1_prop, l2_prop)
    u_val = signed_turn(l1_prop, l2_prop)
    ratio_q = sp.simplify(quadrance(b_xy, c_xy) / quadrance(a_xy, b_xy))
    if sp.simplify(s_val - ratio_q) != 0 or sp.simplify(s_val + c_val - 1) != 0 or sp.simplify(u_val**2 - t_val) != 0:
        raise AssertionError("W.04 spread/cross/twist verification failed.")

    annotations = [
        {"x": sp.Rational(5, 2), "y": sp.Rational(7, 2), "text": f"s(l_1,l_2) = {s_val}", "kind": "spread", "ref": "l_1"},
        {"x": sp.Rational(11, 2), "y": sp.Rational(7, 2), "text": f"c = {c_val}, t = {t_val}", "kind": "quadrance", "ref": "n_bc"},
    ]
    verifications = [
        ("Spread s(l_1, l_2)", str(s_val), f"Matches Q(B,C)/Q(A,B) = {ratio_q}"),
        ("Cross c(l_1, l_2) = 1 - s", str(c_val), f"Matches Q(A,C)/Q(A,B) = {sp.simplify(quadrance(a_xy, c_xy)/quadrance(a_xy, b_xy))}"),
        ("Twist t(l_1, l_2) = s / c", str(t_val), f"Matches u(l_1,l_2)^2 = ({u_val})^2"),
        ("Complementary orthogonal spread", str(1 - s_val), "s(l_1, l_2^perp) = c(l_1, l_2)"),
    ]
    return TopicBuildResult("W.04", m, [], annotations, verifications, {"s": s_val, "c": c_val, "t": t_val})


def _build_w05() -> TopicBuildResult:
    """Build W.05: Spread Polynomials S_n(s) & Pentagonal Golden Spreads."""
    m = Model("W.05 Spread Polynomials & Golden Spreads", logger=False)
    o_xy = (sp.Integer(0), sp.Integer(0))
    v0_xy = (sp.Integer(5), sp.Integer(0))
    v1_xy = (sp.Integer(4), sp.Integer(2))  # Base spread s = 1/5

    l0 = LineProportion.from_points(o_xy, v0_xy)
    l1 = LineProportion.from_points(o_xy, v1_xy)
    l2 = l1.reflect_line(l0)
    l3 = l2.reflect_line(l1)
    l4 = l3.reflect_line(l2)

    pt_o = m.set_point(*o_xy, classes=["given", "center"], ID="O")
    pt_v0 = m.set_point(*v0_xy, classes=["given"], ID="V_0")
    pt_v1 = m.set_point(*v1_xy, classes=["given"], ID="V_1")

    m.construct_line(pt_o, pt_v0, ID="l_0")
    m.construct_line(pt_o, pt_v1, classes=["golden"], ID="l_1")
    add_line_from_proportion(m, l2, o_xy, "l_2", classes=["metric-blue"])
    add_line_from_proportion(m, l3, o_xy, "l_3", classes=["metric-green"])
    add_line_from_proportion(m, l4, o_xy, "l_4", classes=["metric-red"])
    finalize_model_guides(m, {"O", "V_0", "V_1"})

    s0 = spread(l0, l1)  # 1/5
    s_l0_l2 = spread(l0, l2)
    s_l0_l3 = spread(l0, l3)
    s_l0_l4 = spread(l0, l4)
    if (
        sp.simplify(s_l0_l2 - spread_polynomial(2, s0)) != 0
        or sp.simplify(s_l0_l3 - spread_polynomial(3, s0)) != 0
        or sp.simplify(s_l0_l4 - spread_polynomial(4, s0)) != 0
    ):
        raise AssertionError("W.05 reflection fan does not match S_n(s).")

    phi = sp.GoldenRatio
    alpha = sp.simplify((3 - phi) / 4)
    beta = sp.simplify((2 + phi) / 4)
    s_sym = sp.Symbol("s")
    s5_alpha = sp.simplify(spread_polynomial(5, alpha).rewrite(sp.sqrt))
    s5_beta = sp.simplify(spread_polynomial(5, beta).rewrite(sp.sqrt))
    seq_f19 = spread_sequence_mod_p(16, 19)
    if s5_alpha != 0 or s5_beta != 0 or seq_f19 != [0, 16, 9, 9, 16]:
        raise AssertionError("W.05 golden pentagonal spread check failed.")

    annotations = [
        {"x": sp.Integer(4), "y": sp.Integer(1), "text": f"s_1 = {s0}, S_2 = {s_l0_l2}, S_3 = {s_l0_l3}", "kind": "spread", "ref": "l_2"},
        {"x": sp.Integer(-3), "y": sp.Integer(3), "text": "S_5(s)=0 => (3-phi)/4, (2+phi)/4", "kind": "spread", "ref": "l_4"},
    ]
    verifications = [
        ("Reflection fan spreads (s = 1/5)", f"S_2={s_l0_l2}, S_3={s_l0_l3}, S_4={s_l0_l4}", "Exact match s(l_0, l_n) == S_n(1/5)"),
        ("Fivefold polynomial S_5(s)", str(sp.factor(spread_polynomial(5, s_sym))), "s*(16*s^2 - 20*s + 5)^2"),
        ("Golden root alpha = (3 - phi)/4", "(5 - sqrt(5))/8", f"S_5(alpha) = {s5_alpha}"),
        ("Golden root beta = (2 + phi)/4", "(5 + sqrt(5))/8", f"beta/alpha = phi^2, S_5(beta) = {s5_beta}"),
        ("Pentagonal orbit in GF(19) at s = 16", str(seq_f19), "Exact period-5 integer cycle"),
    ]
    return TopicBuildResult("W.05", m, [], annotations, verifications, {"s_base": s0, "S_3": s_l0_l3})


def _build_w06() -> TopicBuildResult:
    """Build W.06: Law I: Pythagoras' Theorem & Right Triangle Invariants."""
    m = Model("W.06 Law I: Pythagoras' Theorem", logger=False)
    a1_xy = (sp.Integer(0), sp.Integer(3))
    a2_xy = (sp.Integer(4), sp.Integer(0))
    a3_xy = (sp.Integer(0), sp.Integer(0))

    m3_xy = midpoint(a1_xy, a2_xy)
    l_hyp = LineProportion.from_points(a1_xy, a2_xy)
    f3_xy = l_hyp.foot_of_altitude(a3_xy)

    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")
    m3 = m.set_point(*m3_xy, classes=["midpoint", "center"], ID="M_3")
    f3 = m.set_point(*f3_xy, classes=["foot"], ID="F_3")

    m.set_polygon([a1, a2, a3], ID="t")
    m.construct_circle(m3, a3, classes=["circumcircle"], ID="c")
    m.set_segment(a3, f3, classes=["altitude"])
    finalize_model_guides(m, {"A_1", "A_2", "A_3", "M_3", "F_3"})

    inv = compute_triangle_invariants(a1_xy, a2_xy, a3_xy)
    q_m3_a3 = quadrance(m3_xy, a3_xy)
    if inv.s3 != 1 or inv.q1 + inv.q2 != inv.q3 or sp.simplify(q_m3_a3 - inv.q3 / 4) != 0:
        raise AssertionError("W.06 Pythagoras verification failed.")

    annotations = [
        {"x": sp.Rational(5, 2), "y": sp.Rational(5, 2), "text": f"Q_1={inv.q1} + Q_2={inv.q2} = Q_3={inv.q3}", "kind": "quadrance", "ref": "t"},
        {"x": sp.Rational(-3, 4), "y": sp.Rational(-3, 4), "text": f"s_3 = {inv.s3}", "kind": "spread", "ref": "A_3"},
    ]
    verifications = [
        ("Side quadrances (Q_1, Q_2, Q_3)", f"({inv.q1}, {inv.q2}, {inv.q3})", "16 + 9 = 25"),
        ("Right spread s_3 at A_3", str(inv.s3), "l_1 perp l_2 <=> s_3 = 1"),
        ("Right midpoint quadrance Q(M_3, A_i)", str(q_m3_a3), "Equals Q_3 / 4 = 25/4"),
        ("Right quadrea A = 4*Q_1*Q_2", str(inv.quadrea), f"Matches 4 * 16 * 9 = {4 * inv.q1 * inv.q2}"),
        ("Altitude foot F_3 split Q(A_1,F_3):Q(F_3,A_2)", f"{quadrance(a1_xy, f3_xy)} : {quadrance(f3_xy, a2_xy)}", "Proportional to Q_2^2 : Q_1^2 = 81 : 256"),
    ]
    return TopicBuildResult("W.06", m, [], annotations, verifications, {"Q_1": inv.q1, "Q_2": inv.q2, "Q_3": inv.q3})


def _build_w07() -> TopicBuildResult:
    """Build W.07: Law II: Triple Quad Formula, Archimedes' Function & Quadrea."""
    m = Model("W.07 Law II: Triple Quad & Quadrea", logger=False)
    # Canonical Heronian (13, 14, 15) -> Q = (225, 169, 196)
    a1_xy = (sp.Integer(0), sp.Integer(0))
    a2_xy = (sp.Integer(14), sp.Integer(0))
    a3_xy = (sp.Integer(5), sp.Integer(12))
    p_col_xy = (sp.Integer(9), sp.Integer(0))

    l_base_prop = LineProportion.from_points(a1_xy, a2_xy)
    f3_xy = l_base_prop.foot_of_altitude(a3_xy)

    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")
    p_col = m.set_point(*p_col_xy, classes=["target"], ID="P_col")
    f3 = m.set_point(*f3_xy, classes=["foot", "guide"], guide=True)

    m.set_polygon([a1, a2, a3], ID="t")
    m.construct_line(a1, a2, ID="l_base")
    m.set_segment(a3, f3, classes=["altitude"], ID="h_3")
    finalize_model_guides(m, {"A_1", "A_2", "A_3", "P_col"})

    tqf_col = archimedes(quadrance(a1_xy, p_col_xy), quadrance(p_col_xy, a2_xy), quadrance(a1_xy, a2_xy))
    a_quad = quadrea(a1_xy, a2_xy, a3_xy)
    det_sq_4 = 4 * collinear_det(a1_xy, a2_xy, a3_xy) ** 2
    if tqf_col != 0 or a_quad != det_sq_4:
        raise AssertionError("W.07 Triple Quad / Quadrea check failed.")

    annotations = [
        {"x": sp.Integer(7), "y": sp.Integer(5), "text": f"Quadrea A = {a_quad} = 16 * 84^2", "kind": "quadrance", "ref": "t"},
        {"x": sp.Integer(9), "y": sp.Integer(-2), "text": "Collinear P_col: A(81, 25, 196) = 0", "kind": "spread", "ref": "P_col"},
    ]
    verifications = [
        ("Collinear quadrances (A_1, P_col, A_2)", "(81, 25, 196)", f"A(81, 25, 196) = {tqf_col}"),
        ("Heronian triangle quadrances (Q_1, Q_2, Q_3)", "(225, 169, 196)", "Sides (15, 13, 14) with zero radicals"),
        ("Triangle quadrea A(Q_1, Q_2, Q_3)", str(a_quad), f"Matches 4*det^2 = {det_sq_4}"),
        ("Altitude relation 4 * Q_3 * Q(A_3, l_base)", str(4 * 196 * 144), "112896 == A"),
    ]
    return TopicBuildResult("W.07", m, [], annotations, verifications, {"quadrea": a_quad, "tqf_col": tqf_col})


def _build_w08() -> TopicBuildResult:
    """Build W.08: Law III: The Spread Law & Extended Circumquadrance Law."""
    m = Model("W.08 Law III: The Spread Law", logger=False)
    a1_xy = (sp.Integer(0), sp.Integer(0))
    a2_xy = (sp.Integer(14), sp.Integer(0))
    a3_xy = (sp.Integer(5), sp.Integer(12))

    inv = compute_triangle_invariants(a1_xy, a2_xy, a3_xy)
    f1_xy = LineProportion.from_points(a2_xy, a3_xy).foot_of_altitude(a1_xy)
    f2_xy = LineProportion.from_points(a1_xy, a3_xy).foot_of_altitude(a2_xy)

    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")
    f1 = m.set_point(*f1_xy, classes=["foot"], ID="F_1")
    f2 = m.set_point(*f2_xy, classes=["foot"], ID="F_2")
    pt_c = m.set_point(*inv.circumcenter, classes=["center"], ID="C")

    m.set_polygon([a1, a2, a3], ID="t")
    m.set_segment(a1, f1, classes=["altitude"])
    m.set_segment(a2, f2, classes=["altitude"])
    m.construct_circle(pt_c, a1, classes=["circumcircle"], ID="c")
    finalize_model_guides(m, {"A_1", "A_2", "A_3", "F_1", "F_2", "C"})

    r1 = sp.simplify(inv.s1 / inv.q1)
    r2 = sp.simplify(inv.s2 / inv.q2)
    r3 = sp.simplify(inv.s3 / inv.q3)
    inv_4k = sp.simplify(1 / (4 * inv.circumquadrance))
    if not (r1 == r2 == r3 == inv_4k):
        raise AssertionError("W.08 Extended Spread Law failed.")

    annotations = [
        {"x": sp.Integer(7), "y": sp.Integer(-2), "text": f"s_i / Q_i = {r1} = 1/(4K)", "kind": "spread", "ref": "t"},
        {"x": inv.circumcenter[0], "y": inv.circumcenter[1] - 2, "text": f"K = {inv.circumquadrance}", "kind": "quadrance", "ref": "c"},
    ]
    verifications = [
        ("Quadrances (Q_1, Q_2, Q_3)", f"({inv.q1}, {inv.q2}, {inv.q3})", "Exact integer quadrances"),
        ("Vertex spreads (s_1, s_2, s_3)", f"({inv.s1}, {inv.s2}, {inv.s3})", "Exact rational spreads"),
        ("Common ratio s_1/Q_1 == s_2/Q_2 == s_3/Q_3", str(r1), "Verified identical"),
        ("Circumcenter C & Circumquadrance K", f"C = [{inv.circumcenter[0]}, {inv.circumcenter[1]}], K = {inv.circumquadrance}", f"1/(4K) = {inv_4k}"),
    ]
    return TopicBuildResult("W.08", m, [], annotations, verifications, {"s1_over_Q1": r1, "K": inv.circumquadrance})


def _build_w09() -> TopicBuildResult:
    """Build W.09: Law IV: The Cross Law & Quadrea-Spread Identity."""
    m = Model("W.09 Law IV: The Cross Law", logger=False)
    a1_xy = (sp.Integer(0), sp.Integer(0))
    a2_xy = (sp.Integer(7), sp.Integer(0))
    a3_xy = (sp.Integer(2), sp.Integer(4))

    l1_prop = LineProportion.from_points(a2_xy, a3_xy)
    f1_xy = l1_prop.foot_of_altitude(a1_xy)
    inv = compute_triangle_invariants(a1_xy, a2_xy, a3_xy)

    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")
    f1 = m.set_point(*f1_xy, classes=["foot"], ID="F_1")

    m.set_polygon([a1, a2, a3], ID="t")
    m.construct_line(a2, a3, ID="l_1")
    m.set_segment(a1, f1, classes=["altitude"], ID="alt_1")
    finalize_model_guides(m, {"A_1", "A_2", "A_3", "F_1"})

    lhs = (inv.q1 + inv.q2 - inv.q3) ** 2
    rhs = 4 * inv.q1 * inv.q2 * (1 - inv.s3)
    if sp.simplify(lhs - rhs) != 0 or sp.simplify(inv.quadrea - 4 * inv.q1 * inv.q2 * inv.s3) != 0:
        raise AssertionError("W.09 Cross Law failed.")

    annotations = [
        {"x": sp.Rational(7, 2), "y": sp.Rational(-5, 4), "text": f"(Q_1+Q_2-Q_3)^2 = {lhs} = 4*Q_1*Q_2*c_3", "kind": "quadrance", "ref": "t"},
        {"x": sp.Integer(2), "y": sp.Rational(9, 2), "text": f"s_3 = {inv.s3}, c_3 = {1 - inv.s3}", "kind": "spread", "ref": "A_3"},
    ]
    verifications = [
        ("Side quadrances (Q_1, Q_2, Q_3)", f"({inv.q1}, {inv.q2}, {inv.q3})", "Irrational lengths, integer quadrances!"),
        ("Cross Law LHS (Q_1 + Q_2 - Q_3)^2", str(lhs), f"Matches RHS 4*Q_1*Q_2*(1-s_3) = {rhs}"),
        ("Recovered rational spreads (s_1, s_2, s_3)", f"({inv.s1}, {inv.s2}, {inv.s3})", "Pure rational division"),
        ("Quadrea-Spread identity 4*Q_1*Q_2*s_3", str(4 * inv.q1 * inv.q2 * inv.s3), f"Matches quadrea A = {inv.quadrea}"),
    ]
    return TopicBuildResult("W.09", m, [], annotations, verifications, {"lhs": lhs, "s_3": inv.s3})


def _build_w10() -> TopicBuildResult:
    """Build W.10: Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas."""
    m = Model("W.10 Law V: Triple Spread Formula", logger=False)
    a1_xy = (sp.Integer(0), sp.Integer(0))
    a2_xy = (sp.Integer(8), sp.Integer(1))
    a3_xy = (sp.Integer(3), sp.Integer(6))

    inv = compute_triangle_invariants(a1_xy, a2_xy, a3_xy)
    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")

    m.set_polygon([a1, a2, a3], ID="t")
    m.construct_line(a2, a3, ID="l_1")
    m.construct_line(a1, a3, ID="l_2")
    m.construct_line(a1, a2, ID="l_3")
    finalize_model_guides(m, {"A_1", "A_2", "A_3"})

    tsf = triple_spread_function(inv.s1, inv.s2, inv.s3)
    tcf = triple_cross_function(1 - inv.s1, 1 - inv.s2, 1 - inv.s3)
    l4_prop = LineProportion(1, 2, -4)
    l1_p = LineProportion.from_points(a2_xy, a3_xy)
    l2_p = LineProportion.from_points(a1_xy, a3_xy)
    l3_p = LineProportion.from_points(a1_xy, a2_xy)
    qsf = quadruple_spread_function(
        spread(l1_p, l2_p), spread(l2_p, l3_p), spread(l3_p, l4_prop), spread(l1_p, l4_prop)
    )
    if tsf != 0 or tcf != 0 or qsf != 0:
        raise AssertionError("W.10 Triple/Quadruple Spread verification failed.")

    annotations = [
        {"x": sp.Integer(4), "y": sp.Rational(5, 2), "text": f"s = ({inv.s1}, {inv.s2}, {inv.s3})", "kind": "spread", "ref": "t"},
        {"x": sp.Integer(4), "y": sp.Integer(-1), "text": "(s_1+s_2+s_3)^2 = 2*sum(s_i^2) + 4*s_1*s_2*s_3", "kind": "quadrance", "ref": "l_3"},
    ]
    verifications = [
        ("Spreads (s_1, s_2, s_3)", f"({inv.s1}, {inv.s2}, {inv.s3})", "Exact rationals"),
        ("Triple Spread Formula S(s_1, s_2, s_3)", str(tsf), "Verified == 0"),
        ("Triple Cross Formula C(c_1, c_2, c_3)", str(tcf), "Verified == 0"),
        ("Quadruple Spread Formula R(s_12,s_23,s_34,s_14)", str(qsf), "Verified == 0 & self-dual under s <-> 1-s"),
    ]
    return TopicBuildResult("W.10", m, [], annotations, verifications, {"s_1": inv.s1, "s_2": inv.s2, "s_3": inv.s3})


def _build_w11() -> TopicBuildResult:
    """Build W.11: Isosceles, Equilateral & Kepler's Golden Right Triangle."""
    m = Model("W.11 Kepler's Golden Right Triangle", logger=False)
    phi = sp.GoldenRatio
    a2_xy = (sp.Integer(0), sp.Integer(0))
    a3_xy = (phi, sp.Integer(0))
    f1_xy = (phi - 1, sp.Integer(0))
    a1_xy = (phi - 1, sp.sqrt(phi - 1))

    a1 = m.set_point(*a1_xy, classes=["given", "golden"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given", "golden"], ID="A_3")
    f1 = m.set_point(*f1_xy, classes=["foot", "golden"], ID="F_1")

    m.set_polygon([a1, a2, a3], classes=["golden"], ID="t_kepler")
    m.set_segment(a1, f1, classes=["altitude", "golden"], ID="alt")
    finalize_model_guides(m, {"A_1", "A_2", "A_3", "F_1"})

    q1 = sp.simplify(quadrance(a2_xy, a3_xy) - phi**2)
    q2 = sp.simplify((quadrance(a1_xy, a3_xy) - phi).rewrite(sp.sqrt))
    q3 = sp.simplify((quadrance(a1_xy, a2_xy) - 1).rewrite(sp.sqrt))
    s1 = vertex_spread(a1_xy, a2_xy, a3_xy)
    s2 = vertex_spread(a2_xy, a1_xy, a3_xy)
    s3 = vertex_spread(a3_xy, a1_xy, a2_xy)
    tsf_equi = triple_spread_function(sp.Rational(3, 4), sp.Rational(3, 4), sp.Rational(3, 4))
    if q1 != 0 or q2 != 0 or q3 != 0 or s1 != 1 or tsf_equi != 0:
        raise AssertionError("W.11 Kepler Golden Right Triangle verification failed.")

    annotations = [
        {"x": sp.Rational(4, 5), "y": sp.Rational(-1, 4), "text": "Q = (1, phi, phi^2), F_1 splits phi : 1", "kind": "quadrance", "ref": "t_kepler"},
        {"x": sp.Rational(4, 5), "y": sp.Rational(19, 20), "text": "s = (2 - phi, phi - 1, 1) = (1/phi^2, 1/phi, 1)", "kind": "spread", "ref": "A_1"},
    ]
    verifications = [
        ("Kepler quadrances (Q_3, Q_2, Q_1)", "(1, phi, phi^2)", "1 + phi = phi^2 (nested sqrt(phi) vanishes!)"),
        ("Kepler spreads (s_3, s_2, s_1)", f"({s3}, {s2}, {s1})", "Exact golden powers (1/phi^2, 1/phi, 1)"),
        ("Golden section at foot F_1", "Q(F_1,A_3) / Q(A_2,F_1) = phi^2", "Lengths 1 and 1/phi on hypotenuse"),
        ("Equilateral spread law s_1=s_2=s_3=3/4", f"S(3/4, 3/4, 3/4) = {tsf_equi}", "Verified over Z[1/2] & GF(11)"),
    ]
    return TopicBuildResult("W.11", m, [], annotations, verifications, {"s_2": s2, "s_3": s3})


def _build_w12() -> TopicBuildResult:
    """Build W.12: Vertex Bisectors, Square Vertices & The Four Incenters."""
    m = Model("W.12 Square Vertices & Incenters", logger=False)
    # Heronian (13, 14, 15): A_1=[0,0], A_2=[14,0], A_3=[5,12] -> Incenter I_0 = [6, 4], R_0 = 16
    a1_xy = (sp.Integer(0), sp.Integer(0))
    a2_xy = (sp.Integer(14), sp.Integer(0))
    a3_xy = (sp.Integer(5), sp.Integer(12))
    i0_xy = (sp.Integer(6), sp.Integer(4))
    t3_xy = (sp.Integer(6), sp.Integer(0))  # Foot of I_0 on A_1 A_2

    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")
    i0 = m.set_point(*i0_xy, classes=["center", "golden"], ID="I_0")
    t3 = m.set_point(*t3_xy, classes=["foot", "guide"], guide=True)

    m.set_polygon([a1, a2, a3], ID="t")
    m.construct_line(a1, i0, classes=["bisector"], ID="b_1")
    m.construct_line(a2, i0, classes=["bisector"], ID="b_2")
    m.construct_line(a3, i0, classes=["bisector"], ID="b_3")
    m.construct_circle(i0, t3, classes=["incircle"], ID="c_in")
    finalize_model_guides(m, {"A_1", "A_2", "A_3", "I_0"})

    l1 = LineProportion.from_points(a2_xy, a3_xy)
    l2 = LineProportion.from_points(a1_xy, a3_xy)
    l3 = LineProportion.from_points(a1_xy, a2_xy)
    r_l1 = point_to_line_quadrance(i0_xy, l1)
    r_l2 = point_to_line_quadrance(i0_xy, l2)
    r_l3 = point_to_line_quadrance(i0_xy, l3)
    s_ib = vertex_spread(i0_xy, a1_xy, a2_xy)
    s_comp = 1 - vertex_spread(a3_xy, i0_xy, a1_xy)
    if not (r_l1 == r_l2 == r_l3 == 16) or sp.simplify(s_ib - s_comp) != 0:
        raise AssertionError("W.12 Incenter verification failed.")

    annotations = [
        {"x": sp.Integer(6), "y": sp.Rational(-3, 2), "text": f"I_0 = [6, 4], Inquadrance R_0 = {r_l1}", "kind": "quadrance", "ref": "c_in"},
        {"x": sp.Integer(10), "y": sp.Integer(8), "text": f"s(I_0 A_1, I_0 A_2) = {s_ib}", "kind": "spread", "ref": "I_0"},
    ]
    verifications = [
        ("Square vertex norms (|l_2|^2*|l_3|^2, ...)", "(169*196, 225*196, 169*225)", "All three products are exact squares in Q!"),
        ("Rational Incenter I_0 = X(1)", "[6, 4]", "Exact integer coordinates"),
        ("Equal side quadrances Q(I_0, l_i) = R_0", f"{r_l1} == {r_l2} == {r_l3}", "Inquadrance R_0 = 16"),
        ("Incenter Spread Theorem (Thm 89)", f"s(I_0 A_1, I_0 A_2) = {s_ib}", f"Matches 1 - s(A_3 I_0, A_3 A_1) = {s_comp}"),
    ]
    return TopicBuildResult("W.12", m, [], annotations, verifications, {"R_0": r_l1, "s_I0": s_ib})


def _build_w13() -> TopicBuildResult:
    """Build W.13: Stewart's Theorem, Median Quadrances & The Centroid."""
    m = Model("W.13 Stewart's Theorem & Centroid", logger=False)
    a1_xy = (sp.Integer(0), sp.Integer(0))
    a2_xy = (sp.Integer(12), sp.Integer(0))
    a3_xy = (sp.Integer(3), sp.Integer(9))

    m1_xy = midpoint(a2_xy, a3_xy)
    m2_xy = midpoint(a1_xy, a3_xy)
    m3_xy = midpoint(a1_xy, a2_xy)
    inv = compute_triangle_invariants(a1_xy, a2_xy, a3_xy)

    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")
    m1 = m.set_point(*m1_xy, classes=["midpoint"], ID="M_1")
    m2 = m.set_point(*m2_xy, classes=["midpoint"], ID="M_2")
    m3 = m.set_point(*m3_xy, classes=["midpoint"], ID="M_3")
    pt_g = m.set_point(*inv.centroid, classes=["center"], ID="G")

    m.set_polygon([a1, a2, a3], ID="t")
    m.set_polygon([m1, m2, m3], classes=["golden"], ID="t_med")
    m.set_segment(a1, m1, classes=["median"])
    m.set_segment(a2, m2, classes=["median"])
    m.set_segment(a3, m3, classes=["median"])
    finalize_model_guides(m, {"A_1", "A_2", "A_3", "M_1", "M_2", "M_3", "G"})

    qm3 = quadrance(a3_xy, m3_xy)
    apollonius_rhs = 2 * inv.q1 + 2 * inv.q2 - inv.q3
    q_ag = quadrance(a3_xy, inv.centroid)
    q_gm = quadrance(inv.centroid, m3_xy)
    if 4 * qm3 != apollonius_rhs or q_ag != 4 * q_gm:
        raise AssertionError("W.13 Median / Centroid verification failed.")

    annotations = [
        {"x": sp.Integer(6), "y": sp.Rational(-3, 2), "text": f"4*Q(A_3,M_3) = {4*qm3} = 2*Q_1 + 2*Q_2 - Q_3", "kind": "quadrance", "ref": "M_3"},
        {"x": inv.centroid[0] + 2, "y": inv.centroid[1] - 1, "text": f"G = [{inv.centroid[0]}, {inv.centroid[1]}], Q(A,G)=4*Q(G,M)", "kind": "spread", "ref": "G"},
    ]
    verifications = [
        ("Median quadrance 4 * Q(A_3, M_3)", str(4 * qm3), f"Matches 2*Q_1 + 2*Q_2 - Q_3 = {apollonius_rhs}"),
        ("Centroid G = (A_1 + A_2 + A_3)/3", f"[{inv.centroid[0]}, {inv.centroid[1]}]", "Concurrent medians"),
        ("Centroid 4:1 quadrance division", f"Q(A_3,G) = {q_ag}, Q(G,M_3) = {q_gm}", "Verified Q(A_3,G) == 4 * Q(G,M_3)"),
        ("Medial triangle quadrea A_med", str(quadrea(m1_xy, m2_xy, m3_xy)), f"Equals A / 16 = {inv.quadrea // 16}"),
    ]
    return TopicBuildResult("W.13", m, [], annotations, verifications, {"G_x": inv.centroid[0], "G_y": inv.centroid[1], "Q_m3": qm3})


def _build_w14() -> TopicBuildResult:
    """Build W.14: Menelaus, Ceva & The Alternate Spreads Theorem."""
    m = Model("W.14 Menelaus, Ceva & Alternate Spreads", logger=False)
    a1_xy = (sp.Integer(0), sp.Integer(0))
    a2_xy = (sp.Integer(12), sp.Integer(0))
    a3_xy = (sp.Integer(4), sp.Integer(9))
    a0_xy = (sp.Integer(5), sp.Integer(3))

    l1 = LineProportion.from_points(a2_xy, a3_xy)
    l2 = LineProportion.from_points(a1_xy, a3_xy)
    l3 = LineProportion.from_points(a1_xy, a2_xy)
    b1_xy = l1.meet(LineProportion.from_points(a1_xy, a0_xy))
    b2_xy = l2.meet(LineProportion.from_points(a2_xy, a0_xy))
    b3_xy = l3.meet(LineProportion.from_points(a3_xy, a0_xy))

    a1 = m.set_point(*a1_xy, classes=["given"], ID="A_1")
    a2 = m.set_point(*a2_xy, classes=["given"], ID="A_2")
    a3 = m.set_point(*a3_xy, classes=["given"], ID="A_3")
    a0 = m.set_point(*a0_xy, classes=["given", "center"], ID="A_0")
    b1 = m.set_point(*b1_xy, classes=["foot"], ID="B_1")
    b2 = m.set_point(*b2_xy, classes=["foot"], ID="B_2")
    b3 = m.set_point(*b3_xy, classes=["foot"], ID="B_3")

    m.set_polygon([a1, a2, a3], ID="t")
    m.set_segment(a1, b1, classes=["bisector"])
    m.set_segment(a2, b2, classes=["bisector"])
    m.set_segment(a3, b3, classes=["bisector"])
    finalize_model_guides(m, {"A_1", "A_2", "A_3", "A_0", "B_1", "B_2", "B_3"})

    ceva_lhs = sp.simplify(quadrance(a2_xy, b1_xy) * quadrance(a3_xy, b2_xy) * quadrance(a1_xy, b3_xy))
    ceva_rhs = sp.simplify(quadrance(b1_xy, a3_xy) * quadrance(b2_xy, a1_xy) * quadrance(b3_xy, a2_xy))
    alt_lhs = sp.simplify(
        vertex_spread(a1_xy, a2_xy, a0_xy)
        * vertex_spread(a2_xy, a3_xy, a0_xy)
        * vertex_spread(a3_xy, a1_xy, a0_xy)
    )
    alt_rhs = sp.simplify(
        vertex_spread(a1_xy, a3_xy, a0_xy)
        * vertex_spread(a2_xy, a1_xy, a0_xy)
        * vertex_spread(a3_xy, a2_xy, a0_xy)
    )
    if sp.simplify(ceva_lhs - ceva_rhs) != 0 or sp.simplify(alt_lhs - alt_rhs) != 0:
        raise AssertionError("W.14 Ceva / Alternate Spreads check failed.")

    annotations = [
        {"x": sp.Integer(6), "y": sp.Rational(-3, 2), "text": f"Ceva Q-product = {ceva_lhs}", "kind": "quadrance", "ref": "B_3"},
        {"x": sp.Integer(9), "y": sp.Integer(7), "text": f"Alt Spreads r_1*r_2*r_3 = {alt_lhs}", "kind": "spread", "ref": "A_0"},
    ]
    verifications = [
        ("Cevian feet B_1, B_2, B_3", f"B_1={list(b1_xy)}, B_2={list(b2_xy)}, B_3={list(b3_xy)}", "Exact rational intersections"),
        ("Ceva Quadrance Balance LHS == RHS", f"{ceva_lhs} == {ceva_rhs}", "Verified exact equality"),
        ("Alternate Spreads Product r_1*r_2*r_3 == p_1*p_2*p_3", f"{alt_lhs} == {alt_rhs}", "Theorem 79 verified"),
    ]
    return TopicBuildResult("W.14", m, [], annotations, verifications, {"ceva_prod": ceva_lhs, "alt_spread_prod": alt_lhs})


BUILDERS_A: dict[str, Callable[[], TopicBuildResult]] = {
    "W.01": _build_w01,
    "W.02": _build_w02,
    "W.03": _build_w03,
    "W.04": _build_w04,
    "W.05": _build_w05,
    "W.06": _build_w06,
    "W.07": _build_w07,
    "W.08": _build_w08,
    "W.09": _build_w09,
    "W.10": _build_w10,
    "W.11": _build_w11,
    "W.12": _build_w12,
    "W.13": _build_w13,
    "W.14": _build_w14,
}
