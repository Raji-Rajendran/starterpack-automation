import re
import time

from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configs.config import Config
from utils.helper_functions import HelperFunctions


class Roles:
    def __init__(self, driver):
        self.driver = driver
        self.helper = HelperFunctions(self.driver)  # Create an instance of the Helper class

    # Function to open the base URL
    def open(self):
        self.driver.get(Config.base_url + "admin/login")

    # Function to get the title of the current page
    def get_title(self):
        return self.driver.title

    def clear_field_with_js(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].value = '';", element)

    def click_item(self, locator):
        self.helper.wait_and_click(locator)

    def click_roles(self):
        self.helper.wait_and_click((By.XPATH, "(//li[@class='nav-link'])[4]"))

    def input_text(self, locator, text):
        self.helper.wait_and_input_text(locator, text)

    def wait_for_element_visible(self, locator):
        self.helper.wait_for_element_visible(locator)

    def get_text_from_element(self, locator):
        return self.helper.wait_and_get_text_by_visible_element(locator)

    def clear_text(self, locator):
        self.helper.wait_and_clear_text(locator)

    def verify_placeholder(self):
        # Find all input elements
        input_elements = self.driver.find_elements(By.TAG_NAME, 'input')
        print(input_elements)

        # Check if placeholder attribute is present for each input field
        for input_element in input_elements:
            placeholder = input_element.get_attribute('placeholder')
            print(placeholder)
            if placeholder:
                print(f"Placeholder '{placeholder}' is present for input field")
            else:
                print("No placeholder present for input field")

    def verify_mandatory_fields(self):
        # Find all mandatory input fields
        mandatory_fields = self.driver.find_elements(By.XPATH, "//input[@required]")
        # Find validation messages for each mandatory field
        validation_messages = self.driver.find_elements(By.XPATH, "//div[contains(@id,'messages')]")
        # Check if validation messages are present for each mandatory field
        for message in validation_messages:
            if message.text:
                print("Validation Message:", message.text)
            else:
                raise Exception("No validation message found.")

    def click_on_body(self):
        self.driver.execute_script("document.body.click();")

    def refresh_page(self):
        self.driver.refresh()
        time.sleep(2)

    def check_toggle_buttons_off(self):
        def check_toggle_button_off():
            # Find all toggle buttons on the page
            toggle_buttons = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")

            # Iterate through each toggle button
            for button in toggle_buttons:
                # Check if the toggle button is turned on
                if button.is_selected():
                    # If any toggle button is turned on, return False
                    return False
            # If the loop completes without finding any toggle button turned on, return True
            return True

        # Check if all toggle buttons are turned off
        result = check_toggle_button_off()

        # Output result
        if result:
            raise Exception("Toggle buttons are turned off")
        else:
            print("All toggle buttons are turned on")

    def get_role_names_from_card(self):
        # Wait for the cards to load
        cards = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'v-card')]")))

        # Set to store unique role names
        role_names_set = set()

        # Iterate through each card
        for card in cards:
            try:
                # Extract the name of the role from the card using CSS selector
                role_elements = card.find_elements(By.CSS_SELECTOR, "h4")
                for role_element in role_elements:
                    role_name = role_element.text.strip()
                    role_names_set.add(role_name)
            except NoSuchElementException:
                # Handle case where h4 element is not found within a card
                raise Exception("Role element not found in a card.")

        return role_names_set

    def delete_role(self, role_to_match, popup_card, confirm_btn, removed_icon, ok_btn):
        # Wait for the cards to load
        cards = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'v-card')]")))

        # Iterate through each card
        for card in cards:
            try:
                # Extract the name of the role from the card using CSS selector
                role_elements = card.find_elements(By.CSS_SELECTOR, "h4")
                for role_element in role_elements:
                    role_name = role_element.text.strip()
                    if role_name == role_to_match:
                        # Click on the trash icon if the role name matches
                        trash_icon = card.find_element(By.CSS_SELECTOR, "i.v-icon.tabler-trash")
                        trash_icon.click()
                        self.helper.wait_for_element_visible(popup_card)
                        self.helper.wait_and_click(confirm_btn)
                        time.sleep(2)  # Wait for 2 seconds
                        self.helper.wait_for_element_visible(removed_icon)
                        self.helper.wait_and_click(ok_btn)
                        break
            except StaleElementReferenceException:
                # Handle stale element reference exception by retrying
                self.delete_role(role_to_match, popup_card, confirm_btn, removed_icon, ok_btn)
                break
            except NoSuchElementException:
                # Handle case where h4 element is not found within a card
                raise Exception("Role element not found in a card.")

    def delete_user_added_role(self, role_to_match, popup_card, confirm_btn, removed_icon, not_removed_text, ok_btn):
        # Wait for the cards to load
        cards = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'v-card')]")))

        # Iterate through each card
        for card in cards:
            try:
                # Extract the name of the role from the card using CSS selector
                role_elements = card.find_elements(By.CSS_SELECTOR, "h4")
                for role_element in role_elements:
                    role_name = role_element.text.strip()
                    if role_name == role_to_match:
                        # Click on the trash icon if the role name matches
                        trash_icon = card.find_element(By.CSS_SELECTOR, "i.v-icon.tabler-trash")
                        trash_icon.click()
                        self.helper.wait_for_element_visible(popup_card)
                        self.helper.wait_and_click(confirm_btn)
                        time.sleep(2)  # Wait for 2 seconds
                        self.helper.wait_for_element_visible(removed_icon)
                        not_removed_text = self.helper.wait_and_get_text_by_visible_element(not_removed_text)
                        self.helper.wait_and_click(ok_btn)
                        time.sleep(1)  # Wait for 1 second
                        print(not_removed_text)
                        break
            except StaleElementReferenceException:
                # Handle stale element reference exception by retrying
                self.delete_role(role_to_match, popup_card, confirm_btn, removed_icon, ok_btn)
                break
            except NoSuchElementException:
                # Handle case where h4 element is not found within a card
                raise Exception("Role element not found in a card.")

    def get_error_toaster(self, locator):
        try:
            self.helper.wait_for_element_visible(locator)
            return self.helper.wait_and_get_text_by_visible_element(locator)
        except Exception as e:
            raise Exception("Error Toaster not found")

    def verify_get_validation_messages(self):
        time.sleep(1)  # Wait for 1 second
        self.driver.execute_script("document.body.click();")
        validation_message = self.driver.find_element(By.XPATH, "(//div[@class='v-messages__message'])[1]").text
        return validation_message

    def find_role_from_table(self):
        # Find the <td> element in the third column of the table
        td_element = self.driver.find_element(By.XPATH, "//tbody/tr/td[3]")

        # Extract text from the <td> element
        third_column_value = td_element.text

        return third_column_value

    def add_role_with_all_permissions(self, add_role, select_all, role_name_locator, role_name, submit_btn):
        self.helper.wait_and_click(add_role)
        time.sleep(2)  # Wait for 2 seconds
        self.helper.wait_for_element_visible(select_all)  # Wait for the Select All checkbox to be visible
        self.helper.wait_and_input_text(role_name_locator, role_name)
        self.helper.wait_and_click(select_all)  # Click the Select All checkbox
        self.helper.wait_and_click(submit_btn)  # Click the Submit button
