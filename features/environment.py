import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright

from Utilities import configReader


def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    browser_type = configReader.readConfig("basic info", "browser")

    if browser_type.lower() == "chrome":
        context.browser = context.playwright.chromium.launch(headless=True, channel="chrome")
    elif browser_type.lower() == "firefox":
        context.browser = context.playwright.firefox.launch(headless=False)
    elif browser_type.lower() == "edge":
        context.browser = context.playwright.chromium.launch(headless=False, channel="msedge")
    elif browser_type.lower() == "webkit":
        context.browser = context.playwright.webkit.launch(headless=False)
    else:
        raise Exception(f"Unsupported browser: {browser_type}")

    context.page = context.browser.new_page()
    context.page.set_default_timeout(30000)


def after_scenario(context, scenario):
    if hasattr(context, "page"):
        context.page.close()
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()


def after_step(context, step):
    # Attach a screenshot to the Allure report whenever a step fails.
    if step.status == "failed" and hasattr(context, "page"):
        screenshot = context.page.screenshot()
        allure.attach(screenshot, name="screenshot", attachment_type=AttachmentType.PNG)
