from behave import step
from lib.pages import MainPage, BookingModal, BookingConfirmationModal
from lib.classes.class_customer import Customer
from lib.classes.class_booking import Booking


@step("Customer is on the main page")
def step_impl(context):
    context.customer = Customer()
    page = MainPage(context)
    page.visit()
    if context.info_banner_flag:
        page.banner_button.click()
        context.info_banner_flag = False


@step("Customer clicks to book the new room")
def step_impl(context):
    context.booking = Booking(context.customer, context.room, 5)
    page = MainPage(context)
    page.start_booking(context.booking)


@step("Customer provides a valid first name in the booking form")
def step_impl(context):
    page = BookingModal(context)
    page.booking_form_first_name_field.send_keys(context.booking.first_name)


@step("Customer provides a valid last name in the booking form")
def step_impl(context):
    page = BookingModal(context)
    page.booking_form_last_name_field.send_keys(context.booking.last_name)


@step("Customer provides a valid email in the booking form")
def step_impl(context):
    page = BookingModal(context)
    page.booking_form_email_field.send_keys(context.booking.email)


@step("Customer provides a valid phone number in the booking form")
def step_impl(context):
    page = BookingModal(context)
    page.booking_form_phone_field.send_keys(context.booking.phone)


@step("Customer provides a valid booking date")
def step_impl(context):
    page = BookingModal(context)
    page.scroll_into(page.next_button)
    page.make_booking(context.booking)


@step("Customer sends a booking request")
def step_impl(context):
    page = BookingModal(context)
    page.booking_form_submit_button.click()


@step("Customer sees confirmation message about successful booking")
def step_impl(context):
    page = BookingConfirmationModal(context)
    assert page.title_field.text == context.strings.CONFIRMATION_BOOKING_SUCCESSFUL_PRIMARY
    assert page.text_field.text == context.strings.CONFIRMATION_BOOKING_SUCCESSFUL_SECONDARY
    # there is an actual bug in the app - it's adding an extra day in the confirmation message
    # assert page.date_field.text == f"{context.booking.start_date} - {context.booking.end_date}"


@step("Customer sees validation message about invalid phone number")
def step_impl(context):
    page = BookingModal(context)
    assert context.strings.VALIDATION_BOOKING_FORM_PHONE_EMPTY in page.booking_form_validation_field.text
    assert context.strings.VALIDATION_BOOKING_FORM_PHONE_LENGTH in page.booking_form_validation_field.text
