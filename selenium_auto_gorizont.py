import json
import time

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument()
driver = webdriver.Chrome()

driver.get("http://dsr-admin.k8s.dev002.local/?year=2025")

driver.delete_all_cookies()
with open("cookies.json", "r") as file:
    cookies =json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

time.sleep(10)
