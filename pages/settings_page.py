import logging
import allure
from selenium.webdriver.common.by import By

from actions.ElementActions import ElementActions
from utils.json_utils import get_json_from_file

class SettingsPage():
    
    units = "unit"

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.ele = ElementActions(driver)
        
    @allure.step("select value option")
    def select_units_item(self, value):
        self.logger.info("select %s" %value)
        self.ele.select_value(By.ID, self.units, value)