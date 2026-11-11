"""Codex generator for the 28 Rational Trigonometry Principle Dossiers (`w-01`..`w-28`).

Generates standalone executable `model.py` scripts, interactive `w-NN.svg`
diagrams, Sphinx `index.rst` and `code.rst` dossiers, the master
`docsrc/topics/index.rst` book collection, and the scholarly apparatus files.
"""

from __future__ import annotations

from pathlib import Path

from geometor.wildberger.apparatus import write_apparatus_files
from geometor.wildberger.catalog import (
    PrincipleSpec,
    get_all_principles,
    get_dependents,
    get_principle_by_code,
)
from geometor.wildberger.models import TopicBuildResult, build_principle_model
from geometor.wildberger.render import render_svg


def _escape_dot_label(text: str) -> str:
    """Escape double quotes and wrap long titles cleanly for Graphviz node labels.

    Args:
        text: Raw node title.

    Returns:
        Escaped short label string.
    """
    short = text if len(text) <= 34 else text[:31].rstrip() + "..."
    return short.replace('"', "'")


def _render_dependency_dot(spec: PrincipleSpec) -> list[str]:
    """Generate `.. graphviz::` RST lines for a principle's upstream/downstream DAG.

    Args:
        spec: Current `PrincipleSpec`.

    Returns:
        List of RST lines including the `.. graphviz::` directive and text links.
    """
    upstream = [get_principle_by_code(c) for c in spec.depends_on]
    downstream = get_dependents(spec.code)

    lines = [
        "Constructive Dependency Graph",
        "-----------------------------",
        "",
        ".. graphviz::",
        "",
        "   digraph dependency {",
        "       rankdir=TB;",
        '       bgcolor="transparent";',
        '       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];',
        '       edge [color="#888888", arrowsize=0.7];',
    ]

    for up in upstream:
        lbl = _escape_dot_label(up.title)
        lines.append(
            f'       "{up.code}" [label="{up.code}\\n{lbl}", fillcolor="#d8dee9", '
            f'color="#4c566a", URL="../{up.slug}/index.html"];'
        )

    cur_lbl = _escape_dot_label(spec.title)
    lines.append(
        f'       "{spec.code}" [label="{spec.code}\\n{cur_lbl}", fillcolor="#ffff99", '
        f'color="#d4a017", penwidth=2.0, URL="../{spec.slug}/index.html"];'
    )

    for down in downstream:
        lbl = _escape_dot_label(down.title)
        lines.append(
            f'       "{down.code}" [label="{down.code}\\n{lbl}", fillcolor="#e5e9f0", '
            f'color="#777777", URL="../{down.slug}/index.html"];'
        )

    for up in upstream:
        lines.append(f'       "{up.code}" -> "{spec.code}";')
    for down in downstream:
        lines.append(f'       "{spec.code}" -> "{down.code}";')

    lines.extend(["   }", ""])

    if upstream:
        up_refs = ", ".join(f":ref:`{u.code} {u.title} <{u.slug}>`" for u in upstream)
        lines.append(f"**Depends on**: {up_refs}")
        lines.append("")
    if downstream:
        down_refs = ", ".join(f":ref:`{d.code} {d.title} <{d.slug}>`" for d in downstream)
        lines.append(f"**Required for**: {down_refs}")
        lines.append("")

    return lines


def _render_model_py(spec: PrincipleSpec) -> str:
    """Generate the standalone runnable `model.py` script for `spec`.

    Args:
        spec: Target `PrincipleSpec`.

    Returns:
        Complete Python source code formatted to pass `ruff check` (`ANN`, `D`).
    """
    fn_name = f"construct_{spec.slug.replace('-', '_')}"
    enunc_clean = spec.enunciation.replace('"', "'")
    lines = [
        f'"""GEOMETOR Wildberger symbolic model and proof script for {spec.code}: {spec.title}.',
        "",
        f"Enunciation: {enunc_clean}",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "import sys",
        "from pathlib import Path",
        "",
        "_ROOT_SRC = Path(__file__).resolve().parents[3] / \"src\"",
        "if str(_ROOT_SRC) not in sys.path:",
        "    sys.path.insert(0, str(_ROOT_SRC))",
        "",
        "from geometor.wildberger.models import (  # noqa: E402",
        "    TopicBuildResult,",
        "    assert_zero_floats,",
        "    build_principle_model,",
        ")",
        "from geometor.wildberger.render import render_svg  # noqa: E402",
        "",
        "",
        f"def {fn_name}() -> TopicBuildResult:",
        f'    """Construct the exact symbolic model and verifications for {spec.code}.',
        "",
        "    Returns:",
        f"        Populated `TopicBuildResult` for {spec.code} ({spec.title}).",
        '    """',
        f'    result = build_principle_model("{spec.code}")',
        "    assert_zero_floats(result.model)",
        "    return result",
        "",
        "",
        "def main() -> None:",
        f'    """Execute {spec.code} symbolic construction, render `{spec.slug}.svg`, and print invariants."""',
        "    here = Path(__file__).resolve().parent",
        f"    bundle = {fn_name}()",
        "    svg_out = render_svg(",
        "        bundle.model,",
        f'        here / "{spec.slug}.svg",',
        "        extra_curves=bundle.extra_curves,",
        "        annotations=bundle.annotations,",
        "    )",
        f'    print("{spec.code}: {spec.title}")',
        '    print(f"  Elements in model: {len(bundle.model)}")',
        '    print(f"  Rendered SVG:      {svg_out.name}")',
        "    for label, val, status in bundle.verifications:",
        '        print(f"  [OK] {label}: {val} ({status})")',
        "",
        "",
        'if __name__ == "__main__":',
        "    main()",
        "",
    ]
    return "\n".join(lines)


def _render_topic_index_rst(spec: PrincipleSpec, bundle: TopicBuildResult) -> str:
    """Generate `docsrc/topics/w-NN/index.rst` for `spec`.

    Args:
        spec: Principle specification.
        bundle: Evaluated `TopicBuildResult` containing live `SymPy` verifications.

    Returns:
        Complete RST text for `index.rst`.
    """
    heading = f"{spec.code} {spec.title}"
    bar = "=" * len(heading)
    tags_str = ", ".join(spec.tags)

    lines: list[str] = [
        f":order: {spec.num}",
        ":type: topic",
        f":category: {spec.category}",
        f":tags: {tags_str}",
        "",
        f".. _{spec.slug}:",
        "",
        bar,
        heading,
        bar,
        "",
        f"*{spec.subtitle}*",
        "",
        ".. enunciation::",
        "",
        f"   {spec.enunciation}",
        "",
        f".. figure:: {spec.slug}.svg",
        "   :align: center",
        "   :width: 100%",
        "",
        f"   Interactive GEOMETOR construction for **{spec.code} ({spec.title})**. "
        "Hover any geometric label in the text or figure to highlight the corresponding element.",
        "",
        ".. signature::",
        "",
    ]
    for g in spec.signature_given:
        lines.append(f"   {g}")
    lines.append("   =====")
    for s in spec.signature_steps:
        lines.append(f"   {s}")

    lines.extend(["", "Mathematical Synthesis", "----------------------", ""])
    for para in spec.synthesis:
        lines.append(para)
        lines.append("")

    lines.extend(["Key Algebraic Identities", "------------------------", ""])
    for mb in spec.math_blocks:
        lines.extend([".. math::", "", f"   {mb}", ""])

    lines.extend(
        [
            "Symbolic ``SymPy`` Verification",
            "-------------------------------",
            "",
            ".. list-table::",
            "   :widths: 36 36 28",
            "   :header-rows: 1",
            "",
            "   * - Invariant / Theorem Check",
            "     - Exact ``SymPy`` Value",
            "     - Verification Status",
        ]
    )
    for label, val, status in bundle.verifications:
        lines.extend(
            [
                f"   * - ``{label}``",
                f"     - ``{val}``",
                f"     - {status}",
            ]
        )
    lines.append("")

    lines.extend(
        [
            "Cross-Repository Canon",
            "----------------------",
            "",
            ".. list-table::",
            "   :widths: 28 72",
            "",
            "   * - **Executable Demonstration**",
            f"     - :doc:`code` (Standalone ``model.py`` & ``{spec.slug}.svg``)",
            "   * - **Thematic Part**",
            f"     - {spec.part}",
        ]
    )
    for c_label, c_val in spec.canon_links:
        lines.extend([f"   * - **{c_label}**", f"     - {c_val}"])
    lines.append("")

    lines.extend(_render_dependency_dot(spec))

    lines.extend(
        [
            ".. toctree::",
            "   :hidden:",
            "",
            "   code",
            "",
        ]
    )
    return "\n".join(lines)


def _render_topic_code_rst(spec: PrincipleSpec) -> str:
    """Generate `docsrc/topics/w-NN/code.rst` for `spec`.

    Args:
        spec: Principle specification.

    Returns:
        Complete RST text for `code.rst`.
    """
    heading = f"{spec.code} {spec.title} — Code"
    bar = "=" * len(heading)
    lines = [
        bar,
        heading,
        bar,
        "",
        ".. enunciation::",
        "",
        f"   {spec.enunciation}",
        "",
        f".. figure:: {spec.slug}.svg",
        "   :align: center",
        "   :width: 88%",
        "",
        f"   Exact ``geometor.model`` SVG output of ``model.py`` for **{spec.code} ({spec.title})**.",
        "",
        "Symbolic Construction & Verification Script (``model.py``)",
        "----------------------------------------------------------",
        "",
        ".. literalinclude:: model.py",
        "   :language: python",
        "",
    ]
    return "\n".join(lines)


def _render_master_topics_index(principles: tuple[PrincipleSpec, ...]) -> str:
    """Generate `docsrc/topics/index.rst` book collection and master table.

    Args:
        principles: All 28 `PrincipleSpec` entries.

    Returns:
        Complete RST text for `docsrc/topics/index.rst`.
    """
    lines = [
        ":layout: book",
        ":navigation: header",
        ":order: 10",
        "",
        ".. _topics:",
        "",
        "==========",
        "Principles",
        "==========",
        "",
        "The **GEOMETOR Wildberger Codex** gathers **28 foundational principles**",
        "(:math:`\\text{W.01}` through :math:`\\text{W.28}`) of **Rational Trigonometry** and",
        "**Universal Geometry** (:cite:`Wildberger2005`, :cite:`Wildberger2008`), demonstrating",
        "each theorem through **100% exact** ``SymPy`` symbolic proofs, runnable",
        "``geometor.model`` constructions, and interactive SVG diagrams.",
        "",
        "- **Part I (W.01 – W.05)**: Planar proportions, reflections, quadrance, spread, and spread polynomials :math:`S_n(s)` (including Pentagonal Golden Spreads).",
        "- **Part II (W.06 – W.11)**: The Five Fundamental Laws (Pythagoras, Triple Quad, Spread Law, Cross Law, Triple Spread) and Kepler's Golden Right Triangle.",
        "- **Part III (W.12 – W.23)**: Triangle centers, Euler line & Nine-Point Circle over :math:`\\mathbb{Q}` and :math:`\\mathbb{F}_p`, circles, cyclic quadrilaterals, golden pentagons, metrical conics, Taylor tangents, projective cross-ratio, and **Chromogeometry** (Blue, Red, Green metrics).",
        "- **Part IV (W.24 – W.28)**: Polynomial triangle solvers, Snellius–Pothenot resection, Hansen's surveying benchmark, algebraic physics, exact rational dihedral spreads of all five Platonic solids, rational polar curves, and the **Ellipson**.",
        "",
        ".. collection::",
        "   :type: topic",
        "   :sort: order",
        "",
        "Master Index of Principles (W.01 – W.28)",
        "----------------------------------------",
        "",
        ".. list-table::",
        "   :widths: 9 34 26 31",
        "   :header-rows: 1",
        "",
        "   * - Code",
        "     - Principle",
        "     - Category",
        "     - Thematic Division",
    ]
    for spec in principles:
        lines.extend(
            [
                f"   * - :ref:`{spec.code} <{spec.slug}>`",
                f"     - :ref:`{spec.title} <{spec.slug}>`",
                f"     - {spec.category}",
                f"     - {spec.part}",
            ]
        )
    lines.append("")
    return "\n".join(lines)


def build_codex(repo_root: Path) -> list[Path]:
    """Generate all 28 topic dossiers, SVGs, `model.py` scripts, and apparatus RSTs.

    Args:
        repo_root: Repository root (`/home/phi/PROJECTS/geometor/wildberger`).

    Returns:
        List of all generated file paths.
    """
    docsrc_dir = repo_root / "docsrc"
    topics_dir = docsrc_dir / "topics"
    topics_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    written.extend(write_apparatus_files(docsrc_dir))

    principles = get_all_principles()
    for spec in principles:
        t_dir = topics_dir / spec.slug
        t_dir.mkdir(parents=True, exist_ok=True)

        bundle = build_principle_model(spec.code)
        svg_path = render_svg(
            bundle.model,
            t_dir / f"{spec.slug}.svg",
            extra_curves=bundle.extra_curves,
            annotations=bundle.annotations,
        )
        written.append(svg_path)

        model_py_path = t_dir / "model.py"
        model_py_path.write_text(_render_model_py(spec), encoding="utf-8")
        written.append(model_py_path)

        index_rst_path = t_dir / "index.rst"
        index_rst_path.write_text(_render_topic_index_rst(spec, bundle), encoding="utf-8")
        written.append(index_rst_path)

        code_rst_path = t_dir / "code.rst"
        code_rst_path.write_text(_render_topic_code_rst(spec), encoding="utf-8")
        written.append(code_rst_path)

    master_index = topics_dir / "index.rst"
    master_index.write_text(_render_master_topics_index(principles), encoding="utf-8")
    written.append(master_index)

    return written
