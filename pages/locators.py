from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')


class ProductsPageLocators():
    SHOPPING_CART = (By.ID, 'shopping_cart_container')