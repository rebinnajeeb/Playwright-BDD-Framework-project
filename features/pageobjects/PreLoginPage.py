import logging
import allure
from playwright.sync_api import expect
from features.pageobjects.BasePage import BasePage
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class PreLoginPage(BasePage):

    def open(self, url):
        self.navigate_to(url)

    def accept_cookies(self):
        with allure.step("Accept cookies if shown"):
            cookie_btn = self.page.locator("#onetrust-accept-btn-handler")
            try:
                expect(cookie_btn).to_be_visible(timeout=5000)
                cookie_btn.click()
                expect(cookie_btn).to_be_hidden(timeout=3000)
                log.logger.info("Cookie banner accepted")
            except AssertionError:
                log.logger.info("Cookie banner not visible")

    def go_to_login(self):
        self.click("a.btn.btn-primary.CardBlock-cta[href*='SciProxyCaller']")

    def set_username(self, username):
        with allure.step("Enter username"):
            self.page.locator("//input[@id='j_username']").fill(username)
            log.logger.info("Username entered")

    def click_continue(self):
        self.click("//button[contains(., 'Continue')]")

    def set_password(self, password):
        with allure.step("Enter password"):
            self.page.locator("//input[@id='j_password']").fill(password)
            log.logger.info("Password entered")

    def submit_login(self):
        with allure.step("Click Log On"):
            self.page.get_by_role("button", name="Log On").click()
            log.logger.info("Clicked Log On")

    def is_logged_in(self):
        with allure.step("Check if logged in"):
            self.page.wait_for_url("**/partner-portal/**", timeout=30000)
            try:
                expect(
                    self.page.get_by_text("Willkommen im AEG Partner Portal - Schön, dass Sie da sind")
                ).to_be_visible(timeout=10000)
                log.logger.info("Welcome text visible - login successful")
                return True
            except AssertionError:
                log.logger.info("Welcome text not visible - login failed")
                return False

    def is_error_shown(self):
        with allure.step("Check if login error message is shown"):
            try:
                expect(
                    self.page.locator("#globalMessages .fn-message-strip__text")
                ).to_be_visible(timeout=10000)
                log.logger.info("Error message visible - invalid login confirmed")
                return True
            except AssertionError:
                log.logger.info("Error message not found")
                return False
