"""Make packages importable when running pytest from the repo root."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for pkg in ("packages/theory-sim", "packages/sensor"):
    sys.path.insert(0, os.path.join(ROOT, pkg))
