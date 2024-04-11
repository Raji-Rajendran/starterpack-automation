import time

import pytest

from configs.config import Config, RolesConfig
from locators.login_locator import LoginLocators
from locators.role_locator import RoleLocators
from pages.login.login import Login
from pages.roles import Roles


# Define a pytest fixture that returns a page instance
@pytest.fixture
def login_page(setup_driver):
    return Login(setup_driver)


@pytest.fixture
def role_page(setup_driver):
    return Roles(setup_driver)


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


def test_open_roles_page(role_page):
    role_page.click_roles()  # Click the Admins link
    role_page.wait_for_element_visible(RoleLocators.page_heading)  # Wait for the search box to be visible
    time.sleep(2)  # Wait for 2 seconds
    assert role_page.driver.current_url == Config.base_url + "admin/roles"  # Assert that the current URL is correct


def test_verify_page_heading_description(role_page):
    time.sleep(2)  # Wait for 2 seconds
    assert role_page.get_text_from_element(RoleLocators.page_heading) == "Roles List"  # Assert that the page heading is correct
    assert role_page.get_text_from_element(RoleLocators.page_description) == "A role provided access to predefined menus and features so that depending on assigned role an administrator can have access to what he need."  # Assert that the page description is correct


def test_verify_add_role_with_all_permissions(role_page):
    role_page.click_item(RoleLocators.add_role)  # Wait for the Add Role button to be visible
    time.sleep(2)  # Wait for 2 seconds
    role_page.wait_for_element_visible(RoleLocators.select_all)  # Wait for the Select All checkbox to be visible
    assert role_page.driver.current_url == Config.base_url + "admin/roles/add"  # Assert that the current URL is correct
    assert role_page.get_text_from_element(RoleLocators.page_heading) == "Add New Role"  # Assert that the Add Role button text is correct
    assert role_page.get_text_from_element(RoleLocators.page_description) == "Add New Role and Permissions."  # Assert that the Add Role button text is correct
    role_page.wait_for_element_visible(RoleLocators.select_all)  # Wait for the Select All checkbox to be visible
    role_page.input_text(RoleLocators.role_name, RolesConfig.role_name)  # Input the role name
    role_page.click_item(RoleLocators.select_all)  # Click the Select All checkbox
    role_page.click_item(RoleLocators.submit_btn)  # Click the Submit button

    role_page.wait_for_element_visible(RoleLocators.add_role)  # Wait for the page heading to be visible

    role_names = role_page.get_role_names_from_card()  # Get the role names from the card
    assert RolesConfig.role_name in role_names  # Assert that the role name is correct


def test_delete_role(role_page):
    role_page.delete_role(RolesConfig.role_name, RoleLocators.popup_card, RoleLocators.confirm_btn, RoleLocators.removed_icon, RoleLocators.ok_btn)  # Delete the role
    time.sleep(2)  # Wait for 2 seconds

    role_names = role_page.get_role_names_from_card()  # Get the role names from the card
    assert RolesConfig.role_name not in role_names  # Assert that the role name is correct

# Run the test cases by executing the command: pytest tests/test_roles.py
