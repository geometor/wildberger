"""GEOMETOR Wildberger symbolic model and proof script for W.27: 3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads.

Enunciation: In 3D space over F, quadrance is Q(A_1, A_2) = dx^2 + dy^2 + dz^2, a right-corner tetrahedron satisfies De Gua's Quadrea Theorem A_base = A_xy + A_yz + A_zx, and the dihedral (face) spreads of ALL FIVE regular Platonic solids—Tetrahedron (8/9), Cube (1), Octahedron (8/9), Icosahedron (4/9), and Dodecahedron (4/5)—are exact rational numbers in Q!
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT_SRC = Path(__file__).resolve().parents[3] / "src"
if str(_ROOT_SRC) not in sys.path:
    sys.path.insert(0, str(_ROOT_SRC))

from geometor.wildberger.models import (  # noqa: E402
    TopicBuildResult,
    assert_zero_floats,
    build_principle_model,
)
from geometor.wildberger.render import render_svg  # noqa: E402


def construct_w_27() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.27.

    Returns:
        Populated `TopicBuildResult` for W.27 (3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads).
    """
    result = build_principle_model("W.27")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.27 symbolic construction, render `w-27.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_27()
    svg_out = render_svg(
        bundle.model,
        here / "w-27.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.27: 3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
