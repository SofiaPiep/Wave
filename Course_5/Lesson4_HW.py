# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
#
# def square(x):
#     per = x * 4
#     sq = x * x
#     dia = (x * 2**0.5)
#     return per, sq, dia
#
# print(square(5))
#
# #
# # 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
# #      в формате аргумент: значение. Например:
# # 	name: John
# # 	last_name: Smith
# # 	age: 35
# # 	position: web developer
#
# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
    # name = input('Enter your name: ')
    # last_name = input('Enter your last name: ')
    # age = input('Enter your age: ')
    # position = input('Enter your position: ')
    # print(f'Name: {name}, Last name: {last_name}, Age: {age}, Position: {position}', end="\n")

#info(Name = 'Olga', Last_name = 'Gerber', Age = 34, Position = 'QA')
#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
#
my_list = [20, -3, 15, 2, -1, -21]
new_list = list(filter(lambda x: x > 0, my_list))
print(new_list)
# #
# # 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
from functools import reduce
multi_list = reduce(lambda i, s: i*s, new_list)
print(multi_list)


# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
# from my_calc import my_subst, my_sum, my_div, my_mult
#
# print(my_subst(8, 2))
# print(my_div(15, 0))
# print(my_sum(3, 5))
# print(my_mult(2, 7))
#
# def tests():
#     assert my_sum(1, 2) == 3, f'Wrong number, actual result is {my_sum(1, 2)}'
#     assert my_div(4, 2) == 2, f'Wrong number, actual result is {my_div(4, 2)}'
#     assert my_subst(5, 2) == 3, f'Wrong number, actual result is {my_subst(5, 2)}'
#     assert my_mult(1, 2) == 2, f'Wrong number, actual result is {my_mult(1, 2)}'
#
# tests()