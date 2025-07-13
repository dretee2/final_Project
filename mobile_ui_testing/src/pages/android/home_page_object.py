from appium.webdriver.common.mobileby import MobileBy
from mobile_ui_testing.src.helper.appiumdriver import Driver


class HomeScreen(Driver):
    """
    Page Object representing the Home screen elements.
    """

    # Locators
    LOGIN_MENU = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Login']/android.widget.TextView")
    FORMS_MENU = (MobileBy.ACCESSIBILITY_ID, "Forms")
    HOME_MENU = (MobileBy.ACCESSIBILITY_ID, "Home")
    SWIPE_MENU = (MobileBy.ACCESSIBILITY_ID, "Swipe")
    SUPPORT_LINK = (MobileBy.XPATH, '//android.widget.ScrollView[@content-desc="Home-screen"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[3]')

    def __init__(self, driver):
        super().__init__(driver)
