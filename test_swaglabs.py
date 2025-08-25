import time

import pytest
import allure
from allure_commons.types import Severity
from allure_commons.types import AttachmentType
from selenium import webdriver


@pytest.mark.usefixtures("driver")
@allure.epic("Accounts")
@allure.feature("Auth, order")
@allure.story("Pages")
class TestSwagLabs:

    @pytest.mark.smoke
    @allure.title("открытие страницы авторизации")
    @allure.severity(Severity.BLOCKER)
    @allure.link(url="https://vk.ru/@-229993114-pytest-allure?anchor=&ref=im#:~:text=%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D0%B5%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5,%D1%87%D0%B5%D0%BC%D1%83%20%D0%B2%20%D0%BD%D1%91%D0%BC.")
    def test_login(self):
        with allure.step("Открытие страницы. ШАГ 1"):
            self.driver.get("https://www.saucedemo.com/")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="open login page",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Открытие страницы. ШАГ 2"):
            assert self.driver.current_url == "https://www.saucedemo.com/", "ошибка в url"


    @pytest.mark.smoke
    @pytest.mark.auth
    @allure.title("авторизация")
    @allure.severity(Severity.BLOCKER)
    def test_auth(self):
        self.driver.get("https://www.saucedemo.com/")
        USER_NAME = self.driver.find_element("xpath", "//input[@id='user-name']")
        PASSWORD = self.driver.find_element("xpath", "//input[@id='password']")
        LOGIN = self.driver.find_element("xpath", "//input[@type='submit']")
        USER_NAME.send_keys("standard_user")
        PASSWORD.send_keys("secret_sauce")
        LOGIN.click()
        assert self.driver.title == "Swag Labs"
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    @pytest.mark.sanity
    @pytest.mark.profile
    @pytest.mark.auth
    @allure.title("авторизация и добавление товара в корзину")
    @allure.severity(Severity.CRITICAL)
    def test_adding_product_to_cart(self):

        with allure.step("Открытие страницы авторизации. ШАГ 1"):
             self.driver.get("https://www.saucedemo.com/")

        USER_NAME = self.driver.find_element("xpath", "//input[@id='user-name']")
        PASSWORD = self.driver.find_element("xpath", "//input[@id='password']")
        LOGIN = self.driver.find_element("xpath", "//input[@type='submit']")


        USER_NAME.send_keys("standard_user")
        PASSWORD.send_keys("secret_sauce")
        LOGIN.click()
        assert self.driver.title == "Swag Labs"
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        ADD_TO_CART = self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
        BASKET = self.driver.find_element("xpath", "//a[@class='shopping_cart_link']")
        with allure.step("Добавление товара в корзину. ШАГ 2"):
            ADD_TO_CART.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Добавление товара в корзину",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Переход в корзину. ШАГ 3"):
            BASKET.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Переход в корзину",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("проверка урла корзины. ШАГ 4"):
            assert self.driver.current_url == "https://www.saucedemo.com/cart.html"




    @pytest.mark.smoke
    @pytest.mark.profile
    @pytest.mark.chekcout
    @pytest.mark.regression
    @allure.title("заполнение пользовательских данных, оформление заказа")
    @allure.severity(Severity.CRITICAL)
    def test_checkout(self):
        with allure.step("Открытие страницы авторизации. ШАГ 1"):
             self.driver.get("https://www.saucedemo.com/")

        USER_NAME = self.driver.find_element("xpath", "//input[@id='user-name']")
        PASSWORD = self.driver.find_element("xpath", "//input[@id='password']")
        LOGIN = self.driver.find_element("xpath", "//input[@type='submit']")


        USER_NAME.send_keys("standard_user")
        PASSWORD.send_keys("secret_sauce")
        LOGIN.click()
        assert self.driver.title == "Swag Labs"
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        ADD_TO_CART = self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
        BASKET = self.driver.find_element("xpath", "//a[@class='shopping_cart_link']")
        with allure.step("Добавление товара в корзину. ШАГ 2"):
            ADD_TO_CART.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Добавление товара в корзину",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Переход в корзину. ШАГ 3"):
            BASKET.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Страница корзины",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("проверка урла корзины. ШАГ 4"):
            assert self.driver.current_url == "https://www.saucedemo.com/cart.html"

        CHECKOUT = self.driver.find_element("xpath", "//button[@class='btn btn_action btn_medium checkout_button ']")
        with allure.step("Нажатие на кнопку 'chekcout' . ШАГ 5"):
            CHECKOUT.click()

        with allure.step("проверка урла страницы 'chekcout'. ШАГ 6"):
                assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Страница заполнения данных о пользователе",
            attachment_type=allure.attachment_type.PNG
        )

        FIRST_NAME = self.driver.find_element("xpath", "//input[@class='input_error form_input']")

        FIRST_NAME.click()
        FIRST_NAME.send_keys("Anna")

        LAST_NAME = self.driver.find_element("xpath", "//input[@id='last-name']")
        LAST_NAME.send_keys("Kraevskaya")

        ZIP_POSTAL_CODE = self.driver.find_element("xpath", "//input[@id='postal-code']")
        ZIP_POSTAL_CODE.send_keys("123456")
        time.sleep(3)


        allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Заполненные данные о пользователе",
                attachment_type=allure.attachment_type.PNG
            )

        CONTINUE = self.driver.find_element("xpath", "//input[@type='submit']")
        CONTINUE.click()

        with allure.step("проверка урла страницы 'Overview'. ШАГ 7"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

        FINISH = self.driver.find_element("xpath", "//button[@class='btn btn_action btn_medium cart_button']")
        FINISH.click()
        allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="финишная страница оформления",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("проверка урла страницы 'Complete!'. ШАГ 8"):
                assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"



