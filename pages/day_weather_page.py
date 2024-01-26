import logging
import time
import allure
from selenium.webdriver.common.by import By
from actions.ElementActions import ElementActions
from utils.json_utils import remove_unicode_string

class DayWeatherPage():
    
    quater_day = "(//a[@class='quarter-day-cta spaced-content'])[%s]"
    quater = "//a[@class='quarter-day-cta spaced-content']"
    day_value = "//div[@class='subnav-pagination']//div"

    temp = "(//div[@class='weather']//div[@class='temperature'])[%s]"
    real_feel = "(//div[@class='real-feel'])[%s]"
    main_weather = "(//div[@class='phrase'])[%s]"
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.ele = ElementActions(driver)

    @allure.step("Open quater day")
    def open_quater_day(self, index):
        self.logger.info("open quater of day weather")
        count = 1
        number_quater = self.driver.find_elements(By.XPATH, self.quater)
        if len(number_quater) < 3:
            index = index - 2
        while count < 5 :
            time.sleep(3)
            if self.ele.is_element_visible(By.XPATH, self.quater_day%index):
                break
            count+=1
        self.ele.wait_for_element_and_click(By.XPATH, self.quater_day%index)
    
    @allure.step("check have quater")
    def have_quater(self):
        return self.ele.have_element_displayed(By.XPATH, self.quater)
    
    @allure.step("Retieve weather day")
    def retrieve_weather(self, index):
        self.logger.info("get data of weather")
        if index == 2:
            index = 1
        elif index == 3 or index == 4:
            index = 2
        f = remove_unicode_string(self.ele.get_text_of_element(By.XPATH, self.temp%index)).replace("Lo", "").replace("Hi", "")
        weather = dict();
        weather['main'] = remove_unicode_string(self.ele.get_text_of_element(By.XPATH, self.main_weather%index))
        weather['temperature'] = f+"F"
        weather['real_feel'] = remove_unicode_string(self.ele.get_text_of_element(By.XPATH, self.real_feel%index))
        return weather

    @allure.step("Retieve day value")        
    def retrieve_day_value(self):
        return self.ele.get_text_of_element(By.XPATH, self.day_value)
    
    def validate_temperatureC_day(self, f, index):
        self.logger.info("validate Fahrenheit with Celsius of weather")
        if index == 2:
            index = 1
        elif index == 3 or index == 4:
            index = 2
        actual_tempc = int(remove_unicode_string(self.ele.get_text_of_element(By.XPATH, self.temp%index)).replace("Lo", "").replace("Hi", ""))
        expect_tempc = round(((int(f)-32)*5)/9)
        self.logger.info("actual_tempc: "+str(actual_tempc))
        self.logger.info("expect_tempc: "+str(expect_tempc))
        if actual_tempc == expect_tempc:
            return True
        else:
            return ["False", "temp C UI:"+str(actual_tempc),"Temp C convert F:"+str(expect_tempc)] 