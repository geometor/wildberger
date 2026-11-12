"""GEOMETOR Wildberger symbolic model and proof script for W.07: Law II: Triple Quad Formula, Archimedes' Function & Quadrea.

Enunciation: Three planar points A_1, A_2, A_3 with pairwise quadrances Q_1, Q_2, Q_3 are collinear if and only if Archimedes' symmetric quadratic form A(Q_1, Q_2, Q_3) = (Q_1 + Q_2 + Q_3)^2 - 2(Q_1^2 + Q_2^2 + Q_3^2) vanishes; for any triangle, A(Q_1, Q_2, Q_3) equals 4 times the squared coordinate determinant (16 * Delta^2), defining the triangle's quadrea.
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


def construct_w_07() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.07.

    Returns:
        Populated `TopicBuildResult` for W.07 (Law II: Triple Quad Formula, Archimedes' Function & Quadrea).
    """
    result = build_principle_model("W.07")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.07 symbolic construction, render `w-07.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_07()
    svg_out = render_svg(
        bundle.model,
        here / "w-07.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.07: Law II: Triple Quad Formula, Archimedes' Function & Quadrea")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
