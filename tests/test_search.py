"""
These test cover DuckDuckGo searches
"""
from pages.search import DuckDuckGoSearchPage 
from pages.result import DuckDuckGoResultPage

def test_basic_duckduckgo_search(browser):
    
    # initialize page object and phrase to search
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"

    # given duckduckgo homepage
    search_page.load()

    # when user searches for "panda"
    search_page.search(PHRASE)

    # then search result title contain "panda"
    assert PHRASE in result_page.title()

    # and the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # and the search result links pertain to "panda"
    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()
    
    raise Exception("incomplete test")