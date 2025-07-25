# Импорт всех необходимых библиотек
import time  # модуль time позволяет делать паузы, чтобы успевать увидеть, что происходит
from selenium import webdriver  # импортируем webdriver - он управляет браузером

# Создаём настройки для браузера Chrome
options = webdriver.ChromeOptions()  # создаём переменную с настройками
options.add_argument("--incognito")  # подкидываем режим инкогнито (в том числе, чтобы не мешало окно уведомления о пароле)

# Запускаем браузер с нашими настройками
driver = webdriver.Chrome(options=options)  # создаём переменную driver и подкидываем туда webdriver с настройками
driver.get("https://www.saucedemo.com")  # открываем нужный сайт
time.sleep(2)



# Находим поля для логина и пароля, а также кнопку входа
user_name = driver.find_element("xpath", "//input[@id='user-name']")
password = driver.find_element("xpath", "//input[@id='password']")
login = driver.find_element("xpath", "//input[@type='submit']")

# Вводим логин и пароль с помощью метода send_keys
user_name.send_keys("standard_user")
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(2)

# Нажимаем на кнопку входа
login.click()
time.sleep(2)

# Проверяем, куда попали: выводим адрес и заголовок страницы
print(driver.current_url)  # выводим текущий URL
print(driver.title)  # выводим заголовок страницы
assert driver.title == "Swag Labs"  # убеждаемся, что заголовок правильный
assert driver.current_url == "https://www.saucedemo.com/inventory.html"  # проверяем, что мы на нужной странице

# Добавление товара в корзину

# Находим кнопку "Добавить в корзину" напрример у рюкзака и кликаем по ней
add_to_cart = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
add_to_cart.click()
time.sleep(3)

# Переходим в корзину — находим значок корзины и нажимаем на него
basket = driver.find_element("xpath", "//a[@class='shopping_cart_link']")
basket.click()
time.sleep(3)

# Проверяем, что перешли на страницу корзины
print(driver.current_url)
assert driver.current_url == "https://www.saucedemo.com/cart.html"

#Оформление покупки

# Находим кнопку "Checkout" (оформить заказ) и нажимаем
checkout = driver.find_element("xpath", "//button[@class='btn btn_action btn_medium checkout_button ']")
checkout.click()
time.sleep(5)

# Заполняем данные покупателя — имя, фамилия, индекс
first_name = driver.find_element("xpath", "//input[@id='first-name']")
first_name.send_keys("Anna")
time.sleep(1)

last_name = driver.find_element("xpath", "//input[@id='last-name']")
last_name.send_keys("Kraevskaya")
time.sleep(1)

zip_postal_code = driver.find_element("xpath", "//input[@id='postal-code']")
zip_postal_code.send_keys("123456")
time.sleep(1)

# Нажимаем на кнопку подтверждения - Continue, чтобы перейти к следующему шагу
continue_button = driver.find_element("xpath", "//input[@type='submit']")
continue_button.click()

# Проверяем, что мы на следующем шаге оформления
print(driver.current_url)
assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
time.sleep(3)

# Находим кнопку "Finish" и завершаем оформление покупки
finish = driver.find_element("xpath", "//button[@class='btn btn_action btn_medium cart_button']")
finish.click()
time.sleep(3)

# Проверяем, что попали на финальную страницу "покупка завершена"
print(driver.current_url)
assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
