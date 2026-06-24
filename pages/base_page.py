from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import (
    HEADER_ACCOUNT_LINK,
    HEADER_CONSTRUCTOR_LINK,
    HEADER_FEED_LINK,
    MODAL_CLOSE_BUTTON,
    MODAL_OVERLAY
)
from data.constants import BASE_URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = ""

    def open(self):
        if self.url == "/":
            self.driver.get(BASE_URL)
        else:
            self.driver.get(f"{BASE_URL}{self.url}")

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def close_modal_if_present(self, timeout=3):
        try:
            overlay = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, MODAL_OVERLAY))
            )
            if overlay.is_displayed():
                self.click_element((By.XPATH, MODAL_CLOSE_BUTTON))
        except Exception:
            pass

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_element_displayed(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
    