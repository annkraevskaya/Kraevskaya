# задача 1 - агрумент с дефолтным знчением
# def greet_user(name="Гость"):
#     return f"Привет, {name}! Рады видеть тебя снова!"
#
#
# user_name=greet_user("Anna")
# print(user_name)
# user_name=greet_user()
# print(user_name)
from http.cookiejar import uppercase_escaped_char


# # задача 2-Возвращение данных из функций
#
#
# def calculate_area(length, width=None):
#     if width is None:
#         width=length
#     return length*width
#
# square_rectangle=calculate_area(12,)
# print(square_rectangle)


# # 3 задача создание и вызов функций
#
# def say_hello():
#     return f"Привет, мир!"
#
# message=say_hello()
# print(message)

# 4(раздел: Аргументы функций)

# def multiply(a,b):
#     return a*b
# result=multiply(3,5)
# print(result)


# def say_hello(func):
#     def wrapper():
#         print("Привет!")
#         func()
#     return  wrapper
#
#
# @say_hello
# def say_hello1():
#     print("Пока!")
#
# say_hello1()

def smile(func):
    def wrapper():
        print(":)")
        func()
    return wrapper


@smile
def greet():
    print("Hello!")

greet()