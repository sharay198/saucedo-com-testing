from saucedo_com_testing.pages.cart_page import CartPage
from saucedo_com_testing.pages.checkout_complete_page import CheckoutCompletePage
from saucedo_com_testing.pages.checkout_step_one_page import CheckoutStepOnePage
from saucedo_com_testing.pages.checkout_step_two_page import CheckoutStepTwoPage
from saucedo_com_testing.pages.item_page import ItemPage
from saucedo_com_testing.pages.login_page import LoginPage

payload = {'login': 'standard_user', 'password': 'secret_sauce'}


def test_buy_item(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.open()
    login_page.fill_auth_form(payload['login'], payload['password'])
    login_page.click_button()
    print('Авторизация прошла успешно, переход на страницу с товарами')
    item_page = ItemPage(chrome_driver)
    item_page.open()
    item_page.click_add_button()
    print('Товар добавлен в корзину')
    item_page.go_to_cart()
    print('Переход на страницу корзины')
    cart_page = CartPage(chrome_driver)
    cart_page.click_checkout_btn()
    print('Нажатие на кнопку "checkout"')
    print('Переход на страницу для оформления заказа, шаг 1')
    step_one_page = CheckoutStepOnePage(chrome_driver)
    step_one_page.fill_form('Ivan', 'Sparrow', '104')
    print('Заполнение полей формы для оформления заказа')
    step_one_page.click_continue_btn()
    print('Нажатие на кнопку "continue" ')
    print('Переход на страницу для оформления заказа, шаг 2')
    step_two_page = CheckoutStepTwoPage(chrome_driver)
    step_two_page.click_finish_btn()
    print('Нажатие на кнопку "finish"')
    complete_checkout_page = CheckoutCompletePage(chrome_driver)
    assert complete_checkout_page.container_is_displayed()
    print('Сообщение об успешном оформлении заказа выведено на экран')
    chrome_driver.quit()
