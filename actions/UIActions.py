import pdb
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import POLL_FREQUENCY
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import *
from contextlib import contextmanager
from selenium.webdriver.common.keys import Keys
import urllib.parse as urlparse

class UIActions(object):
    DEFAULT_TIMEOUT = 45
    
    def __init__(self, driver):
        self.driver = driver
    
    def go_previous_page(self):
        self.driver.back()
        self.driver.refresh()

    @contextmanager
    def wait_for_old_page_gone(self):
        old_page_url = self.driver.current_url
        yield
        self.wait_until(lambda: (old_page_url != self.driver.current_url))

    def check_element_exists(self, by, locator):
        try:
            self.driver.find_element(by, locator)
        except NoSuchElementException:
            return False
        return True



