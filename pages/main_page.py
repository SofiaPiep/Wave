from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def login(self):
        self.browser.get(self.link)
        login_field = self.browser.find_element(*MainPageLocators.LOGIN_FIELD)
        login_field.send_keys('standard_user')
        password_field = self.browser.find_element(*MainPageLocators.PASSWORD_FIELD)
        password_field.send_keys('secret_sauce')
        self.browser.find_element(*MainPageLocators.LOGIN_BTN).click()
