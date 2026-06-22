from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.order_page import OrderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data.user_data import LOGIN_EMAIL, LOGIN_PASSWORD
from data.constants import BASE_URL


class TestOrder:

    def test_order_modal_opens(self, driver):
        order_page = OrderPage(driver)
        order_page.open()

        order_page.click_order()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(order_page.modal_order)
        )

        assert order_page.is_modal_displayed()

    def test_counters_increase(self, driver):
        driver.get(f"{BASE_URL}/feed")
        order_page = OrderPage(driver)
        order_page.wait_for_orders()

        total_before = order_page.get_total_counter()
        today_before = order_page.get_today_counter()

        driver.get(f"{BASE_URL}/login")
        login_page = LoginPage(driver)
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)

        login_button = driver.find_element(*login_page.login_button)
        driver.execute_script("arguments[0].click();", login_button)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'BurgerConstructor')]"))
        )

        main_page = MainPage(driver)
        main_page.drag_ingredient_to_basket()
        main_page.click_order_button()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'Modal_modal')]"))
        )

        close_button = driver.find_element(*main_page.modal_close)
        driver.execute_script("arguments[0].click();", close_button)

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]"))
        )

        main_page.click_feed()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )

        order_page.wait_for_orders()

        total_after = order_page.get_total_counter()
        today_after = order_page.get_today_counter()

        assert int(total_after) > int(total_before)
        assert int(today_after) > int(today_before)

    def test_order_appears_in_work(self, driver):
        driver.get(f"{BASE_URL}/login")
        login_page = LoginPage(driver)
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)

        login_button = driver.find_element(*login_page.login_button)
        driver.execute_script("arguments[0].click();", login_button)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'BurgerConstructor')]"))
        )

        main_page = MainPage(driver)
        main_page.drag_ingredient_to_basket()
        main_page.click_order_button()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'Modal_modal')]"))
        )

        close_button = driver.find_element(*main_page.modal_close)
        driver.execute_script("arguments[0].click();", close_button)

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]"))
        )

        main_page.click_feed()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )

        order_page = OrderPage(driver)
        order_page.wait_for_orders()

        work_orders = driver.find_elements(By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')][1]/li")
        assert len(work_orders) > 0

    def test_user_order_in_feed(self, driver):
        driver.get(f"{BASE_URL}/login")
        login_page = LoginPage(driver)
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)

        login_button = driver.find_element(*login_page.login_button)
        driver.execute_script("arguments[0].click();", login_button)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'BurgerConstructor')]"))
        )

        main_page = MainPage(driver)
        main_page.drag_ingredient_to_basket()
        main_page.click_order_button()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'Modal_modal')]"))
        )

        close_button = driver.find_element(*main_page.modal_close)
        driver.execute_script("arguments[0].click();", close_button)

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]"))
        )

        main_page.click_feed()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )

        order_page = OrderPage(driver)
        order_page.wait_for_orders()

        user_orders = driver.find_elements(By.XPATH, "//p[contains(@class, 'text_type_digits-default') and starts-with(text(), '#')]")
        assert len(user_orders) > 0
        