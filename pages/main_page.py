from utils.webdriver_utils import *


class MainPage:

    search_element = "com.fivemobile.thescore:id/search_bar_text_view"
    search_element_with_result = "com.fivemobile.thescore:id/search_src_text"
    search_text_element = "com.fivemobile.thescore:id/search_src_text"
    search_result_first_element = "(//android.widget.TextView)[5]"
    league_element = "Leagues"
    

    def __init__(self, driver):
        self.driver = driver

    def search_and_find(self, term):
        search_el = WebDriverUtils.find_element(self.driver, 'id', self.search_element)
        search_el.click()
        search_text_el = WebDriverUtils.find_element(self.driver, 'id', self.search_text_element)
        search_text_el.send_keys(term)
        search_result_el = WebDriverUtils.find_element(self.driver, 'xpath', self.search_result_first_element)
        search_result_el.click()

    def move_to_league_section(self):
        league_el = WebDriverUtils.find_element(self.driver, 'accessibility_id', self.league_element)
        league_el.click()
       
    def verify_in_search_section(self, last_search):
        search_result_el = WebDriverUtils.find_element(self.driver, 'xpath', self.search_result_first_element)
        assert last_search in search_result_el.text 

        WebDriverUtils.find_element(self.driver, 'id', self.search_element_with_result)


