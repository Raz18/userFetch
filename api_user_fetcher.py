import requests
from userFetch.utils.logger import setup_logger


class UserFetcher:
    def __init__(self, url):
        self.url = url
        self.users = []
        self.logger = setup_logger(self.__class__.__name__)

    def fetch_users(self):
        """fetch users from the given URL"""

        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            self.users = response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching data from {self.url}: {e}")
            self.users = []
            raise
        return self.users

    def check_valid_email(self, email):
        """
        Check if the email is valid, must contain '@' and a domain after it.
        """
        if not email or "@" not in email:
            return False
        username, domain = email.split("@", 1)
        if '.' in domain and len(domain) > 2 and len(username) > 0:
            self.logger.info(f"Valid email: {email}")
            return True

        self.logger.error(f"Invalid email: {email}")
        return False

    def extract_and_parse_user_info(self):
        """Extract and parse user info"""
        valid_users = []
        for user in self.users:
            if self.check_valid_email(user.get('email', '')):
                self.logger.info(
                    f"\nUser ID: {user.get('id')}\n"
                    f"Name: {user.get('name')}\n"
                    f"Email: {user.get('email')}\n"
                    f"Company: {user.get('company', {}).get('name', 'N/A')}\n"
                )
                valid_users.append(user)
            else:
                self.logger.error(f"Invalid email for user ID {user.get('id', 'N/A')}: {user.get('email', 'N/A')}\n")
        return valid_users


# support for direct execution from command line

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    user_fetcher = UserFetcher(url)
    user_fetcher.fetch_users()
    user_fetcher.extract_and_parse_user_info()
