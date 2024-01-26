import logging
import allure
from selenium.webdriver.common.by import By
from actions.ElementActions import ElementActions
from utils.json_utils import remove_unicode_string

class QuaterWeatherPage():
    
    temp = "//div[@class='weather']//div[@class='temperature']"
    real_feel = "//div[@class='real-feel']"
    main_weather = "//div[@class='phrase']"
    humidity = "//div[@class='panels']//div[@class='left']//p[3]"
    
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.ele = ElementActions(driver)

    @allure.step("Get data of weather")
    def retrieve_weather(self):
        self.logger.info("get data of weather")
        self.ele.ui.wait_for_old_page_gone
        f = remove_unicode_string(self.ele.get_text_of_element(By.XPATH, self.temp))
        weather = dict();
        weather['main'] = remove_unicode_string(self.ele.get_text_of_element(By.XPATH, self.main_weather))
        weather['humidity'] = remove_unicode_string(self.ele.get_text_of_element(By.XPATH, self.humidity)).replace("Humidity", "")
        weather['temperature'] = f+"F"
        weather['real_feel'] = remove_unicode_string(self.ele.get_text_of_element(By.XPATH, self.real_feel))
        return weather

    def validate_temperatureC(self, f):
        self.logger.info("validate Fahrenheit with Celsius of weather")
        actual_tempc = int(remove_unicode_string(self.ele.get_text_of_element(By.XPATH, self.temp)))
        expect_tempc = round(((int(f)-32)*5)/9)
        self.logger.info("actual_tempc: "+str(actual_tempc))
        self.logger.info("expect_tempc: "+str(expect_tempc))
        if actual_tempc == expect_tempc:
            return True
        else:
            return ["False","Temp C UI:"+str(actual_tempc),"Temp C convert F:"+str(expect_tempc)]    
