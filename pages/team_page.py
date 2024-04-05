from utils.webdriver_utils import *


class TeamPage:
    
    team_name_element = "com.fivemobile.thescore:id/team_name"
    
    
    def __init__(self, driver):
        self.driver = driver

    def verification_of_team(self, team_name):
        team_name_el = WebDriverUtils.find_element(self.driver, 'id', self.team_name_element)
        assert team_name_el.text == team_name

    