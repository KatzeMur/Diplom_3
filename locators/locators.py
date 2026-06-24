# Локаторы для страницы восстановления пароля
RECOVERY_LINK = "//a[text()='Восстановить пароль']"
EMAIL_INPUT = "//label[text()='Email']/following-sibling::input"
RECOVERY_BUTTON = "//button[text()='Восстановить']"

# Локаторы для страницы входа
PASSWORD_TOGGLE_BUTTON = "//div[contains(@class, 'input__icon-action')]"
PASSWORD_INPUT = "//label[text()='Пароль']/following-sibling::input"
LOGIN_BUTTON = "//button[text()='Войти']"

# Локаторы для личного кабинета
ACCOUNT_LINK = "//a[contains(., 'Личный Кабинет')]"
ORDER_HISTORY_LINK = "//a[text()='История заказов']"
LOGOUT_BUTTON = "//button[text()='Выход']"

# Локаторы для главной страницы
INGREDIENT = "//a[starts-with(@href, '/ingredient/')]"
MODAL_TITLE = "//h2[text()='Детали ингредиента']"
MODAL_CLOSE = "//div[contains(@class, 'Modal_modal')]//button[@type='button']"

# Локаторы для ленты заказов
ORDER_IN_FEED = "//a[starts-with(@href, '/feed/')]"
MODAL_ORDER = "//div[contains(@class, 'Modal_orderBox')]"
ORDER_MODAL_CLOSE = "//div[contains(@class, 'Modal_modal')]//button[@type='button']"
TOTAL_COUNTER = "//p[text()='Выполнено за все время:']/following-sibling::p"
TODAY_COUNTER = "//p[text()='Выполнено за сегодня:']/following-sibling::p"

# Общие локаторы (шапка, модальные окна)
HEADER_ACCOUNT_LINK = "//a[contains(., 'Личный Кабинет')]"
HEADER_CONSTRUCTOR_LINK = "//a[@href='/']"
HEADER_FEED_LINK = "//a[@href='/feed']"
MODAL_CLOSE_BUTTON = "//div[contains(@class, 'Modal_modal')]//button[@type='button']"
MODAL_OVERLAY = "//div[contains(@class, 'Modal_modal_overlay')]"
