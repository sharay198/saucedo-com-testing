import time
from selenium.common import ElementNotVisibleException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    base_url = 'https://www.saucedemo.com'

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def find(self, *args):

        try:
            element: WebElement = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(args))
        except ElementNotVisibleException:
            print('Элемент не виден и не доступен для взаимодействия')
        else:
            time.sleep(1)
            return element
