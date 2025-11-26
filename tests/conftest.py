from __future__ import annotations

"""
Pytest configuration for Smart Shovel project.

Purpose:
- ensure that the project root is on sys.path
  so that `import src...` works in CI and local runs.
"""

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
