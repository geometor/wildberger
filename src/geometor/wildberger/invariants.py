"""Exact algebraic invariants for Rational Trigonometry and Universal Geometry.

Implements quadrance, spread, cross, twist, quadrea (Archimedes' function),
spread polynomials, projective line and conic proportions, 3D dihedral spreads,
cross-ratio quadrance/spread invariants, finite-field arithmetic over GF(p),
and universal symmetric bilinear metric forms (Blue, Red, and Green
Chromogeometry) using 100% exact SymPy symbolic expressions.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeAlias

import sympy as sp
import sympy.geometry as spg

CoordScalar: TypeAlias = sp.Expr | int
Point2DInput: TypeAlias = tuple[CoordScalar, CoordScalar] | spg.Point2D | sp.Matrix
Point3DInput: TypeAlias = (
    tuple[CoordScalar, CoordScalar, CoordScalar] | spg.Point3D | sp.Matrix
)


def _sympify_exact(val: CoordScalar) -> sp.Expr:
    """Convert an integer or symbolic expression to an exact SymPy expression.

    Args:
        val: Integer or exact SymPy expression (never float).

    Returns:
        Exact SymPy expression.

    Raises:
        TypeError: If a floating-point value or `sp.Float` is passed.
    """
    if isinstance(val, float) or isinstance(val, sp.Float):
        raise TypeError("Floating-point values are forbidden in geometor.wildberger.")
    expr = sp.sympify(val)
    if expr.has(sp.Float):
        raise TypeError("Expressions containing sp.Float are forbidden.")
    return expr


def _clean_golden(expr: sp.Expr) -> sp.Expr:
    """Normalize an algebraic expression, expanding GoldenRatio in Q(sqrt(5)) when present.

    Args:
        expr: Exact SymPy expression.

    Returns:
        Canonicalized exact SymPy expression.
    """
    if expr.is_Rational:
        return expr
    if expr.has(sp.GoldenRatio):
        expr = expr.subs(sp.GoldenRatio, (sp.Integer(1) + sp.sqrt(5)) / 2)
    if not expr.free_symbols:
        num, den = sp.fraction(sp.together(expr))
        num_e = sp.expand(num)
        if num_e == 0:
            return sp.Integer(0)
        den_e = sp.expand(den)
        if den_e == 1:
            return num_e
        return sp.simplify(num_e / den_e)
    num, den = sp.fraction(sp.together(expr))
    if den == 1:
        return sp.expand(num)
    num_exp = sp.expand(num)
    if num_exp == 0:
        return sp.Integer(0)
    if len(expr.free_symbols) <= 2:
        return sp.cancel(num_exp / sp.expand(den))
    return num_exp / den


def to_vec2(pt: Point2DInput) -> tuple[sp.Expr, sp.Expr]:
    """Extract an exact 2D coordinate pair `(x, y)` from a supported point input.

    Args:
        pt: A 2-tuple, `sympy.geometry.Point2D`, or 2x1 `sympy.Matrix`.

    Returns:
        Tuple of exact SymPy expressions `(x, y)`.
    """
    if isinstance(pt, spg.Point2D):
        return _sympify_exact(pt.x), _sympify_exact(pt.y)
    if isinstance(pt, sp.MatrixBase):
        return _sympify_exact(pt[0]), _sympify_exact(pt[1])
    return _sympify_exact(pt[0]), _sympify_exact(pt[1])


def to_vec3(pt: Point3DInput) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Extract an exact 3D coordinate triple `(x, y, z)` from a supported point input.

    Args:
        pt: A 3-tuple, `sympy.geometry.Point3D`, or 3x1 `sympy.Matrix`.

    Returns:
        Tuple of exact SymPy expressions `(x, y, z)`.
    """
    if isinstance(pt, spg.Point3D):
        return _sympify_exact(pt.x), _sympify_exact(pt.y), _sympify_exact(pt.z)
    if isinstance(pt, sp.MatrixBase):
        return _sympify_exact(pt[0]), _sympify_exact(pt[1]), _sympify_exact(pt[2])
    return _sympify_exact(pt[0]), _sympify_exact(pt[1]), _sympify_exact(pt[2])


def mod_div(num: CoordScalar, den: CoordScalar, p: int) -> sp.Integer:
    """Compute exact modular division `num * den^(-1) mod p` over GF(p).

    Args:
        num: Numerator integer or SymPy integer expression.
        den: Denominator integer (must be non-zero modulo `p`).
        p: Odd prime modulus (`p > 2`).

    Returns:
        Canonical residue in `{0, 1, ..., p - 1}` as `sp.Integer`.

    Raises:
        ValueError: If `p <= 2` or `den == 0 (mod p)`.
    """
    if p <= 2:
        raise ValueError("Rational trigonometry requires field characteristic != 2.")
    n_mod = int(sp.Integer(num) % p)
    d_mod = int(sp.Integer(den) % p)
    if d_mod == 0:
        raise ValueError(f"Zero denominator modulo {p} (null element).")
    inv = int(sp.invert(d_mod, p))
    return sp.Integer((n_mod * inv) % p)


@dataclass(frozen=True)
class MetricForm:
    """Symmetric bilinear form `B(u, v) = u^T M v` for Universal Geometry.

    Attributes:
        name: Human-readable metric name (e.g., `'Blue'`, `'Red'`, `'Green'`).
        matrix: Exact 2x2 symmetric `sympy.Matrix`.
        modulus: Optional odd prime `p` to evaluate arithmetic in `GF(p)`.
    """

    name: str
    matrix: sp.Matrix
    modulus: int | None = None

    def reduce_scalar(self, val: sp.Expr) -> sp.Expr:
        """Reduce a scalar symbolically or modulo `self.modulus` if over GF(p).

        Args:
            val: Exact SymPy scalar expression.

        Returns:
            Simplified exact expression or `sp.Integer` residue modulo `p`.
        """
        cleaned = _clean_golden(val)
        if self.modulus is None:
            return cleaned
        num, den = sp.fraction(cleaned)
        return mod_div(int(num), int(den), self.modulus)

    def bilinear(
        self, u: tuple[sp.Expr, sp.Expr], v: tuple[sp.Expr, sp.Expr]
    ) -> sp.Expr:
        """Evaluate the symmetric bilinear form `u^T M v`.

        Args:
            u: First 2D displacement vector `(ux, uy)`.
            v: Second 2D displacement vector `(vx, vy)`.

        Returns:
            Exact scalar `B(u, v)`.
        """
        u_vec = sp.Matrix([u[0], u[1]])
        v_vec = sp.Matrix([v[0], v[1]])
        raw = (u_vec.T * self.matrix * v_vec)[0]
        return self.reduce_scalar(raw)

    def quadratic(self, u: tuple[sp.Expr, sp.Expr]) -> sp.Expr:
        """Evaluate the quadratic form `Q(u) = u^T M u`.

        Args:
            u: 2D displacement vector `(ux, uy)`.

        Returns:
            Exact quadrance of vector `u`.
        """
        return self.bilinear(u, u)

    def with_modulus(self, p: int) -> MetricForm:
        """Return a copy of this metric evaluated over the finite field `GF(p)`.

        Args:
            p: Odd prime modulus (`p > 2`).

        Returns:
            New `MetricForm` over `GF(p)`.
        """
        if p <= 2:
            raise ValueError("Characteristic 2 is excluded in Rational Trigonometry.")
        return MetricForm(name=f"{self.name}_GF({p})", matrix=self.matrix, modulus=p)


BLUE_METRIC = MetricForm(
    name="Blue",
    matrix=sp.Matrix([[sp.Integer(1), sp.Integer(0)], [sp.Integer(0), sp.Integer(1)]]),
)
RED_METRIC = MetricForm(
    name="Red",
    matrix=sp.Matrix([[sp.Integer(1), sp.Integer(0)], [sp.Integer(0), sp.Integer(-1)]]),
)
GREEN_METRIC = MetricForm(
    name="Green",
    matrix=sp.Matrix([[sp.Integer(0), sp.Integer(1)], [sp.Integer(1), sp.Integer(0)]]),
)


@dataclass(frozen=True)
class LineProportion:
    """Planar line `<a : b : c>` representing `a*x + b*y + c = 0`.

    Attributes:
        a: Coefficient of `x`.
        b: Coefficient of `y`.
        c: Constant term.
    """

    a: sp.Expr
    b: sp.Expr
    c: sp.Expr

    def __init__(self, a: CoordScalar, b: CoordScalar, c: CoordScalar) -> None:
        """Initialize an exact line proportion `<a : b : c>`.

        Args:
            a: Coefficient of `x`.
            b: Coefficient of `y`.
            c: Constant term.
        """
        object.__setattr__(self, "a", _sympify_exact(a))
        object.__setattr__(self, "b", _sympify_exact(b))
        object.__setattr__(self, "c", _sympify_exact(c))

    @classmethod
    def from_points(cls, p1: Point2DInput, p2: Point2DInput) -> LineProportion:
        """Construct the unique line `<y1 - y2 : x2 - x1 : x1*y2 - x2*y1>` through `p1, p2`.

        Args:
            p1: First point `[x1, y1]`.
            p2: Second point `[x2, y2]`.

        Returns:
            `LineProportion` passing through `p1` and `p2`.
        """
        x1, y1 = to_vec2(p1)
        x2, y2 = to_vec2(p2)
        return cls(
            _clean_golden(y1 - y2),
            _clean_golden(x2 - x1),
            _clean_golden(x1 * y2 - x2 * y1),
        )

    def direction(self) -> tuple[sp.Expr, sp.Expr]:
        """Return a tangent direction vector `(-b, a)` along the line.

        Returns:
            Direction vector `(-b, a)`.
        """
        return (-self.b, self.a)

    def contains(self, pt: Point2DInput, modulus: int | None = None) -> bool:
        """Check whether point `pt` lies on the line.

        Args:
            pt: Point `[x, y]`.
            modulus: Optional prime modulus `p` for `GF(p)`.

        Returns:
            True if `a*x + b*y + c == 0`.
        """
        x, y = to_vec2(pt)
        val = _clean_golden(self.a * x + self.b * y + self.c)
        if modulus is not None:
            num, den = sp.fraction(val)
            return int(mod_div(int(num), int(den), modulus)) == 0
        return sp.simplify(val) == 0

    def is_parallel(self, other: LineProportion, modulus: int | None = None) -> bool:
        """Check whether two lines are parallel (`a1*b2 - a2*b1 == 0`).

        Args:
            other: Second line proportion.
            modulus: Optional prime modulus `p`.

        Returns:
            True if parallel.
        """
        det = _clean_golden(self.a * other.b - other.a * self.b)
        if modulus is not None:
            num, den = sp.fraction(det)
            return int(mod_div(int(num), int(den), modulus)) == 0
        return sp.simplify(det) == 0

    def is_perpendicular(
        self, other: LineProportion, metric: MetricForm = BLUE_METRIC
    ) -> bool:
        """Check whether two lines are perpendicular under `metric`.

        Args:
            other: Second line proportion.
            metric: Symmetric bilinear metric form (defaults to Euclidean Blue).

        Returns:
            True if `B(dir(self), dir(other)) == 0`.
        """
        prod = metric.bilinear(self.direction(), other.direction())
        return sp.simplify(prod) == 0

    def is_null(self, metric: MetricForm = BLUE_METRIC) -> bool:
        """Check whether this line is a null (isotropic) line under `metric`.

        Args:
            metric: Symmetric bilinear metric form.

        Returns:
            True if `Q_M(direction) == 0`.
        """
        return sp.simplify(metric.quadratic(self.direction())) == 0

    def meet(
        self, other: LineProportion, modulus: int | None = None
    ) -> tuple[sp.Expr, sp.Expr]:
        """Compute the intersection point of two non-parallel lines.

        Args:
            other: Intersecting line proportion.
            modulus: Optional prime modulus `p` for `GF(p)`.

        Returns:
            Exact intersection point `(x, y)`.

        Raises:
            ValueError: If the lines are parallel.
        """
        den = _clean_golden(self.a * other.b - other.a * self.b)
        num_x = _clean_golden(self.b * other.c - other.b * self.c)
        num_y = _clean_golden(other.a * self.c - self.a * other.c)
        if modulus is not None:
            return (
                mod_div(int(num_x), int(den), modulus),
                mod_div(int(num_y), int(den), modulus),
            )
        if sp.simplify(den) == 0:
            raise ValueError("Parallel lines do not meet in affine coordinates.")
        return (_clean_golden(num_x / den), _clean_golden(num_y / den))

    def parallel_through(self, pt: Point2DInput) -> LineProportion:
        """Construct the unique line parallel to `self` passing through `pt`.

        Args:
            pt: Point `[x0, y0]`.

        Returns:
            Parallel `LineProportion` `<a : b : -(a*x0 + b*y0)>`.
        """
        x0, y0 = to_vec2(pt)
        return LineProportion(self.a, self.b, _clean_golden(-(self.a * x0 + self.b * y0)))

    def altitude_from(
        self, pt: Point2DInput, metric: MetricForm = BLUE_METRIC
    ) -> LineProportion:
        """Construct the altitude line from `pt` perpendicular to `self` under `metric`.

        Args:
            pt: Point `[x0, y0]`.
            metric: Symmetric bilinear metric form.

        Returns:
            `LineProportion` through `pt` orthogonal to `self` under `metric`.
        """
        x0, y0 = to_vec2(pt)
        d_vec = sp.Matrix([self.direction()[0], self.direction()[1]])
        covec = (d_vec.T * metric.matrix)
        na = metric.reduce_scalar(covec[0])
        nb = metric.reduce_scalar(covec[1])
        nc = metric.reduce_scalar(-(na * x0 + nb * y0))
        return LineProportion(na, nb, nc)

    def foot_of_altitude(
        self, pt: Point2DInput, metric: MetricForm = BLUE_METRIC
    ) -> tuple[sp.Expr, sp.Expr]:
        """Compute the foot `F` of the altitude from `pt` onto non-null line `self`.

        Args:
            pt: Point `[x0, y0]`.
            metric: Symmetric bilinear metric form.

        Returns:
            Exact coordinates `(fx, fy)` of the foot of the altitude.
        """
        alt = self.altitude_from(pt, metric=metric)
        return self.meet(alt, modulus=metric.modulus)

    def reflect_point(
        self, pt: Point2DInput, metric: MetricForm = BLUE_METRIC
    ) -> tuple[sp.Expr, sp.Expr]:
        """Reflect point `pt` across non-null line `self` (`sigma_l(A) = 2*F - A`).

        Args:
            pt: Point `[x0, y0]`.
            metric: Symmetric bilinear metric form.

        Returns:
            Reflected point `(rx, ry)`.
        """
        x0, y0 = to_vec2(pt)
        fx, fy = self.foot_of_altitude(pt, metric=metric)
        return (
            metric.reduce_scalar(2 * fx - x0),
            metric.reduce_scalar(2 * fy - y0),
        )

    def reflect_line(self, other: LineProportion) -> LineProportion:
        """Reflect line `other` across Euclidean non-null line `self` (`Sigma_l(m)`).

        Uses Wildberger's Reflection of a Line in a Line Theorem (Theorem 15):
        no square roots or trigonometric functions required.

        Args:
            other: Line `<a2 : b2 : c2>` to reflect across `self = <a1 : b1 : c1>`.

        Returns:
            Reflected `LineProportion`.
        """
        a1, b1, c1 = self.a, self.b, self.c
        a2, b2, c2 = other.a, other.b, other.c
        ra = _clean_golden((a1**2 - b1**2) * a2 + 2 * a1 * b1 * b2)
        rb = _clean_golden(2 * a1 * b1 * a2 - (a1**2 - b1**2) * b2)
        rc = _clean_golden(2 * c1 * (a1 * a2 + b1 * b2) - (a1**2 + b1**2) * c2)
        return LineProportion(ra, rb, rc)


@dataclass(frozen=True)
class ConicProportion:
    """Planar conic `<d : e : f : a : b : c>` for `d*x^2 + e*x*y + f*y^2 + a*x + b*y + c = 0`.

    Attributes:
        d: Coefficient of `x^2`.
        e: Coefficient of `x*y`.
        f: Coefficient of `y^2`.
        a: Coefficient of `x`.
        b: Coefficient of `y`.
        c: Constant term.
    """

    d: sp.Expr
    e: sp.Expr
    f: sp.Expr
    a: sp.Expr
    b: sp.Expr
    c: sp.Expr

    def __init__(
        self,
        d: CoordScalar,
        e: CoordScalar,
        f: CoordScalar,
        a: CoordScalar,
        b: CoordScalar,
        c: CoordScalar,
    ) -> None:
        """Initialize an exact 6-proportion conic.

        Args:
            d: Coefficient of `x^2`.
            e: Coefficient of `x*y`.
            f: Coefficient of `y^2`.
            a: Coefficient of `x`.
            b: Coefficient of `y`.
            c: Constant term.
        """
        object.__setattr__(self, "d", _sympify_exact(d))
        object.__setattr__(self, "e", _sympify_exact(e))
        object.__setattr__(self, "f", _sympify_exact(f))
        object.__setattr__(self, "a", _sympify_exact(a))
        object.__setattr__(self, "b", _sympify_exact(b))
        object.__setattr__(self, "c", _sympify_exact(c))

    def evaluate(self, pt: Point2DInput) -> sp.Expr:
        """Evaluate `d*x^2 + e*x*y + f*y^2 + a*x + b*y + c` at `pt`.

        Args:
            pt: Point `[x, y]`.

        Returns:
            Exact value of the quadratic polynomial at `pt`.
        """
        x, y = to_vec2(pt)
        return _clean_golden(
            self.d * x**2
            + self.e * x * y
            + self.f * y**2
            + self.a * x
            + self.b * y
            + self.c
        )

    def center(self, modulus: int | None = None) -> tuple[sp.Expr, sp.Expr]:
        """Compute the unique center `[(2af - be)/(e^2 - 4df), (2bd - ae)/(e^2 - 4df)]`.

        Args:
            modulus: Optional prime modulus `p` for `GF(p)`.

        Returns:
            Center coordinates `(cx, cy)`.

        Raises:
            ValueError: If `e^2 - 4*d*f == 0` (parabolic/ribbon case without unique center).
        """
        disc = _clean_golden(self.e**2 - 4 * self.d * self.f)
        num_x = _clean_golden(2 * self.a * self.f - self.b * self.e)
        num_y = _clean_golden(2 * self.b * self.d - self.a * self.e)
        if modulus is not None:
            return (
                mod_div(int(num_x), int(disc), modulus),
                mod_div(int(num_y), int(disc), modulus),
            )
        if sp.simplify(disc) == 0:
            raise ValueError("Conic has e^2 - 4df = 0; unique center does not exist.")
        return (_clean_golden(num_x / disc), _clean_golden(num_y / disc))

    def translate(self, shift: Point2DInput) -> ConicProportion:
        """Translate conic by `shift = [u, v]` (`tau_B(q)` from Theorem 118).

        Args:
            shift: Translation vector `[u, v]`.

        Returns:
            Translated `ConicProportion`.
        """
        u, v = to_vec2(shift)
        a1 = _clean_golden(self.a - 2 * self.d * u - self.e * v)
        b1 = _clean_golden(self.b - 2 * self.f * v - self.e * u)
        c1 = _clean_golden(
            self.d * u**2
            + self.e * u * v
            + self.f * v**2
            - self.a * u
            - self.b * v
            + self.c
        )
        return ConicProportion(self.d, self.e, self.f, a1, b1, c1)

    def taylor_conic(self, pt: Point2DInput) -> ConicProportion:
        """Compute the standard Taylor conic `q_A = tau_A^(-1)(q)` at point `pt` on `q`.

        Args:
            pt: Point `[x0, y0]` lying on the conic.

        Returns:
            Standard `ConicProportion` with constant term `0` when `pt` lies on `q`.
        """
        x0, y0 = to_vec2(pt)
        return self.translate((-x0, -y0))

    def tangent_at(self, pt: Point2DInput) -> LineProportion:
        """Compute the algebraic tangent line `T_A^(1)(q)` at a non-singular point `pt` on `q`.

        Implements Wildberger's calculus-free Tangent to a Conic Theorem (Theorem 119):
        `<a + 2*d*x0 + e*y0 : b + e*x0 + 2*f*y0 : a*x0 + b*y0 + 2*c>`.

        Args:
            pt: Non-singular point `[x0, y0]` on `q`.

        Returns:
            Tangent `LineProportion` at `pt`.
        """
        x0, y0 = to_vec2(pt)
        la = _clean_golden(self.a + 2 * self.d * x0 + self.e * y0)
        lb = _clean_golden(self.b + self.e * x0 + 2 * self.f * y0)
        lc = _clean_golden(self.a * x0 + self.b * y0 + 2 * self.c)
        return LineProportion(la, lb, lc)

    @classmethod
    def from_circle(cls, center: Point2DInput, k_quad: CoordScalar) -> ConicProportion:
        """Construct the circle `Q(X, C) = K` as a 6-proportion conic.

        Args:
            center: Circle center `[u, v]`.
            k_quad: Circle quadrance `K`.

        Returns:
            `ConicProportion` `<1 : 0 : 1 : -2u : -2v : u^2 + v^2 - K>`.
        """
        u, v = to_vec2(center)
        k = _sympify_exact(k_quad)
        return cls(1, 0, 1, -2 * u, -2 * v, _clean_golden(u**2 + v**2 - k))

    @classmethod
    def from_ribbon(cls, line: LineProportion, k_quad: CoordScalar) -> ConicProportion:
        """Construct the ribbon `Q(X, l) = K` around non-null `line`.

        Args:
            line: Axis line `<a : b : c>`.
            k_quad: Ribbon quadrance `K`.

        Returns:
            `ConicProportion` for `(a*x + b*y + c)^2 - K*(a^2 + b^2) = 0`.
        """
        a, b, c = line.a, line.b, line.c
        k = _sympify_exact(k_quad)
        norm = a**2 + b**2
        return cls(
            a**2,
            2 * a * b,
            b**2,
            2 * a * c,
            2 * b * c,
            _clean_golden(c**2 - k * norm),
        )

    @classmethod
    def from_parabola(
        cls, focus: Point2DInput, directrix: LineProportion
    ) -> ConicProportion:
        """Construct the parabola `Q(X, F) = Q(X, l)` from focus and directrix.

        Args:
            focus: Focus point `[u, v]`.
            directrix: Non-null directrix `<a : b : c>` not containing `focus`.

        Returns:
            `ConicProportion` from Theorem 101.
        """
        u, v = to_vec2(focus)
        a, b, c = directrix.a, directrix.b, directrix.c
        norm = a**2 + b**2
        return cls(
            b**2,
            -2 * a * b,
            a**2,
            _clean_golden(-2 * a * c - 2 * norm * u),
            _clean_golden(-2 * b * c - 2 * norm * v),
            _clean_golden(norm * (u**2 + v**2) - c**2),
        )

    @classmethod
    def from_quadrola(
        cls, f1: Point2DInput, f2: Point2DInput, k_quad: CoordScalar
    ) -> ConicProportion:
        """Construct the quadrola `A(Q(X, F1), Q(X, F2), K) = 0` unifying ellipses & hyperbolas.

        Args:
            f1: First focus `[u1, v1]`.
            f2: Second focus `[u2, v2]`.
            k_quad: Associated quadrance `K`.

        Returns:
            `ConicProportion` of degree 2 in `(x, y)` (Exercise 15.11).
        """
        x_sym, y_sym = sp.symbols("_qx _qy")
        q1 = quadrance((x_sym, y_sym), f1)
        q2 = quadrance((x_sym, y_sym), f2)
        k = _sympify_exact(k_quad)
        poly = sp.Poly(sp.expand(archimedes(q1, q2, k)), x_sym, y_sym)
        return cls(
            poly.coeff_monomial(x_sym**2),
            poly.coeff_monomial(x_sym * y_sym),
            poly.coeff_monomial(y_sym**2),
            poly.coeff_monomial(x_sym),
            poly.coeff_monomial(y_sym),
            poly.coeff_monomial(1),
        )

    @classmethod
    def from_grammola(
        cls, l1: LineProportion, l2: LineProportion, k_quad: CoordScalar
    ) -> ConicProportion:
        """Construct the grammola `Q(X, l1) + Q(X, l2) = K` from two diagonal lines.

        Args:
            l1: First non-null diagonal line.
            l2: Second non-null diagonal line.
            k_quad: Grammola quadrance `K`.

        Returns:
            `ConicProportion` representing `Q(X, l1) + Q(X, l2) - K = 0`.
        """
        x_sym, y_sym = sp.symbols("_gx _gy")
        n1 = l1.a**2 + l1.b**2
        n2 = l2.a**2 + l2.b**2
        k = _sympify_exact(k_quad)
        expr = sp.expand(
            n2 * (l1.a * x_sym + l1.b * y_sym + l1.c) ** 2
            + n1 * (l2.a * x_sym + l2.b * y_sym + l2.c) ** 2
            - k * n1 * n2
        )
        poly = sp.Poly(expr, x_sym, y_sym)
        return cls(
            poly.coeff_monomial(x_sym**2),
            poly.coeff_monomial(x_sym * y_sym),
            poly.coeff_monomial(y_sym**2),
            poly.coeff_monomial(x_sym),
            poly.coeff_monomial(y_sym),
            poly.coeff_monomial(1),
        )


def collinear_det(p1: Point2DInput, p2: Point2DInput, p3: Point2DInput) -> sp.Expr:
    """Compute the collinearity determinant `x1*y2 - x1*y3 + x2*y3 - x3*y2 + x3*y1 - x2*y1`.

    Vanishes if and only if `p1, p2, p3` are collinear (Theorem 3), and equals
    twice the signed Euclidean area of oriented triangle `p1 p2 p3`.

    Args:
        p1: First point `[x1, y1]`.
        p2: Second point `[x2, y2]`.
        p3: Third point `[x3, y3]`.

    Returns:
        Exact determinant expression.
    """
    x1, y1 = to_vec2(p1)
    x2, y2 = to_vec2(p2)
    x3, y3 = to_vec2(p3)
    return _clean_golden(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))


def concurrent_det(
    l1: LineProportion, l2: LineProportion, l3: LineProportion
) -> sp.Expr:
    """Compute the concurrency determinant of three planar lines (Theorem 4).

    Args:
        l1: First line `<a1 : b1 : c1>`.
        l2: Second line `<a2 : b2 : c2>`.
        l3: Third line `<a3 : b3 : c3>`.

    Returns:
        Exact 3x3 determinant `det([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])`.
    """
    mat = sp.Matrix([[l1.a, l1.b, l1.c], [l2.a, l2.b, l2.c], [l3.a, l3.b, l3.c]])
    return _clean_golden(mat.det())


def point_rotation(pt: Point2DInput, center: Point2DInput) -> tuple[sp.Expr, sp.Expr]:
    """Apply central half-turn rotation `rho_C([x, y]) = [2u - x, 2v - y]` in `center`.

    Args:
        pt: Point `[x, y]` to rotate.
        center: Center of rotation `C = [u, v]`.

    Returns:
        Rotated point `(2u - x, 2v - y)`.
    """
    x, y = to_vec2(pt)
    u, v = to_vec2(center)
    return (_clean_golden(2 * u - x), _clean_golden(2 * v - y))


def affine_combination(
    p1: Point2DInput, p2: Point2DInput, lam: CoordScalar
) -> tuple[sp.Expr, sp.Expr]:
    """Compute the affine combination `(1 - lam)*p1 + lam*p2`.

    Args:
        p1: First point.
        p2: Second point.
        lam: Affine ratio parameter `lambda`.

    Returns:
        Exact point `((1 - lam)*x1 + lam*x2, (1 - lam)*y1 + lam*y2)`.
    """
    x1, y1 = to_vec2(p1)
    x2, y2 = to_vec2(p2)
    t = _sympify_exact(lam)
    return (
        _clean_golden((1 - t) * x1 + t * x2),
        _clean_golden((1 - t) * y1 + t * y2),
    )


def midpoint(p1: Point2DInput, p2: Point2DInput) -> tuple[sp.Expr, sp.Expr]:
    """Compute the exact midpoint `(p1 + p2) / 2` of a side.

    Args:
        p1: First endpoint.
        p2: Second endpoint.

    Returns:
        Exact midpoint coordinates.
    """
    return affine_combination(p1, p2, sp.Rational(1, 2))


def quadrance(
    p1: Point2DInput, p2: Point2DInput, metric: MetricForm = BLUE_METRIC
) -> sp.Expr:
    """Compute the quadrance `Q_M(p1, p2)` between two planar points under `metric`.

    For the default Euclidean Blue metric, `Q(p1, p2) = (x2 - x1)^2 + (y2 - y1)^2`.

    Args:
        p1: First point `[x1, y1]`.
        p2: Second point `[x2, y2]`.
        metric: Symmetric bilinear metric form (Blue, Red, Green, or custom).

    Returns:
        Exact quadrance expression.
    """
    x1, y1 = to_vec2(p1)
    x2, y2 = to_vec2(p2)
    return metric.quadratic((x2 - x1, y2 - y1))


def point_to_line_quadrance(pt: Point2DInput, line: LineProportion) -> sp.Expr:
    """Compute the Euclidean quadrance `Q(A0, l) = (a*x0 + b*y0 + c)^2 / (a^2 + b^2)` (Theorem 25).

    Args:
        pt: Point `[x0, y0]`.
        line: Non-null line `<a : b : c>`.

    Returns:
        Exact quadrance from `pt` to `line`.
    """
    x0, y0 = to_vec2(pt)
    num = (line.a * x0 + line.b * y0 + line.c) ** 2
    den = line.a**2 + line.b**2
    return _clean_golden(num / den)


def perpendicular_bisector(
    p1: Point2DInput, p2: Point2DInput, metric: MetricForm = BLUE_METRIC
) -> LineProportion:
    """Construct the perpendicular bisector locus `Q_M(X, p1) = Q_M(X, p2)` (Theorem 12/24).

    Args:
        p1: First point `[x1, y1]`.
        p2: Second point `[x2, y2]`.
        metric: Symmetric bilinear metric form.

    Returns:
        `LineProportion` of the perpendicular bisector under `metric`.
    """
    mid = midpoint(p1, p2)
    if metric.modulus is not None:
        x1, y1 = to_vec2(p1)
        x2, y2 = to_vec2(p2)
        mid = (
            mod_div(int(x1 + x2), 2, metric.modulus),
            mod_div(int(y1 + y2), 2, metric.modulus),
        )
    base_line = LineProportion.from_points(p1, p2)
    return base_line.altitude_from(mid, metric=metric)


def cross(
    l1: LineProportion, l2: LineProportion, metric: MetricForm = BLUE_METRIC
) -> sp.Expr:
    """Compute the cross `c_M(l1, l2) = B(u, v)^2 / (Q_M(u) * Q_M(v))` between two non-null lines.

    Args:
        l1: First non-null line.
        l2: Second non-null line.
        metric: Symmetric bilinear metric form.

    Returns:
        Exact cross invariant `c = 1 - s`.
    """
    u = l1.direction()
    v = l2.direction()
    qu = metric.quadratic(u)
    qv = metric.quadratic(v)
    buv = metric.bilinear(u, v)
    return metric.reduce_scalar(buv**2 / (qu * qv))


def spread(
    l1: LineProportion, l2: LineProportion, metric: MetricForm = BLUE_METRIC
) -> sp.Expr:
    """Compute the spread `s_M(l1, l2) = 1 - c_M(l1, l2)` between two non-null lines.

    For Euclidean Blue geometry:
    `s(l1, l2) = (a1*b2 - a2*b1)^2 / ((a1^2 + b1^2)*(a2^2 + b2^2))`.

    Args:
        l1: First non-null line.
        l2: Second non-null line.
        metric: Symmetric bilinear metric form.

    Returns:
        Exact spread invariant `s`.
    """
    return metric.reduce_scalar(sp.Integer(1) - cross(l1, l2, metric=metric))


def twist(
    l1: LineProportion, l2: LineProportion, metric: MetricForm = BLUE_METRIC
) -> sp.Expr:
    """Compute the twist `t_M(l1, l2) = s_M(l1, l2) / c_M(l1, l2)` between non-perpendicular lines.

    Args:
        l1: First non-null line.
        l2: Second non-null line (not orthogonal to `l1`).
        metric: Symmetric bilinear metric form.

    Returns:
        Exact twist invariant `t = s / c`.
    """
    s_val = spread(l1, l2, metric=metric)
    c_val = cross(l1, l2, metric=metric)
    return metric.reduce_scalar(s_val / c_val)


def signed_turn(l1: LineProportion, l2: LineProportion) -> sp.Expr:
    """Compute Wildberger's oriented turn `u(l1, l2) = (a1*b2 - a2*b1) / (a1*a2 + b1*b2)`.

    Satisfies `u(l1, l2)^2 = t(l1, l2)` (the twist) and the rational tangent-addition
    Triple Turn Formula `u1 + u2 + u3 = u1 * u2 * u3` when `l1, l2, l3` cycle!

    Args:
        l1: First oriented line.
        l2: Second oriented line.

    Returns:
        Exact signed turn expression.
    """
    num = l1.a * l2.b - l2.a * l1.b
    den = l1.a * l2.a + l1.b * l2.b
    return _clean_golden(num / den)


def vertex_spread(
    vertex: Point2DInput,
    p1: Point2DInput,
    p2: Point2DInput,
    metric: MetricForm = BLUE_METRIC,
) -> sp.Expr:
    """Compute the spread at `vertex` between lines `(vertex, p1)` and `(vertex, p2)`.

    Args:
        vertex: Common vertex point `A`.
        p1: First arm point `B`.
        p2: Second arm point `C`.
        metric: Symmetric bilinear metric form.

    Returns:
        Exact vertex spread `s_A`.
    """
    l1 = LineProportion.from_points(vertex, p1)
    l2 = LineProportion.from_points(vertex, p2)
    return spread(l1, l2, metric=metric)


def vertex_cross(
    vertex: Point2DInput,
    p1: Point2DInput,
    p2: Point2DInput,
    metric: MetricForm = BLUE_METRIC,
) -> sp.Expr:
    """Compute the cross at `vertex` between lines `(vertex, p1)` and `(vertex, p2)`.

    Args:
        vertex: Common vertex point `A`.
        p1: First arm point `B`.
        p2: Second arm point `C`.
        metric: Symmetric bilinear metric form.

    Returns:
        Exact vertex cross `c_A = 1 - s_A`.
    """
    l1 = LineProportion.from_points(vertex, p1)
    l2 = LineProportion.from_points(vertex, p2)
    return cross(l1, l2, metric=metric)


def archimedes(q1: CoordScalar, q2: CoordScalar, q3: CoordScalar) -> sp.Expr:
    """Evaluate Archimedes' function `A(Q1, Q2, Q3) = (Q1 + Q2 + Q3)^2 - 2*(Q1^2 + Q2^2 + Q3^2)`.

    Args:
        q1: First quadrance.
        q2: Second quadrance.
        q3: Third quadrance.

    Returns:
        Exact value of `A(Q1, Q2, Q3)`.
    """
    a = _sympify_exact(q1)
    b = _sympify_exact(q2)
    c = _sympify_exact(q3)
    return _clean_golden((a + b + c) ** 2 - 2 * (a**2 + b**2 + c**2))


def quadrea(
    p1: Point2DInput,
    p2: Point2DInput,
    p3: Point2DInput,
    metric: MetricForm = BLUE_METRIC,
) -> sp.Expr:
    """Compute the quadrea `A_M` of triangle `p1 p2 p3` (`16 * Area^2` in Euclidean metric).

    Args:
        p1: First vertex `A1`.
        p2: Second vertex `A2`.
        p3: Third vertex `A3`.
        metric: Symmetric bilinear metric form.

    Returns:
        Exact quadrea `A(Q1, Q2, Q3)`.
    """
    q1 = quadrance(p2, p3, metric=metric)
    q2 = quadrance(p1, p3, metric=metric)
    q3 = quadrance(p1, p2, metric=metric)
    return metric.reduce_scalar(archimedes(q1, q2, q3))


def triple_spread_function(
    s1: CoordScalar, s2: CoordScalar, s3: CoordScalar
) -> sp.Expr:
    """Evaluate the Triple Spread polynomial `S(s1, s2, s3) = (s1+s2+s3)^2 - 2(s1^2+s2^2+s3^2) - 4*s1*s2*s3`.

    Vanishes whenever `s1, s2, s3` are the spreads formed by three coplanar lines.

    Args:
        s1: First spread.
        s2: Second spread.
        s3: Third spread.

    Returns:
        Exact polynomial value (zero for valid spread triples).
    """
    a = _sympify_exact(s1)
    b = _sympify_exact(s2)
    c = _sympify_exact(s3)
    return _clean_golden((a + b + c) ** 2 - 2 * (a**2 + b**2 + c**2) - 4 * a * b * c)


def triple_cross_function(
    c1: CoordScalar, c2: CoordScalar, c3: CoordScalar
) -> sp.Expr:
    """Evaluate the Triple Cross polynomial `(c1 + c2 + c3 - 1)^2 - 4*c1*c2*c3` (Theorem 49).

    Args:
        c1: First cross `1 - s1`.
        c2: Second cross `1 - s2`.
        c3: Third cross `1 - s3`.

    Returns:
        Exact polynomial value (zero for valid cross triples).
    """
    a = _sympify_exact(c1)
    b = _sympify_exact(c2)
    c = _sympify_exact(c3)
    return _clean_golden((a + b + c - 1) ** 2 - 4 * a * b * c)


def quadruple_quad_function(
    q1: CoordScalar, q2: CoordScalar, q3: CoordScalar, q4: CoordScalar
) -> sp.Expr:
    """Evaluate Wildberger's Quadruple Quad polynomial `Q(a, b, c, d)` (Theorem 31).

    `Q(a,b,c,d) = ((a+b+c+d)^2 - 2(a^2+b^2+c^2+d^2))^2 - 64*a*b*c*d`.
    Vanishes for four collinear point quadrances OR when a cyclic quadrilateral
    has zero cyclic quadrea (degenerate case).

    Args:
        q1: First quadrance.
        q2: Second quadrance.
        q3: Third quadrance.
        q4: Fourth quadrance.

    Returns:
        Exact polynomial value.
    """
    a, b, c, d = (
        _sympify_exact(q1),
        _sympify_exact(q2),
        _sympify_exact(q3),
        _sympify_exact(q4),
    )
    inner = (a + b + c + d) ** 2 - 2 * (a**2 + b**2 + c**2 + d**2)
    return _clean_golden(inner**2 - 64 * a * b * c * d)


def quadruple_spread_function(
    s1: CoordScalar, s2: CoordScalar, s3: CoordScalar, s4: CoordScalar
) -> sp.Expr:
    """Evaluate the self-dual Quadruple Spread / Cross function `R(a, b, c, d)` (Theorems 54 & 55).

    Satisfies the remarkable symmetry `R(a, b, c, d) == R(1-a, 1-b, 1-c, 1-d)`!

    Args:
        s1: Spread `s_12`.
        s2: Spread `s_23`.
        s3: Spread `s_34`.
        s4: Spread `s_14`.

    Returns:
        Exact polynomial residual.
    """
    a, b, c, d = (
        _sympify_exact(s1),
        _sympify_exact(s2),
        _sympify_exact(s3),
        _sympify_exact(s4),
    )
    inner = (
        (a + b + c + d) ** 2
        - 2 * (a**2 + b**2 + c**2 + d**2)
        - 4 * (a * b * c + a * b * d + a * c * d + b * c * d)
        + 8 * a * b * c * d
    )
    return _clean_golden(
        inner**2 - 64 * a * b * c * d * (1 - a) * (1 - b) * (1 - c) * (1 - d)
    )


def euler_four_point_function(
    q1: CoordScalar,
    q2: CoordScalar,
    q3: CoordScalar,
    p1: CoordScalar,
    p2: CoordScalar,
    p3: CoordScalar,
) -> sp.Expr:
    """Evaluate Euler's Four-Point planar Cayley-Menger relation `E(Q1, Q2, Q3, P1, P2, P3)` (Theorem 115).

    Vanishes for the six pairwise quadrances of ANY four coplanar points `A1, A2, A3, A4`,
    where `Q1=Q(A2,A3), Q2=Q(A1,A3), Q3=Q(A1,A2)` and `P1=Q(A1,A4), P2=Q(A2,A4), P3=Q(A3,A4)`.

    Args:
        q1: `Q(A2, A3)`.
        q2: `Q(A1, A3)`.
        q3: `Q(A1, A2)`.
        p1: `Q(A1, A4)`.
        p2: `Q(A2, A4)`.
        p3: `Q(A3, A4)`.

    Returns:
        Exact polynomial value (zero for any four coplanar points).
    """
    Q1, Q2, Q3 = _sympify_exact(q1), _sympify_exact(q2), _sympify_exact(q3)
    P1, P2, P3 = _sympify_exact(p1), _sympify_exact(p2), _sympify_exact(p3)
    expr = 2 * (
        4 * P1 * P2 * P3
        + (P2 + P1 - Q3) * (P2 + P3 - Q1) * (P1 + P3 - Q2)
        - P1 * (P2 + P3 - Q1) ** 2
        - P2 * (P1 + P3 - Q2) ** 2
        - P3 * (P2 + P1 - Q3) ** 2
    )
    return _clean_golden(expr)


def spread_polynomial(n: int, s: CoordScalar) -> sp.Expr:
    """Compute Wildberger's n-th Spread Polynomial `S_n(s)`.

    Defined over Z[s] by `S_0(s) = 0`, `S_1(s) = s`, and
    `S_n(s) = 2*(1 - 2*s)*S_{n-1}(s) - S_{n-2}(s) + 2*s`.

    Args:
        n: Non-negative degree index.
        s: Spread variable or exact value.

    Returns:
        Expanded exact polynomial expression `S_n(s)`.

    Raises:
        ValueError: If `n < 0`.
    """
    if n < 0:
        raise ValueError("Spread polynomial index n must be >= 0.")
    s_expr = _sympify_exact(s)
    if n == 0:
        return sp.Integer(0)
    if n == 1:
        return s_expr
    prev2: sp.Expr = sp.Integer(0)
    prev1: sp.Expr = s_expr
    for _ in range(2, n + 1):
        curr = sp.expand(2 * (1 - 2 * s_expr) * prev1 - prev2 + 2 * s_expr)
        prev2, prev1 = prev1, curr
    return _clean_golden(prev1)


def cross_polynomial(n: int, c: CoordScalar) -> sp.Expr:
    """Compute Wildberger's n-th Cross Polynomial `C_n(c) = 1 - S_n(1 - c)` (Section 8.7).

    Args:
        n: Non-negative degree index.
        c: Cross variable or exact value `c = 1 - s`.

    Returns:
        Expanded exact polynomial expression `C_n(c)`.
    """
    c_expr = _sympify_exact(c)
    return _clean_golden(sp.Integer(1) - spread_polynomial(n, sp.Integer(1) - c_expr))


def spread_sequence_mod_p(s_val: int, p: int, max_steps: int = 100) -> list[int]:
    """Compute the cyclic spread polynomial orbit `[S_0(s), S_1(s), ..., S_{k-1}(s)]` in `GF(p)`.

    Args:
        s_val: Initial spread residue in `GF(p)`.
        p: Odd prime modulus.
        max_steps: Upper bound on sequence length before stopping.

    Returns:
        Cyclic spread sequence `[0, s_1, s_2, ..., s_{n-1}]` up to first return to `0`.
    """
    s_sym = sp.Symbol("s")
    seq = [0]
    for k in range(1, max_steps + 1):
        val = int(spread_polynomial(k, s_sym).subs(s_sym, s_val)) % p
        if val == 0:
            break
        seq.append(val)
    return seq


@dataclass(frozen=True)
class TriangleInvariants:
    """Complete bundle of exact Rational Trigonometry invariants and centers of a triangle.

    Attributes:
        q1: Quadrance `Q(A2, A3)` opposite `A1`.
        q2: Quadrance `Q(A1, A3)` opposite `A2`.
        q3: Quadrance `Q(A1, A2)` opposite `A3`.
        s1: Spread at vertex `A1`.
        s2: Spread at vertex `A2`.
        s3: Spread at vertex `A3`.
        quadrea: Triangle quadrea `A(Q1, Q2, Q3)`.
        centroid: Universal centroid `G = (A1 + A2 + A3)/3` (`X(2)`).
        circumcenter: Metric circumcenter `C_M` (`X(3)` in Blue).
        circumquadrance: Metric circumquadrance `K_M = Q1*Q2*Q3 / A_M`.
        orthocenter: Metric orthocenter `O_M` (`X(4)` in Blue).
        nine_point_center: Metric nine-point center `N_M = (C_M + O_M)/2` (`X(5)` in Blue).
        nine_point_quadrance: Metric nine-point quadrance `K_9 = K_M / 4`.
    """

    q1: sp.Expr
    q2: sp.Expr
    q3: sp.Expr
    s1: sp.Expr
    s2: sp.Expr
    s3: sp.Expr
    quadrea: sp.Expr
    centroid: tuple[sp.Expr, sp.Expr]
    circumcenter: tuple[sp.Expr, sp.Expr]
    circumquadrance: sp.Expr
    orthocenter: tuple[sp.Expr, sp.Expr]
    nine_point_center: tuple[sp.Expr, sp.Expr]
    nine_point_quadrance: sp.Expr


def compute_triangle_invariants(
    p1: Point2DInput,
    p2: Point2DInput,
    p3: Point2DInput,
    metric: MetricForm = BLUE_METRIC,
) -> TriangleInvariants:
    """Compute exact quadrances, spreads, quadrea, and central points of `p1 p2 p3` under `metric`.

    Uses Wildberger's universal affine barycentric formulas (Theorems 84, 87, 116, 117),
    valid over any field (`char != 2, 3`) and any non-degenerate symmetric bilinear form!

    Args:
        p1: First vertex `A1 = [x1, y1]`.
        p2: Second vertex `A2 = [x2, y2]`.
        p3: Third vertex `A3 = [x3, y3]`.
        metric: Symmetric bilinear metric form (defaults to Blue Euclidean).

    Returns:
        Populated `TriangleInvariants` dataclass.
    """
    x1, y1 = to_vec2(p1)
    x2, y2 = to_vec2(p2)
    x3, y3 = to_vec2(p3)

    q1 = quadrance(p2, p3, metric=metric)
    q2 = quadrance(p1, p3, metric=metric)
    q3 = quadrance(p1, p2, metric=metric)

    s1 = (
        sp.nan
        if (q2 == 0 or q3 == 0)
        else vertex_spread(p1, p2, p3, metric=metric)
    )
    s2 = (
        sp.nan
        if (q1 == 0 or q3 == 0)
        else vertex_spread(p2, p3, p1, metric=metric)
    )
    s3 = (
        sp.nan
        if (q1 == 0 or q2 == 0)
        else vertex_spread(p3, p1, p2, metric=metric)
    )

    a_quad = metric.reduce_scalar(archimedes(q1, q2, q3))

    g1 = metric.reduce_scalar(q1 * (q2 + q3 - q1) / a_quad)
    g2 = metric.reduce_scalar(q2 * (q3 + q1 - q2) / a_quad)
    g3 = metric.reduce_scalar(q3 * (q1 + q2 - q3) / a_quad)

    b1 = metric.reduce_scalar((q3 + q1 - q2) * (q1 + q2 - q3) / a_quad)
    b2 = metric.reduce_scalar((q1 + q2 - q3) * (q2 + q3 - q1) / a_quad)
    b3 = metric.reduce_scalar((q2 + q3 - q1) * (q3 + q1 - q2) / a_quad)

    cx = metric.reduce_scalar(g1 * x1 + g2 * x2 + g3 * x3)
    cy = metric.reduce_scalar(g1 * y1 + g2 * y2 + g3 * y3)

    ox = metric.reduce_scalar(b1 * x1 + b2 * x2 + b3 * x3)
    oy = metric.reduce_scalar(b1 * y1 + b2 * y2 + b3 * y3)

    nx = metric.reduce_scalar((cx + ox) / 2)
    ny = metric.reduce_scalar((cy + oy) / 2)

    gx = metric.reduce_scalar((x1 + x2 + x3) / 3)
    gy = metric.reduce_scalar((y1 + y2 + y3) / 3)

    k_circ = metric.reduce_scalar(q1 * q2 * q3 / a_quad)
    k_nine = metric.reduce_scalar(k_circ / 4)

    return TriangleInvariants(
        q1=q1,
        q2=q2,
        q3=q3,
        s1=s1,
        s2=s2,
        s3=s3,
        quadrea=a_quad,
        centroid=(gx, gy),
        circumcenter=(cx, cy),
        circumquadrance=k_circ,
        orthocenter=(ox, oy),
        nine_point_center=(nx, ny),
        nine_point_quadrance=k_nine,
    )


def quadrance_3d(p1: Point3DInput, p2: Point3DInput) -> sp.Expr:
    """Compute exact 3D Euclidean quadrance `(x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2`.

    Args:
        p1: First 3D point.
        p2: Second 3D point.

    Returns:
        Exact 3D quadrance expression.
    """
    x1, y1, z1 = to_vec3(p1)
    x2, y2, z2 = to_vec3(p2)
    return _clean_golden((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def plane_normal(
    p1: Point3DInput, p2: Point3DInput, p3: Point3DInput
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Compute an exact normal vector `(p2 - p1) x (p3 - p1)` to plane `p1 p2 p3`.

    Args:
        p1: First point in plane.
        p2: Second point in plane.
        p3: Third point in plane.

    Returns:
        Exact 3D normal vector `(nx, ny, nz)`.
    """
    x1, y1, z1 = to_vec3(p1)
    x2, y2, z2 = to_vec3(p2)
    x3, y3, z3 = to_vec3(p3)
    u = sp.Matrix([x2 - x1, y2 - y1, z2 - z1])
    v = sp.Matrix([x3 - x1, y3 - y1, z3 - z1])
    n = u.cross(v)
    return (_clean_golden(n[0]), _clean_golden(n[1]), _clean_golden(n[2]))


def dihedral_spread(n1: Point3DInput, n2: Point3DInput) -> sp.Expr:
    """Compute the dihedral (face/wedge) spread `S = 1 - (n1 . n2)^2 / ((n1.n1)*(n2.n2))` between two planes.

    Args:
        n1: Normal vector to the first plane.
        n2: Normal vector to the second plane.

    Returns:
        Exact dihedral spread `S` in `[0, 1]`.
    """
    x1, y1, z1 = to_vec3(n1)
    x2, y2, z2 = to_vec3(n2)
    dot12 = x1 * x2 + y1 * y2 + z1 * z2
    q1 = x1**2 + y1**2 + z1**2
    q2 = x2**2 + y2**2 + z2**2
    return _clean_golden(sp.Integer(1) - dot12**2 / (q1 * q2))


def collinear_cross_ratio_quadrance(
    a: Point2DInput, b: Point2DInput, c: Point2DInput, d: Point2DInput
) -> sp.Expr:
    """Compute the squared projective cross-ratio `(A, B; C, D)^2 = Q(A,C)*Q(B,D) / (Q(A,D)*Q(B,C))`.

    Equals `1` whenever `(A, B; C, D) = -1` is a harmonic range (with `C != D`)!

    Args:
        a: First collinear point `A`.
        b: Second collinear point `B`.
        c: Third collinear point `C`.
        d: Fourth collinear point `D`.

    Returns:
        Exact quadrance cross-ratio `(A, B; C, D)^2`.
    """
    num = quadrance(a, c) * quadrance(b, d)
    den = quadrance(a, d) * quadrance(b, c)
    return _clean_golden(num / den)


def pencil_cross_ratio_spread(
    origin: Point2DInput,
    a: Point2DInput,
    b: Point2DInput,
    c: Point2DInput,
    d: Point2DInput,
) -> sp.Expr:
    """Compute the projective spread cross-ratio of four concurrent rays through `origin`.

    `CR_s(OA, OB; OC, OD) = (s(OA, OC) * s(OB, OD)) / (s(OA, OD) * s(OB, OC))`.
    Equals `collinear_cross_ratio_quadrance(A, B, C, D)` for any transversal cutting
    the four rays at `A, B, C, D`!

    Args:
        origin: Pencil vertex `O`.
        a: Point on first ray `OA`.
        b: Point on second ray `OB`.
        c: Point on third ray `OC`.
        d: Point on fourth ray `OD`.

    Returns:
        Exact spread cross-ratio invariant.
    """
    la = LineProportion.from_points(origin, a)
    lb = LineProportion.from_points(origin, b)
    lc = LineProportion.from_points(origin, c)
    ld = LineProportion.from_points(origin, d)
    num = spread(la, lc) * spread(lb, ld)
    den = spread(la, ld) * spread(lb, lc)
    return _clean_golden(num / den)


def rational_polar_coords(x: CoordScalar, y: CoordScalar) -> tuple[sp.Expr, sp.Expr]:
    """Convert Cartesian `[x, y]` to Wildberger's rational polar coordinates `[s, Q]`.

    Uses `s = x^2 / (x^2 + y^2)` (polar spread to the y-axis) and `Q = x^2 + y^2`
    (Section 27.1).

    Args:
        x: Cartesian x-coordinate.
        y: Cartesian y-coordinate.

    Returns:
        Tuple `(s, Q)` of exact polar spread and quadrance.
    """
    ex = _sympify_exact(x)
    ey = _sympify_exact(y)
    q_val = _clean_golden(ex**2 + ey**2)
    s_val = _clean_golden(ex**2 / q_val)
    return s_val, q_val
