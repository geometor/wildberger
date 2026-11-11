"""GEOMETOR Wildberger symbolic model and proof script for W.03: Quadrance, Midpoints & Point-to-Line Separation.

Enunciation: The quadrance between A_1 = [x_1, y_1] and A_2 = [x_2, y_2] is the quadratic form Q(A_1, A_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2; midpoint M divides the quadrance by 4, the locus Q(X, A_1) = Q(X, A_2) is the linear perpendicular bisector, and the quadrance from A_0 to a non-null line l = <a : b : c> is (a*x_0 + b*y_0 + c)^2 / (a^2 + b^2).
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


def construct_w_03() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.03.

    Returns:
        Populated `TopicBuildResult` for W.03 (Quadrance, Midpoints & Point-to-Line Separation).
    """
    result = build_principle_model("W.03")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.03 symbolic construction, render `w-03.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_03()
    svg_out = render_svg(
        bundle.model,
        here / "w-03.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.03: Quadrance, Midpoints & Point-to-Line Separation")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
