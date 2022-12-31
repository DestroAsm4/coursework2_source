import pytest
from run import app
#
#
# # создаем фикстуру для тестирования всех вьюшек (main, candidates, vacancies) app.test_client()
@pytest.fixture()
def test_client():
    return app.test_client()