from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from saucedo_com_testing.pages.base_page import BasePage


class CartPage(BasePage):

    item_selector = (By.XPATH, '// *[ @ id = "item_4_title_link"] / div')
    checkout_btn_locator = (By.ID,'checkout')
    cart_page_url = BasePage.base_url + '/cart.html'

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.cart_page_url)

    @property
    def item(self):
        item: WebElement = self.find(*self.item_selector)
        return item

    @property
    def checkout_btn(self):
        return self.find(*self.checkout_btn_locator)

    def click_checkout_btn(self):
        self.checkout_btn.click()
