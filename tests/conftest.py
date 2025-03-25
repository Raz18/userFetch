import pytest
from ..api_user_fetcher import UserFetcher


@pytest.fixture(scope="module")
def user_fetcher():
    test_url = "https://jsonplaceholder.typicode.com/users"
    yield UserFetcher(test_url)

