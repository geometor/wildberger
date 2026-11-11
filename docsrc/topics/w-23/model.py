"""GEOMETOR Wildberger symbolic model and proof script for W.23: Chromogeometry & Universal Symmetric Bilinear Forms.

Enunciation: Replacing the Euclidean quadratic form with any non-degenerate symmetric bilinear form M on F^2 preserves all Five Laws of Rational Trigonometry; in Chromogeometry—pairing Blue (dx^2 + dy^2), Red (dx^2 - dy^2), and Green (2*dx*dy) metrics on the same triangle—the three Euler lines concur at the centroid G, C_B C_R O_B C_G is a parallelogram, and N_B = (C_R + C_G)/2.
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


def construct_w_23() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.23.

    Returns:
        Populated `TopicBuildResult` for W.23 (Chromogeometry & Universal Symmetric Bilinear Forms).
    """
    result = build_principle_model("W.23")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.23 symbolic construction, render `w-23.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_23()
    svg_out = render_svg(
        bundle.model,
        here / "w-23.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.23: Chromogeometry & Universal Symmetric Bilinear Forms")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
