from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_REPEATING = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form>.btn.btn-lg.btn-primary")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_OF_BOOK = (By.CSS_SELECTOR, ".product_main>h1")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, ".product_main>.price_color")
    TITLE_IN_SUCCESS_TEXT = (By.CSS_SELECTOR, "#messages>:first-child>div>strong")
    PRICE_OF_BASKET = (By.CSS_SELECTOR, "#messages>:last-child>div>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>:first-child")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
