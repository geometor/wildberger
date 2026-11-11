"""GEOMETOR Wildberger symbolic model and proof script for W.19: Regular Stars, Golden Pentagons & Finite-Field Polygons.

Enunciation: A regular n-star of lines has consecutive spread s satisfying S_n(s) = 0; for n = 5, a regular pentagon P_0..P_4 has side-to-diagonal spread alpha = (5 - sqrt(5))/8 = (3 - phi)/4, exterior/star spread beta = (5 + sqrt(5))/8 = (2 + phi)/4, and exact golden quadrance ratio Q_diag / Q_side = beta / alpha = phi^2 = phi + 1, existing rationally in F_p^2 whenever 5 and -1/5-dependent discriminants split (e.g. regular 5-stars in F_19).
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


def construct_w_19() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.19.

    Returns:
        Populated `TopicBuildResult` for W.19 (Regular Stars, Golden Pentagons & Finite-Field Polygons).
    """
    result = build_principle_model("W.19")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.19 symbolic construction, render `w-19.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_19()
    svg_out = render_svg(
        bundle.model,
        here / "w-19.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.19: Regular Stars, Golden Pentagons & Finite-Field Polygons")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
