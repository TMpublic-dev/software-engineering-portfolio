"""
Basic tests for TaskFlow constants.
"""

from app.models import VALID_PRIORITIES, VALID_STATUSES


def test_priority_values_exist():
    assert "Low" in VALID_PRIORITIES
    assert "Medium" in VALID_PRIORITIES
    assert "High" in VALID_PRIORITIES
    assert "Urgent" in VALID_PRIORITIES


def test_status_values_exist():
    assert "To Do" in VALID_STATUSES
    assert "In Progress" in VALID_STATUSES
    assert "Completed" in VALID_STATUSES
