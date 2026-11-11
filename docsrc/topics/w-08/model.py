"""GEOMETOR Wildberger symbolic model and proof script for W.08: Law III: The Spread Law & Extended Circumquadrance Law.

Enunciation: In any non-null triangle A_1 A_2 A_3 with side quadrances Q_1, Q_2, Q_3, vertex spreads s_1, s_2, s_3, quadrea A, and circumquadrance K, the ratios of spread to opposite quadrance are equal: s_1 / Q_1 = s_2 / Q_2 = s_3 / Q_3 = A / (4 * Q_1 * Q_2 * Q_3) = 1 / (4 * K).
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


def construct_w_08() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.08.

    Returns:
        Populated `TopicBuildResult` for W.08 (Law III: The Spread Law & Extended Circumquadrance Law).
    """
    result = build_principle_model("W.08")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.08 symbolic construction, render `w-08.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_08()
    svg_out = render_svg(
        bundle.model,
        here / "w-08.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.08: Law III: The Spread Law & Extended Circumquadrance Law")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
