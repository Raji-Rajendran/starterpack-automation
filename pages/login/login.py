import os

from dotenv import load_dotenv

from configs.config import Config
from utils.helper_functions import HelperFunctions


# Function to load environment variables and get credentials
def get_credentials():
    load_dotenv()  # Load environment variables from .env file
    credentials = {
        'email': os.getenv('EMAIL'),
        'password': os.getenv('PASSWORD'),
        'otp': os.getenv('OTP'),
        'invalid_email': os.getenv('INVALID_EMAIL'),
        'invalid_password': os.getenv('INVALID_PASSWORD'),
        'inactive_email': os.getenv('INACTIVE_EMAIL'),
        'inactive_password': os.getenv('INACTIVE_PASSWORD')
    }
    return credentials


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.helper = HelperFunctions(self.driver)  # Create an instance of the Helper class
        self.credentials = get_credentials()  # Fetch credentials once during initialization

    # Function to open the base URL
    def open(self):
        self.driver.get(Config.base_url + "admin/login")

    # Function to get the title of the current page
    def get_title(self):
        return self.driver.title

    # Function to find an element using its locator
    def find_element(self, locator):
        return self.helper.wait_for_element_visible(self.driver, locator)

    # Function to input email into the email field
    def input_email(self, locator):
        email = self.credentials['email']
        self.helper.wait_and_input_text(locator, email)  # Input email

    # Function to input invalid email into the email field
    def input_invalid_email(self, locator):
        invalid_email = self.credentials['invalid_email']
        self.helper.wait_and_input_text(locator, invalid_email)  # Input invalid email

    def input_inactive_credentials(self, email_locator, password_locator):
        inactive_email = self.credentials['inactive_email']
        inactive_password = self.credentials['inactive_password']
        self.helper.wait_and_input_text(email_locator, inactive_email)  # Input invalid email
        self.helper.wait_and_input_text(password_locator, inactive_password)  # Input password

    # Function to input password into the password field
    def input_password(self, locator):
        password = self.credentials['password']
        self.helper.wait_and_input_text(locator, password)  # Input password

    # Function to input invalid password into the password field
    def input_invalid_password(self, locator):
        invalid_password = self.credentials['invalid_password']
        self.helper.wait_and_input_text(locator, invalid_password)  # Input password

    # Function to click the login button
    def click_login(self, locator):
        self.helper.wait_and_click(locator)  # Click sign in button

    def login_form_disappear(self, locator):
        self.helper.wait_until_elements_are_invisible(locator)

    def remember_me_checkbox(self, locator):
        self.helper.wait_and_click(locator)

    # Function to get the error message text
    def get_error_message(self, locator):
        try:
            self.helper.wait_for_element_visible(locator)
            return self.helper.wait_and_get_text_by_visible_element(locator)
        except Exception as e:
            return "Error Toaster not found"

    def get_validation_message(self, locator):
        try:
            self.helper.wait_for_element_visible(locator)
            return self.helper.wait_and_get_text_by_visible_element(locator)
        except Exception as e:
            return "Validation messages not found"
