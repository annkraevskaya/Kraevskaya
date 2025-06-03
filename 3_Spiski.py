# # Задача 1:
# # Создай список из трёх фруктов.
# # Добавь в него ещё один фрукт с помощью метода append() и выведи итоговый список на экран.
# from multiprocessing.context import set_spawning_popen
#
# spisok =["apple", "mango", "banana"]
# print(type(spisok))
# spisok.append("blueberry")
# print(spisok)
# # Задача 2(доступ к элементам списка):
# # Выведи на экран второй элемент из твоего списка фруктов.
#
# print(spisok[1])
#
# # задача 3 Замена элемента в списке”:
# # Замени третий фрукт в своём списке на "kiwi", затем выведи обновлённый список.
#
# spisok[3]="kiwi"
# print(spisok)
#
# # Следующая задача — “Добавление элемента в конкретное место списка”:
# # Вставь фрукт "grape" на второе место в списке (то есть с индексом 1)
# # с помощью метода insert().
#
# spisok.insert(1,"grape")
# print(spisok)
# spisok.remove("banana")
# print(spisok)
#
#
# # Удалить фрукт с индексом 2 с помощью метода pop(),
# # сохрани его в переменную,
# # выведи сначала обновлённый список, потом значение удалённого фрукта.
# save_element=spisok.pop(2)
# print(spisok)
# print(save_element)
#
# print(spisok[:2:1])


numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)
del numbers[1]
print(numbers)
numbers[2]=35
print(numbers)
print(numbers[::-1])