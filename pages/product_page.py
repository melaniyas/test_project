from .locators import LoginPageLocators
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def check_alert_add_to_basket_is_present(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERT), "Alert is not presented"

    def check_name_product_in_alert(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_in_alert = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_ALERT).text
        assert name == name_in_alert, "Names don't match"

    def check_price_product_in_alert(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_ALERT).text
        assert price == price_in_alert, "Prices don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_ALERT), "Success message is presented, but should not be"

    def should_disappeared_be_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_ALERT), "Success message is presented, but should not be"
