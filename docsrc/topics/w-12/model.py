"""GEOMETOR Wildberger symbolic model and proof script for W.12: Vertex Bisectors, Square Vertices & The Four Incenters.

Enunciation: The locus of points X having equal quadrance Q(X, l_1) = Q(X, l_2) to two intersecting non-null lines l_1, l_2 splits into two orthogonal vertex bisectors over F if and only if (a_1^2 + b_1^2)(a_2^2 + b_2^2) is a square in F; when two vertices of a triangle have bisectors in F, so does the third, producing four symmetric incenters I_0, I_1, I_2, I_3.
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


def construct_w_12() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.12.

    Returns:
        Populated `TopicBuildResult` for W.12 (Vertex Bisectors, Square Vertices & The Four Incenters).
    """
    result = build_principle_model("W.12")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.12 symbolic construction, render `w-12.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_12()
    svg_out = render_svg(
        bundle.model,
        here / "w-12.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.12: Vertex Bisectors, Square Vertices & The Four Incenters")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
