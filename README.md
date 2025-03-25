# UserFetcher Project

## Overview

The `UserFetcher` project is a Python application designed to fetch user data from a given URL, validate email addresses, and log user information. The project includes comprehensive tests to ensure the functionality and robustness of the application.

## Functionality

The main functionality of the `UserFetcher` class includes:
- Fetching User Data: Retrieve users from a specified URL.
- Validating Emails: Ensure that each email contains a valid format (i.e., a non-empty username, an '@' symbol, and a domain with at least one dot).
- Extracting and Logging User Information: Log valid user details and report errors for invalid emails.

## Script Explanation

### Output

When you run the script `api_task_cyclops.py`, it will:

-Fetch user data from the specified URL.

-Validate the email addresses of the fetched users.

-Log the details of users with valid emails and report errors for users with invalid emails.

### Implementation

The UserFetcher class is implemented in `api_task_cyclops.py` and includes the following methods:

`__init__(self, url)`: Initializes the UserFetcher instance with the given URL and sets up an empty list for users and a logger.

`fetch_users(self)`: Fetches user data from the URL. If the request is successful, it parses the JSON response and stores it in the users attribute. If an error occurs (e.g., network issue, API failure, malformed response), it logs the error and raises the exception.

`check_valid_email(self, email)`: Validates the email format. Returns True if the email is valid, otherwise False.

`extract_and_parse_user_info(self)`: Iterates through the fetched users, validates their emails, logs the details of valid users, and reports errors for invalid emails.

### Example Output

When running the script, you might see logs similar to the following:
```sh
INFO:UserFetcher:User ID: 1\
Name: Leanne Graham\
Email: Sincere@april.biz\
Company Name: Romaguera-Crona

--for--invalid--input:
ERROR:UserFetcher:Invalid email for user ID 2: invalid-email
```
This output indicates that the script successfully fetched and processed user data, logging valid user details and reporting errors for invalid emails.

## Project Structure
```sh
UserFetcher Project
├── api_task_cyclops.py         # Main script implemented by the UserFetcher class
├── tests
│   ├── conftest.py             # Pytest fixtures for a centralized setup
│   └── test_users_api.py       # Test cases for UserFetcher
├── utils
│   └── logger.py               # Logger setup utility
├── requirements.txt            # Required packages
└── README.md                   # Project documentation file
```

## Usage
1. **Clone the Repository**
```bash
git clone https://github.com/Raz18/wolt_automation.git 
cd userFetch
```
2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate
```
3. **Install the required packages:**

```sh
pip install -r requirements.txt
```
4. **Run the script directly**:
```sh
python api_task_cyclops.py
```
5. **Run the tests:**
```sh
pytest tests
```

## Tests Explanation

The tests are located in the `tests` directory and cover various aspects of the `UserFetcher` class:

- **Basic User Fetching Test:**
  - Ensures that users are fetched successfully from the API.

- **Email Validation Test:**
  - Tests the email validation logic with multiple email inputs.

- **User Parsing Test:**
  - Tests the parsing of user information, including error logging for invalid emails.

- **API Failure Test:**
  - Simulates an API failure (HTTP 500) and ensures that an `HTTPError` is raised.

- **Network Issue Test:**
  - Simulates a network issue and ensures that a `ConnectionError` is raised.

- **Malformed Response Test:**
  - Simulates a malformed response and ensures that a `JSONDecodeError` is raised.


## Additional Information

### Logging
The project uses a custom logger configured in `utils/logger.py` to log both informational and error messages.

### Error Handling
Robust error handling is implemented to catch and log exceptions such as API failures, network issues, and malformed JSON responses.

### Testing
The project uses `pytest` for unit testing. The tests simulate various conditions to ensure the reliability of the fetching, parsing, and validation processes.

### Extensibility
The project structure is designed for easy modifications and future enhancements, such as extending email validation rules or adding additional user fields.
