import os
import pytest
import unittest
from appium import webdriver
from datetime import datetime
from pytest_html_reporter import attach
from appium.options.ios import XCUITestOptions
from mobile_ui_testing.src.helper.business import *
from appium.options.android import UiAutomator2Options


class Driver(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)


    def setUp(self):
        """
        This method instantiates the Appium driver using modern options.
        """

        self.logger.info("Configuring desired capabilities with Appium Options")

        # Check if running in a distributed test (e.g., pytest-xdist worker)
        if os.getenv('PYTEST_XDIST_WORKER'):
            if self.app == 'ios':
                options = XCUITestOptions()
                options.set_capability('deviceName', 'iPhone 14')
                options.set_capability('platformVersion', '17.0')
                options.set_capability('app', f'{os.getcwd()}/data/apps/iOS-Simulator-NativeDemoApp-0.2.1.app')
                options.set_capability('noReset', True)

            elif self.app == 'android':
                options = UiAutomator2Options()
                options.set_capability('platformVersion', '14')
                options.set_capability('deviceName', 'Pixel_7_API_34')
                options.set_capability('wdaLocalPort', Driver.wda_port(self))
                options.set_capability('udid', Driver.android_device_name(self))
                options.set_capability('app', f'{os.getcwd()}/data/apps/app-staging-debug.apk')
                options.set_capability('noReset', True)

        else:
            if self.app == 'ios':
                options = self.ios()
            elif self.app == 'android':
                options = self.android()

        self.logger.info("Initiating Appium driver with modern Options object")
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
        self.driver.implicitly_wait(5)
        self.logger.info(f"Session started with: {self.driver.capabilities}")

    def android(self):
        options = UiAutomator2Options()
        options.set_capability('platformVersion', '14')

        if self.device == 'emulator':
            options.set_capability('deviceName', 'Pixel_7_API_34')
            options.set_capability('app', f'{os.getcwd()}/data/apps/Android-NativeDemoApp-0.2.1.apk')
        elif self.device == 'real device':
            options.set_capability('deviceName', 'Android Device')
            options.set_capability('udid', self.android_device_name())
            options.set_capability('app', f'{os.getcwd()}/data/apps/Android-NativeDemoApp-0.2.1.apk')

        options.set_capability('automationName', 'UiAutomator2')
        options.set_capability('noReset', True)
        return options

    def ios(self):
        options = XCUITestOptions()
        options.set_capability('platformVersion', '17.0')

        if self.device == 'simulator':
            options.set_capability('deviceName', 'iPhone 14')
            options.set_capability('app', f'{os.getcwd()}/data/apps/iOS-Simulator-NativeDemoApp-0.2.1.app')
        elif self.device == 'real device':
            options.set_capability('deviceName', 'iPhone 14 Pro')
            options.set_capability('udid', '<your_real_device_udid>')
            options.set_capability('xcodeOrgId', '<your_xcode_team_id>')
            options.set_capability('xcodeSigningId', 'iPhone Developer')
            options.set_capability('app', f'{os.getcwd()}/data/apps/iOS-RealDevice-NativeDemoApp-0.2.1.ipa')
            options.set_capability('useNewWDA', True)
        elif self.device == 'bitrise':
            options.set_capability('deviceName', 'iPhone 14')
            options.set_capability('udid', 'E04A6F53-4C3B-4810-B210-DD2015D0D064')
            options.set_capability('useNewWDA', True)
            options.set_capability('app', f'{os.getcwd()}/data/apps/iOS-Simulator-NativeDemoApp-0.2.1.app')

        options.set_capability('automationName', 'XCUITest')
        options.set_capability('noReset', True)
        return options

    def tearDown(self):
        Driver.screenshot_on_failure(self)
        attach(data=self.driver.get_screenshot_as_png())
        self.driver.quit()

    def screenshot_on_failure(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        test_name = self._testMethodName
        for self._testMethodName, error in self._outcome.errors:
            if error:
                self.logger.error("Taking screenshot on failure")
                if not os.path.exists('screenshots'):
                    os.makedirs('screenshots')

                self.driver.save_screenshot(f"screenshots/{test_name}_{now}.png")

    @pytest.fixture(autouse=True)
    def cli(self, app, device, get_logger):
        self.app = app
        self.device = device
        self.logger = get_logger

    def wda_port(self):
        if os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
            return 8101
        else:  # include 'master' and 'gw0'
            return 8100

    def android_device_name(self):
        if os.getenv('PYTEST_XDIST_WORKER') == 'gw0':
            return 'emulator-5554'
        elif os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
            return 'emulator-5556'
        else:  # default
            return 'emulator-5554'


if __name__ == '__main__':
    unittest.main()