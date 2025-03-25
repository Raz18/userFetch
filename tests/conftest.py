import os
import sys

import pytest

from .. import api_user_fetcher

# Add the directory containing api_user_fetcher.py to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ..api_user_fetcher
/api_user_fetcher import UserFetcher


@pytest.fixture(scope="module")
def user_fetcher():
    test_url = "https://jsonplaceholder.typicode.com/users"
    yield UserFetcher(test_url)

