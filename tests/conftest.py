import pytest
import os
import sys
import pytest
from api_user_fetcher import UserFetcher

# Add the parent directory of the tests directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="module")
def user_fetcher():
    test_url = "https://jsonplaceholder.typicode.com/users"
    yield UserFetcher(test_url)

