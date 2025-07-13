import pytest
from appium.webdriver.common.appiumby import AppiumBy
from mobile_ui_testing.src.helper.appiumdriver import Driver
from mobile_ui_testing.src.pages.android.login_page_object import LoginScreen
from mobile_ui_testing.src.helper.app import App


class TestLoginScreen(Driver):
    """
    Test cases for Login screen
    """

     # injects driver, app type, etc.
    @pytest.mark.login
    @pytest.mark.regression
    def test_login_elements_are_visible(self):
        """
        Test: Check all login screen elements are visible
        """
        login = LoginScreen(self.driver)

        assert App.is_exist(login.emailField), "Email input field is not visible"
        assert App.is_exist(login.passwordField), "Password input field is not visible"
        assert App.is_exist(login.loginButton), "Login button is not visible"


    @pytest.mark.login
    def test_user_can_enter_credentials_and_tap_login(self):
        """
        Test: Simulate user entering login credentials
        """
        login = LoginScreen(self.driver)

        App.send_keys(login.emailField, text="user@example.com")
        App.send_keys(login.passwordField, text="Password123")
        App.click(login.loginButton)

        # Add your post-login assert or wait logic here
        App.sleep({"sleep": 2})


    """
    Negative tests for Login screen using parameterization
    """

    @pytest.mark.login
    @pytest.mark.parametrize(
        "email, password, expected_error",
        [
            ("", "", "Email is required"),
            ("user@example.com", "", "Password is required"),
            ("", "Password123", "Email is required"),
            ("invalid@example.com", "wrongpass", "Invalid credentials"),
        ]
    )
    def test_invalid_login_attempts(self, email, password, expected_error):
        """
        Parametrized test for multiple negative login cases
        """
        login = LoginScreen(self.driver)

        # Fill in credentials
        App.send_keys(login.emailField, text=email)
        App.send_keys(login.passwordField, text=password)
        App.click(login.loginButton)

        # Wait for the error message to appear (replace locator as needed)
        error_locator = (AppiumBy.ACCESSIBILITY_ID, "error-message")  # You must update this
        assert App.is_exist(error_locator), "Error message not visible"

        # Optionally assert the error text
        App.assert_text(error_locator, expected_error)