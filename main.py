import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.item_page import ItemPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

base_url = 'https://www.saucedemo.com'

payload = {'login': 'standard_user', 'password': 'secret_sauce'}
login = 'standard_user'
password = 'secret_sauce'


def main():
    driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(3)  # ждём некоторое время, чтобы наюлюдать результат открытия страницы
    try:
        username_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'user-name')))
    except ElementNotVisibleException:
        print('Элемент не виден и не доступен для взаимодействия')
    else:
        username_field.send_keys(login)
        time.sleep(2)
    try:
        password_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'password')))
    except ElementNotVisibleException:
        print('Элемент не виден и не доступен для взаимодействия')
    else:
        password_field.send_keys(password)
        time.sleep(2)

    try:
        login_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'login-button')))
    except ElementNotVisibleException:
        print('Элемент не виден и не доступен для взаимодействия')
    else:
        login_button.click()
        time.sleep(2)

    try:
        put_item_btn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'add-to-cart-sauce-labs-backpack')))
    except ElementNotVisibleException:
        print('Элемент не виден и не доступен для взаимодействия')
    else:
        put_item_btn.click()  # добавляем товар в корзину
        time.sleep(2)

    try:
        cart = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'shopping_cart_container')))
    except ElementNotVisibleException:
        print('Элемент не виден и не доступен для взаимодействия')
    else:
        cart.click()  # переходим на страницу корзины
        time.sleep(2)

    try:
        item: WebElement = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'item_4_title_link')))
    except ElementNotVisibleException:
        print('Элемент не виден и не доступен для взаимодействия')
    else:
        assert item.text == 'Sauce Labs Backpack'
        print(f'{item.text} добавлен в корзину')
        # убеждаемся, что товар добавлен в корзину
        time.sleep(2)


if __name__ == '__main__':
    # main()
    login_page = LoginPage(chrome_driver)
    login_page.open()
    login_page.fill_auth_form(payload['login'], payload['password'])
    #login_page.enter_password(payload['password'])
    login_page.click_button()
    # chrome_driver.delete_cookie()
    item_page = ItemPage(chrome_driver)
    item_page.open()
    item_page.click_add_button()
    item_page.go_to_cart()
    cart_page = CartPage(chrome_driver)
    assert cart_page.item.text == 'Sauce Labs Backpack'
    print(cart_page.item.text)
    cart_page.click_checkout_btn()
    step_one_page = CheckoutStepOnePage(chrome_driver)
    step_one_page.fill_form('Ivan', 'Sparrow', '104')
    step_one_page.click_continue_btn()
    step_two_page = CheckoutStepTwoPage(chrome_driver)
    step_two_page.click_finish_btn()
    complete_checkout_page = CheckoutCompletePage(chrome_driver)
    print(complete_checkout_page.container)
    #assert complete_checkout_page.final_message_text == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
    #print(complete_checkout_page.final_message.text)

    # assert complete_checkout_page.final_message.text == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
    # Your order has been dispatched, and will arrive just as fast as the pony can get there!
    # login_field = login_page.login
    # login_field.send_keys(payload['login'])
    # login_page.enter_password()
    #time.sleep(5)
