from behave import step
from lib.pages import AdminLayout, AdminMessagesPage
from time import sleep


@step("Admin sees a new message in the mailbox")
def step_impl(context):
    page = AdminLayout(context)
    page.inbox_tab.click()
    page = AdminMessagesPage(context)
    page.set_format_variable(context.message.name)
    page.message_by_name.click()


@step("Admin sees the message content")
def step_impl(context):
    page = AdminMessagesPage(context)
    sleep(1)  # workaround for dynamically loaded text nodes - could not target them via selenium waits
    assert context.message.name in page.message_author_field.text
    assert context.message.email in page.message_email_field.text
    assert context.message.subject in page.message_subject_field.text
    assert context.message.text in page.message_text_field.text
    assert context.message.phone in page.message_phone_field.text
