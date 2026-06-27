from pages.main_page import MainPage
from pages.login_page import LoginPage
from data.user_data import LOGIN_EMAIL, LOGIN_PASSWORD


class TestMain:

    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_feed()
        main_page.click_constructor()
        assert main_page.is_on_constructor_page() is True

    def test_click_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_feed()
        assert main_page.is_on_feed_page() is True

    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        assert main_page.is_modal_opened() is True

    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        main_page.close_modal()
        assert main_page.is_modal_closed()

    def test_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        initial_value = main_page.get_counter_value()
        main_page.drag_ingredient_to_basket()
        new_value = main_page.get_counter_value()
        assert int(new_value) > int(initial_value)

    def test_create_order(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(LOGIN_EMAIL)
        login_page.enter_password(LOGIN_PASSWORD)
        login_page.click_login()
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_basket()
        main_page.click_order_button()
        assert main_page.is_modal_closed() is True
        