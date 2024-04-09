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


def test_open_admins_page(admin_page):
    admin_page.click_item(AdminLocators.users)  # Click the Admins link
    admin_page.click_item(AdminLocators.admins)  # Click the Admins link
    admin_page.wait_for_element_visible(AdminLocators.search_box)  # Wait for the search box to be visible
    time.sleep(2)  # Wait for 2 seconds
    assert admin_page.driver.current_url == Config.base_url + "admin"  # Assert that the current URL is correct


def test_add_admin(admin_page):
    admin_page.click_item(AdminLocators.add_admin)  # Click the Add Admin button
    admin_page.wait_for_element_visible(AdminLocators.page_heading)  # Wait for the page heading to be visible
    # admin_page.verify_placeholder()  # Verify the placeholder text in all fields
    admin_page.click_item(AdminLocators.save_btn)  # Click the Save button
    admin_page.verify_mandatory_fields()  # Verify the mandatory fields
    page_heading = admin_page.get_text_from_element(AdminLocators.page_heading)  # Get the text from the page heading
    assert page_heading == "Add Admin"  # Assert that the page heading is correct
    page_description = admin_page.get_text_from_element(AdminLocators.page_description)  # Get the text from the page description
    assert page_description == "Add an admin here."  # Assert that the page description is correct
    admin_page.wait_for_element_visible(AdminLocators.first_name)  # Wait for the first name field to be visible
    admin_page.input_text(AdminLocators.first_name, AdminsConfig.first_name)  # Input the first name
    admin_page.input_text(AdminLocators.last_name, AdminsConfig.last_name)  # Input the last name
    admin_page.input_text(AdminLocators.email, AdminsConfig.email)  # Input the email
    admin_page.input_text(AdminLocators.phone, AdminsConfig.phone)  # Input the phone number
    admin_page.select_from_dropdown(AdminLocators.select_role, AdminsConfig.role)  # Select a value from the dropdown
    admin_page.click_item(AdminLocators.save_btn)  # Click the Save button

    time.sleep(2)  # Wait for 2 seconds

    admin_page.wait_for_element_visible(AdminLocators.add_admin)  # Click the Admins link

    admin_page.click_item(AdminLocators.search_box)  # Click the search box
    admin_page.input_text(AdminLocators.search_box, AdminsConfig.email)  # Input the name

    time.sleep(3)  # Wait for 3 seconds

    list_name = admin_page.find_name_from_table()
    assert list_name == AdminsConfig.first_name + " " + AdminsConfig.last_name  # Assert that the name is correct

    list_email = admin_page.find_email_from_table()
    assert list_email == AdminsConfig.email  # Assert that the email is correct

    # list_phone = admin_page.find_phone_from_table()
    # assert list_phone == str(AdminsConfig.phone)  # Assert that the phone number is correct

    admin_page.check_status_is_inactive()  # Check if the status is inactive


def test_view_admin(admin_page):
    admin_page.click_item(AdminLocators.menu_icon)  # Click the Admins link
    time.sleep(1)  # Wait for 1 second
    admin_page.click_item(AdminLocators.view)  # Click the Admins link
    admin_page.wait_for_element_visible(AdminLocators.edit_btn)  # Wait for the edit button to be visible
    time.sleep(2)  # Wait for 2 seconds
    admin_page.verify_admin_view_url()  # Verify the URL

    view_name = admin_page.get_name_from_view()
    assert view_name == AdminsConfig.first_name + " " + AdminsConfig.last_name  # Assert that the name is correct

    view_role = admin_page.get_role_from_view()
    assert view_role == AdminsConfig.role  # Assert that the role is correct

    view_email = admin_page.get_email_from_view()
    assert view_email == AdminsConfig.email  # Assert that the email is correct

    view_phone = admin_page.get_phone_from_view()
    assert view_phone == str(AdminsConfig.phone)  # Assert that the phone number is correct


def test_edit_admin(admin_page):
    time.sleep(1)  # Wait for 1 second
    admin_page.click_item(AdminLocators.edit_btn)  # Click the Admins link
    admin_page.wait_for_element_visible(AdminLocators.first_name)  # Wait for the save button to be visible
    time.sleep(2)  # Wait for 2 seconds
    assert admin_page.get_text_from_element(AdminLocators.page_heading) == "Edit Admin"  # Assert that the page heading is correct
    assert admin_page.get_text_from_element(AdminLocators.page_description) == "Edit an admin here."  # Assert that the page description is correct

    admin_page.verify_fields_validation(AdminLocators.first_name, AdminLocators.clear_first_name, AdminLocators.save_btn, AdminsConfig.first_name)

    admin_page.input_text(AdminLocators.middle_name, AdminsConfig.middle_name)  # Input the middle name
    admin_page.click_item(AdminLocators.save_btn)  # Click the Save button

    admin_page.wait_for_element_visible(AdminLocators.add_admin)  # Click the Admins link

    admin_page.click_item(AdminLocators.search_box)  # Click the search box
    admin_page.input_text(AdminLocators.search_box, AdminsConfig.email)  # Input the email address

    time.sleep(3)  # Wait for 3 seconds

    list_name = admin_page.find_name_from_table()
    assert list_name == AdminsConfig.first_name + " " + AdminsConfig.middle_name + " " + AdminsConfig.last_name  # Assert that the name is correct

    time.sleep(5)  # Wait for 5 seconds


def test_delete_admin(admin_page):
    admin_page.click_item(AdminLocators.delete_btn)  # Click the Admins link
    admin_page.wait_for_element_visible(AdminLocators.popup_card)  # Wait for the popup card to be visible
    time.sleep(2)  # Wait for 2 seconds
    admin_page.click_item(AdminLocators.confirm_btn)  # Click the removed icon
    time.sleep(2)  # Wait for 2 seconds
    admin_page.wait_for_element_visible(AdminLocators.removed_icon)  # Click the OK button
    admin_page.click_item(AdminLocators.ok_btn)  # Click the OK button
    time.sleep(3)  # Wait for 5 seconds

    admin_page.wait_for_element_visible(AdminLocators.search_box)  # Click the Admins link

    admin_page.clear_text(AdminLocators.search_box)  # Clear the search box
    admin_page.click_item(AdminLocators.search_box)  # Click the search box
    admin_page.input_text(AdminLocators.search_box, AdminsConfig.email)  # Input the email address
    time.sleep(3)  # Wait for 3 seconds

    admin_page.empty_table_check()  # Check if the table is empty


def test_email_validations(admin_page):
    time.sleep(2)  # Wait for 2 seconds
    admin_page.click_item(AdminLocators.add_admin)  # Click the Add Admin button
    admin_page.wait_for_element_visible(AdminLocators.page_heading)  # Wait for the page heading to be visible
    validation_message_1, validation_message_2, validation_message_3, validation_message_4 = admin_page.verify_email_validation(AdminLocators.email, AdminLocators.clear_email, AdminsConfig.email_1, AdminsConfig.email_2, AdminsConfig.email_3, AdminsConfig.email_4)  # Verify the email validation

    expected_message = "The Email field must be a valid email"

    assert validation_message_1 == expected_message
    assert validation_message_2 == expected_message
    assert validation_message_3 == expected_message
    assert validation_message_4 == expected_message


def test_add_admin_with_existing_email(admin_page):
    admin_page.input_text(AdminLocators.first_name, AdminsConfig.first_name)  # Input the first name
    admin_page.input_text(AdminLocators.last_name, AdminsConfig.last_name)  # Input the last name
    admin_page.input_text(AdminLocators.email, AdminsConfig.existing_email)  # Input the email

    admin_page.input_text(AdminLocators.phone, AdminsConfig.phone)  # Input the phone number
    admin_page.select_from_dropdown(AdminLocators.select_role, AdminsConfig.role)  # Select a value from the dropdown
    admin_page.click_item(AdminLocators.save_btn)  # Click the Save button

    admin_page.verify_get_validation_messages()


# Run the test cases by executing the command: pytest tests/test_admins.py
