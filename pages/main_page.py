from selenium.webdriver.common.by import By
from locators.locators import (
    INGREDIENT, 
    MODAL_TITLE, 
    MODAL_CLOSE,
    HEADER_CONSTRUCTOR_LINK,
    HEADER_FEED_LINK,
    COUNTER,
    BURGER_CONSTRUCTOR,
    ORDER_BUTTON
)
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/"

    def click_constructor(self):
        self.click_element((By.XPATH, HEADER_CONSTRUCTOR_LINK))

    def is_on_constructor_page(self):
        return self.get_current_url().endswith("/")

    def click_feed(self):
        self.click_element((By.XPATH, HEADER_FEED_LINK))

    def is_on_feed_page(self):
        return "/feed" in self.get_current_url()

    def click_ingredient(self):
        self.click_element((By.XPATH, INGREDIENT))

    def get_modal_title(self):
        return self.get_text((By.XPATH, MODAL_TITLE))

    def is_modal_opened(self):
        return self.is_element_displayed((By.XPATH, MODAL_TITLE))

    def close_modal(self):
        self.click_element((By.XPATH, MODAL_CLOSE))

    def is_modal_closed(self):
        try:
            self.wait_for_element_invisible((By.XPATH, MODAL_TITLE))
            return True
        except Exception:
            return False

    def get_counter_value(self):
        return self.get_text((By.XPATH, COUNTER))

    def drag_ingredient_to_basket(self):
        ingredient_el = self.find_element((By.XPATH, INGREDIENT))
        basket_el = self.find_element((By.XPATH, BURGER_CONSTRUCTOR))

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
        self.click_element((By.XPATH, ORDER_BUTTON))
        