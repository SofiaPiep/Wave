# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

# my_list = ['a', 'b', [1, 2, 3], 'd']
# for x in (my_list[2]):
#     print(x, end=', ')

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

#list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# sum = 0
# for x in list_1:
#     if type(x) == int:
#         sum += x
# print(sum)

### lambda-variant
# print(sum(filter(lambda x: type(x) == int, list_1)))

# for x in list_1:
#     if str(x).__contains__('a'):
#         print(x)

###lambda-variant
#print(list(filter(lambda x: str(x).__contains__('a'), list_1)))


# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
# a = ['cat', 'dog', 'horse', 'cow']
# b = tuple(a)
# print(type(b))

#
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family1 = tuple(input('Enter all numbers of your family: ').split(','))
# family2 = tuple(input("Enter all numbers of your friend's family: ").split(','))
# if len(family1) > len(family2):
#     print("First family has more members")
# elif len(family1) < len(family2):
#     print("Second family has more members")
# else:
#     print("Equal")

#
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

# film = {'title': 'The Lord of the Rings', 'director': 'Peter Jackson', 'budget': '280 000 000',
#         'main_actor': 'Elijah Jordan Wood', 'slogan': 'Power can be held in the smallest of things...'}
# for x in film.values():
#     print(x)
# for y in film.keys():
#     print(y)
# for z in film.items():
#     print(z)
#
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_sum = 0
# for x in my_dictionary.values():
#     my_sum += x
# print(my_sum)
# #
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# my_list = [1, 2, 3, 4, 5, 3, 2, 1]
# unique_list = list(set(my_list))
# print(unique_list)

#
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1.issubset(set2))
# print(set1.issuperset(set2))

###import module
# from my_file import my_sum
# my_sum(5, 8)

import datetime
current_date = datetime.date.today()
print(current_date)
year = current_date.year
month = current_date.month
day = current_date.day
print(year)
print(month)
print(day)

