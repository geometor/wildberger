"""GEOMETOR Wildberger symbolic model and proof script for W.16: The Euler Line & Nine-Point Circle Over Arbitrary Fields.

Enunciation: In any non-null triangle A_1 A_2 A_3 over a field F (char F != 2), the nine-point center N = (C + O)/2 satisfies 2*N - C = O (and 3*G = 2*C + O when char F != 3), placing C, G, N, O on the Euler line with quadrance proportions Q(C, G) : Q(C, N) : Q(C, O) = 4 : 9 : 36; the three side midpoints M_i, three altitude feet F_i, and three Euler midpoints E_i = (A_i + O)/2 all have exact quadrance K / 4 from N.
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


def construct_w_16() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.16.

    Returns:
        Populated `TopicBuildResult` for W.16 (The Euler Line & Nine-Point Circle Over Arbitrary Fields).
    """
    result = build_principle_model("W.16")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.16 symbolic construction, render `w-16.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_16()
    svg_out = render_svg(
        bundle.model,
        here / "w-16.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.16: The Euler Line & Nine-Point Circle Over Arbitrary Fields")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
