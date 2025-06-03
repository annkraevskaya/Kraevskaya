#Задача 1 (Срезы)
#Дана строка s = "Python". Выведи первые 3 символа и последние 2 символа.
from tkinter.font import names

stroka = "Python"
symbol1 =stroka[0]
symbol2 =stroka[1]
symbol3 =stroka[2]
symbol5 =stroka[-2]
symbol4 =stroka[-1]
#print(symbol1,symbol2,symbol3,symbol5,symbol4)


stroka = "Python"
#result1 = stroka[0:3:1]    # Вывод первых трех символов
#result2 = stroka[-2:]      # Вывод двух последних символов
#print(result1,result2)

#Задание:text = "Hello, World!" Выведи подстроку "World" (используй срезы)
#Проверь, начинается ли строка с "Hello" (метод .startswith())
#Переведи весь текст в нижний регистр
#Замени восклицательный знак на вопросительный

#text = "Hello, World!"
#result = text[-6:-1]  # Для вывода результата среза слова "World"
#print(result)
#result1 = text.startswith("Hello") # Проверка, что строка начинается с "Hello"
#print(result1)
#result2 =text.lower()    #   Переводим строку в нижний регистр
#print(result2)
#result3 =text.replace("!","?")  # Заменяем знаки с "!" на "?"
#print(result3)

#Задания: s = "   Я изучаю Python 3.10!   "
#Удали лишние пробелы в начале и конце
#Найди позицию подстроки "Python" в строке (её индекс)
#Проверь, состоит ли строка только из букв (без цифр и символов)
#Раздели строку на слова по пробелам
#Замени "3.10" на "3.11"


#stroka1 = "   Я изучаю Python 3.10!   "
#result = stroka1.strip()
#print(result)
#result1 =result.index("Python")
#print(result1)

#result2 =result.isalpha()
#print(result2)

#result3 =result.split()
#print(result3)

#result4 =result.replace("3.10","3.11")
#print(result4)



#Задача 24 (Срезы строк + f-строки)дана строка:
#text = "Программирование"
#Выведи подстроку "грамм" (срезы)
#Переведи строку в верхний регистр
#Используя f-строку, выведи:
#"Слово 'ПРОГРАММИРОВАНИЕ' содержит X букв" (где X — длина строки)

#text = "Программирование"
#print(text[3:8:1].upper())
#print(len(text))
#text = f'"Слово {"'ПРОГРАММИРОВАНИЕ'"} содержит 16 букв"'
#print(text)


#Задача 1 (тема: Слияние списков)
#У тебя есть два списка:
#fruits = ['apple', 'banana', 'cherry']
#vegetables = ['carrot', 'tomato', 'pepper']
#Объедини эти два списка в один список под названием groceries.

fruits = ['apple', 'banana', 'cherry']
vegetables = ['carrot', 'tomato', 'pepper']
groceries = fruits + vegetables # `Объединение списков при помощи конкатенации
#print(groceries)

#Задача 2 (тема: Удаление элементов из списка и его очистка)
#У тебя есть список: colors = ['red', 'green', 'blue', 'yellow']
#Удали из списка элемент 'blue'.
#Затем полностью очисти список colors.
#colors = ['red', 'green', 'blue', 'yellow']
#colors.pop(2)
#print(colors)
#colors.clear()
#print(colors)
#
# text = "Цены: 100₽, 200₽, 150₽"
# clean_text =text.replace("₽"," ").replace("Цены:", "")
# print(clean_text)
# print(clean_text.strip())
# element1 = clean_text[0:4]
# print(element1)
# element1 = int(element1)
# print(type(element1))
# element2=clean_text[6:10]
# print(element2)
# element2 = int(element2)
# print(type(element2))
# element3=clean_text[13:16]
# print(element3)
# element3 = int(element3)
# print(type(element3))
# print(len(clean_text))
#
# fruits = ['яблоко', 'банан', 'киви', 'груша', 'персик']
# #Выведи на экран второй и четвертый элементы списка.
# element_2 = fruits[1]
# element_4 = fruits[3]
# print(element_2)
# print(element_4)



# закрепление темы спустя время(28мая)

# text ="Python"
# new_peremennaya=text[0:3:1]
# print(new_peremennaya)

# name ="Иван"
# age = 30
# print(f"Меня зовут {name} и мне {age} лет")

# s = "python"
# print(s.upper())
#
# word = "программа"
# print(word[1])

# my_string = "Hello, world!"
# print(len(my_string))

# a = "Python"
# b = "3.10"
# print(a+b)
#
# new_message ="Дурак дураку рознь"
# print(new_message)

# text = "автоматизация"
# print(text[-4:])
#
# phrase = "информатика"
# print(phrase[:6])
#
# word = "автоматизация"
# print(word[2:8:1])
#
# sentence = "программирование"
# print(sentence[::2])
#
# msg = "машиностроение"
# print(msg[-5:])
#
# text = "компьютер"
# print(text[::-1])


text = "Python is awesome!"

print(len(text))
print(text.upper())
print(text.replace("awesome", "powerful"))
print(text[7:11])
