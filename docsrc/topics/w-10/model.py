"""GEOMETOR Wildberger symbolic model and proof script for W.10: Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas.

Enunciation: For any three coplanar non-null lines l_1, l_2, l_3 with pairwise spreads s_1, s_2, s_3 and crosses c_i = 1 - s_i, the spreads satisfy the cubic Triple Spread Formula (s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4*s_1*s_2*s_3 and the crosses satisfy (c_1 + c_2 + c_3 - 1)^2 = 4*c_1*c_2*c_3; for four lines, the Quadruple Spread polynomial R(s_12, s_23, s_34, s_14) = 0 is identically invariant under s_ij <-> 1 - s_ij.
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


def construct_w_10() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.10.

    Returns:
        Populated `TopicBuildResult` for W.10 (Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas).
    """
    result = build_principle_model("W.10")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.10 symbolic construction, render `w-10.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_10()
    svg_out = render_svg(
        bundle.model,
        here / "w-10.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.10: Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
