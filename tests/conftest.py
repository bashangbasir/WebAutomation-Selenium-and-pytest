"""
This module contains shared fixtures
"""

import pytest
import selenium.webdriver
import json

@pytest.fixture
def config(scope="session"):
    
    # Read the json file
    with open("config.json") as config_file:
        config = json.load(config_file)

    # Assert values are acceptable : Validate value
    assert config["browser"] in ["Firefox", "Chrome", "Headless Chrome"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    # Return config so it can be used
    return config    

@pytest.fixture
def browser(config):
    # Initialize the chromewebdriver instance
    if config["browser"] == "Firefox":
        b = selenium.webdriver.Firefox()
    elif config["browser"] == "Chrome":
        b = selenium.webdriver.Chrome()
    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser {config["browser"]} is not supported.')
    
    # Make its call wait up to 10s for elements to appear
    b.implicitly_wait(config["implicit_wait"])

    # return the webdriver for the setup 
    yield b

    # quit webdriver for the cleanup
    b.quit()

