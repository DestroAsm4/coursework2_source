import pytest
from run import app

# creating fixture for all tests
@pytest.fixture()
def test_client():
    return app.test_client()