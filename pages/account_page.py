from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def click_logout(self):
        self.close_modal_if_present()
        self.click_element((By.XPATH, LOGOUT_BUTTON))
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/login")
        )

    def click_order_history(self):
        self.click_element((By.XPATH, ORDER_HISTORY_LINK))
        