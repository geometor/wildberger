"""GEOMETOR Wildberger symbolic model and proof script for W.04: Spread, Cross, Twist & Line Separation Ratios.

Enunciation: For two non-null lines l_1 = <a_1 : b_1 : c_1> and l_2 = <a_2 : b_2 : c_2>, the spread s(l_1, l_2) = (a_1*b_2 - a_2*b_1)^2 / ((a_1^2 + b_1^2)*(a_2^2 + b_2^2)) depends only on the unoriented lines, vanishes iff l_1 || l_2, equals 1 iff l_1 perp l_2, and equals Q(B, C) / Q(A, B) for any altitude BC dropped from B on l_1 to C on l_2.
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


def construct_w_04() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.04.

    Returns:
        Populated `TopicBuildResult` for W.04 (Spread, Cross, Twist & Line Separation Ratios).
    """
    result = build_principle_model("W.04")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.04 symbolic construction, render `w-04.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_04()
    svg_out = render_svg(
        bundle.model,
        here / "w-04.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.04: Spread, Cross, Twist & Line Separation Ratios")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
