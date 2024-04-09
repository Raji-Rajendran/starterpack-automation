from selenium.webdriver.common.by import By


class AdminLocators:
    users = By.XPATH, "(//div[@class='nav-group-label'])[1]"
    admins = By.XPATH, "(//li[@class='nav-link'])[2]"
    search_box = By.XPATH, "(//input[@type='text'])[2]"
    add_admin = By.XPATH, "(//button[@type='button'])[7]"
    page_heading = By.XPATH, "//h4[@class='text-h4 mb-6 text-capitalize']"
    page_description = By.XPATH, "//div[@class='v-row']//p"
    first_name = By.XPATH, "(//input[@type='text'])[1]"
    middle_name = By.XPATH, "(//input[@type='text'])[2]"
    last_name = By.XPATH, "(//input[@type='text'])[3]"
    email = By.XPATH, "(//input[@type='email'])[1]"
    phone = By.XPATH, "(//input[@type='text'])[4]"
    select_role = By.XPATH, "(//input[@aria-label='Open'])[1]"
    select_status = By.XPATH, "(//input[@aria-label='Open'])[2]"
    menu_icon = (By.XPATH, "(//i[contains(@class, 'tabler-dots-vertical')])[1]")
    view = By.XPATH, "(//a[@class='v-list-item v-list-item--link v-theme--dark v-list-item--density-comfortable v-list-item--one-line v-list-item--variant-text'])[1]"
    edit_btn = By.XPATH, "(//a[@class='v-btn v-btn--elevated v-theme--dark bg-primary v-btn--density-default v-btn--size-default v-btn--variant-elevated me-4'])[1]"
    delete_btn = By.XPATH, "(//i[@class='v-icon notranslate v-theme--dark tabler-trash v-icon notranslate v-theme--dark'])[1]"
    popup_card = By.XPATH, "(//div[@class='v-card v-theme--dark v-card--density-default v-card--variant-elevated text-center px-10 py-6'])[1]"
    removed_icon = By.XPATH, "(//button[@class='v-btn v-btn--icon v-theme--dark text-success v-btn--density-default v-btn--size-default v-btn--variant-outlined my-4'])[1]"
    confirm_btn = By.XPATH, "(//span[normalize-space()='Confirm'])[1]"
    ok_btn = By.XPATH, "(//button[@class='v-btn v-btn--elevated v-theme--dark bg-success v-btn--density-default v-btn--size-default v-btn--variant-elevated'])[1]"
    save_btn = By.XPATH, "(//span[normalize-space()='Save changes'])[1]"
    clear_email = By.XPATH, "(//i[@role='button'])[7]"
    clear_first_name = By.XPATH, "(//i[@role='button'])[4]"
