from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from lib.pages.base_page_object import BasePage
from datetime import datetime


class MainPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.site_url = "/#"
        self.locator_dictionary.update(self.page_locator_dictionary)

    def start_booking(self, booking):
        self.find_element("room_button_by_room_number", frmt=booking.room).click()

    page_locator_dictionary = {
        "room_button_by_room_number": (By.XPATH, '//div/img[@alt="Preview image of room{}"]/../../div/button'),
        "brand_description_field": (By.XPATH, '//div[@class="row hotel-description"]//p'),
        "brand_logo": (By.CSS_SELECTOR, '.hotel-logoUrl'),
        "brand_contact_details_field": (By.XPATH, '//div[@class="row contact"]/div[@class="col-sm-5" and not(form)]'),
        "contact_form_name_field": (By.CSS_SELECTOR, '#name'),
        "contact_form_email_field": (By.CSS_SELECTOR, '#email'),
        "contact_form_phone_field": (By.CSS_SELECTOR, '#phone'),
        "contact_form_subject_field": (By.CSS_SELECTOR, '#subject'),
        "contact_form_message_field": (By.CSS_SELECTOR, '#description'),
        "contact_form_submit_button": (By.CSS_SELECTOR, '#submitContact'),
        "contact_form_validation_field": (By.CSS_SELECTOR, '.alert.alert-danger'),
        "banner_button": (By.CSS_SELECTOR, 'div[data-target="#collapseBanner"]>button'),
    }


class BookingModal(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.locator_dictionary.update(self.page_locator_dictionary)

    def make_booking(self, booking):
        month_difference = int(booking.start_date[5:7]) - datetime.now().month
        if month_difference < 0:
            month_difference += 12
        for _ in range(month_difference):
            self.find_element("next_button").click()

        start = self.find_element("date_button", frmt=booking.start_date[-2:])
        start_secondary = self.find_element("date_secondary_button", frmt=booking.start_date[-2:])
        end = self.find_element("date_button", frmt=booking.end_date[-2:])

        ActionChains(self.browser)\
            .click_and_hold(start)\
            .move_to_element(start_secondary)\
            .move_to_element(end)\
            .release(end)\
            .perform()

    page_locator_dictionary = {
        "booking_form_first_name_field": (By.CSS_SELECTOR, '[name="firstname"]'),
        "booking_form_last_name_field": (By.CSS_SELECTOR, '[name="lastname"]'),
        "booking_form_email_field": (By.CSS_SELECTOR, '[name="email"]'),
        "booking_form_phone_field": (By.CSS_SELECTOR, '[name="phone"]'),
        "booking_form_submit_button": (By.CSS_SELECTOR, '.btn.btn-outline-primary.float-right.book-room'),
        "booking_form_cancel_button": (By.CSS_SELECTOR, '.btn.btn-outline-danger.float-right.book-room'),
        "next_button": (By.XPATH, '//button[contains(text(), "Next")]'),
        "date_button": (By.XPATH, '//button[@role="cell" and contains(text(), "{}") and not(@class="rbc-off-range")]'),
        "date_secondary_button": (By.XPATH, '//button[@role="cell" and contains(text(), "{}") and not(@class="rbc-off-range")]/parent::div'),
        "booking_form_validation_field": (By.CSS_SELECTOR, '.alert.alert-danger'),
    }


class BookingConfirmationModal(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.locator_dictionary.update(self.page_locator_dictionary)

    page_locator_dictionary = {
        "title_field": (By.CSS_SELECTOR, '.ReactModalPortal h3'),
        "text_field": (By.CSS_SELECTOR, '.ReactModalPortal h3 ~ p'),
        "date_field": (By.CSS_SELECTOR, '.ReactModalPortal p ~ p'),
        "close_button": (By.CSS_SELECTOR, '.ReactModalPortal button')
    }