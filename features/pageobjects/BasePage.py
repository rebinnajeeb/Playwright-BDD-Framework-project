import logging
import allure
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate_to(self, url):
        with allure.step(f"Navigate to {url}"):
            self.page.goto(url, timeout=70000)
            log.logger.info(f"Navigated to {url}")

    def click(self, selector):
        with allure.step(f"Click {selector}"):
            self.page.locator(selector).click()
            log.logger.info(f"Clicked {selector}")
