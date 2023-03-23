from .base_page import BasePage
from .locators import BasketPageLocators
class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/basket/", "Basket url is not correct"
    def should_be_basket_header(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_HEADER).text
        assert basket == "Basket", "Basket header is not correct"
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET)
    def should_be_not_message_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET)
    def should_be_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.ITEMS)
    def should_be_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS)
