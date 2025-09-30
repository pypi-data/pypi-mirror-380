#!/usr/bin/env python3
"""
ASTODOJO Autopilot Test Runner

Simple wrapper to run the comprehensive autopilot test suite.
"""

import sys
import os
from pathlib import Path

def main():
    """Run the autopilot test suite."""
    # Add the test directory to Python path
    test_dir = Path(__file__).parent
    sys.path.insert(0, str(test_dir))

    # Import and run the autopilot test
    try:
        from suites.autopilot_test import main as run_autopilot
        run_autopilot()
    except ImportError as e:
        print(f"❌ Failed to import autopilot test: {e}")
        print("Make sure you're running from the test directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
