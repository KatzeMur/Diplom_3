from pages.order_page import OrderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data.user_data import LOGIN_EMAIL, LOGIN_PASSWORD


class TestOrder:

    def test_order_modal_opens(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.click_order()
        assert order_page.is_modal_displayed() is True

    def test_counters_increase(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.wait_for_orders()

        total_before = order_page.get_total_counter()
        today_before = order_page.get_today_counter()

        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)
        login_page.click_login()

        main_page = MainPage(driver)
        main_page.drag_ingredient_to_basket()
        main_page.click_order_button()
        main_page.close_modal()

        order_page.open()
        order_page.wait_for_orders()

        total_after = order_page.get_total_counter()
        today_after = order_page.get_today_counter()

        assert int(total_after) > int(total_before)
        assert int(today_after) > int(today_before)

    def test_order_appears_in_work(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)
        login_page.click_login()

        main_page = MainPage(driver)
        main_page.drag_ingredient_to_basket()
        main_page.click_order_button()
        main_page.close_modal()

        order_page = OrderPage(driver)
        order_page.open()
        order_page.wait_for_orders()

        work_orders = order_page.get_work_orders_count()
        assert work_orders > 0

    def test_user_order_in_feed(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)
        login_page.click_login()

        main_page = MainPage(driver)
        main_page.drag_ingredient_to_basket()
        main_page.click_order_button()
        main_page.close_modal()

        order_page = OrderPage(driver)
        order_page.open()
        order_page.wait_for_orders()

        user_orders = order_page.get_user_orders_count()
        assert user_orders > 0
        