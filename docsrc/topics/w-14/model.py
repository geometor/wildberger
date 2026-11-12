"""GEOMETOR Wildberger symbolic model and proof script for W.14: Menelaus, Ceva & The Alternate Spreads Theorem.

Enunciation: If either a transversal line l cuts the sidelines A_2 A_3, A_3 A_1, A_1 A_2 of a non-null triangle at B_1, B_2, B_3 (Menelaus) or three cevians through a point A_0 meet the opposite sidelines at B_1, B_2, B_3 (Ceva), then the six segment quadrances satisfy Q(A_2, B_1) * Q(A_3, B_2) * Q(A_1, B_3) = Q(B_1, A_3) * Q(B_2, A_1) * Q(B_3, A_2).
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


def construct_w_14() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.14.

    Returns:
        Populated `TopicBuildResult` for W.14 (Menelaus, Ceva & The Alternate Spreads Theorem).
    """
    result = build_principle_model("W.14")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.14 symbolic construction, render `w-14.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_14()
    svg_out = render_svg(
        bundle.model,
        here / "w-14.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.14: Menelaus, Ceva & The Alternate Spreads Theorem")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
