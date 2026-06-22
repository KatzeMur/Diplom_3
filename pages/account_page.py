from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.locators import (
    ACCOUNT_LINK,
    ORDER_HISTORY_LINK,
    LOGOUT_BUTTON
)
from data.constants import BASE_URL


class AccountPage:
    """Page Object для личного кабинета"""
    
    def __init__(self, driver):
        self.driver = driver
        self.url = f"{BASE_URL}/account"
    
    account_link = (By.XPATH, ACCOUNT_LINK)
    order_history_link = (By.XPATH, ORDER_HISTORY_LINK)
    logout_button = (By.XPATH, LOGOUT_BUTTON)
    modal_overlay = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    modal_close = (By.XPATH, "//button[contains(@class, 'Modal_modal_close')]")
    
    def open(self):
        self.driver.get(self.url)
    
    def wait_for_account_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.account_link)
        )
    
    def click_account_link(self):
        self.wait_for_account_link()
        element = self.driver.find_element(*self.account_link)
        self.driver.execute_script("arguments[0].click();", element)
    
    def close_modal_if_present(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.modal_overlay)
            )
            self.driver.find_element(*self.modal_close).click()
        except TimeoutException:
            pass
    
    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//nav[contains(@class, 'Account_nav')]"))
        )
        self.close_modal_if_present()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_button)
        )
        element = self.driver.find_element(*self.logout_button)
        self.driver.execute_script("arguments[0].click();", element)
    
    def click_order_history(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.order_history_link)
        )
        self.driver.find_element(*self.order_history_link).click()
        