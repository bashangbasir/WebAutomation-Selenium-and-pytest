"""
These test cover DuckDuckGo searches
"""
import pytest
from pages.search import DuckDuckGoSearchPage 
from pages.result import DuckDuckGoResultPage

@pytest.mark.parametrize("phrase",["panda", "python","polar bear"]) #for parallel testing
def test_basic_duckduckgo_search(browser,phrase):
    
    # initialize page object and phrase to search
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # given duckduckgo homepage
    search_page.load()

    # when user searches for "panda"
    search_page.search(phrase)

    # then the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # and the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = []
    for t in titles:
        if phrase.lower() in t.lower():
            matches.append(t)
    assert len(matches)>0 # return true when there is title in the matches

    # And search result title contain "panda"
    assert phrase in result_page.title()