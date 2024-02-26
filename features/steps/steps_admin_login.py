from behave import step
from lib.pages import AdminLoginPage, AdminLayout
import lib.misc.variables as v


@step("Admin is on the log in page")
def step_impl(context):
    page = AdminLoginPage(context)
    page.visit()
    if context.info_banner_flag:
        page.banner_button.click()
        context.info_banner_flag = False


@step("Admin provides a valid username")
def step_impl(context):
    page = AdminLoginPage(context)
    page.visit()
    page.username_field.send_keys(v.ADMIN_USERNAME)


@step("Admin provides a valid password")
def step_impl(context):
    page = AdminLoginPage(context)
    page.password_field.send_keys(v.ADMIN_PASSWORD)


@step("Admin provides an invalid password")
def step_impl(context):
    page = AdminLoginPage(context)
    page.password_field.send_keys(v.ADMIN_INVALID_PASSWORD)


@step("Admin submits the log in request")
def step_impl(context):
    page = AdminLoginPage(context)
    page.login_button.click()


@step("Admin is logged in")
def step_impl(context):
    page = AdminLayout(context)
    assert page.logout_button


@step("Admin is not logged in")
def step_impl(context):
    page = AdminLoginPage(context)
    assert page.username_field
    assert page.password_field
    assert page.login_button


@step("Admin logs out")
def step_impl(context):
    page = AdminLayout(context)
    page.logout_button.click()
    assert page.username_field
    page.mainpage_tab.click()


@step("Admin sees validation markings in the log in form")
def step_impl(context):
    page = AdminLoginPage(context)
    assert page.username_validation_border
    assert page.password_validation_border
