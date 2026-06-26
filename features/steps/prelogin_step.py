from behave import given, when, then
from playwright.sync_api import expect

from Utilities import configReader
from Utilities.ExcelReader import ExcelReader
from features.pageobjects.PreLoginPage import PreLoginPage


@given(u'I navigate to the AEG B2B pre-login page')
def step_impl(context):
    context.prelogin = PreLoginPage(context.page)

    market = configReader.readConfig("basic info", "market")
    url = configReader.readConfig("urls", market)
    context.prelogin.open(url)  # Navigate HERE


@then(u'the current url should contain "{fragment}"')
def step_impl(context, fragment):
    current_url = context.page.url
    assert fragment in current_url, f"Expected '{fragment}' in URL but got '{current_url}'"
    expect(context.page.get_by_role("button", name="Alle Cookies akzeptieren")).to_be_visible()

@when(u'I accept cookies if shown')
def step_impl(context):
    context.prelogin.accept_cookies()


@when(u'I go to the login form')
def step_impl(context):
    context.prelogin.go_to_login()


#@when(u'I enter the username as "{username}"')
#def step_impl(context, username):
#    context.prelogin.set_username(username)


#@when(u'I enter the password as "{password}"')
#def step_impl(context, password):
#    context.prelogin.set_password(password)


@when(u'I enter username from Excel')
def step_impl(context):
    market = configReader.readConfig("basic info", "market")
    login_data = ExcelReader.read_data("LoginData.xlsx", sheet_name=market)

    if login_data:
        username = login_data[0]['username']
        context.prelogin.set_username(username)
    else:
        raise Exception(f"No login credentials found for market '{market}'")


@when(u'I click continue')
def step_impl(context):
    context.prelogin.click_continue()

@when(u'I enter password from Excel')
def step_impl(context):
    market = configReader.readConfig("basic info", "market")
    login_data = ExcelReader.read_data("LoginData.xlsx", sheet_name=market)

    if login_data:
        password = login_data[0]['password']
        context.prelogin.set_password(password)
    else:
        raise Exception(f"No login credentials found for market '{market}'")

@when(u'I submit the login form')
def step_impl(context):
    context.prelogin.submit_login()


@then(u'I should be logged in')
def step_impl(context):
    assert context.prelogin.is_logged_in(), "Login did not succeed"


@when(u'I enter invalid username')
def step_impl(context):
    context.prelogin.set_username("invalid.user@aeg-test.com")


@when(u'I enter invalid password')
def step_impl(context):
    context.prelogin.set_password("WrongPassword123!")


@then(u'I should see a login error')
def step_impl(context):
    assert context.prelogin.is_error_shown(), "Expected login error message but none was shown"
