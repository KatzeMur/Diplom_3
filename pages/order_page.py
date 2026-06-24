from selenium.webdriver.common.by import By
from locators.locators import (
    ORDER_IN_FEED, 
    MODAL_ORDER, 
    ORDER_MODAL_CLOSE, 
    TOTAL_COUNTER, 
    TODAY_COUNTER
)
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/feed"

    def wait_for_orders(self):
        self.find_element((By.XPATH, ORDER_IN_FEED))

    def click_order(self):
        self.wait_for_orders()
        self.click_element((By.XPATH, ORDER_IN_FEED))

    def is_modal_displayed(self):
        return self.is_element_displayed((By.XPATH, MODAL_ORDER))

    def close_modal(self):
        self.click_element((By.XPATH, ORDER_MODAL_CLOSE))

    def get_total_counter(self):
        return self.get_text((By.XPATH, TOTAL_COUNTER))

    def get_today_counter(self):
        return self.get_text((By.XPATH, TODAY_COUNTER))

    def get_work_orders_count(self):
        return len(self.driver.find_elements(By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')][1]/li"))

    def get_user_orders_count(self):
        return len(self.driver.find_elements(By.XPATH, "//p[contains(@class, 'text_type_digits-default') and starts-with(text(), '#')]"))
    