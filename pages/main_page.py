from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import (
    INGREDIENT, 
    MODAL_TITLE, 
    MODAL_CLOSE,
    HEADER_CONSTRUCTOR_LINK,
    HEADER_FEED_LINK
)
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/"

    def click_constructor(self):
        self.click_element((By.XPATH, HEADER_CONSTRUCTOR_LINK))

    def click_feed(self):
        self.click_element((By.XPATH, HEADER_FEED_LINK))

    def click_ingredient(self):
        self.click_element((By.XPATH, INGREDIENT))

    def get_modal_title(self):
        return self.get_text((By.XPATH, MODAL_TITLE))

    def close_modal(self):
        self.click_element((By.XPATH, MODAL_CLOSE))

    def is_modal_closed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, MODAL_TITLE))
            )
            return True
        except Exception:
            return False

    def get_counter_value(self):
        return self.get_text((By.XPATH, "//p[contains(@class, 'counter_counter__num')]"))

    def drag_ingredient_to_basket(self):
        ingredient_el = self.find_element((By.XPATH, INGREDIENT))
        basket_el = self.find_element((By.XPATH, "//*[contains(@class, 'BurgerConstructor')]"))

        script = """
            function createDragEvent(type, target, dataTransfer) {
                var event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                target.dispatchEvent(event);
            }
            var source = arguments[0];
            var target = arguments[1];
            var dataTransfer = new DataTransfer();
            dataTransfer.setData('text/plain', source.id || source.textContent);
            createDragEvent('dragstart', source, dataTransfer);
            createDragEvent('dragover', target, dataTransfer);
            target.focus();
            createDragEvent('drop', target, dataTransfer);
            createDragEvent('dragend', source, dataTransfer);
        """
        self.execute_script(script, ingredient_el, basket_el)

    def click_order_button(self):
        self.click_element((By.XPATH, "//button[text()='Оформить заказ']"))
        