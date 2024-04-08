import time

import pytest

from configs.config import Config
from locators.login_locator import LoginLocators
from pages.login.login import Login
from pages.login.logout import Logout


# Define a pytest fixture that returns a page instance
@pytest.fixture
def login_page(setup_driver):
    return Login(setup_driver)


@pytest.fixture
def logout_page(setup_driver):
    return Logout(setup_driver)


def test_admin_login(login_page, logout_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "Starter Pack | Login" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email)  # Input email
    login_page.input_password(LoginLocators.password)  # Input password
    login_page.click_login(LoginLocators.login)  # Click the sign-in button
    login_page.login_form_disappear(LoginLocators.login)  # Wait for the login form to disappear
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == Config.base_url + "dashboard"  # Assert that the current URL is correct

    time.sleep(2)  # Wait for 2 seconds
    logout_page.click_profile_icon(LoginLocators.profile_icon)  # Click the profile icon
    logout_page.click_logout(LoginLocators.logout)
    time.sleep(5)  # Wait for 5 seconds
    logout_page.login_form_visible(LoginLocators.login)  # Wait for the login form to appear
    assert "Starter Pack | Login" in logout_page.get_title()  # Assert that the page title is correct


def test_invalid_email_login(login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "Starter Pack | Login" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_invalid_email(LoginLocators.email)  # Input email
    login_page.input_password(LoginLocators.password)  # Input password
    login_page.click_login(LoginLocators.login)  # Click the sign-in button
    error_message = login_page.get_error_message(LoginLocators.error_message)  # Get the error message
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == Config.base_url + "admin/login"  # Assert that the current URL is correct
    assert error_message == "Email ID or Password is not valid"  # Assert that the error message is correct


def test_invalid_password_login(login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "Starter Pack | Login" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email)  # Input email
    login_page.input_invalid_password(LoginLocators.password)  # Input invalid password
    login_page.click_login(LoginLocators.login)  # Click the sign-in button
    error_message = login_page.get_error_message(LoginLocators.error_message)  # Get the error message
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == Config.base_url + "admin/login"  # Assert that the current URL is correct
    assert error_message == "Email ID or Password is not valid"  # Assert that the error message is correct


def test_empty_email_login(login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "Starter Pack | Login" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_password(LoginLocators.password)  # Input password
    login_page.click_login(LoginLocators.login)  # Click the sign-in button
    validation_message = login_page.get_validation_message(LoginLocators.validation_message)  # Get the error message
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == Config.base_url + "admin/login"  # Assert that the current URL is correct
    assert validation_message == "This field is required"  # Assert that the error message is correct


def test_empty_password_login(login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "Starter Pack | Login" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email)  # Input email
    login_page.click_login(LoginLocators.login)  # Click the sign-in button
    validation_message = login_page.get_validation_message(LoginLocators.validation_message)  # Get the error message
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == Config.base_url + "admin/login"  # Assert that the current URL is correct
    assert validation_message == "This field is required"  # Assert that the error message is correct


def test_inactive_account_login(login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "Starter Pack | Login" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_inactive_credentials(LoginLocators.email, LoginLocators.password)  # Input email
    login_page.click_login(LoginLocators.login)  # Click the sign-in button
    error_message = login_page.get_error_message(LoginLocators.error_message)  # Get the error message
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == Config.base_url + "admin/login"  # Assert that the current URL is correct
    assert error_message == "Logged in user is inactive"  # Assert that the error message is correct


def test_remember_me_checkbox(login_page, logout_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "Starter Pack | Login" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email)  # Input email
    login_page.input_password(LoginLocators.password)  # Input password
    login_page.remember_me_checkbox(LoginLocators.remember_me)  # Click the remember me checkbox
    login_page.click_login(LoginLocators.login)  # Click the sign-in button
    login_page.login_form_disappear(LoginLocators.login)  # Wait for the login form to disappear
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == Config.base_url + "dashboard"  # Assert that the current URL is correct
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "Starter Pack | Dashboard" in login_page.get_title()  # Assert that the page title is correct

    time.sleep(2)  # Wait for 2 seconds
    logout_page.click_profile_icon(LoginLocators.profile_icon)  # Click the profile icon
    logout_page.click_logout(LoginLocators.logout)
    time.sleep(5)  # Wait for 5 seconds
    logout_page.login_form_visible(LoginLocators.login)  # Wait for the login form to appear
    assert "Starter Pack | Login" in logout_page.get_title()  # Assert that the page title is correct

# Run the test cases by executing the command: pytest tests/test_login.py
