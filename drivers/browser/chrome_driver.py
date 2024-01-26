from drivers.browser.base_driver import BaseDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class ChromeDriver(BaseDriver):

    def create_driver(self, headless):
        chrome_options = webdriver.ChromeOptions()
        
        if headless == "yes":
            chrome_options.add_argument("--headless")

        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--incognito")
        return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)