"""GEOMETOR Wildberger symbolic model and proof script for W.18: Cyclic Quadrilaterals, Ptolemy & Euler's Four-Point Relation.

Enunciation: Four non-collinear points A_1, A_2, A_3, A_4 on a circle c satisfy equal opposite spreads s(A_1 A_2, A_1 A_4) = s(A_3 A_2, A_3 A_4), Ptolemy's Triple-Quad Law A(Q_12*Q_34, Q_23*Q_14, Q_13*Q_24) = 0 among product quadrances, and the cyclic quadrea / circumquadrance formulas, while four collinear points satisfy Q(Q_12, Q_23, Q_34, Q_14) = 0.
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


def construct_w_18() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.18.

    Returns:
        Populated `TopicBuildResult` for W.18 (Cyclic Quadrilaterals, Ptolemy & Euler's Four-Point Relation).
    """
    result = build_principle_model("W.18")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.18 symbolic construction, render `w-18.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_18()
    svg_out = render_svg(
        bundle.model,
        here / "w-18.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.18: Cyclic Quadrilaterals, Ptolemy & Euler's Four-Point Relation")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
