import logging
import allure
from selenium.webdriver.common.by import By

from actions.ElementActions import ElementActions
from utils.json_utils import get_json_from_file

class HomePage():
    
    menu = "svg[data-qa='navigationMenu']"
    menu_item = "//a[contains(text(), '%s')]"
    settings = "div[class='settings-link']"

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.ele = ElementActions(driver)
        self.env = get_json_from_file("config/env_config.json")

    @allure.step("Open Page")
    def open_page(self, sub_url):
        self.logger.info(self.env["url"] + sub_url)
        self.driver.get(self.env["url"] + sub_url)
        
    @allure.step("Navigating to menu item")
    def navigate_to_menu_item(self, item):
        self.logger.info("open menu")
        self.ele.wait_for_element_and_click(By.CSS_SELECTOR, self.menu)
        self.logger.info("click menu item %s" %item)
        self.ele.wait_for_element_and_click(By.XPATH, self.menu_item %item)

    @allure.step("Open Settings")
    def open_setting(self):
        self.logger.info("open menu")
        self.ele.wait_for_element_and_click(By.CSS_SELECTOR, self.menu)
        self.logger.info("open settings")
        self.ele.wait_for_element_and_click(By.CSS_SELECTOR, self.settings)

        