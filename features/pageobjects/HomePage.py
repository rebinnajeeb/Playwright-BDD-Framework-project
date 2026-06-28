import logging
import allure
from features.pageobjects.BasePage import BasePage
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class HomePage(BasePage):

    def open_profile_dropdown(self):
        with allure.step("Open profile dropdown"):
            self.page.get_by_text("Muhammed Najeeb").first.click()
            log.logger.info("Profile dropdown opened")

    def click_logout(self):
        with allure.step("Click logout"):
            self.page.locator("//a[contains(@class,'NavDropdown-list-item-link') and contains(@href,'logout')]").click()
            log.logger.info("Clicked logout")

    def is_on_prelogin(self):
        with allure.step("Verify back on pre-login page"):
            self.page.wait_for_url("**/pre-login/**", timeout=30000)
            on_prelogin = "pre-login" in self.page.url
            log.logger.info(f"Back on pre-login page: {on_prelogin}")
            return on_prelogin
