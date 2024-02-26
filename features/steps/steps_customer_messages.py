from behave import step
from lib.pages import MainPage
import lib.misc.variables as v
from lib.classes.class_message import Message


@step("Customer scrolls down to the contact form to send a message")
def step_impl(context):
    context.message = Message(context.customer)
    page = MainPage(context)
    page.scroll_into(page.contact_form_name_field)


@step("Customer provides a valid name in the contact form")
def step_impl(context):
    page = MainPage(context)
    page.contact_form_name_field.send_keys(context.message.name)


@step("Customer provides a valid email in the contact form")
def step_impl(context):
    page = MainPage(context)
    page.contact_form_email_field.send_keys(context.message.email)


@step("Customer provides a valid phone number in the contact form")
def step_impl(context):
    page = MainPage(context)
    page.contact_form_phone_field.send_keys(context.message.phone)


@step("Customer provides a valid subject in the contact form")
def step_impl(context):
    page = MainPage(context)
    page.contact_form_subject_field.send_keys(context.message.subject)


@step("Customer provides a valid message in the contact form")
def step_impl(context):
    page = MainPage(context)
    page.contact_form_message_field.send_keys(context.message.text)


@step("Customer sends a message through the contact form")
def step_impl(context):
    page = MainPage(context)
    page.contact_form_submit_button.click()


@step("Customer provides an invalid email in the contact form")
def step_impl(context):
    page = MainPage(context)
    page.contact_form_email_field.send_keys(v.INVALID_EMAIL)


@step("Customer sees a message about invalid mail formatting")
def step_impl(context):
    page = MainPage(context)
    assert context.strings.VALIDATION_CONTACT_FORM_EMAIL_INVALID in page.contact_form_validation_field.text
