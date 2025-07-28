# Импорт всех необходимых библиотек

import time      # модуль "time" позволяет задавать паузы между действиями ( для наглядности)
from selenium import webdriver # импорт пакета "webdriver"



options = webdriver.ChromeOptions() #подкидываем опции для браузера Chrome
options.add_argument("--incognito") # добавляем опцию "режим инкогнито" (в том числе чтобы обойти окно слитого пароля)

driver = webdriver.Chrome(options=options) #создаем переменную "driver" и подкидываем туда пакет "webdriver" и опции
driver.get("https://www.saucedemo.com")  # открываем сайт
time.sleep(2)


#Авторизация.
#Находим элементы кнопкок в консоли, создаем переменную для каждой кнопки.
#подкидываем в наш driver  метод "find_element" и через локатор находим необходмую кнопку.

USER_NAME = driver.find_element("xpath", "//input[@id='user-name']")
PASSWORD = driver.find_element("xpath", "//input[@id='password']")
LOGIN = driver.find_element("xpath", "//input[@type='submit']")

USER_NAME.send_keys("standard_user")  #с мопощью метода ".send_keys" вводим в поле "USER_NAME" наш логин
time.sleep(2)
PASSWORD.send_keys("secret_sauce")  #с мопощью метода ".send_keys" вводим в поле "PASSWORD" наш пароль
time.sleep(2)

LOGIN.click()  #методом "click" нажимаем на кнопку и происходит авторизация в системе

time.sleep(2)

# Проверки: получаем и сравниваем текущий URL и заголовок страницы

print(driver.current_url)     # методом ".current_url" получаем url нашей страницы
print(driver.title)        # методом ".titll" получаем title нашей страницы
assert driver.title == "Swag Labs"    # ассертим наш   title
assert driver.current_url =="https://www.saucedemo.com/inventory.html"  # ассертим наш  url


#Добавление товара в корзину.
#Создаем переменную и кладем в нее элемент кнопки добавления товара в корзину
ADD_TO_CART = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
ADD_TO_CART.click()  #кликаем на кнопку,чтобы товар добавился в корзину
time.sleep(3)

#Создаем переменную и кладем в нее элемент кнопки перехода в корзину
BASKET = driver.find_element("xpath", "//a[@class='shopping_cart_link']")

BASKET.click()   #кликаем на кнопку,чтобы перейти в корзину
time.sleep(3)


#получаем урл страницы на которуб мы попали, чтобы убедиться, что мы верно перешли
print(driver.current_url)
assert driver.current_url == "https://www.saucedemo.com/cart.html"  # ассертим для проверки


#Создаем переменную в которуб кладем элемент кнопки "Checkout"
CHECKOUT = driver.find_element("xpath", "//button[@class='btn btn_action btn_medium checkout_button ']")

CHECKOUT.click()  #кликаем на кнопку,чтобы перейти на этап заполнения данныхх о покупателе

time.sleep(5)

#Создаем переменную в которуб кладем элемент поля для заполнения имени
FIRST_NAME =driver.find_element("xpath", "//input[@class='input_error form_input']")

FIRST_NAME.click()
FIRST_NAME.send_keys("Anna")
time.sleep(1)


#Создаем переменную в которуб кладем элемент поля для заполнения фамилии
LAST_NAME = driver.find_element("xpath", "//input[@id='last-name']")
LAST_NAME.send_keys("Kraevskaya")
time.sleep(1)

#Создаем переменную в которуб кладем элемент поля для заполнения индекса
ZIP_POSTAL_CODE = driver.find_element("xpath", "//input[@id='postal-code']")
ZIP_POSTAL_CODE.send_keys("123456")

time.sleep(1)

#Создаем переменную в которуб кладем элемент кнопки подтвержления (Continue)
CONTINUE = driver.find_element("xpath", "//input[@type='submit']")


CONTINUE.click()   #кликаем на кнопку,чтобы подтвердить данные

#получаем урл страницы на которуб мы попали, чтобы убедиться, что мы верно перешли
print(driver.current_url)
assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

time.sleep(3)

#Создаем переменную в которую кладем элемент кнопки завершения покупки (Finish)
FINISH = driver.find_element("xpath", "//button[@class='btn btn_action btn_medium cart_button']")
FINISH.click()
time.sleep(3)


#получаем урл страницы на которуб мы попали, чтобы убедиться, что мы верно перешли
print(driver.current_url)
assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
