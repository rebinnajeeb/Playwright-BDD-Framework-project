from behave import given, when, then

from features.pageobjects.HomePage import HomePage


@given(u'I am on the home page')
def step_impl(context):
    context.home = HomePage(context.page)


@when(u'I open the profile dropdown')
def step_impl(context):
    context.home.open_profile_dropdown()


@when(u'I click logout')
def step_impl(context):
    context.home.click_logout()


@then(u'I should be back on the pre-login page')
def step_impl(context):
    assert context.home.is_on_prelogin(), "User did not return to pre-login page after logout"
