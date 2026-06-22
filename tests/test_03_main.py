from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data.constants import BASE_URL
from data.user_data import LOGIN_EMAIL, LOGIN_PASSWORD


class TestMain:

    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_feed()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )

        main_page.click_constructor()
        WebDriverWait(driver, 10).until(
            EC.url_contains(BASE_URL)
        )

        assert driver.current_url == BASE_URL + "/"

    def test_click_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_feed()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )

        assert "/feed" in driver.current_url

    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_ingredient()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(main_page.modal_title)
        )

        assert main_page.get_modal_title() == "Детали ингредиента"

    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_ingredient()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(main_page.modal_title)
        )

        main_page.close_modal()

        assert main_page.is_modal_closed()

    def test_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        initial_value = main_page.get_counter_value()

        main_page.drag_ingredient_to_basket()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'counter_counter__num')]"))
        )

        new_value = main_page.get_counter_value()

        assert int(new_value) > int(initial_value)

    def test_create_order(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)
        login_page.click_login()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'BurgerConstructor')]"))
        )

        main_page = MainPage(driver)
        main_page.drag_ingredient_to_basket()
        main_page.click_order_button()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'Modal_modal')]"))
        )

        assert driver.find_element(By.XPATH, "//*[contains(@class, 'Modal_modal')]").is_displayed()
        