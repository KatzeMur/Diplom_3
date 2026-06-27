from selenium.webdriver.common.by import By
from locators.locators import (
    ACCOUNT_LINK,
    ORDER_HISTORY_LINK,
    LOGOUT_BUTTON
)
from pages.base_page import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/account"

    def click_account_link(self):
        self.scroll_to_element((By.XPATH, ACCOUNT_LINK))
        self.click_element((By.XPATH, ACCOUNT_LINK))

    def is_on_account_page(self):
        return "/account" in self.get_current_url()

    def is_on_order_history_page(self):
        return "/account/order-history" in self.get_current_url()

    def click_logout(self):
        self.close_modal_if_present()
        self.click_element((By.XPATH, LOGOUT_BUTTON))
        self.wait_for_url_contains("/login")

    def is_on_login_page(self):
        return "/login" in self.get_current_url()

    def click_order_history(self):
        self.click_element((By.XPATH, ORDER_HISTORY_LINK))
        