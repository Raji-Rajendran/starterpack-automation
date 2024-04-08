from selenium.webdriver.common.by import By


class LoginLocators:
    email = By.XPATH, "(//input[@type='email'])[1]"
    password = By.XPATH, "(//input[@type='password'])[1]"
    login = By.XPATH, "(//button[@type='submit'])[1]"
    error_message = By.XPATH, "(//div[@role='status'])[1]"
    validation_message = By.XPATH, "(//div[@class='v-messages__message'])[1]"
    remember_me = By.XPATH, "(//label[normalize-space()='Remember me'])[1]"
    profile_icon = By.XPATH, "(//img[@class='v-img__img v-img__img--cover'])[1]"
    logout = By.XPATH, "(//div[contains(text(),'Logout')])[1]"
