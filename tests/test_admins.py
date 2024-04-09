import time

import pytest
from selenium.webdriver.common.by import By

from configs.config import Config, AdminsConfig
from locators.admin_locator import AdminLocators
from locators.login_locator import LoginLocators
from pages.admins import Admins
from pages.login.login import Login


# Define a pytest fixture that returns a page instance
@pytest.fixture
def login_page(setup_driver):
    return Login(setup_driver)


@pytest.fixture
def admin_page(setup_driver):
    return Admins(setup_driver)


def test_admin_login(login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "Starter Pack | Login" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email)  # Input email
    login_page.input_password(LoginLocators.password)  # Input password
    login_page.click_login(LoginLocators.login)  # Click the sign-in button
    login_page.login_form_disappear(LoginLocators.login)  # Wait for the login form to disappear
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == Config.base_url + "dashboard"  # Assert that the current URL is correct


def test_add_admin(admin_page):
    admin_page.click_item(AdminLocators.users)  # Click the Admins link
    admin_page.click_item(AdminLocators.admins)  # Click the Admins link
    admin_page.wait_for_element_visible(AdminLocators.search_box)  # Wait for the search box to be visible
    admin_page.click_item(AdminLocators.add_admin)  # Click the Add Admin button
    admin_page.wait_for_element_visible(AdminLocators.page_heading)  # Wait for the page heading to be visible
    # admin_page.verify_placeholder()  # Verify the placeholder text in all fields
    admin_page.click_item(AdminLocators.save_btn)  # Click the Save button
    admin_page.verify_mandatory_fields()  # Verify the mandatory fields
    page_heading = admin_page.get_text_from_element(AdminLocators.page_heading)  # Get the text from the page heading
    assert page_heading == "Add Admin"  # Assert that the page heading is correct
    admin_page.wait_for_element_visible(AdminLocators.first_name)  # Wait for the first name field to be visible
    admin_page.input_text(AdminLocators.first_name, AdminsConfig.first_name)  # Input the first name
    admin_page.input_text(AdminLocators.last_name, AdminsConfig.last_name)  # Input the last name
    admin_page.input_text(AdminLocators.email, AdminsConfig.email)  # Input the email
    admin_page.input_text(AdminLocators.phone, AdminsConfig.phone)  # Input the phone number
    admin_page.select_from_dropdown(AdminLocators.select_role, AdminsConfig.role)  # Select a value from the dropdown
    admin_page.click_item(AdminLocators.save_btn)  # Click the Save button

    time.sleep(2)

    admin_page.wait_for_element_visible(AdminLocators.search_box)  # Click the Admins link

    admin_page.click_item(AdminLocators.search_box)  # Click the search box
    admin_page.input_text(AdminLocators.search_box, AdminsConfig.email)  # Input the name

    time.sleep(5)  # Wait for 5 seconds

    name = admin_page.find_name_from_table()
    email = admin_page.find_email_from_table()
    assert email == AdminsConfig.email  # Assert that the email is correct


# Run the test cases by executing the command: pytest tests/test_admins.py
