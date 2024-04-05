from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from data.data import *
from utils.webdriver_utils import *
from selenium.common.exceptions import NoSuchElementException

class WebDriverUtils:

    news_element = "//android.widget.LinearLayout[@content-desc='News']"
    sub_tab_class_name = "android.widget.TextView"
    back_element = "Navigate up"

    @staticmethod
    def wait_for_element(driver, locator_strategy , locator_value = '', timeout = 2):
        return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((locator_strategy, locator_value))
        )

    @staticmethod
    def find_element(driver, locator_strategy, locator_value = ''):

        locator_strategies = {
            'id': AppiumBy.ID,
            'xpath': AppiumBy.XPATH,
            'accessibility_id': AppiumBy.ACCESSIBILITY_ID,
            'name': AppiumBy.NAME,
            'class_name': AppiumBy.CLASS_NAME,
            'UiAutomator': AppiumBy.ANDROID_UIAUTOMATOR
        }

        if locator_strategy not in locator_strategies:
            raise ValueError(f"Unsupported locator strategy: {locator_strategy}")

        strategy = locator_strategies[locator_strategy]
        element = driver.find_element(strategy, locator_value)
        return element
    

    @staticmethod
    def scrollGesture(driver, element, direction, percent = 1):
        if direction == "down":
            return driver.execute_script('mobile: scrollGesture', {
            'elementId': element,
            'direction': 'down',
            'percent': percent,
            })

        elif direction == "up":
            return driver.execute_script('mobile: scrollGesture', {
            'elementId': element,
            'direction': 'up',
            'percent': percent,
            })
    
    
    @staticmethod
    def scroll_to_end(driver):
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(4)')
    
    @staticmethod
    def find_and_verify_sub_page(driver, sub_page):

        if sub_page != "News":
            sub_tab_section = WebDriverUtils.find_element(driver, 'accessibility_id', sub_page)
        
        elif sub_page == "News":
            sub_tab_section = WebDriverUtils.find_element(driver, 'xpath', WebDriverUtils.news_element)
        
        sub_tab_section.click()
        sub_el = sub_tab_section.find_element(AppiumBy.CLASS_NAME, WebDriverUtils.sub_tab_class_name)
        
        assert sub_el.get_attribute('selected') == 'true'
        result = sub_el.get_attribute('text')
        assert sub_page.upper() == result

    @staticmethod
    def verify_page_content(driver, term):

        page_source = driver.page_source

        for item in TRUSTED_SOURCE[term]:
                if item in page_source:
                    return True
                
        raise AssertionError("Expected words were not found in the page source.")
            
    @staticmethod
    def back_button(driver):
        WebDriverUtils.find_element(driver, 'accessibility_id', WebDriverUtils.back_element).click()