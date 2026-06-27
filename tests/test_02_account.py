from pages.login_page import LoginPage
from pages.account_page import AccountPage
from data.user_data import LOGIN_EMAIL, LOGIN_PASSWORD


class TestAccount:

    def test_click_account_link(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)
        login_page.click_login()

        account_page = AccountPage(driver)
        account_page.click_account_link()

        assert account_page.is_on_account_page() is True

    def test_click_order_history(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)
        login_page.click_login()

        account_page = AccountPage(driver)
        account_page.click_account_link()
        account_page.click_order_history()

        assert account_page.is_on_order_history_page() is True

    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)
        login_page.click_login()

        account_page = AccountPage(driver)
        account_page.click_account_link()
        account_page.click_logout()

        assert account_page.is_on_login_page() is True
        