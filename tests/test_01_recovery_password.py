import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from data.constants import BASE_URL


class TestRecoveryPassword:
    """Тесты для проверки восстановления пароля"""
    
    def test_recovery_link_exists(self, driver):
        driver.get(f"{BASE_URL}/login")
        login_page = LoginPage(driver)
        
        assert driver.find_element(*login_page.recovery_link).is_displayed()
    
    def test_recovery_password_flow(self, driver):
        driver.get(f"{BASE_URL}/login")
        login_page = LoginPage(driver)
        
        login_page.click_recovery_link()
        
        test_email = "test@example.com"
        login_page.enter_email(test_email)
        
        login_page.click_recovery_button()
    
    def test_password_toggle_button(self, driver):
        driver.get(f"{BASE_URL}/login")
        login_page = LoginPage(driver)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(login_page.password_toggle_button)
        )
        
        login_page.click_password_toggle()
        
        assert driver.find_element(*login_page.password_toggle_button).is_displayed()
        