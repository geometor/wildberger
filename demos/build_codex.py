"""Verify all SymPy proofs and build the 28-Principle GEOMETOR Wildberger Codex."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from geometor.wildberger.__main__ import main  # noqa: E402

if __name__ == "__main__":
    rc_verify = main(["verify"])
    if rc_verify != 0:
        raise SystemExit(rc_verify)
    raise SystemExit(main(["build", "--root", str(_REPO_ROOT)]))
