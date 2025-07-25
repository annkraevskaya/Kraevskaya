import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Настройки Chrome, чтобы не было уведомлений о паролях
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")
time.sleep(2)

USER_NAME = driver.find_element("xpath", "//input[@id='user-name']")
PASSWORD = driver.find_element("xpath", "//input[@id='password']")
LOGIN = driver.find_element("xpath", "//input[@type='submit']")

USER_NAME.send_keys("standard_user")
time.sleep(2)
PASSWORD.send_keys("secret_sauce")
time.sleep(2)

LOGIN.click()

time.sleep(2)

print(driver.current_url)
print(driver.title)
assert driver.title == "Swag Labs"
assert driver.current_url =="https://www.saucedemo.com/inventory.html"

ADD_TO_CART = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
ADD_TO_CART.click()
time.sleep(3)

BASKET = driver.find_element("xpath", "//a[@class='shopping_cart_link']")

BASKET.click()
time.sleep(3)

print(driver.current_url)
assert driver.current_url == "https://www.saucedemo.com/cart.html"

CHECKOUT = driver.find_element("xpath", "//button[@class='btn btn_action btn_medium checkout_button ']")

CHECKOUT.click()

time.sleep(5)

FIRST_NAME =driver.find_element("xpath", "//input[@class='input_error form_input']")

FIRST_NAME.click()
FIRST_NAME.send_keys("Anna")
time.sleep(1)

LAST_NAME = driver.find_element("xpath", "//input[@id='last-name']")
LAST_NAME.send_keys("Kraevskaya")
time.sleep(1)

ZIP_POSTAL_CODE = driver.find_element("xpath", "//input[@id='postal-code']")
ZIP_POSTAL_CODE.send_keys("123456")

time.sleep(1)


CONTINUE = driver.find_element("xpath", "//input[@type='submit']")

CONTINUE.click()
print(driver.current_url)
assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

time.sleep(3)

FINISH = driver.find_element("xpath", "//button[@class='btn btn_action btn_medium cart_button']")
FINISH.click()
time.sleep(3)

print(driver.current_url)
assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
