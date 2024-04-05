# Data input
TEST_DATA = [
      {"type": "player", "search_term": "Lionel Messi", "expected_result": "Lionel Messi", "sub_page": "News"},
      # {"type": "team", "search_term": "Manchester United", "expected_result": "Manchester United", "sub_page": "News"},
      {"type": "team", "search_term": "Manchester United", "expected_result": "Manchester United", "sub_page": "Player Stats"},
      {"type": "league", "sport": "Racing", "league": "Formula 1", "expected_result": "Formula 1", "sub_page": "Standings"},
      # {"type": "league", "sport": "Racing", "league": "Formula 1", "expected_result": "Formula 1", "sub_page": "News"},
      # {"type": "league", "sport": "Soccer", "league": "MLS", "expected_result": "MLS", "sub_page": "Table"},
      # {"type": "team", "search_term": "Liverpool FC", "expected_result": "Liverpool FC", "sub_page": "Player Stats"},
      {"type": "team", "search_term": "Liverpool FC", "expected_result": "Liverpool FC", "sub_page": "News"}

]

# Source for checking the pages' content
TRUSTED_SOURCE = {
    "Formula 1": ["F1", "Formula 1", "Alonso", 'Hamilton', "Ferrari", "Perez"],
    "Lionel Messi": ["Messi", "Lionel Messi", "Argentina", "Inter Miami"],
    "Liverpool FC": ["Liverpool", "Gomez", "Salah", "Klopp"],
    "Manchester United": ["Manchester United", "Ferdinand", "Man United", "Man Utd", "Fernandes", "Rashford", "Eriksen", "Shaw"],
    "MLS": ["MLS", "Inter Miami", "Toronto FC", "Morgan", "Arango"]
    }
