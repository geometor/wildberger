"""GEOMETOR Wildberger: Rational Trigonometry & Universal Geometry Principles Codex.

Provides exact `SymPy` algebraic invariants (quadrance, spread, cross, twist,
quadrea, spread polynomials, projective line/conic proportions, 3D dihedral
spreads, cross-ratios, finite-field arithmetic, and Blue/Red/Green
Chromogeometry), automated theorem provers, exact polynomial triangle and
surveying solvers, and `geometor.model` interactive SVG constructions for the
28 Principles (`W.01`..`W.28`).
"""

from __future__ import annotations

from geometor.wildberger.catalog import (
    PrincipleSpec,
    get_all_principles,
    get_dependents,
    get_principle_by_code,
)
from geometor.wildberger.invariants import (
    BLUE_METRIC,
    GREEN_METRIC,
    RED_METRIC,
    ConicProportion,
    LineProportion,
    MetricForm,
    TriangleInvariants,
    archimedes,
    collinear_cross_ratio_quadrance,
    compute_triangle_invariants,
    cross,
    cross_polynomial,
    dihedral_spread,
    euler_four_point_function,
    midpoint,
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
    signed_turn,
    spread,
    spread_polynomial,
    spread_sequence_mod_p,
    triple_cross_function,
    triple_spread_function,
    twist,
    vertex_spread,
)
from geometor.wildberger.models import TopicBuildResult, build_principle_model
from geometor.wildberger.proofs import (
    ProofCertificate,
    prove_platonic_dihedral_spreads,
    verify_all_proofs,
)
from geometor.wildberger.render import render_svg
from geometor.wildberger.solvers import (
    SolvedTriangle,
    solve_hansen_benchmark,
    solve_inaccessible_height,
    solve_qqq,
    solve_qqs,
    solve_qss,
    solve_regiomontanus,
    solve_snellius_pothenot_coordinates,
    solve_sqq,
    solve_sss_proportional,
)
from geometor.wildberger.topics import build_codex

__version__ = "0.1.1"

__all__ = [
    "__version__",
    "BLUE_METRIC",
    "RED_METRIC",
    "GREEN_METRIC",
    "MetricForm",
    "LineProportion",
    "ConicProportion",
    "TriangleInvariants",
    "PrincipleSpec",
    "TopicBuildResult",
    "ProofCertificate",
    "SolvedTriangle",
    "archimedes",
    "build_codex",
    "build_principle_model",
    "collinear_cross_ratio_quadrance",
    "compute_triangle_invariants",
    "cross",
    "cross_polynomial",
    "dihedral_spread",
    "euler_four_point_function",
    "get_all_principles",
    "get_dependents",
    "get_principle_by_code",
    "midpoint",
    "pencil_cross_ratio_spread",
    "perpendicular_bisector",
    "plane_normal",
    "point_to_line_quadrance",
    "prove_platonic_dihedral_spreads",
    "quadrance",
    "quadrance_3d",
    "quadrea",
    "quadruple_quad_function",
    "quadruple_spread_function",
    "rational_polar_coords",
    "render_svg",
    "signed_turn",
    "solve_hansen_benchmark",
    "solve_inaccessible_height",
    "solve_qqq",
    "solve_qqs",
    "solve_qss",
    "solve_regiomontanus",
    "solve_snellius_pothenot_coordinates",
    "solve_sqq",
    "solve_sss_proportional",
    "spread",
    "spread_polynomial",
    "spread_sequence_mod_p",
    "triple_cross_function",
    "triple_spread_function",
    "twist",
    "verify_all_proofs",
    "vertex_spread",
]
