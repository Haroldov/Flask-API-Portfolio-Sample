import pytest

from main import app

@pytest.fixture(scope="class")
def client(request):
    app.config['TESTING'] = True

    with app.test_client() as client:
        request.cls.client = client
