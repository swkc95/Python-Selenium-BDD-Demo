from selenium.webdriver.common.by import By
from lib.pages.base_page_object import BasePage


class AdminLoginPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.site_url = "/#/admin"
        self.locator_dictionary.update(self.page_locator_dictionary)

    page_locator_dictionary = {
        "banner_button": (By.CSS_SELECTOR, 'div[data-target="#collapseBanner"]>button'),
        "username_field": (By.CSS_SELECTOR, '#username'),
        "username_validation_border": (By.CSS_SELECTOR, '#username[style="border: 1px solid red;"]'),
        "password_field": (By.CSS_SELECTOR, '#password'),
        "password_validation_border": (By.CSS_SELECTOR, '#password[style="border: 1px solid red;"]'),
        "login_button": (By.CSS_SELECTOR, '#doLogin')
    }
