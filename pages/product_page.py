from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()
        BasePage.solve_quiz_and_get_code(self)
        self.should_be_added_correct_title_of_book_in_basket()
        self.should_be_added_correct_price_of_book_in_basket()

    def should_be_added_correct_title_of_book_in_basket(self):
        book_title = self.browser.find_element(*ProductPageLocators.TITLE_OF_BOOK)
        basket_title = self.browser.find_element(*ProductPageLocators.TITLE_IN_SUCCESS_TEXT)
        assert book_title.text == basket_title.text, "The title of the book and the title in the basket do not match"

    def should_be_added_correct_price_of_book_in_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET)
        assert book_price.text == basket_price.text, "The price of the book and the price of the basket do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_success_message_is_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be 2"
