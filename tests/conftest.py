"""
Demo slowdown: set TEST_DEMO_SLOWDOWN (seconds) so the full suite runs long enough
to showcase Smarter Testing impact (e.g. 30+ min full run vs only impacted tests).

Example: TEST_DEMO_SLOWDOWN=120 pytest   → ~30 min for 15 test files (2 min per file)
Default: 0 (no delay).
"""
import os
import time

import pytest


@pytest.fixture(scope="module", autouse=True)
def _demo_slowdown():
    """Sleep once per test module when TEST_DEMO_SLOWDOWN is set (for long-running demo)."""
    sec = int(os.environ.get("TEST_DEMO_SLOWDOWN", "0"))
    if sec > 0:
        time.sleep(sec)
