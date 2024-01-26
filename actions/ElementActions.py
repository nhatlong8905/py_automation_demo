import pdb
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import POLL_FREQUENCY
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from actions.UIActions import UIActions

class ElementActions(object):
    DEFAULT_TIMEOUT = 60
    ELEMENT_DISPLAY_TIMEOUT = 3
    modules = []

    def __init__(self, driver):
        self.driver = driver
        self.ui = UIActions(driver)

    def wait_for_element_visible(self, by, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for an element visible"""
        driver = self.driver
        WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located((by, locator)))
        return driver.find_element(by, locator)

    def wait_for_element_clickable(self, by, locator):
        """Wait for an element clickable"""
        driver = self.driver
        WebDriverWait(driver, self.DEFAULT_TIMEOUT).until(expected_conditions.element_to_be_clickable((by, locator)))
        return driver.find_element(by, locator)

    def wait_for_element_and_click(self, by, locator):
        element = self.wait_for_element_clickable(by, locator)
        element.click()
    
    def wait_element_and_click_location(self, by, locator):
        element = self.wait_for_element_clickable(by, locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).move_by_offset(10, 10).perform()
        time.sleep(0.5)
        element.click()

    def have_element_displayed(self, by, locator, timeout=ELEMENT_DISPLAY_TIMEOUT, poll_frequency=POLL_FREQUENCY):
        driver = self.driver
        try:
            WebDriverWait(driver, timeout, poll_frequency=poll_frequency)\
                .until(expected_conditions.visibility_of_element_located((by, locator)))
        except Exception:
            return False
        return True

    def is_element_visible(self, by, locator):
        return self.driver.find_element(by, locator).is_displayed()

    def get_text_of_element(self, by, locator):
        element= self.wait_for_element_visible(by, locator)
        return element.text
   
    def select_value(self,  by, locator, value):
        select = Select(self.driver.find_element(by, locator))
        select.select_by_value(value)
        