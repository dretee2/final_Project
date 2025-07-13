import pytest
from mobile_ui_testing.src.helper.appiumdriver import Driver
from mobile_ui_testing.src.pages.android.home_page_object import HomeScreen
from mobile_ui_testing.src.helper.app import App


@pytest.mark.usefixtures("setup")  # Applies to all tests in the class
@pytest.mark.home
class TestHomeScreen:

    def test_home_1(self):
        """
        Verify presence of all main home screen buttons using App.element.
        """
        App.element(self.driver, HomeScreen.homeMenu)
        App.element(self.driver, HomeScreen.loginMenu)
        App.element(self.driver, HomeScreen.formsMenu)
        App.element(self.driver, HomeScreen.swipeMenu)
        App.swipe_until(self.driver, HomeScreen.supportLink, start_x=144, start_y=434)

    def test_home_2(self):
        """
        Verify HOME_MENU and LOGIN_MENU exist.
        """
        App.element(self.driver, HomeScreen.homeMenu)
        App.element(self.driver, HomeScreen.loginMenu)

    def test_all_buttons_visible_on_home_screen(self):
        """
        Verify that key buttons are visible on the Home screen using App.is_exist.
        """
        home = HomeScreen(self.driver)

        assert App.is_exist(self.driver, home.loginMenu), "Login menu not visible"
        assert App.is_exist(self.driver, home.formsMenu), "Forms menu not visible"
        assert App.is_exist(self.driver, home.homeMenu), "Home menu not visible"
        assert App.is_exist(self.driver, home.swipeMenu), "Swipe menu not visible"
        assert App.is_exist(self.driver, home.supportLink), "Support link not visible"
