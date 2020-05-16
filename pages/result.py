"""
This module contains DuckDuckGo Result Page
the page object for the DuckDuckGo search result
"""
from selenium.webdriver.common.by import By
class DuckDuckGoResultPage:

    RESULT_LINK = (By.CSS_SELECTOR,"a.result__a")
    SEARCH_INPUT = (By.ID, "search_form_input")

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        #TODO
        return []

    def search_input_value(self):
        #TODO
        return ""

    def title(self):
        #TODO
        return ""
