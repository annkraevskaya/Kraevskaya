import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

# Полное отключение управления паролями и всех всплывающих окон
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_setting_values.popups": 2
}
options.add_experimental_option("prefs", prefs)

# Дополнительно — отключаем автоматические расширения Google
options.add_argument("--disable-extensions")
options.add_argument("--disable-save-password-bubble")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-popup-blocking")

# Запуск драйвера
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")

# Вход
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Ждём переход на страницу товаров
WebDriverWait(driver, 5).until(
    EC.url_to_be("https://www.saucedemo.com/inventory.html")
)



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


