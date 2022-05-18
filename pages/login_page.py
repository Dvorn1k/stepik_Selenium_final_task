from .base_page import BasePage
from .locators import LoginPageLocators
import faker
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Incorrect link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        input1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        input1.send_keys(email)
        password = 9078563412
        input2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_REPEATING)
        input3.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
        time.sleep(5)