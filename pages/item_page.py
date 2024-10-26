from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from saucedo_com_testing.pages.base_page import BasePage

cart_selector = (By.ID, 'shopping_cart_container')
add_item_selector = (By.ID, 'add-to-cart-sauce-labs-backpack')


class ItemPage(BasePage):
    item_page_url = BasePage.base_url + '/inventory.html'

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.item_page_url)

    # add to cart button
    @property
    def add_button(self):
        return self.find(*add_item_selector)

    def click_add_button(self):
        self.add_button.click()

    @property
    def cart(self):
        cart: WebElement = self.find(*cart_selector)
        return cart

    def go_to_cart(self):
        self.cart.click()
