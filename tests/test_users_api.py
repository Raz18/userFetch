import pytest
import requests


#basic user fetching test
def test_users_fetching(user_fetcher):
    """testing the user fetching"""
    users = user_fetcher.fetch_users()
    assert len(users) > 0, "No users fetched"


#test with multiple email inputs, not from the api
@pytest.mark.parametrize('email', [
    ('test@example.com', True), ('testexample.com', False), ('test@examplecom', False), ('testexamplecom', False),
    ('test', False), ('', False), ('@', False), ('@example.com', False), ('test@', False), ('test@example', False)])

def test_check_valid_email(user_fetcher, email):
    """testing the email validation logic with multiple email inputs"""
    parsed_user = user_fetcher.check_valid_email(email[0])
    assert parsed_user == email[1], f"Email: {email[0]}, Expected: {email[1]}, Actual: {parsed_user}"


#test with parsed api input
def test_valid_users_parsing(user_fetcher):
    """testing the user parsing, including error logging"""
    users = user_fetcher.fetch_users()
    valid_users = user_fetcher.extract_and_parse_user_info()
    for user in valid_users:
        assert user in users, f"User {user} not in fetched users"
        assert user.get('email') is not None, f"User {user} has no email"
        assert user.get('company', {}).get('name') is not None, f"User {user} has no company name"
        assert user_fetcher.check_valid_email(user.get('email')), f"User {user} has invalid email"


def test_api_failure(user_fetcher, requests_mock):
    """Testing API failure (HTTP 500) raises HTTPError."""
    requests_mock.get(user_fetcher.url, status_code=500)
    with pytest.raises(requests.exceptions.HTTPError):
        user_fetcher.fetch_users()


def test_network_issue(user_fetcher, requests_mock):
    """Testing network issue raises ConnectionError."""
    requests_mock.get(user_fetcher.url, exc=requests.exceptions.ConnectionError)
    with pytest.raises(requests.exceptions.ConnectionError):
        user_fetcher.fetch_users()


def test_malformed_response(user_fetcher, requests_mock):
    """Testing malformed response raises JSONDecodeError."""
    requests_mock.get(user_fetcher.url, text='not a json')
    with pytest.raises(requests.exceptions.JSONDecodeError):
        user_fetcher.fetch_users()
