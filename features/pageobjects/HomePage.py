import logging
import allure
from playwright.sync_api import expect
from features.pageobjects.BasePage import BasePage
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class HomePage(BasePage):

    # ── Logout ────────────────────────────────────────────────────

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
            self.page.wait_for_url("**/pre-login/**", timeout=60000)
            on_prelogin = "pre-login" in self.page.url
            log.logger.info(f"Back on pre-login page: {on_prelogin}")
            return on_prelogin

    # ── Navigation menus ─────────────────────────────────────────

    def click_sales_and_marketing(self):
        with allure.step("Click Sales & Marketing"):
            self.page.locator("//a[@data-binding='NavL1' and contains(normalize-space(),'Marketing')]").click()
            log.logger.info("Clicked Sales & Marketing")

    def is_sales_submenu_visible(self):
        with allure.step("Verify Sales & Marketing submenu visible"):
            expect(self.page.locator("//div[contains(@class,'NavSite-l2') and contains(@class,'is-visible')]")).to_be_visible(timeout=50000)
            log.logger.info("Sales & Marketing submenu visible")

    def click_orders(self):
        with allure.step("Click Orders"):
            self.page.locator("//a[@data-binding='NavL1' and contains(normalize-space(),'Bestellungen')]").click()
            log.logger.info("Clicked Orders")

    def is_orders_submenu_visible(self):
        with allure.step("Verify Orders submenu visible"):
            expect(self.page.locator("//div[contains(@class,'NavSite-l2') and contains(@class,'is-visible')]")).to_be_visible(timeout=30000)
            log.logger.info("Orders submenu visible")

    def click_training(self):
        with allure.step("Click Training"):
            self.page.locator("//a[@data-binding='NavL1' and contains(normalize-space(),'Trainings')]").click()
            log.logger.info("Clicked Training")

    def is_training_submenu_visible(self):
        with allure.step("Verify Training submenu visible"):
            expect(self.page.locator("//div[contains(@class,'NavSite-l2') and contains(@class,'is-visible')]")).to_be_visible(timeout=30000)
            log.logger.info("Training submenu visible")

    def click_tools_and_services(self):
        with allure.step("Click Tools & Services"):
            self.page.locator("//a[@data-binding='NavL1' and contains(normalize-space(),'Tools')]").click()
            log.logger.info("Clicked Tools & Services")

    def is_tools_submenu_visible(self):
        with allure.step("Verify Tools & Services submenu visible"):
            expect(self.page.locator("//div[contains(@class,'NavSite-l2') and contains(@class,'is-visible')]")).to_be_visible(timeout=30000)
            log.logger.info("Tools & Services submenu visible")

    # ── Footer ───────────────────────────────────────────────────

    def scroll_to_footer(self):
        with allure.step("Scroll to footer"):
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            log.logger.info("Scrolled to footer")

    def click_first_footer_heading(self):
        with allure.step("Click first footer heading link"):
            self.page.locator("(//div[@class='site-footer-column'])//h2[1]//a").first.click()
            log.logger.info("Clicked first footer heading")

    def click_third_footer_consumer_link(self):
        with allure.step("Click third footer consumer link"):
            self.page.locator("//*[contains(@href,'/consumer-links/')]").first.click()
            log.logger.info("Clicked third footer consumer link")

    def is_url_containing(self, expected_part):
        with allure.step(f"Verify URL contains: {expected_part}"):
            self.page.wait_for_url(f"**{expected_part}**", timeout=15000)
            result = expected_part in self.page.url
            log.logger.info(f"URL contains '{expected_part}': {result}")
            return result
