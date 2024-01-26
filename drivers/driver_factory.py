from importlib import import_module
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:
    driver_factory = None
    
    @classmethod
    def get_instance(cls):
        if cls.driver_factory is None:
            cls.driver_factory = DriverFactory()
        return cls.driver_factory
        
    def start_driver(self, browser, headless):
        modulePath = "%s.%s_driver" % ("drivers.browser", browser)
        className = "%sDriver" % browser.capitalize()
        module = import_module(modulePath)
        driverClass = getattr(module, className)
        driver = driverClass().create_driver(headless)
        return driver
