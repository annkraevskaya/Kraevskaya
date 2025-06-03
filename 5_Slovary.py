# 1) Условие:
# Создай словарь student с ключами:
#
# "name" (значение — твоё имя, например "Анна")
#
# "age" (значение — твой возраст, например 25)
#
# "courses" (значение — список из 2 предметов, например ["Математика", "История"])
#
# Выведи словарь и его тип через type().

# student = {
# "name": "Anna",
# "age": 25,
# "courses":["Математика", "История"]
#
# }
#
# print(type(student))


# 2
# Выведи название книги (по ключу "title")
#
# Выведи год издания + 10 лет
#
# Выведи автора в верхнем регистре
# book = {
#     "title": "Гарри Поттер",
#     "year": 2001,
#     "author": "Дж. Роулинг"
# }
#
# print("Название:", book["title"])
# print("Год издания:", book["year"]+10)
# print("Автор:", book["author"].upper())

# 3
# Дан пустой словарь shop = {}
# Добавь в него 3 элемента:
#
# Ключ "fruit" → значение "apple"
#
# Ключ "price" → значение 1.99
#
# Ключ "count" → значение 10
#
# Затем измени цену на 2.49
#
# Выведи итоговый словарь

# shop = {}
#
# shop= {
# "fruit":"apple",
# "price": 1.99,
# "count":10
# }
# print(shop)
#
# shop["price"]=2.49
# print(shop)

# 4
# Дан словарь:

# person = {
#     "name": "Иван",
#     "age": 30,
#     "city": "Москва",
#     "phone": "123-456"
# }
# Удали ключ "phone"
#
# Выведи:
#
# Итоговый словарь
#
# Количество оставшихся элементов (используй len())


# person = {
#     "name": "Иван",
#     "age": 30,
#     "city": "Москва",
#     "phone": "123-456"
# }
#
# del person["phone"]
# print(person)
# print(len(person))


slovar ={
    "Moscow":1000,
    "Saint-P":12345,
    "Kazan":10200
}
# slovar["Sochi"]=600
# print(slovar)
#
# slovar["Saint-P"]=9999
# print(slovar)
# udalenie= slovar.pop("Moscow")
# print(slovar)
# print(udalenie)
# print(slovar.keys())
# print(slovar.values())
#
# proverka=10200 in slovar.values()
# print(proverka)
# import json
# values = {
#     "country":{
#         "Russia":{
#     "city":{
#         "Moscow":"Население - 100000",
#         "Saint-P":"Население - 1000",
#         "Sochi":"Население - 900"
#     }
#     }
#
#
#     }
# }
# print(values)
# print(values["country"]["Russia"]["city"]["Sochi"])
#
# box ={
#     "box1": [1, "dva", True]
# }
# values["New element"]={
#     "one":1,
#     2:"two"
# }
#
#
# print(json.dumps(values, ensure_ascii=False, indent=4))




# device = {
#     "name": "Sensor-1",
#     "status": "online",
#     "battery": 87
# }
#
# device["location"]="Server Room"
# device["battery"]= 95
# del device["status"]
# print(device)


#
# settings = {
#     "ip": "192.168.1.10",
#     "port": 8080,
#     "user": "admin",
#     "timeout": 120
# }
#
# assert settings["port"]==8080


student={
    "name":"Hanna",
    "age":27,
    "courses":["Python", "Math", "English"]

}

student["grade"]="A"
print(student)
student["age"]=25
print(student)
for course in student["courses"]:
    print(course)


