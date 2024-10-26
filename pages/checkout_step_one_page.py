from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from saucedo_com_testing.pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):

    step_one_url = BasePage.base_url + '/checkout-step-one.html'

    first_name_locator = (By.ID, 'first-name')
    last_name_locator = (By.ID, 'last-name')
    postal_code_locator = (By.ID, 'postal-code')
    continue_btn_locator = (By.ID, 'continue')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.step_one_url)

    @property
    def first_name(self):
        first_name: WebElement = self.find(*self.first_name_locator)
        return first_name

    @property
    def last_name(self):
        last_name: WebElement = self.find(*self.last_name_locator)
        return last_name

    @property
    def postal_code(self):
        postal_code: WebElement = self.find(*self.postal_code_locator)
        return postal_code

    def fill_form(self, first_name, last_name, postal_code):
        self.first_name.send_keys(first_name)
        self.last_name.send_keys(last_name)
        self.postal_code.send_keys(postal_code)

    @property
    def continue_btn(self):
        return self.find(*self.continue_btn_locator)

    def click_continue_btn(self):
        self.continue_btn.click()
