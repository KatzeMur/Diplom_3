from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import (
    RECOVERY_LINK,
    EMAIL_INPUT,
    RECOVERY_BUTTON,
    PASSWORD_TOGGLE_BUTTON,
    PASSWORD_INPUT,
    LOGIN_BUTTON
)
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/login"

    def click_recovery_link(self):
        self.click_element((By.XPATH, RECOVERY_LINK))

    def enter_email(self, email):
        self.enter_text((By.XPATH, EMAIL_INPUT), email)

    def click_recovery_button(self):
        self.click_element((By.XPATH, RECOVERY_BUTTON))

    def click_password_toggle(self):
        self.click_element((By.XPATH, PASSWORD_TOGGLE_BUTTON))

    def enter_password(self, password):
        self.enter_text((By.XPATH, PASSWORD_INPUT), password)

    def click_login(self):
        self.click_element((By.XPATH, LOGIN_BUTTON))
        # Ждем появления маркера успешного входа (конструктора)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'BurgerConstructor')]"))
        )
        