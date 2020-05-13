"""
This module contains shared fixtures
"""

import pytest
import selenium.webdriver

@pytest.fixture
def browser():
    PATH = "F:\Selenium-introduction\chromedriver.exe"
    # Initialize the chromewebdriver instance
    b = selenium.webdriver.Chrome(PATH)

    # Make its call wait up to 10s for elements to appear
    b.implicitly_wait(10)

    # return the webdriver for the setup 
    yield b

    # quit webdriver for the cleanup
    b.quit()

