from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    USERNAME_INPUT = (AppiumBy.ID, "com.example.app:id/username")
    PASSWORD_INPUT = (AppiumBy.ID, "com.example.app:id/password")
    LOGIN_BUTTON = (AppiumBy.ID, "com.example.app:id/loginBtn")

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def tap_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
