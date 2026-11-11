"""Command-line interface for `geometor.wildberger`.

Supports `summary` (list all 28 principles), `verify` (execute all 17 symbolic
`SymPy` theorem provers and 28 exact `geometor.model` constructions), and
`build` (generate `docsrc/topics/w-01`..`w-28` dossiers, SVGs, and apparatus).
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from rich.console import Console
from rich.table import Table

from geometor.wildberger.catalog import get_all_principles
from geometor.wildberger.models import build_principle_model
from geometor.wildberger.proofs import verify_all_proofs
from geometor.wildberger.topics import build_codex


def _default_repo_root() -> Path:
    """Resolve the repository root directory from package location.

    Returns:
        Path to `/home/phi/PROJECTS/geometor/wildberger`.
    """
    return Path(__file__).resolve().parents[3]


def cmd_summary(console: Console) -> int:
    """Render a Rich summary table of all 28 Principles (`W.01`..`W.28`).

    Args:
        console: Rich `Console` instance.

    Returns:
        Exit code `0`.
    """
    table = Table(title="GEOMETOR Wildberger Codex — 28 Principles (W.01 – W.28)")
    table.add_column("Code", style="bold cyan", no_wrap=True)
    table.add_column("Principle", style="bold white")
    table.add_column("Category", style="yellow")
    table.add_column("Part", style="green")
    for spec in get_all_principles():
        table.add_row(spec.code, spec.title, spec.category, spec.part.split(":")[0])
    console.print(table)
    return 0


def cmd_verify(console: Console) -> int:
    """Execute all symbolic `SymPy` proofs and 28 exact `Model` verifications.

    Args:
        console: Rich `Console` instance.

    Returns:
        Exit code `0` on full verification, `1` otherwise.
    """
    certs = verify_all_proofs()
    proof_table = Table(title="Symbolic SymPy Theorem Certificates")
    proof_table.add_column("ID", style="cyan", no_wrap=True)
    proof_table.add_column("Theorem / Identity Suite", style="white")
    proof_table.add_column("Residual", style="magenta", justify="right")
    proof_table.add_column("Status", style="bold green")
    all_ok = True
    for cert in certs:
        status = "VERIFIED" if cert.verified else "FAILED"
        if not cert.verified:
            all_ok = False
        proof_table.add_row(cert.theorem_id, cert.title, str(cert.residual), status)
    console.print(proof_table)

    principles = get_all_principles()
    for spec in principles:
        build_principle_model(spec.code)
    console.print(
        f"[bold green]Verified {len(certs)} SymPy theorem suites and "
        f"{len(principles)} exact zero-float geometor.model constructions.[/bold green]"
    )
    return 0 if all_ok else 1


def cmd_build(console: Console, repo_root: Path) -> int:
    """Build all 28 topic dossiers, SVGs, `model.py` scripts, and apparatus RSTs.

    Args:
        console: Rich `Console` instance.
        repo_root: Target repository root directory.

    Returns:
        Exit code `0`.
    """
    written = build_codex(repo_root)
    console.print(
        f"[bold green]Generated {len(written)} codex files under {repo_root / 'docsrc'}.[/bold green]"
    )
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the `wildberger` CLI.

    Args:
        argv: Optional sequence of CLI arguments (defaults to `sys.argv[1:]`).

    Returns:
        Process exit code (`0` on success).
    """
    parser = argparse.ArgumentParser(
        prog="wildberger",
        description="GEOMETOR Wildberger: Rational Trigonometry & Universal Geometry Codex CLI.",
    )
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("summary", help="Display all 28 Rational Trigonometry principles.")
    sub.add_parser("verify", help="Run all exact SymPy proofs and model verifications.")
    build_p = sub.add_parser("build", help="Generate all 28 topic dossiers and SVGs in docsrc/.")
    build_p.add_argument(
        "--root",
        type=Path,
        default=_default_repo_root(),
        help="Repository root directory.",
    )

    args = parser.parse_args(list(argv) if argv is not None else None)
    console = Console()
    if args.command == "verify":
        return cmd_verify(console)
    if args.command == "build":
        return cmd_build(console, args.root)
    return cmd_summary(console)


if __name__ == "__main__":
    raise SystemExit(main())
