import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from configs.config_loader import load_config
from pages.launch_page import LaunchPage
from utils.webdriver_utils import WebDriverUtils
from appium.webdriver.common.appiumby import AppiumBy


class TestBase:
    @pytest.fixture(scope = "function", autouse = True)
    def driver_setup(self, request):
        
        # Load the configuration
        config = load_config()
        appium_options = UiAutomator2Options().load_capabilities(config['capabilities'])
        
        # Create the driver instance
        driver = webdriver.Remote(
            command_executor=config['appium_server_url'],
            options=appium_options
        )

        # First actions after launching app
        launch_app = LaunchPage(driver)
        launch_app.perform_initial_action()
        favorite_el = WebDriverUtils.wait_for_element(driver, AppiumBy.ID, launch_app.favorite_icon)
    
        result = favorite_el.text
        assert result == "Favorites"


        if request.cls is not None:
            request.cls.driver = driver
        else:
            self.driver = driver

        def teardown():
            driver.quit()
        
        request.addfinalizer(teardown)


