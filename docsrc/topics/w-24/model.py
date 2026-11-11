"""GEOMETOR Wildberger symbolic model and proof script for W.24: Exact Triangle Solvers & Surveying Triangulation.

Enunciation: Every classical triangle specification (QQQ, QQS, QSS, SQQ, and SSS up to scaling) reduces to linear or quadratic equations in quadrances and spreads with exact discriminant branching; applied to surveying, inaccessible heights and Regiomontanus' maximum-spread viewing problem resolve by pure rational algebra without trigonometric tables.
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


def construct_w_24() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.24.

    Returns:
        Populated `TopicBuildResult` for W.24 (Exact Triangle Solvers & Surveying Triangulation).
    """
    result = build_principle_model("W.24")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.24 symbolic construction, render `w-24.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_24()
    svg_out = render_svg(
        bundle.model,
        here / "w-24.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.24: Exact Triangle Solvers & Surveying Triangulation")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
