"""GEOMETOR Wildberger symbolic model and proof script for W.15: Circumcenter, Orthocenter & Universal Affine Barycentrics.

Enunciation: Every non-null triangle A_1 A_2 A_3 over a field F (char F != 2) has a unique circumcenter C at the intersection of its side perpendicular bisectors and a unique orthocenter O at the intersection of its altitudes, with affine barycentric weights beta_i = Q_i*(Q_j + Q_k - Q_i)/(2*A) for C and gamma_i = (Q_i + Q_j - Q_k)*(Q_k + Q_i - Q_j)/(2*A) for O.
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


def construct_w_15() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.15.

    Returns:
        Populated `TopicBuildResult` for W.15 (Circumcenter, Orthocenter & Universal Affine Barycentrics).
    """
    result = build_principle_model("W.15")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.15 symbolic construction, render `w-15.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_15()
    svg_out = render_svg(
        bundle.model,
        here / "w-15.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.15: Circumcenter, Orthocenter & Universal Affine Barycentrics")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
