import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options = chrome_options)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(autouse=True)
def setup_environment_properties():
    properties = {
        "STAGE": os.environ["STAGE"],
        "BROWSER": os.environ["BROWSER"]
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")






