"""GEOMETOR Wildberger symbolic model and proof script for W.17: Circle Geometry: Subtended Spreads, Secant Products & Rational Points.

Enunciation: On a circle Q(X, O_c) = K over F, a diameter subtends spread 1 at every other circle point (Thales), any chord P_1 P_2 subtends constant spread s_3 at the circumference with Q(P_1, P_2) = 4*K*s_3 and central spread s(O_c P_1, O_c P_2) = S_2(s_3) = 4*s_3*(1 - s_3), and any external or internal point A_0 has invariant secant quadrance product Q(A_0, P_1)*Q(A_0, P_2) = (Q(A_0, O_c) - K)^2.
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


def construct_w_17() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.17.

    Returns:
        Populated `TopicBuildResult` for W.17 (Circle Geometry: Subtended Spreads, Secant Products & Rational Points).
    """
    result = build_principle_model("W.17")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.17 symbolic construction, render `w-17.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_17()
    svg_out = render_svg(
        bundle.model,
        here / "w-17.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.17: Circle Geometry: Subtended Spreads, Secant Products & Rational Points")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
