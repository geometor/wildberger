"""GEOMETOR Wildberger symbolic model and proof script for W.25: Snellius–Pothenot Resection & Hansen's Surveying Problem.

Enunciation: In Snellius-Pothenot resection, an observer P measuring spreads to three known beacons A, B, C lies on the algebraic intersection of two subtended-spread conics; in Hansen's problem, knowing one baseline quadrance Q(A, B) and four sighting spreads at unobserved stations C, D determines every side and diagonal quadrance exactly via Triple Spread Systems and Alternate Spreads.
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


def construct_w_25() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.25.

    Returns:
        Populated `TopicBuildResult` for W.25 (Snellius–Pothenot Resection & Hansen's Surveying Problem).
    """
    result = build_principle_model("W.25")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.25 symbolic construction, render `w-25.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_25()
    svg_out = render_svg(
        bundle.model,
        here / "w-25.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.25: Snellius–Pothenot Resection & Hansen's Surveying Problem")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
