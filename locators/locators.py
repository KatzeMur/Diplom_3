# Локаторы для страницы восстановления пароля
RECOVERY_LINK = "//*[@id='root']/div/main/div/div/p[2]/a"
EMAIL_INPUT = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"
RECOVERY_BUTTON = "//*[@id='root']/div/main/div/form/button"

# Локаторы для страницы входа
PASSWORD_TOGGLE_BUTTON = "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/div"
PASSWORD_INPUT = "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"
LOGIN_BUTTON = "//*[@id='root']/div/main/div/form/button"

# Локаторы для личного кабинета
ACCOUNT_LINK = "//*[@id='root']/div/header/nav/a"
ORDER_HISTORY_LINK = "//a[text()='История заказов']"
LOGOUT_BUTTON = "//button[text()='Выход']"

# Локаторы для главной страницы
INGREDIENT = "//a[contains(@class, 'BurgerIngredient_ingredient')]"
MODAL_TITLE = "//h2[text()='Детали ингредиента']"
MODAL_CLOSE = "//button[contains(@class, 'Modal_modal__close')]"

# Локаторы для ленты заказов
ORDER_IN_FEED = "//*[contains(@class, 'OrderHistory_link')]"
MODAL_ORDER = "//*[contains(@class, 'Modal_orderBox')]"
ORDER_MODAL_CLOSE = "//button[contains(@class, 'Modal_modal__close')]"
TOTAL_COUNTER = "//p[text()='Выполнено за все время:']/following-sibling::p"
TODAY_COUNTER = "//p[text()='Выполнено за сегодня:']/following-sibling::p"
