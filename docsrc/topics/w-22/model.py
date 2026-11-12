"""GEOMETOR Wildberger symbolic model and proof script for W.22: Projective Cross-Ratio, Harmonic Pencils & The Pappus Bridge.

Enunciation: If four concurrent lines r_1, r_2, r_3, r_4 through O_p meet a transversal l_a at collinear points A_1, A_2, A_3, A_4 and another transversal l_b at B_1, B_2, B_3, B_4, then the squared cross-ratio in quadrances (Q(A_1, A_3)*Q(A_2, A_4)) / (Q(A_1, A_4)*Q(A_2, A_3)) equals the pencil spread cross-ratio (s_13 * s_24) / (s_14 * s_23) and is invariant across all transversals.
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


def construct_w_22() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.22.

    Returns:
        Populated `TopicBuildResult` for W.22 (Projective Cross-Ratio, Harmonic Pencils & The Pappus Bridge).
    """
    result = build_principle_model("W.22")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.22 symbolic construction, render `w-22.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_22()
    svg_out = render_svg(
        bundle.model,
        here / "w-22.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.22: Projective Cross-Ratio, Harmonic Pencils & The Pappus Bridge")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
