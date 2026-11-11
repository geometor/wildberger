"""GEOMETOR Wildberger symbolic model and proof script for W.20: Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas.

Enunciation: A conic is the zero locus of a quadratic polynomial proportion C = <a:b:c:d:e:f>; metrically, Q(X, l) = R defines a ribbon, Q(X, F_0) = Q(X, l_dir) defines a parabola, the squared-sum/difference bifocal locus A(Q(X, F_1), Q(X, F_2), S) = 0 defines a quadrola (unifying ellipses and hyperbolas into one irreducible algebraic curve), and Q(X, l_1) +/- Q(X, l_2) = R defines a grammola.
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


def construct_w_20() -> TopicBuildResult:
    """Construct the exact symbolic model and verifications for W.20.

    Returns:
        Populated `TopicBuildResult` for W.20 (Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas).
    """
    result = build_principle_model("W.20")
    assert_zero_floats(result.model)
    return result


def main() -> None:
    """Execute W.20 symbolic construction, render `w-20.svg`, and print invariants."""
    here = Path(__file__).resolve().parent
    bundle = construct_w_20()
    svg_out = render_svg(
        bundle.model,
        here / "w-20.svg",
        extra_curves=bundle.extra_curves,
        annotations=bundle.annotations,
    )
    print("W.20: Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas")
    print(f"  Elements in model: {len(bundle.model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for label, val, status in bundle.verifications:
        print(f"  [OK] {label}: {val} ({status})")


if __name__ == "__main__":
    main()
