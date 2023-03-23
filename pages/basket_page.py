from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET)

    def should_be_not_message_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET)

    def should_be_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.ITEMS)

    def should_be_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS)
