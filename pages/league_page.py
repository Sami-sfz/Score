from utils.webdriver_utils import WebDriverUtils

class LeaguePage:
    
    leagues_list_element = "com.fivemobile.thescore:id/recyclerView"
    all_sports_elements = "//android.widget.TextView[@resource-id='com.fivemobile.thescore:id/sports_name'"
    all_leagues_elements = "//android.widget.TextView[@resource-id='com.fivemobile.thescore:id/league_name'"
    league_title_element = "com.fivemobile.thescore:id/titleTextView"
    league_icon = "Leagues"
    scroll_element_news = "//android.widget.ScrollView/android.view.ViewGroup"
    scroll_element_league = "com.fivemobile.thescore:id/recyclerView"
     
    
    
    def __init__(self, driver):
        self.driver = driver

    def find_and_verify_league(self, sport, league_name, expected_result):

        WebDriverUtils.scroll_to_end(self.driver)
    
        exact_sport_element = self.all_sports_elements + f" and @text=\"{sport}\"]"
        sport_el = WebDriverUtils.find_element(self.driver, 'xpath', exact_sport_element)
        sport_el.click()
        
        # TODO: This section should be changed to scroll more dynamic dependant to the element's location
        scroll_el = WebDriverUtils.find_element(self.driver, 'id', self.scroll_element_league)
        WebDriverUtils.scrollGesture(self.driver, scroll_el, 'down', 1)

        exact_league_element = self.all_leagues_elements + f" and @text=\"{league_name}\"]"
        league_el = WebDriverUtils.find_element(self.driver, 'xpath', exact_league_element)
        league_el.click()
        
        league_title_el = WebDriverUtils.find_element(self.driver, 'id', self.league_title_element)
        assert league_title_el.text == expected_result
        

    def verify_in_league_page(self):
       league_icon_el = WebDriverUtils.find_element(self.driver, 'accessibility_id', self.league_icon)
       assert league_icon_el.get_attribute('selected') == 'true'

       league_title_el = WebDriverUtils.find_element(self.driver, 'id', self.league_title_element)
       assert league_title_el.text == 'Leagues'

       