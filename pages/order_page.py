from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import ORDER_IN_FEED, MODAL_ORDER, ORDER_MODAL_CLOSE, TOTAL_COUNTER, TODAY_COUNTER
from data.constants import BASE_URL


class OrderPage:
    """Page Object для страницы Лента заказов"""
    
    def __init__(self, driver):
        self.driver = driver
        self.url = f"{BASE_URL}/feed"
    
    order_in_feed = (By.XPATH, ORDER_IN_FEED)
    modal_order = (By.XPATH, MODAL_ORDER)
    modal_close = (By.XPATH, ORDER_MODAL_CLOSE)
    total_counter = (By.XPATH, TOTAL_COUNTER)
    today_counter = (By.XPATH, TODAY_COUNTER)
    
    def open(self):
        self.driver.get(self.url)
    
    def wait_for_orders(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.order_in_feed)
        )
    
    def click_order(self):
        self.wait_for_orders()
        element = self.driver.find_element(*self.order_in_feed)
        self.driver.execute_script("arguments[0].click();", element)
    
    def is_modal_displayed(self):
        return self.driver.find_element(*self.modal_order).is_displayed()
    
    def close_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.modal_close)
        )
        self.driver.find_element(*self.modal_close).click()
    
    def get_total_counter(self):
        return self.driver.find_element(*self.total_counter).text
    
    def get_today_counter(self):
        return self.driver.find_element(*self.today_counter).text
    