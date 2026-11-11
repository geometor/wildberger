"""Exact `geometor.model.Model` builders and SymPy verifiers for `W.01`..`W.28`.

Provides `TopicBuildResult` and `build_principle_model(code)` dispatching to
`models_a` (`W.01`..`W.14`) and `models_b` (`W.15`..`W.28`). Every geometric
coordinate in every `Model` is 100% exact (`sp.Integer`, `sp.Rational`,
`sp.GoldenRatio`, `sp.sqrt`), containing zero `sp.Float` approximations.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.wildberger.invariants import LineProportion


@dataclass
class TopicBuildResult:
    """Complete exact geometric model and SymPy verification bundle for a Principle.

    Attributes:
        code: Canonical principle code `'W.01'`..`'W.28'`.
        model: Populated exact `geometor.model.Model`.
        extra_curves: Optional rational-sampled curves for SVG rendering.
        annotations: Quadrance and Spread callout badges for SVG rendering.
        verifications: List of `(label, exact_expression_str, status_str)` rows.
        invariants: Dictionary of named exact `SymPy` invariants.
    """

    code: str
    model: Model
    extra_curves: list[dict[str, object]]
    annotations: list[dict[str, object]]
    verifications: list[tuple[str, str, str]]
    invariants: dict[str, sp.Expr | str]


def foot_on_line(pt: tuple[sp.Expr, sp.Expr], line: LineProportion) -> tuple[sp.Expr, sp.Expr]:
    """Return the exact rational foot of the altitude from `pt` to `line`.

    Args:
        pt: External point `(x0, y0)`.
        line: Target non-null `LineProportion`.

    Returns:
        Exact coordinate pair `(fx, fy)`.
    """
    return line.foot_of_altitude(pt)


def midpoint_xy(
    p1: tuple[sp.Expr, sp.Expr],
    p2: tuple[sp.Expr, sp.Expr],
) -> tuple[sp.Expr, sp.Expr]:
    """Return the exact midpoint of two planar coordinate pairs.

    Args:
        p1: First point `(x1, y1)`.
        p2: Second point `(x2, y2)`.

    Returns:
        Exact midpoint `(mx, my)`.
    """
    return (sp.simplify((p1[0] + p2[0]) / 2), sp.simplify((p1[1] + p2[1]) / 2))


def second_point_on_line(
    line: LineProportion,
    avoid: tuple[sp.Expr, sp.Expr],
) -> tuple[sp.Expr, sp.Expr]:
    """Pick a deterministic exact rational point on `line` distinct from `avoid`.

    Args:
        line: Homogeneous `LineProportion` `<a : b : c>`.
        avoid: Point `(x0, y0)` to stay distinct from.

    Returns:
        Exact point `(x1, y1)` lying on `line`.
    """
    a, b, c = line.a, line.b, line.c
    if sp.simplify(b) != 0:
        x_try = avoid[0] + sp.Integer(2)
        y_try = sp.simplify((-a * x_try - c) / b)
        return (x_try, y_try)
    y_try = avoid[1] + sp.Integer(2)
    x_try = sp.simplify((-b * y_try - c) / a)
    return (x_try, y_try)


def add_line_from_proportion(
    model: Model,
    line: LineProportion,
    anchor: tuple[sp.Expr, sp.Expr],
    line_id: str,
    classes: list[str] | None = None,
) -> spg.Line:
    """Register a `LineProportion` in `model` using two exact guide/anchor points.

    Args:
        model: Target `geometor.model.Model`.
        line: Exact `LineProportion` to add.
        anchor: Known point `(x0, y0)` on `line`.
        line_id: Element `ID` for `:g:` hover synchronization.
        classes: Optional CSS class list.

    Returns:
        Constructed `sympy.geometry.Line`.
    """
    q_xy = second_point_on_line(line, anchor)
    p_pt = model.set_point(anchor[0], anchor[1], classes=["guide"], guide=True)
    q_pt = model.set_point(q_xy[0], q_xy[1], classes=["guide"], guide=True)
    return model.construct_line(p_pt, q_pt, classes=classes or [], ID=line_id)


def finalize_model_guides(model: Model, named_point_ids: set[str]) -> None:
    """Ensure named points stay visible and mark unlisted intersection points as guides.

    Args:
        model: Populated `geometor.model.Model`.
        named_point_ids: Explicit point IDs intended for visible diagram labels.
    """
    for el, info in model.items():
        if isinstance(el, spg.Point):
            if info.ID in named_point_ids:
                info.classes.pop("guide", None)
            else:
                info.classes["guide"] = ""


def assert_zero_floats(model: Model) -> None:
    """Verify that no element in `model` contains `sp.Float` approximations.

    Args:
        model: Populated `geometor.model.Model`.

    Raises:
        AssertionError: If any `sp.Float` atom is detected in `model`.
    """
    for el in model:
        if isinstance(el, spg.Point):
            atoms = el.x.atoms(sp.Float) | el.y.atoms(sp.Float)
            if atoms:
                raise AssertionError(f"Float atom found in Point {el}: {atoms}")


def build_principle_model(code: str) -> TopicBuildResult:
    """Build the exact `Model`, SVG callouts, and `SymPy` verifications for `code`.

    Args:
        code: Canonical code `'W.01'`..`'W.28'` or slug `'w-01'`..`'w-28'`.

    Returns:
        Populated `TopicBuildResult` verified to contain zero `sp.Float` atoms.

    Raises:
        KeyError: If `code` does not match `W.01`..`W.28`.
    """
    from geometor.wildberger.catalog import get_principle_by_code
    from geometor.wildberger.models_a import BUILDERS_A
    from geometor.wildberger.models_b import BUILDERS_B

    spec = get_principle_by_code(code)
    builders = {**BUILDERS_A, **BUILDERS_B}
    result = builders[spec.code]()
    assert_zero_floats(result.model)
    return result
