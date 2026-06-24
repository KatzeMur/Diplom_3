from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from locators.locators import RECOVERY_LINK, PASSWORD_TOGGLE_BUTTON
from data.constants import BASE_URL


class TestRecoveryPassword:

    def test_recovery_link_exists(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        assert login_page.is_element_displayed((By.XPATH, RECOVERY_LINK)) is True

    def test_recovery_password_flow(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_recovery_link()
        test_email = "test@example.com"
        login_page.enter_email(test_email)
        login_page.click_recovery_button()

    def test_password_toggle_button(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_password_toggle()
        assert login_page.is_element_displayed((By.XPATH, PASSWORD_TOGGLE_BUTTON)) is True
        