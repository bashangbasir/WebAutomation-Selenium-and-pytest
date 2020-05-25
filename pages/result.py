"""
This module contains DuckDuckGo Result Page
the page object for the DuckDuckGo search result
"""
from selenium.webdriver.common.by import By
class DuckDuckGoResultPage:

    RESULT_LINK = (By.CSS_SELECTOR,"a.result__a") #same for new and normal type search
    SEARCH_INPUT = (By.ID, "search_form_input")
    SEARCH_IMAGES = (By.CSS_SELECTOR, "a.zcm__link.js-zci-link.js-zci-link--images")
    SEARCH_NEWS = (By.CSS_SELECTOR, "a.zcm__link.js-zci-link.js-zci-link--news")
    SEARCH_VIDEOS = (By.CSS_SELECTOR, "a.zcm__link.js-zci-link.js-zci-link--videos")
    RESULT_LINK_VIDEO =(By.CSS_SELECTOR,"h6.tile__title.tile__title--2")
    RESULT_LINK_IMAGES = (By.CSS_SELECTOR,".tile--img__title")

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self, mode=""):
        if mode == "" or mode == "news":
            links = self.browser.find_elements(*self.RESULT_LINK)
        elif mode == "videos":
            links = self.browser.find_elements(*self.RESULT_LINK_VIDEO)
        elif mode == "images":
            links = self.browser.find_elements(*self.RESULT_LINK_IMAGES)
        else: 
            raise Exception("Wrong mode!")
        titles = []
        for link in links:
            titles.append(link.text)
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        # get content of input form by using get_attribute() method, not text attribute as above 
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title

    def change_search_type(self,mode):
        if mode == "news":
            news_mode = self.browser.find_element(*self.SEARCH_NEWS)
            news_mode.click()
        elif mode == "images":
            images_mode = self.browser.find_element(*self.SEARCH_IMAGES)
            images_mode.click()
        elif mode == "videos":
            videos_mode = self.browser.find_element(*self.SEARCH_VIDEOS)
            videos_mode.click()
        else:
            raise Exception("Wrong mode!")