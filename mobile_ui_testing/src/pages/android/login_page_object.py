from appium.webdriver.common.appiumby import AppiumBy
from mobile_ui_testing.src.helper.appiumdriver import Driver


class LoginScreen(Driver):
    """
    login screen locators
    """
    emailField = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="input-email"]')
    passwordField = (AppiumBy.ACCESSIBILITY_ID, 'input-password')
    loginButton = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="button-LOGIN"]/android.view.ViewGroup')

    def __init__(self, driver):
        super().__init__(driver)