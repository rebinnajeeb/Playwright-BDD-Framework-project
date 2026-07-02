from behave import when, then
from features.pageobjects.HomePage import HomePage


# ── Navigation menus ─────────────────────────────────────────

@when(u'I click on Sales and Marketing')
def step_impl(context):
    context.home.click_sales_and_marketing()


@then(u'the Sales and Marketing submenu should be visible')
def step_impl(context):
    context.home.is_sales_submenu_visible()


@when(u'I click on Orders')
def step_impl(context):
    context.home.click_orders()


@then(u'the Orders submenu should be visible')
def step_impl(context):
    context.home.is_orders_submenu_visible()


@when(u'I click on Training')
def step_impl(context):
    context.home.click_training()


@then(u'the Training submenu should be visible')
def step_impl(context):
    context.home.is_training_submenu_visible()


@when(u'I click on Tools and Services')
def step_impl(context):
    context.home.click_tools_and_services()


@then(u'the Tools and Services submenu should be visible')
def step_impl(context):
    context.home.is_tools_submenu_visible()


# ── Footer ───────────────────────────────────────────────────

@when(u'I scroll to the footer')
def step_impl(context):
    context.home.scroll_to_footer()


@when(u'I click on the first footer heading link')
def step_impl(context):
    context.home.click_first_footer_heading()


@then(u'the URL should contain sales-and-marketing')
def step_impl(context):
    assert context.home.is_url_containing("/sales-and-marketing/"), "URL did not contain /sales-and-marketing/"


@when(u'I click on the third footer consumer link')
def step_impl(context):
    context.home.click_third_footer_consumer_link()


@then(u'the URL should contain consumer-links')
def step_impl(context):
    assert context.home.is_url_containing("/consumer-links/"), "URL did not contain /consumer-links/"
