from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from drivers.browser.base_driver import BaseDriver

class FirefoxDriver(BaseDriver):

    def create_driver(self, headless):
        firefox_options = webdriver.FirefoxOptions()
        
        if headless == "yes":
            firefox_options.add_argument("--headless")
        
        firefox_options.add_argument("start-maximized")
        return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
