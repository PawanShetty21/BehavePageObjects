import logging

from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage
from utilities.Logger_utils import Logger


class LoginPage(BasePage):
    log = Logger.custom_logger(loglevel=logging.WARNING)

    def __init__(self, driver):
        self.driver = driver

    # Locators
    USERNAME_FIELD_ID = "Email"
    PASSWORD_FIELD_ID = "Password"
    LOGIN_BUTTON_XPATH = "//button[@type='submit']"

    # Locator return functions
    def get_username_field(self):
        return self.wait_until_element_is_clickable(By.ID, self.USERNAME_FIELD_ID)

    def get_password_field(self):
        return self.wait_until_element_is_clickable(By.ID, self.PASSWORD_FIELD_ID)

    def get_login_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LOGIN_BUTTON_XPATH)

    # Operating functions
    def enter_username(self, username):
        self.get_username_field().clear()
        self.get_username_field().send_keys(username)
        self.log.info("Entered Username : ")
        self.log.warning("Entered Username")

    def enter_password(self, password):
        self.get_password_field().clear()
        self.get_password_field().send_keys(password)
        self.log.info("Entered Password")

    def click_login_button(self):
        self.get_login_button().click()
        self.log.info("Clicked on login button")
        assert 2 + 2 == 5