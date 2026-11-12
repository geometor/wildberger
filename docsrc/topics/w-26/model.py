"""GEOMETOR Wildberger symbolic model and proof script for W.26: Algebraic Physics: Projectile Parabolas, Snell's Law & Relativity.

Enunciation: A Galilean projectile launched from O with initial speed-squared v^2 and elevation spread s traces a parabola whose apex height h = v^2*s/(2*g), horizontal range quadrance Q_range = 16*(v^4/(4*g^2))*s*(1 - s) = (v^4/g^2)*S_2(s), and focus-directrix geometry depend rationally on s; Snell's refraction law becomes n_1^2 * s_1 = n_2^2 * s_2 in spreads.
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


def construct_w_26() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.26.

    Returns:
        Populated `TopicBuildResult` for W.26 (Algebraic Physics: Projectile Parabolas, Snell's Law & Relativity).
    """
    result = build_principle_model("W.26")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.26 symbolic construction, render `w-26.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_26()
    svg_out = render_svg(
        bundle.model,
        here / "w-26.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.26: Algebraic Physics: Projectile Parabolas, Snell's Law & Relativity")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
