import json
import time

from selenium import webdriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")

driver.delete_all_cookies()
with open("cookies_free_conference.json", "r") as file:
    cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

driver.refresh()  # Обязательно
time.sleep(2)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

# Ожидание кнопки профиля
settings_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='full-name']")))
settings_button.click()

# Ожидание перехода на настройки
my_settings_for_profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Мои настройки профиля']")))
my_settings_for_profile.click()

my_settings_for_profile =driver.find_element("xpath", "//a[text() = 'Мои настройки профиля']")
my_settings_for_profile.click()
time.sleep(2)

foto_load = driver.find_element("xpath",  "//button[@class='photo-veil']")
foto_load.click()

load_file = driver.find_element("xpath", "//button[@id='drop-zone-ember1013']")
load_file.click()
time.sleep(2)

load_file.send_keys(r"/Users/annakraevskaa/Downloads/ИноТ дайвер.jpeg")

time.sleep(5)

close_button = driver.find_element("xpath", "//button[@class='btn btn-block apply-edit btn-blue']")
close_button.click()
time.sleep(5)
