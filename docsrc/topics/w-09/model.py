"""GEOMETOR Wildberger symbolic model and proof script for W.09: Law IV: The Cross Law & Quadrea-Spread Identity.

Enunciation: In any triangle A_1 A_2 A_3 with non-null sides Q_1, Q_2 meeting with spread s_3 and cross c_3 = 1 - s_3 at vertex A_3, the quadrances satisfy (Q_1 + Q_2 - Q_3)^2 = 4 * Q_1 * Q_2 * (1 - s_3) = 4 * Q_1 * Q_2 * c_3, equivalently A(Q_1, Q_2, Q_3) = 4 * Q_1 * Q_2 * s_3.
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


def construct_w_09() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.09.

    Returns:
        Populated `TopicBuildResult` for W.09 (Law IV: The Cross Law & Quadrea-Spread Identity).
    """
    result = build_principle_model("W.09")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.09 symbolic construction, render `w-09.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_09()
    svg_out = render_svg(
        bundle.model,
        here / "w-09.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.09: Law IV: The Cross Law & Quadrea-Spread Identity")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
