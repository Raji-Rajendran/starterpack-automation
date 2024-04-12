from selenium.webdriver.common.by import By


class RoleLocators:
    roles = "(//li[@class='nav-link'])[4]"
    page_heading = By.XPATH, "//h4[@class='text-h4 mb-6 text-capitalize']"
    page_description = By.XPATH, "//div[@class='v-row']//p"
    add_role = By.XPATH, "(//span[normalize-space()='Add Role'])[1]"
    role_name = By.XPATH, "(//input[@type='text'])[1]"
    select_all = By.XPATH, "(//label[normalize-space()='Select All'])[1]"
    submit_btn = By.XPATH, "(//span[normalize-space()='Submit'])[1]"
    popup_card = By.XPATH, "(//div[@class='v-card v-theme--light v-card--density-default v-card--variant-elevated text-center px-10 py-6'])[1]"
    removed_icon = By.XPATH, "(//button[@class='v-btn v-btn--icon v-theme--light text-success v-btn--density-default v-btn--size-default v-btn--variant-outlined my-4'])[1]"
    not_removed_icon = By.XPATH, "(//button[@class='v-btn v-btn--icon v-theme--light text-error v-btn--density-default v-btn--size-default v-btn--variant-outlined my-4'])[1]"
    confirm_btn = By.XPATH, "(//span[normalize-space()='Confirm'])[1]"
    ok_btn = By.XPATH, "(//button[@class='v-btn v-btn--elevated v-theme--light bg-success v-btn--density-default v-btn--size-default v-btn--variant-elevated'])[1]"
    error_toster = By.XPATH, "(//div[@role='status'])[1]"
    not_removed_text = By.XPATH, "//div[contains(@class, 'v-card-text')]/h1"
