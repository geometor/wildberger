"""Comprehensive test suite for `geometor.wildberger`.

Verifies exact quadratic invariants, floating-point rejection, all 18 multivariate
`SymPy` theorem provers, exact polynomial triangle and surveying solvers, the
28-Principle codex (`W.01`..`W.28`), zero-`sp.Float` model purity, SVG XML
validity, `:g:` <-> `data-ref` hover binding integrity, and the CLI.
"""

from __future__ import annotations

import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import sympy as sp

from geometor.wildberger import (
    BLUE_METRIC,
    GREEN_METRIC,
    RED_METRIC,
    ConicProportion,
    LineProportion,
    archimedes,
    build_principle_model,
    collinear_cross_ratio_quadrance,
    compute_triangle_invariants,
    cross,
    cross_polynomial,
    dihedral_spread,
    euler_four_point_function,
    get_all_principles,
    get_dependents,
    get_principle_by_code,
    pencil_cross_ratio_spread,
    perpendicular_bisector,
    plane_normal,
    point_to_line_quadrance,
    quadrance,
    quadrance_3d,
    quadrea,
    quadruple_quad_function,
    quadruple_spread_function,
    rational_polar_coords,
    solve_hansen_benchmark,
    solve_inaccessible_height,
    solve_qqq,
    solve_qqs,
    solve_qss,
    solve_regiomontanus,
    solve_snellius_pothenot_coordinates,
    solve_sqq,
    solve_sss_proportional,
    spread,
    spread_polynomial,
    spread_sequence_mod_p,
    triple_cross_function,
    triple_spread_function,
    twist,
    verify_all_proofs,
    vertex_spread,
)
from geometor.wildberger.__main__ import main
from geometor.wildberger.invariants import signed_turn

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_rejects_floating_point_inputs() -> None:
    """Ensure Python `float` and `sp.Float` inputs raise `TypeError`."""
    with pytest.raises(TypeError):
        quadrance((0.5, 0), (1, 1))
    with pytest.raises(TypeError):
        quadrance((sp.Float("0.5"), 0), (1, 1))
    with pytest.raises(TypeError):
        LineProportion(1.0, 2, 3)


def test_fundamental_invariants_and_signed_turn() -> None:
    """Verify quadrance, spread, cross, twist, quadrea, and Triple Turn Formula."""
    p1, p2, p3 = (0, 0), (4, 0), (0, 3)
    assert quadrance(p1, p2) == 16
    assert quadrance(p1, p3) == 9
    assert quadrance(p2, p3) == 25
    assert quadrea(p1, p2, p3) == 16 * 9 * 4 // 1  # 576 = 16 * (6)^2

    l1 = LineProportion.from_points(p1, p2)
    l2 = LineProportion.from_points(p2, p3)
    l3 = LineProportion.from_points(p3, p1)

    assert spread(l1, l3) == 1
    assert cross(l1, l3) == 0
    assert spread(l1, l2) == sp.Rational(9, 25)
    assert cross(l1, l2) == sp.Rational(16, 25)
    assert twist(l1, l2) == sp.Rational(9, 16)
    assert vertex_spread(p2, p1, p3) == sp.Rational(9, 25)
    assert triple_spread_function(1, sp.Rational(9, 25), sp.Rational(16, 25)) == 0
    assert triple_cross_function(0, sp.Rational(16, 25), sp.Rational(9, 25)) == 0

    # Non-perpendicular triangle for Triple Turn Formula: u1 + u2 + u3 == u1*u2*u3
    m1 = LineProportion.from_points((0, 0), (5, 1))
    m2 = LineProportion.from_points((5, 1), (2, 6))
    m3 = LineProportion.from_points((2, 6), (0, 0))
    u1 = signed_turn(m1, m2)
    u2 = signed_turn(m2, m3)
    u3 = signed_turn(m3, m1)
    assert sp.simplify((u1 + u2 + u3) - u1 * u2 * u3) == 0
    assert sp.simplify(u1**2 - twist(m1, m2)) == 0


def test_quadruple_and_euler_four_point_functions() -> None:
    """Verify Quadruple Quad, self-dual Quadruple Spread, and Euler Four-Point relations."""
    # Collinear points (0,0), (2,0), (5,0) -> quadrances 4, 9, 25, 0
    assert quadruple_quad_function(4, 9, 25, 0) == 0

    a, b, c, d = sp.Rational(1, 5), sp.Rational(2, 5), sp.Rational(3, 10), sp.Rational(1, 2)
    assert quadruple_spread_function(a, b, c, d) == quadruple_spread_function(
        1 - a, 1 - b, 1 - c, 1 - d
    )

    pts = [(0, 0), (4, 1), (2, 5), (6, 3)]
    q1 = quadrance(pts[1], pts[2])
    q2 = quadrance(pts[0], pts[2])
    q3 = quadrance(pts[0], pts[1])
    p1 = quadrance(pts[0], pts[3])
    p2 = quadrance(pts[1], pts[3])
    p3 = quadrance(pts[2], pts[3])
    assert euler_four_point_function(q1, q2, q3, p1, p2, p3) == 0


def test_line_and_conic_proportions() -> None:
    """Verify reflections, perpendicular bisectors, null lines, and Taylor conic tangents."""
    line = LineProportion(1, -2, 3)
    pt = (4, -1)
    foot = line.foot_of_altitude(pt)
    refl = line.reflect_point(pt)
    assert line.contains(foot)
    assert quadrance(pt, foot) == point_to_line_quadrance(pt, line)
    assert quadrance(pt, foot) == quadrance(refl, foot)

    pb = perpendicular_bisector(pt, refl)
    assert pb.is_parallel(line) and pb.contains(foot)

    other = LineProportion(3, 1, -2)
    refl_line = line.reflect_line(other)
    meet_pt = line.meet(other)
    assert refl_line.contains(meet_pt)
    assert spread(line, other) == spread(line, refl_line)

    # Null lines in Red and Green metrics
    assert LineProportion(1, -1, 0).is_null(RED_METRIC)
    assert LineProportion(1, 0, 0).is_null(GREEN_METRIC)
    assert not LineProportion(1, -1, 0).is_null(BLUE_METRIC)

    # Wildberger Example 19.3 (scan-verified p. 199 / p-220.png):
    conic = ConicProportion(1, -2, -1, 1, 0, -5)
    pt_on_conic = (3, 1)
    assert conic.evaluate(pt_on_conic) == 0
    assert conic.center() == (sp.Rational(-1, 4), sp.Rational(1, 4))
    taylor = conic.taylor_conic(pt_on_conic)
    assert (taylor.d, taylor.e, taylor.f, taylor.a, taylor.b, taylor.c) == (1, -2, -1, 5, -8, 0)
    tang = conic.tangent_at(pt_on_conic)
    assert (tang.a, tang.b, tang.c) == (5, -8, -7)
    assert tang.contains(pt_on_conic)

    # Circle, Parabola, Quadrola, Grammola builders
    circ = ConicProportion.from_circle((2, -1), 25)
    assert circ.evaluate((5, 3)) == 0
    parab = ConicProportion.from_parabola((0, 1), LineProportion(0, 1, 1))
    assert parab.evaluate((2, 1)) == 0
    quad = ConicProportion.from_quadrola((-2, 0), (2, 0), 36)
    assert quad.evaluate((3, 0)) == 0
    gram = ConicProportion.from_grammola(LineProportion(1, 0, 0), LineProportion(0, 1, 0), 13)
    assert gram.evaluate((2, 3)) == 0


def test_spread_polynomials_and_finite_fields() -> None:
    """Verify spread/cross polynomials and finite-field pentagram/heptagram orbits."""
    s = sp.Symbol("s")
    assert sp.factor(spread_polynomial(5, s)) == s * (16 * s**2 - 20 * s + 5) ** 2
    assert sp.factor(spread_polynomial(7, s)) == s * (64 * s**3 - 112 * s**2 + 56 * s - 7) ** 2
    c = sp.Symbol("c")
    assert sp.expand(cross_polynomial(3, c) - (1 - spread_polynomial(3, 1 - c))) == 0

    # Order-5 star in GF(19) with s = 16 and s = 9 (Wildberger Example 14.7, p. 161)
    assert spread_sequence_mod_p(16, 19) == [0, 16, 9, 9, 16]
    # Order-7 star in GF(29) with s = 6 -> {0, 6, 25, 7} (Wildberger Example 14.9, p. 162)
    seq_29 = spread_sequence_mod_p(6, 29)
    assert seq_29 == [0, 6, 25, 7, 7, 25, 6]


def test_chromogeometry_and_3d_and_polar() -> None:
    """Verify Chromogeometry theorems, 3D dihedral spreads, cross-ratios, and `[s, Q]`."""
    a1, a2, a3 = (0, 0), (8, 2), (2, 6)
    inv_b = compute_triangle_invariants(a1, a2, a3, metric=BLUE_METRIC)
    inv_r = compute_triangle_invariants(a1, a2, a3, metric=RED_METRIC)
    inv_g = compute_triangle_invariants(a1, a2, a3, metric=GREEN_METRIC)
    assert inv_b.q3**2 == inv_r.q3**2 + inv_g.q3**2
    assert inv_b.nine_point_center == (
        (inv_r.circumcenter[0] + inv_g.circumcenter[0]) / 2,
        (inv_r.circumcenter[1] + inv_g.circumcenter[1]) / 2,
    )

    # Regular tetrahedron dihedral spread == 8/9
    v0, v1, v2, v3 = (1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)
    assert quadrance_3d(v0, v1) == 8
    n1 = plane_normal(v0, v1, v2)
    n2 = plane_normal(v0, v1, v3)
    assert dihedral_spread(n1, n2) == sp.Rational(8, 9)

    # Projective cross-ratio bridge
    origin = (0, 4)
    pts = [(-2, 0), (1, 0), (3, 0), (6, 0)]
    assert collinear_cross_ratio_quadrance(*pts) == pencil_cross_ratio_spread(origin, *pts)

    # Rational polar coordinates [s, Q] with s = x^2 / (x^2 + y^2) (scan-verified p. 286)
    s_val, q_val = rational_polar_coords(3, 4)
    assert (s_val, q_val) == (sp.Rational(9, 25), 25)


def test_all_18_symbolic_proofs() -> None:
    """Execute all 18 multivariate SymPy theorem provers and check exact zero residuals."""
    certs = verify_all_proofs()
    assert len(certs) == 18
    for cert in certs:
        assert cert.verified is True, f"Proof failed: {cert.theorem_id}"
        assert cert.residual == 0, f"Non-zero residual in {cert.theorem_id}: {cert.residual}"


def test_triangle_and_surveying_solvers() -> None:
    """Verify exact QQQ, QQS, QSS, SQQ, SSS, height, Regiomontanus, Pothenot, and Hansen solvers."""
    tri = solve_qqq(9, 16, 25)
    assert (tri.s1, tri.s2, tri.s3) == (sp.Rational(9, 25), sp.Rational(16, 25), 1)
    assert tri.quadrea == archimedes(9, 16, 25)

    qqs_branches = solve_qqs(25, 16, sp.Rational(9, 25))
    assert any(b.q3 == 9 for b in qqs_branches) and len(qqs_branches) == 2

    qss_branches = solve_qss(25, 1, sp.Rational(9, 25))
    assert any(b.q3 == 16 for b in qss_branches)

    sqq_branches = solve_sqq(1, 25, 9)
    assert any(b.q3 == 16 for b in sqq_branches)

    sss_tri = solve_sss_proportional(sp.Rational(9, 25), sp.Rational(16, 25), 1, q1=9)
    assert (sss_tri.q2, sss_tri.q3) == (16, 25)

    heights = solve_inaccessible_height(9, sp.Rational(9, 25), sp.Rational(9, 58))
    assert sp.Integer(9) in heights

    regio = solve_regiomontanus(4, 9)
    assert regio["optimal_x_quadrance"] == 36
    assert regio["max_spread"] == sp.Rational(25, 169)

    pothenot = solve_snellius_pothenot_coordinates((0, 0), (4, 0), (4, 3), (1, -2))
    assert pothenot["triple_spread_residual"] == 0

    hansen = solve_hansen_benchmark()
    assert (hansen["Q_AD"], hansen["Q_BC"], hansen["Q_AC"], hansen["Q_BD"]) == (17, 17, 41, 25)


def test_codex_models_svgs_and_zero_floats() -> None:
    """Verify all 28 codex principles (`W.01`..`W.28`), zero `sp.Float` purity, and SVG `:g:` bindings."""
    specs = get_all_principles()
    assert len(specs) == 28
    codes = {s.code for s in specs}
    assert get_principle_by_code("W.01").slug == "w-01"
    assert len(get_dependents("W.01")) >= 3

    g_role_re = re.compile(r":g:`([^`]+)`")

    for spec in specs:
        for dep in spec.depends_on:
            assert dep in codes, f"Unknown dependency {dep} in {spec.code}"

        built = build_principle_model(spec.code)
        assert len(built.model) > 0, f"Empty model for {spec.code}"
        for elem in built.model:
            floats = elem.atoms(sp.Float)
            assert not floats, f"sp.Float found in {spec.code} element {elem}: {floats}"

        topic_dir = REPO_ROOT / "docsrc" / "topics" / spec.slug
        svg_path = topic_dir / f"{spec.slug}.svg"
        rst_path = topic_dir / "index.rst"
        model_py = topic_dir / "model.py"

        assert svg_path.exists(), f"Missing SVG: {svg_path}"
        assert rst_path.exists(), f"Missing RST: {rst_path}"
        assert model_py.exists(), f"Missing model.py: {model_py}"

        root = ET.parse(svg_path).getroot()
        data_refs = {
            el.attrib["data-ref"]
            for el in root.iter()
            if "data-ref" in el.attrib
        }
        rst_text = rst_path.read_text(encoding="utf-8")
        for g_label in g_role_re.findall(rst_text):
            assert g_label in data_refs, (
                f"{spec.code} index.rst references :g:`{g_label}` missing from {svg_path.name} data-ref={sorted(data_refs)}"
            )


def test_cli_commands_and_standalone_topic_script() -> None:
    """Verify CLI `summary` and `verify` commands and standalone `model.py` execution."""
    assert main(["summary"]) == 0
    assert main(["verify"]) == 0

    proc = subprocess.run(
        [sys.executable, str(REPO_ROOT / "docsrc" / "topics" / "w-28" / "model.py")],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, f"w-28/model.py failed: {proc.stderr}"
