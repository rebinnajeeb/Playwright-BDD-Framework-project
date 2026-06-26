import logging
import allure
from playwright.sync_api import expect
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate_to(self, url):
        with allure.step(f"Navigate to {url}"):
            self.page.goto(url, timeout=60000)
            log.logger.info(f"Navigated to {url}")

    def click(self, selector):
        with allure.step(f"Click {selector}"):
            self.page.locator(selector).click()
            log.logger.info(f"Clicked {selector}")

    def click_by_role(self, role, name):
        with allure.step(f"Click {role} '{name}'"):
            self.page.get_by_role(role, name=name).click()
            log.logger.info(f"Clicked {role} '{name}'")

    def fill(self, selector, value):
        with allure.step(f"Fill {selector}"):
            self.page.locator(selector).fill(value)
            log.logger.info(f"Filled {selector}")

    def hover(self, selector):
        with allure.step(f"Hover {selector}"):
            self.page.locator(selector).hover()
            log.logger.info(f"Hovered {selector}")

    def get_text(self, selector):
        with allure.step(f"Get text of {selector}"):
            text = self.page.locator(selector).inner_text()
            log.logger.info(f"Text of {selector}: {text}")
            return text

    def is_visible(self, selector):
        with allure.step(f"Check visibility of {selector}"):
            visible = self.page.locator(selector).is_visible()
            log.logger.info(f"Visibility of {selector}: {visible}")
            return visible

    def wait_for_visible(self, selector, timeout=10000):
        with allure.step(f"Wait for {selector} to be visible"):
            expect(self.page.locator(selector)).to_be_visible(timeout=timeout)
            log.logger.info(f"Element visible: {selector}")

    def wait_for_url(self, pattern, timeout=30000):
        with allure.step(f"Wait for url {pattern}"):
            self.page.wait_for_url(pattern, timeout=timeout)
            log.logger.info(f"URL matched: {pattern}")

    def get_title(self):
        with allure.step("Get page title"):
            title = self.page.title()
            log.logger.info(f"Page title: {title}")
            return title
