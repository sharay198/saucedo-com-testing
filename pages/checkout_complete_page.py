from selenium.webdriver.common.by import By
from saucedo_com_testing.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    checkout_complete_url = BasePage.base_url + '/checkout-complete.html'
    final_message_locator = (By.XPATH, '//*[@id="checkout_complete_container"]/div')
    complete_container_locator = (By.ID, 'checkout_complete_container')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.checkout_complete_url)

    @property
    def final_message(self):
        return self.find(*self.final_message_locator)

    def final_message_text(self):
        return self.final_message.text

    @property
    def container(self):
        return self.find(*self.complete_container_locator)

    def container_is_displayed(self):
        return self.container.is_displayed()
