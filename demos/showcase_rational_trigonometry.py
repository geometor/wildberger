"""Interactive Rich showcase of Rational Trigonometry, Universal Geometry & Chromogeometry."""

from __future__ import annotations

import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import sympy as sp

_REPO_ROOT = Path(__file__).resolve().parents[1]
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from geometor.wildberger import (  # noqa: E402
    BLUE_METRIC,
    GREEN_METRIC,
    LineProportion,
    RED_METRIC,
    archimedes,
    compute_triangle_invariants,
    midpoint,
    prove_platonic_dihedral_spreads,
    quadrance,
    solve_hansen_benchmark,
    spread,
    spread_polynomial,
    triple_spread_function,
)


def run_showcase() -> None:
    """Execute a 5-part live SymPy demonstration of Wildberger's Universal Geometry."""
    console = Console()
    console.print(
        Panel.fit(
            "[bold gold1]GEOMETOR • wildberger[/bold gold1]\n"
            "Exact Symbolic Showcase: Rational Trigonometry, Chromogeometry & Universal Geometry",
            border_style="gold1",
        )
    )

    # 1. Five Main Laws on Rational Triangle A_1=[0,0], A_2=[6,0], A_3=[2,4]
    a1, a2, a3 = (sp.Integer(0), sp.Integer(0)), (sp.Integer(6), sp.Integer(0)), (sp.Integer(2), sp.Integer(4))
    inv = compute_triangle_invariants(a1, a2, a3)
    t1 = Table(title="1. The Five Laws on Rational Triangle [0,0], [6,0], [2,4]")
    t1.add_column("Quantity / Law", style="cyan")
    t1.add_column("Exact Value (in Q)", style="green")
    t1.add_row("Quadrances (Q_1, Q_2, Q_3)", f"({inv.q1}, {inv.q2}, {inv.q3})")
    t1.add_row("Spreads (s_1, s_2, s_3)", f"({inv.s1}, {inv.s2}, {inv.s3})")
    t1.add_row("Quadrea A = 16 * Area^2", f"{inv.quadrea}")
    t1.add_row("Spread Law s_1/Q_1 == s_2/Q_2 == s_3/Q_3", f"{inv.s1 / inv.q1}")
    t1.add_row("Triple Spread S(s_1, s_2, s_3)", f"{triple_spread_function(inv.s1, inv.s2, inv.s3)}")
    console.print(t1)

    # 2. Kepler's Golden Triangle & Spread Polynomial S_5(s) in Q(sqrt(5)) and GF(19)
    phi = (sp.Integer(1) + sp.sqrt(5)) / 2
    s_sym = sp.Symbol("s")
    s5_factored = sp.factor(spread_polynomial(5, s_sym))
    q_leg = phi**2
    s_base_kepler = sp.simplify(1 - sp.Integer(1) / (4 * q_leg))
    s_apex_kepler = sp.simplify(4 * s_base_kepler * (1 - s_base_kepler))

    # Order-5 star in GF(19): lines <0:1:0>, <2:1:0>, <5:1:0>, <-5:1:0>, <-2:1:0>
    blue_19 = BLUE_METRIC.with_modulus(19)
    star_19 = [
        LineProportion(0, 1, 0),
        LineProportion(2, 1, 0),
        LineProportion(5, 1, 0),
        LineProportion(14, 1, 0),
        LineProportion(17, 1, 0),
    ]
    adj_spreads_19 = [
        spread(star_19[i], star_19[(i + 1) % 5], metric=blue_19) for i in range(5)
    ]

    t2 = Table(title="2. Divine Proportion, Spread Polynomial S_5(s) & Five-Fold Symmetry in GF(19)")
    t2.add_column("Identity", style="cyan")
    t2.add_column("Exact Symbolic Result", style="gold1")
    t2.add_row("Factored S_5(s)", str(s5_factored))
    t2.add_row("Kepler (phi^2, phi^2, 1) spreads", f"s_apex = {s_apex_kepler}, s_base = {s_base_kepler}")
    t2.add_row("S_5(s_apex), S_5(s_base)", f"({sp.simplify(spread_polynomial(5, s_apex_kepler))}, {sp.simplify(spread_polynomial(5, s_base_kepler))})")
    t2.add_row("GF(19) Order-5 Star adjacent spreads", f"{adj_spreads_19} (all == 16 mod 19, S_5(16) == {int(spread_polynomial(5, 16)) % 19})")
    console.print(t2)

    # 3. Chromogeometry (Blue, Red, Green)
    p1, p2, p3 = (sp.Integer(0), sp.Integer(0)), (sp.Integer(8), sp.Integer(2)), (sp.Integer(2), sp.Integer(6))
    ib = compute_triangle_invariants(p1, p2, p3, metric=BLUE_METRIC)
    ir = compute_triangle_invariants(p1, p2, p3, metric=RED_METRIC)
    ig = compute_triangle_invariants(p1, p2, p3, metric=GREEN_METRIC)
    t3 = Table(title="3. Chromogeometry (Blue Euclidean, Red Minkowski, Green Split)")
    t3.add_column("Chromo Theorem", style="cyan")
    t3.add_column("Verification on [0,0], [8,2], [2,6]", style="magenta")
    t3.add_row("Q_B^2 == Q_R^2 + Q_G^2", f"{ib.q3}^2 == {ir.q3}^2 + {ig.q3}^2 ({ib.q3**2} == {ir.q3**2 + ig.q3**2})")
    t3.add_row("Chromo Nine-Point Midpoint N_B == (C_R + C_G)/2", f"N_B = {list(ib.nine_point_center)} == {list(midpoint(ir.circumcenter, ig.circumcenter))}")
    console.print(t3)

    # 4. Hansen's Surveying Problem & Platonic Solid Dihedral Spreads
    hansen = solve_hansen_benchmark()
    platonic = prove_platonic_dihedral_spreads()
    de_gua_check = archimedes(13, 45, 40) == (4 * 4 * 9 + 4 * 9 * 36 + 4 * 4 * 36)
    t4 = Table(title="4. Exact Geodesy & 3D Platonic Dihedral Spreads")
    t4.add_column("Domain", style="cyan")
    t4.add_column("Exact Rational Output", style="green")
    t4.add_row(
        "Hansen's Surveying Problem (Q_AB = 26)",
        f"Q_AD={hansen['Q_AD']}, Q_BC={hansen['Q_BC']}, Q_AC={hansen['Q_AC']}, Q_BD={hansen['Q_BD']}",
    )
    t4.add_row("Platonic Dihedral Spreads (Tet, Cube, Oct, Ico, Dod)", f"(8/9, 1, 8/9, 4/9, 4/5) — verified={platonic.verified}")
    t4.add_row("De Gua 3D Quadrea Theorem ([2,0,0],[0,3,0],[0,0,6])", f"A_slant = {archimedes(13, 45, 40)} (verified={de_gua_check})")
    t4.add_row("Sample quadrance Q([0,0],[3,4])", f"{quadrance((0, 0), (3, 4))}")
    console.print(t4)


if __name__ == "__main__":
    run_showcase()
