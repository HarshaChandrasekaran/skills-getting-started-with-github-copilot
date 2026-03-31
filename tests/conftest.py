import pytest
import copy
from fastapi.testclient import TestClient
from src.app import app, activities

# Store the original activities for reset between tests
ORIGINAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture
def client():
    """Provides a TestClient instance for testing"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Resets activities to original state before each test"""
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
