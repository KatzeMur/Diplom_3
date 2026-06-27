from pages.login_page import LoginPage
from data.constants import BASE_URL


class TestRecoveryPassword:

    def test_recovery_link_exists(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        assert login_page.is_recovery_link_displayed() is True

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
        assert login_page.is_password_toggle_displayed() is True
        