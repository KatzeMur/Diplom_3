from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import INGREDIENT, MODAL_TITLE, MODAL_CLOSE
from data.constants import BASE_URL


class MainPage:
    """Page Object для главной страницы"""
    
    def __init__(self, driver):
        self.driver = driver
        self.url = BASE_URL
    
    constructor_link = (By.XPATH, "//a[@href='/']")
    feed_link = (By.XPATH, "//a[@href='/feed']")
    ingredient = (By.XPATH, INGREDIENT)
    modal_title = (By.XPATH, MODAL_TITLE)
    modal_close = (By.XPATH, MODAL_CLOSE)
    counter = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    order_basket = (By.XPATH, "//*[contains(@class, 'BurgerConstructor')]")
    order_button = (By.XPATH, "//button[text()='Оформить заказ']")
    
    def open(self):
        self.driver.get(self.url)
    
    def click_constructor(self):
        self.driver.find_element(*self.constructor_link).click()
    
    def click_feed(self):
        self.driver.find_element(*self.feed_link).click()
    
    def click_ingredient(self):
        self.driver.find_element(*self.ingredient).click()
    
    def get_modal_title(self):
        return self.driver.find_element(*self.modal_title).text
    
    def close_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.modal_close)
        )
        self.driver.find_element(*self.modal_close).click()
    
    def is_modal_closed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(self.modal_title)
            )
            return True
        except:
            return False
    
    def get_counter_value(self):
        return self.driver.find_element(*self.counter).text
    
    def drag_ingredient_to_basket(self):
        ingredient_element = self.driver.find_element(*self.ingredient)
        basket_element = self.driver.find_element(*self.order_basket)

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
        self.driver.execute_script(script, ingredient_element, basket_element)
    
    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.order_button)
        )
        element = self.driver.find_element(*self.order_button)
        self.driver.execute_script("arguments[0].click();", element)
        