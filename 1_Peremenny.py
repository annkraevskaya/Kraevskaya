#задание 1 (Арифметические операции)

#a = 10
#b = 3
#print(a+b)  # Операция сложения, Вывод: 13
#print(a-b)  # Операция вычетания, Вывод:7
#print(a*b)  #Умножение, Вывод: 30
#print(a/b)  #Деление, Вывод:3.33333
#print(a%b)  #Остаток от деления, Вывод: 1
#print(a//b) #Целочисленное деление , Вывод: 3
#print(a**b) #Возведения в степень, Вывод : 1000

# задание 2 ( Операции сравнения)
x = 15
y = 9
#print(x > y)    # x > y (true)
#print(x < y)    # x < y (false)
#print(x == y)   # x == y (false)
#print(x != y)   # x != y (true)
#print(x >= y)   # x >= y (true)
#print(x <= y)   # x <= y (false)


# задание 3 ( Преобразование типов данных)
string_number = "123"          # исходный класс - строка
#print(type(string_number))    # запрашиваем какой тип данных, чтобы убедиться какой класс имеем на данный момент
number = int (string_number)   # создаем новую переменную, преобразовывая имеющуюся строку в число
#print(number)                 # выводим значение новой переменной
#print(type(number))           # запрашиваем тип данных, чтобы убедиться какой присвоен класс после изменений

#number_float = float(number)  # присваиваем новой переменной  новый тип данных "число с плавающей точкой"
#print(type(number_float))     # запрашиваем тип данных, чтобы убедиться что преобразование прошло успешно
#print(number_float)           # выводим значение новой переменной

#string_1 = str (number_float)  # присваиваем новой переменной  новый тип данных "строка"
#print(type(string_1))          #запрашиваем тип данных, чтобы убедиться что преобразование прошло успешно
#print(string_1)                # выводим значение новой переменной



#задание 4  Замена значения переменных без временной переменной
#color = "Красный"  #Создала переменную color со значением "красный"
#print(type(color)) #Вывела тип переменной
#print(color)       #Вывела значение переменной

#color_number = 255        #Создала переменную color_number со значением 255
#print(type(color_number)) #Вывела тип переменной
#print(color_number)       #Вывела ее значение переменной

#color, color_number = color_number,color  #Поменяла значения местами
#print("color =", color)
#print("color_number =", color_number)
#print(type(color))
#print(type(color_number))

#задание 4.1 (Переопределение типа переменных)
color = "Красный"
#print(type(color))
color = 255
#print(color)
#print(type(color))
color = ["Красный", 255]
#print(type(color))

# задание 5 ( Именование переменных)
name_book = "Превращение"  #создала переменную с типом str
year_of_publication = 1912 #создала еще одну переменную с типом int
availability = True        #создала переменную с типом boolean

text = "Программирование"
srez = text[::3]
#print(srez) # срез выводящий каждый 3й элемент из строки

textsrez = "Nirvana"
polindrom = textsrez[::-1]
#print(polindrom) # полиндром(вывод строки в обратном порядке)


text = "Hello, World!"
#print(text.upper()) #вывод копии строки в верхнем регистре

text1 = "Hello, World!"
#print(text1.startswith("hello")) # проверка содержит ли строка слово "hello" в начале строки - вывод - False

cars = ["мерседес", "бмв", "ауди"]
#print(cars[-2]) #получение элемента списка по его индексу

# my_list = [1, 2, 3, ["a", "b", "c"], 4]
# #print(my_list[3][0]) #получение элемента из вложенного списка в основном списке по его индексу
#
# fruits = ["яблоко", "банан"]
# fruits.append("mango") # использование метода .append для добавления элемента в конец списка
# #print(fruits)
#
# spisok = ["мяч", "ракетка", "шорты", "кепка"]
# spisok.insert(1, "игра") # использование метода insert() для добавления элемента в список
# # на определенное место по индексу
#
# #print(spisok)
#
# fruct =["mango","kivi"]
# fruct[1]="lichi"   #замена одного элемента в списке на другой с помощью
# # обращения к нему по индексу и присваивание нового значения
# #print(fruct)
#
# fruit = ["яблоко", "банан", "апельсин", "виноград"]
# fruit.remove("апельсин") # удаление элемента из списка указав удаляемый элемент в кавычках (методом .remove)
# #print(fruit)
#
# fru = ["яблоко", "банан", "апельсин", "виноград"]
# fru.pop(1)  # удаление  элемента из списка указав индекс удаляемого элемента (методом .pop)
# #print(fru)
#
#
#
# numbers = [1, 2, 3, 2, 4, 2, 5, 2, 1,2,3,4,2]
# skolko = numbers.count(2)  #сколько раз определенный элемент(2) встречается в списке
# print(skolko)
#
# kopi_numbers = numbers.copy()
# print(kopi_numbers)
# import copy

# a= "123"
# b=10
#
# a=int("123")
# print(a+b)

# name = "Anna"
# age = 27
# city = "Moscow"
# print(name)
# print(age)
# print(city)

# x=7
# y=3
# print(x/y)
# print(x//y)


# a =15
# b =20
# print(a>b)
# print(a==15)

# x = 100
# print(x)
# print(type(x))
#
# x=("сто")
# print(x)
# print(type(x))

# box_in_market = "20 kg Apples"
# student_of_universyty= "Alex"
# print("Коробка в магазине содержит:",box_in_market)
# print("Студент колледжа по имени:", student_of_universyty)

# number_int= 100
# number_float = 20.5
# stroka ="строка"
# logicheskoe_znachenie= 5==5
# print(number_int)
# print(type(number_int))
# print(number_float)
# print(type(number_float))
# print(stroka)
# print(type(stroka))
# print(logicheskoe_znachenie)
# print(type(logicheskoe_znachenie))

# pi =3.14
# print(pi)
# print(type(pi))
#
# pi ="π"
# print(pi)
# print(type(pi))

# a =5.7
# a=int(5.7)
# print(a)
#
# a=str(a)
# print(a)
# print(type(a))
#
# x=12
# y=8
# print(x<y)
# print(x>y)
# print(x==y)

# a = 9
# a+=5
# print(a)



# name = "Hanna"
# age = 27
# height=1.64
# is_student = True
# print(f"Имя:{name}, Возраст: {age}, Рост:{height}м, Студент:{is_student}")

# answer=int(input("Введите Ваш возраст: "))
# if answer >= 18:
#     print("Доступ разрешён")
# else:
#     print("Доступ запрещён")


