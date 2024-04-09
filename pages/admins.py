import re
import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configs.config import Config
from utils.helper_functions import HelperFunctions


class Admins:
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

    def select_from_dropdown(self, locator, value):
        dropdown_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        dropdown_element.send_keys(value)

    def find_email_from_table(self):
        email_element = self.driver.find_element(By.XPATH, "//tbody/tr/td[contains(@class, 'v-data-table__td')]/div/div/span[@class='text-sm text-medium-emphasis']")
        # Extract the text value
        email_value = email_element.text
        return email_value

    def find_name_from_table(self):
        # Find the element containing the name value
        name_element = self.driver.find_element(By.XPATH, "//tbody/tr/td[contains(@class, 'v-data-table__td')]/div/div/h6/a[@class='font-weight-medium text-link']")
        # Extract the text value
        name_value = name_element.text
        return name_value

    def verify_admin_added(self):
        try:
            self.driver.find_element(By.XPATH, "//tbody/tr/td[contains(@class, 'v-data-table__td')]/div/div/h6/a[@class='font-weight-medium text-link']")
            return True
        except NoSuchElementException:
            return False

    def find_role_from_table(self):
        # Find all the <td> elements in the table
        td_elements = self.driver.find_elements(By.XPATH, "//tbody/tr/td[3]")

        # Extract text from each <td> element and store in a list
        third_column_values = [td.text for td in td_elements]

        # Print the list of values
        print(third_column_values)

        return third_column_values

    def find_phone_from_table(self):
        # Find the element containing the phone value
        phone_element = self.driver.find_element(By.XPATH, "//tbody/tr/td[contains(@class, 'v-data-table__td')]/div/label[@class='v-label']")
        # Extract the text value
        phone_value = phone_element.text
        # Slicing the phone number to get the desired part
        sliced_phone = phone_value.split(" ")[1]
        return sliced_phone

    def check_status_is_inactive(self):
        # Find the toggle button element
        toggle_button = self.driver.find_element(By.CLASS_NAME, "v-selection-control__input")
        # Check if the toggle button is turned off
        if not toggle_button.is_selected():
            print("Toggle button is turned off.")
        else:
            raise Exception("Toggle button is turned on.")

    def verify_admin_view_url(self):
        # Get the current URL
        current_url = self.driver.current_url
        # Check if the URL contains the expected value
        pattern = r"https://qa\.starterpack\.2base\.in/admin/[a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12}/view"
        # Check if the current URL matches the pattern
        assert re.match(pattern, current_url), f"URL '{current_url}' does not match as the expected!"

    def verify_admin_edit_url(self):
        # Get the current URL
        current_url = self.driver.current_url
        # Check if the URL contains the expected value
        pattern = r"https://qa\.starterpack\.2base\.in/admin/[a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12}"
        # Check if the current URL matches the pattern
        assert re.match(pattern, current_url), f"URL '{current_url}' does not match as the expected!"

    def get_name_from_view(self):
        # Find the element containing the value "Gena Andre"
        name = self.driver.find_element(By.XPATH, "(//span[@class='text-capitalize'])[1]")
        # Extract the text from the element
        name_value = name.text
        return name_value

    def get_role_from_view(self):
        # Find the element containing the value "Gena Andre"
        role = self.driver.find_element(By.XPATH, "(//span[@class='text-capitalize'])[2]")
        # Extract the text from the element
        role_value = role.text
        return role_value

    def get_email_from_view(self):
        # Find the element containing the email text
        email_element = self.driver.find_element(By.XPATH, "//div[@class='v-list-item-title']//a[contains(@href, 'mailto:')]")
        # Extract the email text from the element
        email_text = email_element.text
        return email_text

    def get_phone_from_view(self):
        # Find the element containing the value "Gena Andre"
        phone_element = self.driver.find_element(By.XPATH, "(//span[@class='text-capitalize'])[4]")
        # Extract the text value
        phone_value = phone_element.text
        # Slicing the phone number to get the desired part
        sliced_phone = phone_value.split(" ")[1]
        return sliced_phone

    def check_status_is_active(self):
        # Find the toggle button element
        toggle_button = self.driver.find_element(By.CLASS_NAME, "v-selection-control__input")
        # Check if the toggle button is turned on
        if toggle_button.is_selected():
            print("Toggle button is turned on.")
        else:
            raise Exception("Toggle button is turned off.")

    def empty_table_check(self):
        table_element = self.driver.find_element(By.XPATH, "//td[@colspan='8']")
        # Locate the 'No data available' text within the table
        no_data_text = table_element.text
        return no_data_text

    def verify_email_validation(self, locator, clear_locator, email_1, email_2, email_3, email_4):
        self.helper.wait_and_input_text(locator, email_1)
        time.sleep(1)  # Wait for 1 second
        self.driver.execute_script("document.body.click();")
        validation_message_1 = self.driver.find_element(By.XPATH, "(//div[@class='v-messages__message'])[1]").text

        self.helper.wait_and_click(clear_locator)
        self.helper.wait_and_input_text(locator, email_2)
        time.sleep(1)  # Wait for 1 second
        self.driver.execute_script("document.body.click();")
        validation_message_2 = self.driver.find_element(By.XPATH, "(//div[@class='v-messages__message'])[1]").text

        self.helper.wait_and_click(clear_locator)
        self.helper.wait_and_input_text(locator, email_3)
        time.sleep(1)  # Wait for 1 second
        self.driver.execute_script("document.body.click();")
        validation_message_3 = self.driver.find_element(By.XPATH, "(//div[@class='v-messages__message'])[1]").text

        self.helper.wait_and_click(clear_locator)
        self.helper.wait_and_input_text(locator, email_4)
        time.sleep(1)  # Wait for 1 second
        self.driver.execute_script("document.body.click();")
        validation_message_4 = self.driver.find_element(By.XPATH, "(//div[@class='v-messages__message'])[1]").text

        self.helper.wait_and_click(clear_locator)

        return validation_message_1, validation_message_2, validation_message_3, validation_message_4

    def verify_get_validation_messages(self):
        time.sleep(1)  # Wait for 1 second
        self.driver.execute_script("document.body.click();")
        validation_message = self.driver.find_element(By.XPATH, "(//div[@class='v-messages__message'])[1]").text
        return validation_message

    def verify_fields_validation(self, field_locator, clear_locator, save_locator, field_value):
        self.helper.wait_and_click(field_locator)
        self.helper.wait_and_click(clear_locator)
        self.helper.wait_and_click(save_locator)
        validation_message = self.verify_get_validation_messages()  # Verify the mandatory fields
        assert validation_message == "This field is required"  # Assert that the validation message is correct
        self.helper.wait_and_input_text(field_locator, field_value)

    def get_error_toaster(self, locator):
        try:
            self.helper.wait_for_element_visible(locator)
            return self.helper.wait_and_get_text_by_visible_element(locator)
        except Exception as e:
            return "Error Toaster not found"

    def click_on_body(self):
        self.driver.execute_script("document.body.click();")

    def get_all_statuses(self):
        # Find all the toggle button elements
        toggle_buttons = self.driver.find_elements(By.CLASS_NAME, "v-selection-control__input")

        # Initialize an empty list to store the statuses
        statuses = []

        # Iterate through each toggle button element
        for toggle_button in toggle_buttons:
            # Check if the toggle button is turned on (active)
            if toggle_button.is_selected():
                # Append "Active" to the statuses list
                statuses.append("Active")
            else:
                # Append "Inactive" to the statuses list
                statuses.append("Inactive")
        print(statuses)
        return statuses

    def get_all_names(self):
        names = []
        # Find the element containing the name value
        name_elements = self.driver.find_elements(By.XPATH, "//tbody/tr/td[contains(@class, 'v-data-table__td')]/div/div/h6/a[@class='font-weight-medium text-link']")
        for name in name_elements:
            names.append(name.text)
        return names

    def check_names_in_alphabetical_order(self):
        # Get all names
        names = self.get_all_names()

        # Extract first names
        first_names = [name.split()[0] for name in names]

        # Check if first names are in alphabetical order
        sorted_first_names = sorted(first_names)
        if first_names == sorted_first_names:
            print("All first names are in alphabetical order.")
        else:
            # Find the index where the alphabetical order breaks
            index = next(i for i, (name1, name2) in enumerate(zip(first_names, sorted_first_names)) if name1 != name2)
            print(f"Issue occurred at index {index}: {first_names[index]} is not in alphabetical order.")
            raise Exception("First names are not in alphabetical order.")
