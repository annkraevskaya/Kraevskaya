import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support. ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

wait =WebDriverWait(driver, 5,poll_frequency=1)
driver.get("https://www.freeconferencecall.com/ru/ru/login")

driver.delete_all_cookies()
with open ("cookies_free_conference.json", "r") as file:
    cokies = json.load(file)
    for cookie in cokies:
        driver.add_cookie(cookie)

time.sleep(3)

driver.refresh()
time.sleep(2)


settings_button = driver.find_element("xpath", "//div[@class='__navigation__profile-menu__6c7ac    ']")

settings_button.click()
time.sleep(2)

my_settings_for_profile =driver.find_element("xpath", "//a[text() = 'Мои настройки профиля']")
my_settings_for_profile.click()
time.sleep(2)

foto_load = driver.find_element("xpath",  "//button[@class='photo-veil']")
foto_load.click()

load_file = driver.find_element("xpath", "//input[@type='file']")

load_file.send_keys(r"/Users/annakraevskaa/Downloads/ИноТ дайвер.jpeg")

time.sleep(5)

close_button = driver.find_element("xpath", "//button[text()='Закрыть']")
wait =WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable(close_button)).click()

time.sleep(2)


time.sleep(2)

save_button = driver.find_element("xpath", "//button[text()='Сохранить изменения']")
wait =WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable(save_button)).click()
time.sleep(5)