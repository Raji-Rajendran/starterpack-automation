from selenium.webdriver.common.by import By


class AdminLocators:
    users = By.XPATH, "(//div[@class='nav-group-label'])[1]"
    admins = By.XPATH, "(//li[@class='nav-link'])[2]"
    search_box = By.XPATH, "(//input[@type='text'])[2]"
    add_admin = By.XPATH, "(//button[@type='button'])[7]"
    page_heading = By.XPATH, "//h4[@class='text-h4 mb-6 text-capitalize']"
    first_name = By.XPATH, "(//input[@type='text'])[1]"
    middle_name = By.XPATH, "(//input[@type='text'])[2]"
    last_name = By.XPATH, "(//input[@type='text'])[3]"
    email = By.XPATH, "(//input[@type='email'])[1]"
    phone = By.XPATH, "(//input[@type='text'])[4]"
    select_role = By.XPATH, "//input[@aria-label='Open']"
    save_btn = By.XPATH, "(//span[normalize-space()='Save changes'])[1]"
