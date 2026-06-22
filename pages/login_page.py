from selenium.webdriver.common.by import By
from locators.locators import (
    RECOVERY_LINK,
    EMAIL_INPUT,
    RECOVERY_BUTTON,
    PASSWORD_TOGGLE_BUTTON,
    PASSWORD_INPUT,
    LOGIN_BUTTON
)
from data.constants import BASE_URL


class LoginPage:
    """Page Object для страницы входа"""
    
    def __init__(self, driver):
        self.driver = driver
        self.url = f"{BASE_URL}/login"
    
    recovery_link = (By.XPATH, RECOVERY_LINK)
    email_input = (By.XPATH, EMAIL_INPUT)
    recovery_button = (By.XPATH, RECOVERY_BUTTON)
    password_toggle_button = (By.XPATH, PASSWORD_TOGGLE_BUTTON)
    password_input = (By.XPATH, PASSWORD_INPUT)
    login_button = (By.XPATH, LOGIN_BUTTON)
    
    def open(self):
        self.driver.get(self.url)
    
    def click_recovery_link(self):
        self.driver.find_element(*self.recovery_link).click()
    
    def enter_email(self, email):
        self.driver.find_element(*self.email_input).clear()
        self.driver.find_element(*self.email_input).send_keys(email)
    
    def click_recovery_button(self):
        self.driver.find_element(*self.recovery_button).click()
    
    def click_password_toggle(self):
        self.driver.find_element(*self.password_toggle_button).click()
    
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        