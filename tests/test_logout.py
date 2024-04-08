import time

import pytest

from configs.config import Config
from locators.login_locator import LoginLocators
from pages.login.login import Login
from pages.login.logout import Logout


# Define a pytest fixture that returns a page instance
@pytest.fixture
def logout_page(setup_driver):
    return Logout(setup_driver)


@pytest.fixture
def login_page(setup_driver):
    return Login(setup_driver)


def test_admin_logout(logout_page, login_page):
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

    logout_page.driver.execute_script("window.open('');")
    logout_page.driver.switch_to.window(logout_page.driver.window_handles[1])
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "Starter Pack | Login" in login_page.get_title()  # Assert that the page title is correct


def test_url_after_admin_logout(logout_page, login_page):
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

    logout_page.driver.execute_script("window.open('');")
    logout_page.driver.switch_to.window(logout_page.driver.window_handles[1])
    logout_page.open_dashboard()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert login_page.driver.current_url == Config.base_url + "admin/login?to=/dashboard"  # Assert that the current URL is correct


# Run the test cases by executing the command: pytest tests/test_logout.py
