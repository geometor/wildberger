"""GEOMETOR Wildberger symbolic model and proof script for W.28: Rational Polar Coordinates, Classical Curves & The Ellipson.

Enunciation: Replacing polar coordinates (r, theta) with rational polar coordinates [s, Q] where s = x^2 / (x^2 + y^2) (spread to the y-axis) and Q = x^2 + y^2 converts classical polar curves into exact polynomial relations—Bernoulli's lemniscate s = (Q + 2)/4 (or Q = a*(2*s - 1)), Descartes' folium (2*s - 1)^2*(s^2 - s + 1)^2*Q^2 - 18*s*(1 - s)*(1 - 3*s + 3*s^2)*Q + 81*s^2*(1 - s)^2 = 0, and the deltoid/ellipson S_3(s) law—while (s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4*s_1*s_2*s_3 cuts out the tetrahedral Ellipson.
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


def construct_w_28() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.28.

    Returns:
        Populated `TopicBuildResult` for W.28 (Rational Polar Coordinates, Classical Curves & The Ellipson).
    """
    result = build_principle_model("W.28")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.28 symbolic construction, render `w-28.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_28()
    svg_out = render_svg(
        bundle.model,
        here / "w-28.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.28: Rational Polar Coordinates, Classical Curves & The Ellipson")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
