import logging
import allure
from selenium.webdriver.common.by import By
from actions.ElementActions import ElementActions

class DailyWeatherPage():
    
    daily_item = "//div[@data-qa='dailyCard%s']//a"

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.ele = ElementActions(driver)

    @allure.step("Open day")
    def open_daily_item(self, index):
        self.logger.info("open %s day of weather"%str(index))
        self.ele.wait_element_and_click_location(By.XPATH, self.daily_item %index)
        