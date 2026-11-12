"""GEOMETOR Wildberger symbolic model and proof script for W.21: Taylor Conics, Algebraic Tangents & Optical Reflection Laws.

Enunciation: Translating any conic f(x, y) = 0 to a point A = [x_0, y_0] on the conic isolates a unique linear term l_1(x - x_0, y - y_0) = 0 defining its algebraic tangent t_tan without limits; for a parabola, t_tan is the perpendicular bisector of focus F_0 and directrix foot D_0 (giving equal spreads with F_0 A and the axis), and for a quadrola, t_tan makes equal spreads with both focal lines F_1 P_q and F_2 P_q.
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


def construct_w_21() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.21.

    Returns:
        Populated `TopicBuildResult` for W.21 (Taylor Conics, Algebraic Tangents & Optical Reflection Laws).
    """
    result = build_principle_model("W.21")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.21 symbolic construction, render `w-21.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_21()
    svg_out = render_svg(
        bundle.model,
        here / "w-21.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.21: Taylor Conics, Algebraic Tangents & Optical Reflection Laws")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
