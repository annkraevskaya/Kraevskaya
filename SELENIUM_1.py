# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://dsr-admin.k8s.dev002.local/calendar?year=2025")
# time.sleep(5)
import time

from selenium import webdriver    #импорт пакета вебрайвер из библиотеки селениум
driver = webdriver.Chrome()       # инициализация объекта-открытие браузера хром
driver.get("https://www.google.com/webhp?hl=ru&ictx=0&sa=X&ved=0ahUKEwiKk-r0vMaOAxU1hv0HHZVoEyIQpYkNCAo") #открытие страницы сайта по урлу
time.sleep(3)   # фриз времени , для того чтобы увидеть загрузку страницы

print(driver.current_url)   # вывод урла ( для проверки на ту ли страницу мы попали?)
print(driver.title)         # вывод тайтла ( для проверки, так ли страница открыла ( не случилось ли редиректа) )

assert driver.title == "Google"  , "ошибка - не тот тайтл"  # ассёртим, чтобы убедиться что тайтл совпадает  и тест не падает