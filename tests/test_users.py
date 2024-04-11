import time

import pytest

from configs.config import Config, UsersConfig
from locators.login_locator import LoginLocators
from locators.user_locator import UserLocators
from pages.login.login import Login
from pages.users import Users


# Define a pytest fixture that returns a page instance
@pytest.fixture
def login_page(setup_driver):
    return Login(setup_driver)


@pytest.fixture
def user_page(setup_driver):
    return Users(setup_driver)


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


def test_open_users_page(user_page):
    user_page.click_item(UserLocators.users)  # Click the Admins link
    user_page.click_item(UserLocators.users_menu)  # Click the Admins link
    user_page.wait_for_element_visible(UserLocators.search_box)  # Wait for the search box to be visible
    time.sleep(2)  # Wait for 2 seconds
    assert user_page.driver.current_url == Config.base_url + "user"  # Assert that the current URL is correct


def test_view_user(user_page):
    user_page.click_item(UserLocators.search_box)  # Click the search box
    user_page.input_text(UserLocators.search_box, UsersConfig.email)  # Input the name

    time.sleep(3)  # Wait for 3 seconds

    list_name = user_page.find_name_from_table()
    list_email = user_page.find_email_from_table()
    list_phone = user_page.find_phone_from_table()

    user_page.click_item(UserLocators.menu_icon)  # Click the Admins link
    time.sleep(1)  # Wait for 1 second
    user_page.click_item(UserLocators.view)  # Click the Admins link
    time.sleep(2)  # Wait for 2 seconds
    user_page.verify_user_view_url()  # Verify the URL

    user_page.wait_for_element_visible(UserLocators.view_name)  # Wait for the page heading to be visible

    view_name = user_page.get_name_from_view()
    assert list_name == view_name  # Assert that the name is correct

    view_email = user_page.get_email_from_view()
    assert list_email == view_email  # Assert that the email is correct

    view_phone = user_page.get_phone_from_view()
    assert list_phone == view_phone  # Assert that the phone number is correct


def test_delete_user(user_page):
    user_page.click_item(UserLocators.users_menu)  # Click the search box
    user_page.click_item(UserLocators.search_box)  # Click the search box
    user_page.input_text(UserLocators.search_box, UsersConfig.email)  # Input the name

    time.sleep(3)  # Wait for 3 seconds
    user_page.wait_for_element_visible(UserLocators.search_box)  # Click the Admins link

    user_page.click_item(UserLocators.delete_btn)  # Click the Admins link
    user_page.wait_for_element_visible(UserLocators.popup_card)  # Wait for the popup card to be visible
    time.sleep(2)  # Wait for 2 seconds
    user_page.click_item(UserLocators.confirm_btn)  # Click the removed icon
    time.sleep(2)  # Wait for 2 seconds
    user_page.wait_for_element_visible(UserLocators.removed_icon)  # Click the OK button
    user_page.click_item(UserLocators.ok_btn)  # Click the OK button
    time.sleep(3)  # Wait for 5 seconds

    user_page.wait_for_element_visible(UserLocators.search_box)  # Click the Admins link

    user_page.clear_text(UserLocators.search_box)  # Clear the search box
    user_page.click_item(UserLocators.search_box)  # Click the search box
    user_page.input_text(UserLocators.search_box, UsersConfig.email)  # Input the email address
    time.sleep(3)  # Wait for 3 seconds

    user_page.empty_table_check()  # Check if the table is empty
    user_page.refresh_page()  # Refresh the page


def test_sort_by_name(user_page):
    user_page.wait_for_element_visible(UserLocators.search_box)  # Wait for the search box to be visible

    user_page.click_item(UserLocators.sort_by_name)  # Click the menu icon
    time.sleep(3)  # Wait for 3 seconds
    user_page.get_all_names()  # Get all the names from the table
    user_page.check_names_in_alphabetical_order()  # Check if the names are in alphabetical order


def test_filter(user_page):
    user_page.wait_for_element_visible(UserLocators.search_box)  # Wait for the add admin button to be visible

    user_page.click_item(UserLocators.filter_btn)  # Click the filter button
    user_page.wait_for_element_visible(UserLocators.save_filter)  # Wait for the save filter button to be visible

    user_page.input_text(UserLocators.select_filter_status, UsersConfig.filter_status)  # Input the status
    user_page.click_item(UserLocators.filter_close)  # Click the save filter button

    user_page.click_on_body()  # Click on the body

    time.sleep(5)

    user_page.wait_for_element_visible(UserLocators.table_tbody)  # Wait for the add admin button to be visible

    time.sleep(10)

    user_page.check_toggle_buttons_off()

# Run the test cases by executing the command: pytest tests/test_admins.py
