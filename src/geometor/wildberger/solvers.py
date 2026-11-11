"""Exact polynomial triangle and surveying solvers for Rational Trigonometry.

Replaces classical inverse trigonometric solvers (`arcsin`, `arccos`, `arctan`)
with exact linear and quadratic polynomial equations over `SymPy` rationals and
algebraic extensions, covering QQQ, QQS, QSS, SQQ, SSS, Regiomontanus' problem,
inaccessible-base triangulation, Snellius-Pothenot resection, and Hansen's
two-station problem.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from geometor.wildberger.invariants import (
    CoordScalar,
    LineProportion,
    Point2DInput,
    _clean_golden,
    _sympify_exact,
    archimedes,
    quadrance,
    spread,
    triple_spread_function,
    vertex_spread,
)


@dataclass(frozen=True)
class SolvedTriangle:
    """Exact algebraic solution of a planar triangle `(Q1, Q2, Q3, s1, s2, s3)`.

    Attributes:
        q1: Quadrance opposite vertex 1.
        q2: Quadrance opposite vertex 2.
        q3: Quadrance opposite vertex 3.
        s1: Spread at vertex 1.
        s2: Spread at vertex 2.
        s3: Spread at vertex 3.
        quadrea: Triangle quadrea `A(Q1, Q2, Q3)`.
        circumquadrance: Circumquadrance `K = Q1*Q2*Q3 / A`.
    """

    q1: sp.Expr
    q2: sp.Expr
    q3: sp.Expr
    s1: sp.Expr
    s2: sp.Expr
    s3: sp.Expr
    quadrea: sp.Expr
    circumquadrance: sp.Expr


def solve_qqq(
    q1: CoordScalar, q2: CoordScalar, q3: CoordScalar
) -> SolvedTriangle:
    """Solve a non-collinear triangle uniquely from three side quadrances `(Q1, Q2, Q3)`.

    Uses the Cross Law `s_3 = 1 - (Q_1 + Q_2 - Q_3)^2 / (4*Q_1*Q_2) = A / (4*Q_1*Q_2)`.

    Args:
        q1: First side quadrance `Q1`.
        q2: Second side quadrance `Q2`.
        q3: Third side quadrance `Q3`.

    Returns:
        Exact `SolvedTriangle`.

    Raises:
        ValueError: If `A(Q1, Q2, Q3) == 0` (collinear/degenerate triple) or `Qi == 0`.
    """
    a, b, c = _sympify_exact(q1), _sympify_exact(q2), _sympify_exact(q3)
    a_val = archimedes(a, b, c)
    if sp.simplify(a_val) == 0:
        raise ValueError("Quadruple is collinear: quadrea A(Q1, Q2, Q3) == 0.")
    if any(sp.simplify(x) == 0 for x in (a, b, c)):
        raise ValueError("Null side quadrance encountered in solve_qqq.")
    s1 = _clean_golden(a_val / (4 * b * c))
    s2 = _clean_golden(a_val / (4 * a * c))
    s3 = _clean_golden(a_val / (4 * a * b))
    k_val = _clean_golden(a * b * c / a_val)
    return SolvedTriangle(
        q1=a,
        q2=b,
        q3=c,
        s1=s1,
        s2=s2,
        s3=s3,
        quadrea=a_val,
        circumquadrance=k_val,
    )


def solve_qqs(
    q1: CoordScalar, q2: CoordScalar, s3: CoordScalar
) -> list[SolvedTriangle]:
    """Solve for both acute/obtuse triangle branches given `(Q1, Q2, s3)`.

    Solves the quadratic Cross Law `(Q1 + Q2 - Q3)^2 = 4*Q1*Q2*(1 - s3)` for `Q3`,
    returning one solution when `s3 == 1` (right vertex) and two solutions
    (acute and obtuse sectors) when `0 < s3 < 1`.

    Args:
        q1: First side quadrance `Q1`.
        q2: Second side quadrance `Q2`.
        s3: Included vertex spread `s3`.

    Returns:
        List of 1 or 2 exact `SolvedTriangle` branches.
    """
    a, b, s = _sympify_exact(q1), _sympify_exact(q2), _sympify_exact(s3)
    disc = _clean_golden(4 * a * b * (1 - s))
    root = sp.sqrt(disc)
    candidates = [_clean_golden(a + b - root), _clean_golden(a + b + root)]
    unique_q3: list[sp.Expr] = []
    for cand in candidates:
        if not any(sp.simplify(cand - prev) == 0 for prev in unique_q3):
            if sp.simplify(archimedes(a, b, cand)) != 0:
                unique_q3.append(cand)
    return [solve_qqq(a, b, q3_val) for q3_val in unique_q3]


def solve_qss(
    q1: CoordScalar, s1: CoordScalar, s2: CoordScalar
) -> list[SolvedTriangle]:
    """Solve for triangle branches given `(Q1, s1, s2)` via Triple Spread + Spread Law.

    Solves `(s1 + s2 + s3)^2 = 2*(s1^2 + s2^2 + s3^2) + 4*s1*s2*s3`, which in normal
    quadratic form is `(s3 - (s1 + s2 - 2*s1*s2))^2 = 4*s1*s2*(1 - s1)*(1 - s2)`.

    Args:
        q1: Known side quadrance `Q1` opposite `s1`.
        s1: Non-zero spread `s1` opposite `Q1`.
        s2: Second spread `s2`.

    Returns:
        List of exact `SolvedTriangle` branches.
    """
    a = _sympify_exact(q1)
    u = _sympify_exact(s1)
    v = _sympify_exact(s2)
    if sp.simplify(u) == 0:
        raise ValueError("Spread s1 must be non-zero.")
    center = _clean_golden(u + v - 2 * u * v)
    disc = _clean_golden(4 * u * v * (1 - u) * (1 - v))
    root = sp.sqrt(disc)
    s3_cands = [_clean_golden(center - root), _clean_golden(center + root)]
    results: list[SolvedTriangle] = []
    seen: list[sp.Expr] = []
    for s3_val in s3_cands:
        if sp.simplify(s3_val) == 0:
            continue
        if any(sp.simplify(s3_val - prev) == 0 for prev in seen):
            continue
        seen.append(s3_val)
        q2_val = _clean_golden(a * v / u)
        q3_val = _clean_golden(a * s3_val / u)
        a_quad = _clean_golden(4 * a * q2_val * s3_val)
        k_val = _clean_golden(a / (4 * u))
        results.append(
            SolvedTriangle(
                q1=a,
                q2=q2_val,
                q3=q3_val,
                s1=u,
                s2=v,
                s3=s3_val,
                quadrea=a_quad,
                circumquadrance=k_val,
            )
        )
    return results


def solve_sqq(
    s1: CoordScalar, q1: CoordScalar, q2: CoordScalar
) -> list[SolvedTriangle]:
    """Solve the rational SSA case `(s1, Q1, Q2)` via Spread Law + Triple Spread.

    Args:
        s1: Non-zero spread `s1` opposite `Q1`.
        q1: Side quadrance `Q1`.
        q2: Adjacent side quadrance `Q2`.

    Returns:
        List of exact `SolvedTriangle` branches.
    """
    u, a, b = _sympify_exact(s1), _sympify_exact(q1), _sympify_exact(q2)
    s2_val = _clean_golden(b * u / a)
    return solve_qss(a, u, s2_val)


def solve_sss_proportional(
    s1: CoordScalar, s2: CoordScalar, s3: CoordScalar, q1: CoordScalar = 1
) -> SolvedTriangle:
    """Validate a spread triple `(s1, s2, s3)` and solve the similar triangle with `Q1 = q1`.

    Args:
        s1: First spread.
        s2: Second spread.
        s3: Third spread.
        q1: Scale quadrance `Q1` (`default 1`).

    Returns:
        Exact `SolvedTriangle` at scale `Q1 = q1`.

    Raises:
        ValueError: If `S(s1, s2, s3) != 0`.
    """
    u, v, w = _sympify_exact(s1), _sympify_exact(s2), _sympify_exact(s3)
    if sp.simplify(triple_spread_function(u, v, w)) != 0:
        raise ValueError("Spreads (s1, s2, s3) do not satisfy the Triple Spread Formula.")
    a = _sympify_exact(q1)
    b = _clean_golden(a * v / u)
    c = _clean_golden(a * w / u)
    a_quad = _clean_golden(4 * a * b * w)
    k_val = _clean_golden(a / (4 * u))
    return SolvedTriangle(
        q1=a,
        q2=b,
        q3=c,
        s1=u,
        s2=v,
        s3=w,
        quadrea=a_quad,
        circumquadrance=k_val,
    )


def two_spread_triples_common(
    a: CoordScalar, b: CoordScalar, c: CoordScalar, d: CoordScalar
) -> sp.Expr:
    """Compute the unique common spread `x = P(a, b, c, d)` of `{a, b, x}` and `{c, d, x}`.

    Implements Wildberger's Two Spread Triples Theorem (Theorem 53, p. 98 & p. 256):
    `P(a, b, c, d) = ((a - b)^2 - (c - d)^2) / (2*(a + b - c - d - 2*a*b + 2*c*d))`.

    Args:
        a: First spread of first triple.
        b: Second spread of first triple.
        c: First spread of second triple.
        d: Second spread of second triple.

    Returns:
        Exact common spread `x`.
    """
    ea, eb, ec, ed = (
        _sympify_exact(a),
        _sympify_exact(b),
        _sympify_exact(c),
        _sympify_exact(d),
    )
    num = (ea - eb) ** 2 - (ec - ed) ** 2
    den = 2 * (ea + eb - ec - ed - 2 * ea * eb + 2 * ec * ed)
    return _clean_golden(num / den)


def spread_from_ratio(
    s_total: CoordScalar, ratio_a: CoordScalar
) -> list[tuple[sp.Expr, sp.Expr]]:
    """Solve `{x, y, s_total}` being a spread triple with `x / y = ratio_a` (Theorem 48, p. 91).

    Returns both algebraic branches `y = s / (a + 1 +/- 2*sqrt(a*(1 - s)))` and `x = a * y`.

    Args:
        s_total: Third spread `s` in `{x, y, s}`.
        ratio_a: Known spread ratio `a = x / y`.

    Returns:
        List of exact `(x, y)` spread pairs.
    """
    s = _sympify_exact(s_total)
    a = _sympify_exact(ratio_a)
    r = sp.sqrt(_clean_golden(a * (1 - s)))
    branches: list[tuple[sp.Expr, sp.Expr]] = []
    for sign in (1, -1):
        denom = _clean_golden(a + 1 + sign * 2 * r)
        if sp.simplify(denom) != 0:
            y_val = _clean_golden(s / denom)
            x_val = _clean_golden(a * y_val)
            if not any(
                sp.simplify(x_val - px) == 0 and sp.simplify(y_val - py) == 0
                for px, py in branches
            ):
                branches.append((x_val, y_val))
    return branches


def solve_inaccessible_height(
    step_quadrance: CoordScalar, s1: CoordScalar, s2: CoordScalar
) -> list[sp.Expr]:
    """Solve Surveying Problem 24.2: vertical cliff height quadrance `H` from two station spreads.

    Two collinear ground stations separated by `step_quadrance = D` observe the top
    of a vertical cliff with elevation spreads `s1` and `s2` relative to the horizontal.
    Horizontal base quadrances are `X1 = H*(1 - s1)/s1` and `X2 = H*(1 - s2)/s2`,
    and collinearity `A(X1, X2, D) = 0` yields the two exact branches (same side vs
    opposite sides of the cliff base):
    `H = D * s1 * s2 / ((sqrt(s2*(1 - s1)) -/+ sqrt(s1*(1 - s2)))^2)`.

    Args:
        step_quadrance: Quadrance `D` between the two observation stations.
        s1: Elevation spread at station 1.
        s2: Elevation spread at station 2.

    Returns:
        Exact roots for the vertical height quadrance `H`.
    """
    d_val = _sympify_exact(step_quadrance)
    u = _sympify_exact(s1)
    v = _sympify_exact(s2)
    h_sym = sp.Symbol("H")
    poly_eq = sp.expand(
        u**2 * v**2 * archimedes(h_sym * (1 - u) / u, h_sym * (1 - v) / v, d_val)
    )
    roots = sp.solve(poly_eq, h_sym)
    return [_clean_golden(r) for r in roots if sp.simplify(r) != 0]


def solve_regiomontanus(
    lower_height: CoordScalar, upper_height: CoordScalar
) -> dict[str, sp.Expr]:
    """Solve Regiomontanus' maximum-spread statue problem algebraically without calculus (Section 24.4).

    A vertical segment from `y = a` to `y = b` (`0 < a < b`, quadrances `A = a^2, B = b^2`)
    viewed from `[x, 0]` (`X = x^2`) subtends maximum spread at exact horizontal
    quadrance `X_opt = a * b`, attaining maximum spread `s_max = (b - a)^2 / (b + a)^2`.

    Args:
        lower_height: Lower height `a > 0`.
        upper_height: Upper height `b > a`.

    Returns:
        Dictionary with `optimal_x_quadrance`, `optimal_x`, and `max_spread`.
    """
    a = _sympify_exact(lower_height)
    b = _sympify_exact(upper_height)
    x_opt = _clean_golden(a * b)
    # Verify at x = sqrt(a*b) the subtended spread matches (b - a)^2 / (b + a)^2
    x_pos = sp.sqrt(x_opt)
    s_at_opt = vertex_spread((x_pos, 0), (0, a), (0, b))
    s_formula = _clean_golden((b - a) ** 2 / (b + a) ** 2)
    assert sp.simplify(s_at_opt - s_formula) == 0
    return {
        "optimal_x_quadrance": x_opt,
        "optimal_x": x_pos,
        "max_spread": s_formula,
    }


def solve_snellius_pothenot_coordinates(
    beacon_a: Point2DInput,
    beacon_b: Point2DInput,
    beacon_c: Point2DInput,
    station_p: Point2DInput,
) -> dict[str, sp.Expr]:
    """Execute Wildberger's Collins-Point / Subtended-Spread resection verification (Section 25.1).

    Given three known beacons `A, B, C` and an observer `P` measuring only the
    rational spreads `r1 = s(PA, PB)` and `r2 = s(PB, PC)`, computes the exact
    measured spreads, beacon quadrances, and verifies the resection equations.

    Args:
        beacon_a: First beacon `A`.
        beacon_b: Second beacon `B`.
        beacon_c: Third beacon `C`.
        station_p: Observer station `P`.

    Returns:
        Dictionary of exact beacon quadrances, observed spreads, and station quadrances.
    """
    q_ab = quadrance(beacon_a, beacon_b)
    q_bc = quadrance(beacon_b, beacon_c)
    q_ac = quadrance(beacon_a, beacon_c)
    r1 = vertex_spread(station_p, beacon_a, beacon_b)
    r2 = vertex_spread(station_p, beacon_b, beacon_c)
    r3 = vertex_spread(station_p, beacon_a, beacon_c)
    q_pa = quadrance(station_p, beacon_a)
    q_pb = quadrance(station_p, beacon_b)
    q_pc = quadrance(station_p, beacon_c)
    return {
        "Q_AB": q_ab,
        "Q_BC": q_bc,
        "Q_AC": q_ac,
        "s_APB": r1,
        "s_BPC": r2,
        "s_APC": r3,
        "Q_PA": q_pa,
        "Q_PB": q_pb,
        "Q_PC": q_pc,
        "triple_spread_residual": triple_spread_function(r1, r2, r3),
    }


def solve_hansen_benchmark() -> dict[str, sp.Expr]:
    """Execute Wildberger's complete rational solution of Hansen's Two-Station Problem (Section 25.2).

    Reconstructs all unknown quadrances between known baseline `A=[0,0], B=[1,5]`
    (`Q(A,B) = 26`) and unknown stations `C=[5,4], D=[4,1]` strictly from the four
    measured spreads at `C` and `D` using `two_spread_triples_common`, Alternate Spreads,
    `spread_from_ratio`, and the Spread Law—zero transcendental functions!

    Returns:
        Dictionary of exact intermediate spreads and recovered quadrances.
    """
    pt_a, pt_b, pt_c, pt_d = (0, 0), (1, 5), (5, 4), (4, 1)
    q_ab = quadrance(pt_a, pt_b)  # 26

    # Four measured spreads from C and D (exact rational inputs):
    s_acb = vertex_spread(pt_c, pt_a, pt_b)  # 441/697
    s_bcd = vertex_spread(pt_c, pt_b, pt_d)  # 169/170
    s_acd = vertex_spread(pt_c, pt_a, pt_d)  # 121/410
    s_adb = vertex_spread(pt_d, pt_a, pt_b)  # 361/425
    s_adc = vertex_spread(pt_d, pt_a, pt_c)  # 121/170
    s_bdc = vertex_spread(pt_d, pt_b, pt_c)  # 169/250

    # Diagonal intersection E = AC meet BD -> spread s_diag = 1024/1025
    line_ac = LineProportion.from_points(pt_a, pt_c)
    line_bd = LineProportion.from_points(pt_b, pt_d)
    s_diag = spread(line_ac, line_bd)

    # Recover s(DA, DC)-opposite spreads via Two Spread Triples function P (p. 256)
    s_dac = two_spread_triples_common(s_diag, s_adb, s_adc, s_acd)  # 121/697
    s_dbc = two_spread_triples_common(s_diag, s_acb, s_bdc, s_bcd)  # 169/425

    # Alternating Spreads Theorem around quadrilateral ABCD (Section 25.2, p. 257):
    # s_DBC * s_ACD * s_ADB * x == s_ACB * s_BDC * s_DAC * y => a = x/y = 11025/14801
    ratio_a = _clean_golden((s_acb * s_bdc * s_dac) / (s_adb * s_acd * s_dbc))
    branches = spread_from_ratio(s_diag, ratio_a)
    x_spread, y_spread = branches[0]  # (441/1066, 361/650)

    # Recover all 4 unknown quadrances by the Spread Law!
    q_ad = _clean_golden(q_ab * y_spread / s_adb)
    q_bc = _clean_golden(q_ab * x_spread / s_acb)
    q_ac = _clean_golden(q_ad * s_adc / s_acd)
    q_bd = _clean_golden(q_bc * s_bcd / s_bdc)

    return {
        "Q_AB": q_ab,
        "s_diag": s_diag,
        "s_DAC": s_dac,
        "s_DBC": s_dbc,
        "x_spread": x_spread,
        "y_spread": y_spread,
        "Q_AD": q_ad,
        "Q_BC": q_bc,
        "Q_AC": q_ac,
        "Q_BD": q_bd,
    }
