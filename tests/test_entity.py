from utils.webdriver_utils import *
from pages.main_page import MainPage
from pages.player_page import PlayerPage
from pages.team_page import TeamPage
from pages.league_page import LeaguePage
from .test_base import *
from data.data import *



class TestEntity(TestBase):
    
    @pytest.mark.parametrize("test_data", TEST_DATA)
    def test_entity(self, test_data):
        
        main_page = MainPage(self.driver)
        
        if test_data["type"] == "player":
            player_page = PlayerPage(self.driver)
            main_page.search_and_find(test_data["search_term"])
            player_page.verification_of_player(test_data["expected_result"])
            WebDriverUtils.find_and_verify_sub_page(self.driver, test_data["sub_page"])
            WebDriverUtils.verify_page_content(self.driver, test_data["search_term"])
            WebDriverUtils.back_button(self.driver)
            main_page.verify_in_search_section(test_data["search_term"])

        elif test_data["type"] == "team":
            team_page = TeamPage(self.driver)
            main_page.search_and_find(test_data["search_term"])
            team_page.verification_of_team(test_data["expected_result"])
            WebDriverUtils.find_and_verify_sub_page(self.driver, test_data["sub_page"])
            WebDriverUtils.verify_page_content(self.driver, test_data["search_term"])
            WebDriverUtils.back_button(self.driver)
            main_page.verify_in_search_section(test_data["search_term"])

        elif test_data["type"] == "league":
            main_page.move_to_league_section()
            league_page = LeaguePage(self.driver)
            league_page.find_and_verify_league(test_data["sport"], test_data["league"], test_data["expected_result"])
            WebDriverUtils.find_and_verify_sub_page(self.driver,test_data["sub_page"])
            WebDriverUtils.verify_page_content(self.driver, test_data["league"])
            WebDriverUtils.back_button(self.driver)
            league_page.verify_in_league_page()


        
        
