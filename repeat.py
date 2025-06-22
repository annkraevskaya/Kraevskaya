# 6. Циклы
# Задача:
# Используя цикл for, выведи все элементы списка numbers = [1, 2, 3, 4, 5], умноженные на 2.

numbers = [1, 2, 3, 4, 5]
for numb in numbers:
    print(numb*2)


# 5- Словари - проработка
slovar = {                             #создание простого словаря
    "country1":"Russia",
    "country2":"Belarus",
    "country3":"Kazakhstan"
 }

print(slovar["country3"])   #вывод значения из словаря при помощи обращения по ключу "country3"
print(list(slovar.keys()))    #вывод ключей из словаря при помощи метода .keys() и преобразование вывода в список
print(list(slovar.values()))   #вывод значений для ключей из словаря при помощи метода .values() и преобразование вывода в список
print(list(slovar.items())) #вывод всех ключ-значений для словаря при помощи метода .items() и преобразование вывода в список


name =slovar["country1"]   #сохранение значения для ключа"country1":"Russia" в переменную name для дальнейшего
slovar["country1"]={        # добавления нового вложенного словаря с городами в город Россия ******!
"name": name,
"city":{
     "city1": "Moscow",
     "city2": "Saint-P"
}
}
                    #добавление вложенного словаря с городами
print(slovar)

slovar["country3"]="Kazakhstan7"  #замена значения для ключ-значения -"country3" - добавлена 7 в названии страны
print(slovar)


# //////////  создание другого словаря

slovar = [
    {
    "country1":"Russia",
    "country2":"Belarus",
    "country3":"Kazakhstan"
},

{
    "city1":"Moscow",
     "city2":"Saint-P"
},
    {
        "Minsk":"Belarus",
        "Moscow":"Russia",
        "Alma-Ata":"Kazakhstan"
    }
]


slovar[1]["city2"]="Kazan'"  # замена значения для ключа"city2"
print(slovar[1])


# //////////  работа с новым словарем

slovar ={
"city":["Moscow","Saint-P", "Kazan'", "Tambov"],

"country":{
    "country1":"Russia",
    "country2":"Belarus",
    "country3":"Kazakhstan"
    }
}

print(slovar["city"][3])  # вывод значения по ключу и индексу из вложенного списка в словаре

slovar["city"][3]="michurinsk"   # заменям значение во вложенном списке словаря с индексом 3 "Tambov" - на новое значение "michurinsk"
print(slovar["city"][3])

del slovar["country"]["country3"]    # удаляем ключ-значение "country3":"Kazakhstan" из вложенного словаря "country"
print(slovar)
#
# deletes=slovar.pop("country")  # удаляем вложенный словарь "country" и передаем его инфо в новую переменную "deletes"

# print(slovar)
# print(deletes)

assert slovar["country"]["country1"] == "Russia"   # проверяем наличие определенного значения(страны) в словаре
                                                                      # при помощи assert

assert slovar["city"][0] == "Moscow" , "ошибка в индексе для города"  # проверяем наличие определенного значения(города) в словаре
                                                                      # при помощи assert


if "country" in slovar:            # проверяем наличие определенного значения(страны) в словаре с помощью if in
    print("страны есть в списке")

if "Saint-P" in slovar["city"][1]:     # проверяем наличие определенного значения(города) в словаре с помощью if in
    print("est'!")
