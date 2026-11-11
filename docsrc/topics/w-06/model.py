"""GEOMETOR Wildberger symbolic model and proof script for W.06: Law I: Pythagoras' Theorem & Right Triangle Invariants.

Enunciation: For any three non-collinear points A_1, A_2, A_3 over a field F (char F != 2) with non-null lines A_1 A_3 and A_2 A_3, the lines A_1 A_3 and A_2 A_3 are perpendicular (s_3 = 1) if and only if Q(A_2, A_3) + Q(A_1, A_3) = Q(A_1, A_2), in which case the hypotenuse midpoint M_3 is equidistant in quadrance (Q_3 / 4) from all three vertices.
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


def construct_w_06() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.06.

    Returns:
        Populated `TopicBuildResult` for W.06 (Law I: Pythagoras' Theorem & Right Triangle Invariants).
    """
    result = build_principle_model("W.06")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.06 symbolic construction, render `w-06.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_06()
    svg_out = render_svg(
        bundle.model,
        here / "w-06.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.06: Law I: Pythagoras' Theorem & Right Triangle Invariants")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
