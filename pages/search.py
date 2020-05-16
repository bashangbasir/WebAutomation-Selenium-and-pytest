"""
This module contains DuckDuckGo Search page
the page object for the DuckDuckgo search page.
"""
from selenium.webdriver.common.by import By

class DuckDuckGoSearchPage:
    
    #store locator using tuple
    SEARCH_INPUT = (By.ID, "search_form_input_homepage")

    #constructor method 
    def __init__(self,browser):
        self.browser = browser

    def load(self):
        # TODO
        pass

    def search(self, phrase):
        #TODO
        pass
