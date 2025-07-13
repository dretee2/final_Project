import pytest
from page_objects.login_page import LoginPage
from utils.config_reader import ReadConfig
from utils.logger import RecordLogger

@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = LoginPage(self.driver)
        self.config = ReadConfig()
        self.logger = RecordLogger.get_logger()

    def test_login_valid_user(self):
        self.logger.info("🔐 Starting login test with valid credentials")
        username = self.config.get_default("username")
        password = self.config.get_default("password")

        self.login.enter_username(username)
        self.login.enter_password(password)
        self.login.tap_login()

        self.logger.info("✅ Login test completed")
