"""Master catalog of the 28 Rational Trigonometry & Universal Geometry Principles.

Organizes the mathematical principles of Rational Trigonometry and Universal
Geometry into four parts (`W.01` through `W.28`), with constructive signatures,
original GEOMETOR synthesis prose, exact LaTeX identities, cross-repository
canon mappings, and constructive dependency DAG links.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PrincipleSpec:
    """Specification of a single Principle Dossier (`W.01`..`W.28`).

    Attributes:
        num: Integer order `1..28`.
        code: Canonical identifier `'W.01'`..`'W.28'`.
        slug: Directory slug `'w-01'`..`'w-28'`.
        part: Four-part thematic division name.
        category: Sub-domain category label.
        tags: Tuple of index tags.
        title: Principle title.
        subtitle: Concise descriptive subtitle.
        enunciation: Formal mathematical statement for `.. enunciation::`.
        signature_given: Tuple of `given` declarations for `.. signature::`.
        signature_steps: Tuple of constructive/algebraic steps for `.. signature::`.
        synthesis: Tuple of original GEOMETOR synthesis paragraphs (RST).
        math_blocks: Tuple of LaTeX display math strings for `.. math::`.
        canon_links: Tuple of `(label, rst_value)` cross-repository canon rows.
        depends_on: Tuple of upstream `'W.NN'` codes in the dependency DAG.
    """

    num: int
    code: str
    slug: str
    part: str
    category: str
    tags: tuple[str, ...]
    title: str
    subtitle: str
    enunciation: str
    signature_given: tuple[str, ...]
    signature_steps: tuple[str, ...]
    synthesis: tuple[str, ...]
    math_blocks: tuple[str, ...]
    canon_links: tuple[tuple[str, str], ...]
    depends_on: tuple[str, ...]


def get_all_principles() -> tuple[PrincipleSpec, ...]:
    """Return all 28 `PrincipleSpec` entries ordered from `W.01` to `W.28`.

    Returns:
        Tuple of 28 `PrincipleSpec` objects.
    """
    from geometor.wildberger.catalog_a import PRINCIPLES_A
    from geometor.wildberger.catalog_b import PRINCIPLES_B

    return PRINCIPLES_A + PRINCIPLES_B


def get_principle_by_code(code: str) -> PrincipleSpec:
    """Look up a `PrincipleSpec` by canonical code (`'W.01'`) or slug (`'w-01'`).

    Args:
        code: Canonical code or directory slug.

    Returns:
        Matching `PrincipleSpec`.

    Raises:
        KeyError: If no principle matches `code`.
    """
    norm = code.strip().upper()
    slug_norm = code.strip().lower()
    for spec in get_all_principles():
        if spec.code.upper() == norm or spec.slug == slug_norm:
            return spec
    raise KeyError(f"Unknown Wildberger principle identifier: {code!r}")


def get_dependents(code: str) -> list[PrincipleSpec]:
    """Return all downstream principles that directly depend on `code`.

    Args:
        code: Upstream canonical code `'W.NN'`.

    Returns:
        Ordered list of downstream `PrincipleSpec` items.
    """
    target = code.strip().upper()
    return [
        spec
        for spec in get_all_principles()
        if any(dep.upper() == target for dep in spec.depends_on)
    ]
