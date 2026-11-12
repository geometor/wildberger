"""GEOMETOR Wildberger symbolic model and proof script for W.11: Isosceles, Equilateral & Kepler's Golden Right Triangle.

Enunciation: In a non-null triangle, Q_1 = Q_2 iff s_1 = s_2 (with apex spread s_3 = (Q_3/Q_1)(1 - Q_3/(4*Q_1))), and Q_1 = Q_2 = Q_3 iff s_1 = s_2 = s_3 = 3/4; in Kepler's Golden Right Triangle with side lengths (1, sqrt(phi), phi), the nested radical vanishes in quadrance to give Q = (1, phi, phi^2) and exact golden spreads (s_1, s_2, s_3) = (2 - phi, phi - 1, 1) = (1/phi^2, 1/phi, 1).
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


def construct_w_11() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.11.

    Returns:
        Populated `TopicBuildResult` for W.11 (Isosceles, Equilateral & Kepler's Golden Right Triangle).
    """
    result = build_principle_model("W.11")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.11 symbolic construction, render `w-11.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_11()
    svg_out = render_svg(
        bundle.model,
        here / "w-11.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.11: Isosceles, Equilateral & Kepler's Golden Right Triangle")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
