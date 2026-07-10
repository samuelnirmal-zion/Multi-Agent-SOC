import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agents.coordinator import coordinator


def test_coordinator_returns_string_for_basic_message():
    result = coordinator("Suspicious login from an unknown IP")
    assert isinstance(result, str)
    assert len(result) > 0
