from utils.webdriver_utils import *


class LaunchPage:

    get_start_element = "com.fivemobile.thescore:id/btn_primary"
    continue_element = "com.fivemobile.thescore:id/btn_primary"
    favorite_element = "(//android.widget.ImageView[@resource-id='com.fivemobile.thescore:id/follow_icon'])[1]"
    favorite_icon = "com.fivemobile.thescore:id/navigation_bar_item_large_label_view"
    next_continue_element = "com.fivemobile.thescore:id/action_button_text"
    done_element = "com.fivemobile.thescore:id/action_button_text"
    later_element = "com.fivemobile.thescore:id/btn_secondary"
   
    def __init__(self, driver):
        self.driver = driver


    def perform_initial_action(self):
        start_element = WebDriverUtils.wait_for_element(self.driver, AppiumBy.ID, self.get_start_element)
        start_element.click()
        WebDriverUtils.find_element(self.driver, 'id', self.continue_element).click()
        WebDriverUtils.find_element(self.driver, 'xpath', self.favorite_element).click()
        WebDriverUtils.find_element(self.driver, 'id', self.next_continue_element).click()
        WebDriverUtils.find_element(self.driver, 'id', self.done_element).click()
        WebDriverUtils.find_element(self.driver, 'id', self.later_element).click()
       
     