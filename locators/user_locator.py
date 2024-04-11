from selenium.webdriver.common.by import By


class UserLocators:
    users = By.XPATH, "(//div[@class='nav-group-label'])[1]"
    users_menu = By.XPATH, "(//span[@class='nav-item-title'][normalize-space()='Users'])[2]"
    search_box = By.XPATH, "(//input[@type='text'])[2]"
    page_heading = By.XPATH, "//h4[@class='text-h4 mb-6 text-capitalize']"
    page_description = By.XPATH, "//div[@class='v-row']//p"
    menu_icon = (By.XPATH, "(//i[contains(@class, 'tabler-dots-vertical')])[1]")
    view = By.XPATH, "(//a[@class='v-list-item v-list-item--link v-theme--dark v-list-item--density-comfortable v-list-item--one-line v-list-item--variant-text'])[1]"
    delete_btn = By.XPATH, "(//i[@class='v-icon notranslate v-theme--dark tabler-trash v-icon notranslate v-theme--dark'])[1]"
    popup_card = By.XPATH, "(//div[@class='v-card v-theme--dark v-card--density-default v-card--variant-elevated text-center px-10 py-6'])[1]"
    removed_icon = By.XPATH, "(//button[@class='v-btn v-btn--icon v-theme--dark text-success v-btn--density-default v-btn--size-default v-btn--variant-outlined my-4'])[1]"
    confirm_btn = By.XPATH, "(//span[normalize-space()='Confirm'])[1]"
    ok_btn = By.XPATH, "(//button[@class='v-btn v-btn--elevated v-theme--dark bg-success v-btn--density-default v-btn--size-default v-btn--variant-elevated'])[1]"
    save_btn = By.XPATH, "(//span[normalize-space()='Save changes'])[1]"
    error_message = By.XPATH, "(//div[@role='status'])[1]"
    filter_btn = By.XPATH, "(//i[@class='v-icon notranslate v-theme--dark v-icon--size-default tabler-filter-edit v-icon notranslate v-theme--dark v-icon--size-default'])[1]"
    save_filter = By.XPATH, "(//span[@class='v-btn__content'][normalize-space()='Save Filter'])[2]"
    select_filter_status = By.XPATH, "(//input[@type='text'])[8]"
    filter_close = By.XPATH, "(//i[@class='v-icon notranslate v-theme--dark tabler-x v-icon notranslate v-theme--dark'])[2]"
    sort_by_name = By.XPATH, "(//th[@class='v-data-table__td v-data-table-column--align-start v-data-table__th v-data-table__th--sortable v-data-table__th v-data-table__th--sortable'])[1]"
    table_tbody = By.XPATH, "(//span[normalize-space()='User'])[1]"
    view_name = By.XPATH, "//div[@class='v-list-item-title']/span[text()='Full Name:']/following-sibling::span"
