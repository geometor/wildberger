"""GEOMETOR Wildberger symbolic model and proof script for W.01: Planar Points, Line Proportions & Incidence Determinants.

Enunciation: Over any field F of characteristic not equal to 2, a planar point is an ordered pair A = [x, y] and a planar line is a homogeneous 3-proportion l = <a : b : c> with (a, b) != (0, 0) representing a*x + b*y + c = 0; three points are collinear and three lines are concurrent if and only if their respective 3x3 coordinate determinants vanish.
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


def construct_w_01() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.01.

    Returns:
        Populated `TopicBuildResult` for W.01 (Planar Points, Line Proportions & Incidence Determinants).
    """
    result = build_principle_model("W.01")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.01 symbolic construction, render `w-01.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_01()
    svg_out = render_svg(
        bundle.model,
        here / "w-01.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.01: Planar Points, Line Proportions & Incidence Determinants")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
