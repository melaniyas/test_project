from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    LOG_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.NAME, "registration_submit")
class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, ".alert-success strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, ".alert-info strong")

class BasketPageLocators():
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_HEADER = (By.CSS_SELECTOR, ".page-header h1")
