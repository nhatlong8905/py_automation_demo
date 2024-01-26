import pdb
from selenium.webdriver.common.by import By
import pytest
import allure
from actions.ElementActions import ElementActions
from actions.UIActions import UIActions
from contants.quater import Quater
from pages.daily_weather_page import DailyWeatherPage
from pages.day_weather_page import DayWeatherPage
from pages.home_page import HomePage
from pages.popup_page import PopupPage
from pages.quarter_weather_page import QuaterWeatherPage
from pages.settings_page import SettingsPage
from utils.json_utils import create_json_file, get_json_from_file
from contants import locator_contants

@pytest.mark.usefixtures("setup")
class TestReportTemperature:

    @allure.title("Test report")
    @allure.description("This is test of report weather")
    def test_report_temperature(self):
        input = get_json_from_file("test_data/input_day.json")
        days = []
        count = 0
        day_failed = []
        to_day=""
        infor = {}
        for i, text_quater in enumerate(input["quaters"]):
            day = self.retrive_data_weather_of_day(input["url"], input["unit"], input["menu"], i, text_quater)
            if day["validate"] !=True:
                count +=1
                day_failed.append(day[next(iter(day))])
            days.append(day)
        from_day = days[0][next(iter(days[0]))]
        to_day = days[len(days)-1][next(iter(days[len(days)-1]))]
        summary = {"summary":"SUMMARY REPORT DAY OF WEATHER","from" :from_day, "to":to_day, "number_validate_failed":count, "days_failed":day_failed}
        infor.update(summary)
        infor.update({"days":days})
        
        create_json_file("test_output/", input["output"], infor)
        assert count == 0

    def retrive_data_weather_of_day(self, url, unit, menu, index_day, text_quater,flag_remove = False):
        home = HomePage(self.driver)
        home.open_page(url)    
        home.open_setting()
        settings = SettingsPage(self.driver)
        settings.select_units_item(unit)

        ui = UIActions(self.driver)
        ui.go_previous_page()

        home.navigate_to_menu_item(menu)

        boolean_popup = ui.check_element_exists(By.ID,locator_contants.pop_up_ad_id)
        if boolean_popup == True:
            popup = PopupPage(self.driver)
            popup.close_popup_ad()

        daily = DailyWeatherPage(self.driver)
        daily.open_daily_item(index_day)
        
        day_weather = DayWeatherPage(self.driver)
        value_day = day_weather.retrieve_day_value()
        if day_weather.have_quater():
            day_weather.open_quater_day(Quater[text_quater].value)
            quater = QuaterWeatherPage(self.driver)
            weather = quater.retrieve_weather()
            day = {"day_%s"%text_quater:value_day}
        else:
            day = {"day":value_day}
            weather = day_weather.retrieve_weather(Quater[text_quater].value)
        home.open_setting()
        settings = SettingsPage(self.driver)
        settings.select_units_item("C")

        ui.go_previous_page()
        if day_weather.have_quater():
            validate = quater.validate_temperatureC(weather['temperature'].replace("F",""))
        else:
            validate = day_weather.validate_temperatureC_day(weather['temperature'].replace("F",""), Quater[text_quater].value)
        weather["validate"] = validate
        return {**day, **weather}

