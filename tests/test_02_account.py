from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from data.constants import BASE_URL
from data.user_data import LOGIN_EMAIL, LOGIN_PASSWORD


class TestAccount:

    def test_click_account_link(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)
        login_page.click_login()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'BurgerConstructor')]"))
        )

        account_page = AccountPage(driver)
        account_page.click_account_link()

        assert "/account" in driver.current_url

    def test_click_order_history(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)
        login_page.click_login()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'BurgerConstructor')]"))
        )

        account_page = AccountPage(driver)
        account_page.click_account_link()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//nav[contains(@class, 'Account_nav')]"))
        )

        account_page.click_order_history()

        assert "/account/order-history" in driver.current_url

    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)
        login_page.click_login()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'BurgerConstructor')]"))
        )

        account_page = AccountPage(driver)
        account_page.click_account_link()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//nav[contains(@class, 'Account_nav')]"))
        )

        account_page.click_logout()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        assert "/login" in driver.current_url
