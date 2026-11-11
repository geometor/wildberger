"""GEOMETOR Wildberger symbolic model and proof script for W.05: Spread Polynomials S_n(s) & Pentagonal Golden Spreads.

Enunciation: The integer-coefficient spread polynomials S_0(s) = 0, S_1(s) = s, S_n(s) = 2(1 - 2s)S_{n-1}(s) - S_{n-2}(s) + 2s satisfy the semigroup composition law S_n(S_m(s)) = S_{nm}(s) over every commutative ring, and the fivefold polynomial S_5(s) = s(16s^2 - 20s + 5)^2 vanishes precisely at the Pentagonal Golden Spreads s = (5 -/+ sqrt(5))/8 = (3 - phi)/4 and (2 + phi)/4.
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


def construct_w_05() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.05.

    Returns:
        Populated `TopicBuildResult` for W.05 (Spread Polynomials S_n(s) & Pentagonal Golden Spreads).
    """
    result = build_principle_model("W.05")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.05 symbolic construction, render `w-05.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_05()
    svg_out = render_svg(
        bundle.model,
        here / "w-05.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.05: Spread Polynomials S_n(s) & Pentagonal Golden Spreads")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
