NAME = "hw4_part2"

def test(a):
    return a * 22

def fun_plus(a):
    return a + 22

def fun_minus(a):
    return a - 22


# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
def square(arg):
    print(f'Периметр квадрата {arg * 4}', f'Площадь квадрата {arg ** 4}', f'Диагональ квадрата {(2*arg**2)**.5}')
    return arg

# square(5)


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer


# def argu(aaaa):
#     return aaaa
#
# print(argu('name: John'))
# print(argu('last_name: Smith'))
# print(argu('age: 35'))
# print(argu('position: web developer'))

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
#

import functools

# lst = [20, -3, 15, 2, -1, -21]
#
# def get_numbers(a, lam_func):
#     res = []
#     for x in a:
#         if lam_func(x):
#             res.append(x)
#
#     return res
#
# r = get_numbers(lst, lambda x: x >= 0)
# print(f'Положительные числа из списка', *r)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке


# res = functools.reduce(lambda x, y: x*y, r)
# print(f'Результат перемножения значений в предыдущем списке {res}')




