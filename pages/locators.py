from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    LOG_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, ".alert-success strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, ".alert-info strong")