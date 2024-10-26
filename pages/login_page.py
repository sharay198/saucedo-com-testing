from selenium.webdriver.common.by import By
from saucedo_com_testing.pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class LoginPage(BasePage):
    login_selector = (By.ID, 'user-name')
    password_selector = (By.ID, 'password')
    button_selector = (By.ID, 'login-button')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.base_url)

    @property
    def login(self):
        login_field: WebElement = self.find(*self.login_selector)
        return login_field

    @property
    def password(self):
        password_field: WebElement = self.find(*self.password_selector)
        return password_field

    @property
    def button_login(self):
        button_login = self.find(*self.button_selector)
        return button_login

    def fill_auth_form(self, login, password):
        self.login.send_keys(login)
        self.password.send_keys(password)

    def click_button(self):
        self.button_login.click()
