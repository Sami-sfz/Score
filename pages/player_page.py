from utils.webdriver_utils import *


class PlayerPage:
    
    player_name_element = "com.fivemobile.thescore:id/txt_player_name"
    
    def __init__(self, driver):
        self.driver = driver

    def verification_of_player(self, player_name):
        player_name_el = WebDriverUtils.find_element(self.driver, 'id', self.player_name_element)
        assert player_name_el.get_attribute('text') == player_name