
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
    
    # and click news
    result_page.change_search_type("images")

    # then the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # And search result title contain "panda"
    assert PHRASE in result_page.title()

    # and the search result links pertain to "panda"
    titles = result_page.result_link_titles("images")
    matches = []
    for t in titles:
        if PHRASE.lower() in t.lower():
            matches.append(t)
    assert len(matches)>0
    