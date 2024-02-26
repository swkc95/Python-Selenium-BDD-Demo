from selenium.webdriver.common.by import By
from lib.pages.base_page_object import BasePage


class AdminLayout(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.site_url = "/#/admin"
        self.locator_dictionary.update(self.page_locator_dictionary)

    page_locator_dictionary = {
        "rooms_tab": (By.CSS_SELECTOR, '[href="#/admin/"]'),
        "report_tab": (By.CSS_SELECTOR, '#reportLink'),
        "branding_tab": (By.CSS_SELECTOR, '#brandingLink'),
        "inbox_tab": (By.CSS_SELECTOR, '.fa.fa-inbox'),
        "logout_button": (By.CSS_SELECTOR, '[href="#/admin"]'),
        "mainpage_tab": (By.CSS_SELECTOR, '[href="#"]')
    }
