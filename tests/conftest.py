import allure
import pytest
from allure_commons.types import AttachmentType
from drivers.driver_factory import DriverFactory

@pytest.fixture()
def setup(request):
    driver_name = request.config.getoption("--driver")
    headless = request.config.getoption("--headless")
    driver = DriverFactory.get_instance().start_driver(driver_name, headless)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome",
                     help='Driver to use. Valid options: chrome, firefox')
    parser.addoption("--headless", action="store", default="no",
                     help='Headless is an option to run selenium with launched browser or not')