"""GEOMETOR Wildberger symbolic model and proof script for W.02: Lineations, Central Rotations & Reflections in Lines.

Enunciation: For any non-null line l = <a : b : c> over a field F (char F != 2), the reflection sigma_l maps every point A = [x, y] and every line m = <a_2 : b_2 : c_2> to exact rational images whose denominators depend only on the quadratic norm a^2 + b^2, without radicals or angles.
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


def construct_w_02() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.02.

    Returns:
        Populated `TopicBuildResult` for W.02 (Lineations, Central Rotations & Reflections in Lines).
    """
    result = build_principle_model("W.02")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.02 symbolic construction, render `w-02.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_02()
    svg_out = render_svg(
        bundle.model,
        here / "w-02.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.02: Lineations, Central Rotations & Reflections in Lines")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
