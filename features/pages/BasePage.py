from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import ConfigReader


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # For wait condition
    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, ConfigReader.readConfig("basic info", "explicit.wait"))
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_until_element_is_visible(self, locator_type, locator):
        wait = WebDriverWait(self.driver, ConfigReader.readConfig("basic info", "explicit.wait"))
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element
