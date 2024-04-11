import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configs.config import Config
from utils.helper_functions import HelperFunctions


class Users:
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
        # Find the elements containing name and email
        name_and_email_elements = self.driver.find_elements(By.XPATH,
                                                            "//tbody//div[contains(@class, 'v-avatar')]//following-sibling::div")

        # Extract the name from the first element
        email_element = name_and_email_elements[0]
        email = email_element.find_element(By.TAG_NAME, "span").text

        return email

    def find_name_from_table(self):
        # Find the elements containing name and email
        name_and_email_elements = self.driver.find_elements(By.XPATH,
                                                            "//tbody//div[contains(@class, 'v-avatar')]//following-sibling::div")

        # Extract the name from the first element
        name_element = name_and_email_elements[0]
        full_name = name_element.find_element(By.TAG_NAME, "h6").text

        cropped_name = ' '.join(full_name.split()[2:]) if '.' in full_name.split()[1] else full_name
        return cropped_name

    def find_phone_from_table(self):
        # Find the element containing the phone value
        phone_element = self.driver.find_element(By.XPATH, "//tbody/tr/td[5]")
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

    def verify_user_view_url(self):
        # Get the current URL
        current_url = self.driver.current_url
        # Check if the URL contains the expected value
        pattern = r"https://qa\.starterpack\.2base\.in/user/[a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12}/view"
        # Check if the current URL matches the pattern
        assert re.match(pattern, current_url), f"URL '{current_url}' does not match as the expected!"

    def get_name_from_view(self):
        # Find the element containing the value "Gena Andre"
        name = self.driver.find_element(By.XPATH,
                                        "//div[@class='v-list-item-title']/span[text()='Full Name:']/following-sibling::span")
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
        email_element = self.driver.find_element(By.XPATH,
                                                 "//div[@class='v-list-item-title']//a[contains(@href, 'mailto:')]")
        # Extract the email text from the element
        email_text = email_element.text
        return email_text

    def get_phone_from_view(self):
        # Find the element containing the value "Gena Andre"
        phone_element = self.driver.find_element(By.XPATH, "(//span[@class='text-capitalize'])[2]")
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

    def verify_get_validation_messages(self):
        time.sleep(1)  # Wait for 1 second
        self.driver.execute_script("document.body.click();")
        validation_message = self.driver.find_element(By.XPATH, "(//div[@class='v-messages__message'])[1]").text
        return validation_message

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
        # Find the elements containing name and email
        name_and_email_elements = self.driver.find_elements(By.XPATH,
                                                            "//tbody//div[contains(@class, 'v-avatar')]//following-sibling::div")

        # Initialize a list to store extracted names
        names_list = []

        # Loop through each element to extract names
        for name_element in name_and_email_elements:
            full_name = name_element.find_element(By.TAG_NAME, "h6").text
            cropped_name = ' '.join(full_name.split()[2:]) if '.' in full_name.split()[1] else full_name
            names_list.append(cropped_name)
        return names_list

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

    def refresh_page(self):
        self.driver.refresh()
        time.sleep(2)

    def find_emails_from_table(self):
        # Find the elements containing name and email
        name_and_email_elements = self.driver.find_elements(By.XPATH,
                                                            "//tbody//div[contains(@class, 'v-avatar')]//following-sibling::div")

        # Initialize a list to store extracted emails
        emails_list = []

        # Loop through each element to extract emails
        for email_element in name_and_email_elements:
            email = email_element.find_element(By.TAG_NAME, "span").text
            emails_list.append(email)

        print(emails_list)

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
