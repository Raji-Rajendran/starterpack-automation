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

    def click_item(self, locator):
        self.helper.wait_and_click(locator)

    def input_text(self, locator, text):
        self.helper.wait_and_input_text(locator, text)

    def wait_for_element_visible(self, locator):
        self.helper.wait_for_element_visible(locator)

    def get_text_from_element(self, locator):
        return self.helper.wait_and_get_text_by_visible_element(locator)

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
