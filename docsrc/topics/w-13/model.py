"""GEOMETOR Wildberger symbolic model and proof script for W.13: Stewart's Theorem, Median Quadrances & The Centroid.

Enunciation: For any affine point D = (1 - lambda)*A_1 + lambda*A_2 on side A_1 A_2 of triangle A_1 A_2 A_3, the cevian quadrance satisfies Q(A_3, D) = (1 - lambda)*Q_2 + lambda*Q_1 - lambda*(1 - lambda)*Q_3; at lambda = 1/2, the median quadrance satisfies 4*Q(A_3, M_3) = 2*Q_1 + 2*Q_2 - Q_3, and the three medians concur at G = (A_1 + A_2 + A_3)/3.
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


def construct_w_13() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.13.

    Returns:
        Populated `TopicBuildResult` for W.13 (Stewart's Theorem, Median Quadrances & The Centroid).
    """
    result = build_principle_model("W.13")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.13 symbolic construction, render `w-13.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_13()
    svg_out = render_svg(
        bundle.model,
        here / "w-13.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.13: Stewart's Theorem, Median Quadrances & The Centroid")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
