from selenium.webdriver.common.by import By
from locators.locators import (
    RECOVERY_LINK,
    EMAIL_INPUT,
    RECOVERY_BUTTON,
    PASSWORD_TOGGLE_BUTTON,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    BURGER_CONSTRUCTOR
)
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/login"

    def click_recovery_link(self):
        self.click_element((By.XPATH, RECOVERY_LINK))

    def is_recovery_link_displayed(self):
        return self.is_element_displayed((By.XPATH, RECOVERY_LINK))

    def enter_email(self, email):
        self.enter_text((By.XPATH, EMAIL_INPUT), email)

    def click_recovery_button(self):
        self.click_element((By.XPATH, RECOVERY_BUTTON))

    def click_password_toggle(self):
        self.click_element((By.XPATH, PASSWORD_TOGGLE_BUTTON))

    def is_password_toggle_displayed(self):
        return self.is_element_displayed((By.XPATH, PASSWORD_TOGGLE_BUTTON))

    def enter_password(self, password):
        self.enter_text((By.XPATH, PASSWORD_INPUT), password)

    def click_login(self):
        self.click_element((By.XPATH, LOGIN_BUTTON))
        self.wait_for_element_visible((By.XPATH, BURGER_CONSTRUCTOR))
        