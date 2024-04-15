import time

import pytest
from selenium.common import NoSuchElementException

from configs.config import Config, RolesConfig
from locators.admin_locator import AdminLocators
from locators.login_locator import LoginLocators
from locators.role_locator import RoleLocators
from pages.admins import Admins
from pages.login.login import Login
from pages.roles import Roles


# Define a pytest fixture that returns a page instance
@pytest.fixture
def login_page(setup_driver):
    return Login(setup_driver)


@pytest.fixture
def role_page(setup_driver):
    return Roles(setup_driver)


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


def test_open_roles_page(role_page):
    role_page.click_roles()  # Click the Admins link
    role_page.wait_for_element_visible(RoleLocators.page_heading)  # Wait for the search box to be visible
    time.sleep(2)  # Wait for 2 seconds
    assert role_page.driver.current_url == Config.base_url + "admin/roles"  # Assert that the current URL is correct


def test_verify_page_heading_description(role_page):
    time.sleep(2)  # Wait for 2 seconds
    assert role_page.get_text_from_element(
        RoleLocators.page_heading) == "Roles List"  # Assert that the page heading is correct
    assert role_page.get_text_from_element(
        RoleLocators.page_description) == "A role provided access to predefined menus and features so that depending on assigned role an administrator can have access to what he need."  # Assert that the page description is correct


# def test_verify_add_role_with_all_permissions(role_page):
#     role_page.click_item(RoleLocators.add_role)  # Wait for the Add Role button to be visible
#     time.sleep(2)  # Wait for 2 seconds
#     role_page.wait_for_element_visible(RoleLocators.select_all)  # Wait for the Select All checkbox to be visible
#     assert role_page.driver.current_url == Config.base_url + "admin/roles/add"  # Assert that the current URL is correct
#     assert role_page.get_text_from_element(
#         RoleLocators.page_heading) == "Add New Role"  # Assert that the Add Role button text is correct
#     # assert role_page.get_text_from_element(
#     #     RoleLocators.page_description) == "Add New Role and Permissions."  # Assert that the Add Role button text is correct
#     role_page.wait_for_element_visible(RoleLocators.select_all)  # Wait for the Select All checkbox to be visible
#     role_page.input_text(RoleLocators.role_name, RolesConfig.role_name)  # Input the role name
#     role_page.click_item(RoleLocators.select_all)  # Click the Select All checkbox
#     role_page.click_item(RoleLocators.submit_btn)  # Click the Submit button
#
#     role_page.wait_for_element_visible(RoleLocators.add_role)  # Wait for the page heading to be visible
#
#     role_names = role_page.get_role_names_from_card()  # Get the role names from the card
#     # Convert both `RolesConfig.role_name` and `role_names` to lowercase
#     role_name_lowercase = RolesConfig.role_name.lower()
#     role_names_lowercase = [name.lower() for name in role_names]
#     # Assert that the role name is correct (case-insensitive)
#     assert role_name_lowercase in role_names_lowercase  # Assert that the role name is correct
#
#
# def test_created_role_is_present(admin_page, role_page):
#     time.sleep(2)  # Wait for 2 seconds
#     admin_page.click_item(AdminLocators.users)  # Click the Admins link
#     admin_page.click_item(AdminLocators.admins)  # Click the Admins link
#     time.sleep(2)  # Wait for 2 seconds
#     admin_page.wait_for_element_visible(AdminLocators.search_box)  # Wait for the search box to be visible
#     admin_page.click_item(AdminLocators.add_admin)  # Click the Add Admin button
#     time.sleep(2)  # Wait for 2 seconds
#     admin_page.wait_for_element_visible(AdminLocators.email)  # Wait for the first name field to be visible
#     admin_page.input_text(AdminLocators.first_name, RolesConfig.admin_first_name)  # Input the first name
#     admin_page.input_text(AdminLocators.last_name, RolesConfig.admin_last_name)  # Input the last name
#     admin_page.input_text(AdminLocators.email, RolesConfig.admin_email)  # Input the email
#     admin_page.input_text(AdminLocators.phone, RolesConfig.admin_phone)  # Input the phone number
#     admin_page.click_item(AdminLocators.role)  # Click the role dropdown
#     try:
#         admin_page.select_role_from_dropdown(RolesConfig.role_name)  # Select a value from the dropdown
#         admin_page.click_item(AdminLocators.save_btn)  # Click the Save button
#
#         admin_page.wait_for_element_visible(AdminLocators.add_admin)  # Click the Admins link
#
#         admin_page.click_item(AdminLocators.search_box)  # Click the search box
#         admin_page.input_text(AdminLocators.search_box, RolesConfig.admin_email)  # Input the name
#
#         time.sleep(3)  # Wait for 3 seconds
#
#         list_name = admin_page.find_name_from_table()
#         assert list_name == RolesConfig.admin_first_name + " " + RolesConfig.admin_last_name  # Assert that the name is correct
#
#         list_email = admin_page.find_email_from_table()
#         assert list_email == RolesConfig.admin_email  # Assert that the email is correct
#
#         list_role = admin_page.find_role_from_table()
#         # Convert both `RolesConfig.role_name` and `role_names` to lowercase
#         role_name_lowercase = RolesConfig.role_name.lower()
#         role_names_lowercase = [name.lower() for name in list_role]
#         # Assert that the role name is correct (case-insensitive)
#         assert role_name_lowercase in role_names_lowercase  # Assert that the role name is correct
#
#     except Exception:
#         admin_page.click_item(AdminLocators.save_btn)  # Click the Save button
#         validation_message = role_page.verify_get_validation_messages()  # Verify the validation messages
#         if validation_message == "This field is required":
#             raise Exception("Added Role is not present in the dropdown list")
#
#
# def test_delete_role_with_users(role_page):
#     time.sleep(3)  # Wait for 3 seconds
#     role_page.click_on_body()  # Click on the body
#     role_page.click_roles()  # Click the Admins link
#     role_page.wait_for_element_visible(RoleLocators.page_heading)  # Wait for the search box to be visible
#
#     role_page.delete_user_added_role(RolesConfig.role_name, RoleLocators.popup_card, RoleLocators.confirm_btn,
#                                      RoleLocators.not_removed_icon, RoleLocators.not_removed_text,
#                                      RoleLocators.ok_btn)  # Delete the role
#     time.sleep(2)  # Wait for 2 seconds
#
#     role_names = role_page.get_role_names_from_card()  # Get the role names from the card
#     assert RolesConfig.role_name in role_names  # Assert that the role name is correct
#
#
# def test_delete_role(role_page):
#     time.sleep(2)  # Wait for 2 seconds
#
#     role_page.add_role_with_all_permissions(RoleLocators.add_role, RoleLocators.select_all, RoleLocators.role_name,
#                                             RolesConfig.new_role_name,
#                                             RoleLocators.submit_btn)  # Add a role with all permissions
#     role_page.wait_for_element_visible(RoleLocators.add_role)  # Wait for the page heading to be visible
#     time.sleep(2)  # Wait for 2 seconds
#     role_page.delete_role(RolesConfig.new_role_name, RoleLocators.popup_card, RoleLocators.confirm_btn,
#                           RoleLocators.removed_icon, RoleLocators.ok_btn)  # Delete the role
#     time.sleep(2)  # Wait for 2 seconds
#
#     role_names = role_page.get_role_names_from_card()  # Get the role names from the card
#     assert RolesConfig.new_role_name not in role_names  # Assert that the role name is correct
#
#
# def test_role_name_validation(role_page):
#     role_page.click_item(RoleLocators.add_role)  # Wait for the Add Role button to be visible
#     time.sleep(2)  # Wait for 2 seconds
#     role_page.wait_for_element_visible(RoleLocators.select_all)  # Wait for the Select All checkbox to be visible
#     role_page.click_item(RoleLocators.submit_btn)
#
#     error_toaster = role_page.get_error_toaster(RoleLocators.error_toster)  # Get the error toaster
#     assert error_toaster == "The name field is required."  # Assert that the error toaster is correct
#
#     role_page.input_text(RoleLocators.role_name, "Admin")  # Click the OK button
#     role_page.click_item(RoleLocators.submit_btn)  # Click the OK button
#
#     error_toaster = role_page.get_error_toaster(RoleLocators.error_toster)  # Get the error toaster
#     assert error_toaster == "The name has already been taken."  # Assert that the error toaster is correct


def test_edit_role(role_page):
    time.sleep(3)  # Wait for 3 seconds
    # # role_page.click_on_body()  # Click on the body
    # # role_page.click_roles()  # Click the Admins link
    # role_page.wait_for_element_visible(RoleLocators.page_heading)  # Wait for the search box to be visible
    #
    # role_page.add_role_with_all_permissions(RoleLocators.add_role, RoleLocators.select_all, RoleLocators.role_name,
    #                                         RolesConfig.new_role_name,
    #                                         RoleLocators.submit_btn)  # Add a role with all permissions
    # role_page.wait_for_element_visible(RoleLocators.add_role)  # Wait for the page heading to be visible
    # time.sleep(2)  # Wait for 2 seconds
    # role_page.edit_role_page(RolesConfig.new_role_name)  # Delete the role
    # time.sleep(2)  # Wait for 2 seconds
    # assert role_page.get_text_from_element(RoleLocators.page_heading) == "Edit Role"  # Assert that the page heading is correct
    # # assert role_page.get_text_from_element(RoleLocators.page_description) == "Edit Role and Permissions."  # Assert that the page description is correct
    # role_page.click_item(RoleLocators.role_name)  # Input the role name
    # role_page.clear_text(RoleLocators.role_name)  # Input the role name
    # role_page.click_item(RoleLocators.submit_btn)  # Click the Submit button
    # error_toaster = role_page.get_error_toaster(RoleLocators.error_toster)  # Get the error toaster
    # assert error_toaster == "The name field is required."  # Assert that the error toaster is correct
    #
    # validation_message = role_page.verify_get_validation_messages()  # Verify the validation messages
    # assert validation_message == "This field is required"  # Assert that the validation message is correct
    #
    # role_page.input_text(RoleLocators.role_name, "Admin")  # Input the role name
    # role_page.click_item(RoleLocators.submit_btn)  # Click the Submit button
    #
    # error_toaster = role_page.get_error_toaster(RoleLocators.error_toster)  # Get the error toaster
    # assert error_toaster == "The name has already been taken."  # Assert that the error toaster is correct


def test_create_role_with_permissions(role_page):
    # time.sleep(3)  # Wait for 3 seconds
    # role_page.click_on_body()  # Click on the body
    # role_page.click_roles()  # Click the Admins link
    # role_page.wait_for_element_visible(RoleLocators.page_heading)  # Wait for the search box to be visible

    role_page.click_item(RoleLocators.add_role)  # Wait for the Add Role button to be visible
    time.sleep(2)  # Wait for 2 seconds
    role_page.wait_for_element_visible(RoleLocators.select_all)  # Wait for the Select All checkbox to be visible

    role_page.input_text(RoleLocators.role_name, RolesConfig.role_name)  # Input the role name

    role_page.click_random_roles()  # Click the Select All checkbox
    time.sleep(2)  # Wait for 2 seconds

    role_page.click_item(RoleLocators.submit_btn)  # Click the Submit button

    role_page.wait_for_element_visible(RoleLocators.add_role)  # Wait for the page heading to be visible

    role_page.edit_role_page(RolesConfig.role_name)
    time.sleep(2)  # Wait for 2 seconds
    role_page.wait_for_element_visible(RoleLocators.select_all)  # Wait for the search box to be visible

    role_page.verify_clicked_checkboxes()  # Verify the clicked checkboxes

    role_page.click_on_body()  # Click on the body
    role_page.click_roles()  # Click the Admins link
    role_page.wait_for_element_visible(RoleLocators.page_heading)  # Wait for the search box to be visible

    role_page.delete_role(RolesConfig.role_name, RoleLocators.popup_card, RoleLocators.confirm_btn, RoleLocators.removed_icon, RoleLocators.ok_btn)  # Delete the role





# Run the test cases by executing the command: pytest tests/test_roles.py
