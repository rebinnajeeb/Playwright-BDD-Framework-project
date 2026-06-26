import logging
import allure
from features.pageobjects.BasePage import BasePage
from Utilities.configReader import readConfig
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class PreLoginPage(BasePage):
    SECTION = "prelogin"

    def open(self, url):
        self.navigate_to(url)

    def accept_cookies(self):
        with allure.step("Accept cookies if shown"):
            if self.is_visible(readConfig(self.SECTION, "cookie_btn")):
                self.click(readConfig(self.SECTION, "cookie_btn"))
                log.logger.info("Cookie banner accepted")
            else:
                log.logger.info("Cookie banner not visible")

    def go_to_login(self):
        self.click(readConfig(self.SECTION, "login_link"))

    def set_username(self, username):
        self.fill(readConfig(self.SECTION, "username_field"), username)

    def click_continue(self):
        self.click(readConfig(self.SECTION, "continue_btn"))

    def set_password(self, password):
        self.fill(readConfig(self.SECTION, "password_field"), password)

    def submit_login(self):
        self.click_by_role("button", "Log On")

    def is_logged_in(self):
        with allure.step("Check if logged in"):
            self.wait_for_url("**/partner-portal/**", timeout=30000)
            try:
                self.wait_for_visible(readConfig(self.SECTION, "welcome_text"), timeout=10000)
                log.logger.info("Welcome text visible - login successful")
                return True
            except AssertionError:
                log.logger.info("Welcome text not visible - login failed")
                return False

    def is_error_shown(self):
        with allure.step("Check if login error message is shown"):
            try:
                self.wait_for_visible(readConfig(self.SECTION, "error_msg"), timeout=10000)
                log.logger.info("Error message visible - invalid login confirmed")
                return True
            except AssertionError:
                log.logger.info("Error message not found")
                return False
