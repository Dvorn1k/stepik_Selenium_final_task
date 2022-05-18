from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_OF_BOOK = (By.CSS_SELECTOR, ".product_main>h1")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, ".product_main>.price_color")
    TITLE_IN_SUCCESS_TEXT = (By.CSS_SELECTOR, "#messages>:first-child>div>strong")
    PRICE_OF_BASKET = (By.CSS_SELECTOR, "#messages>:last-child>div>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>:first-child")
