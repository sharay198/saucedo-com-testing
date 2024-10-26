from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from saucedo_com_testing.pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    step_two_url = BasePage.base_url + '/checkout-step-two.html'

    finish_btn_locator = (By.ID, 'finish')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.step_two_url)

    @property
    def finish_btn(self):
        first_name: WebElement = self.find(*self.finish_btn_locator)
        return first_name

    def click_finish_btn(self):
        self.finish_btn.click()
