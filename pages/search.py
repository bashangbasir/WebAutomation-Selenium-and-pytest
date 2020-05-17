"""
This module contains DuckDuckGo Search page
the page object for the DuckDuckgo search page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:
    
    #store locator using tuple
    SEARCH_INPUT = (By.ID, "search_form_input_homepage")

    # URL
    URL = "https://duckduckgo.com/"

    #constructor method 
    def __init__(self,browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        # * in the find_element() method will unpack the tuple into this --> (By.ID, "search_form_input_homepage")
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
        
