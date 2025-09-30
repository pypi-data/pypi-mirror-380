#!/usr/bin/env python3
"""
OpRouter CLI entry point for 'python -m oprouter' command.
"""

import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from oprouter.ui.cli import main

if __name__ == "__main__":
    main()
