import logging
import allure
from selenium.webdriver.common.by import By
from actions.ElementActions import ElementActions

class PopupPage():
    
    ad_close = "//div[@id='ad_position_box']//div[@id='card']//div[@class='toprow']//div[@id='dismiss-button']"
    frame_id = "google_ads_iframe_/6581/web/asi/interstitial/news_info/country_home_0"

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.ele = ElementActions(driver)
        frame = self.ele.wait_for_element_visible(By.ID, self.frame_id)
        self.driver.switch_to.frame(frame)
        
    @allure.step("Checking and close popup appeared")
    def close_popup_ad(self):
        self.logger.info("close ad")
        self.ele.wait_for_element_and_click(By.XPATH,self.ad_close)
        self.driver.switch_to.default_content()
        