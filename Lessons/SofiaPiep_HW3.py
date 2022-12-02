#sentence = "What a wonderful life!"
#my_list = list(sentence)
#print(my_list)
#my_list1 = sentence.split(' ')
#print(my_list1)
#my_list2 = sentence.split('a')
#print(my_list2)
#3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2][0],",", my_list[2][1],",",my_list[2][2])

#3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   #- получите сумму всех чисел,
print(sum(filter(lambda x: isinstance(x, int), list_1)))
# - распечатайте все строки, где есть буква 'a'
print([x for x in list_1 if isinstance(x, str) and 'a' in x])

#3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
list=['cat', 'dog', 'horse', 'cow']
list=tuple(list)
print(type(list))

#3.4. Напишите программу, которая определяет, какая семья больше.
     # 1) Программа имеет два input() - например, family_1, family_2.
     # 2) Членов семьи нужно перечислить через запятую.
    # Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
family_1 = tuple(input('Введите текст через запятую: ').split(','))
family_2 = tuple(input('Введите текст через запятую: ').split(','))
family_3 = input('Введите текст через запятую: ').split(',')
if len(family_1) == len(family_2):
    print('Equal')
elif len(family_1) > len(family_2):
    print('family_1')
else:
    print('family_2')
print(type(family_3))

#3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    #о вашем любимом фильме.
    #- распечатайте только ключи
   # - распечатайте только значения
    #- распечатайте пары ключ - значение

My_dict={'title1':'Supernatural',
         'director': 'untitle1', 'year': 2017, 'budget': 'nodata2', 'main_actor':'James', 'slogan': 'noname'}
print(My_dict)
#3.6. Найдите сумму всех значений в словаре
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))
print(my_dictionary.values())

#3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
list4=[1, 2, 3, 4, 5, 3, 2, 1]
dict4= set(list4)
print(type(dict4))
print(dict4)
#3.8. Даны два множества:
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     #- найдите значения, которые встречаются в обоих множествах
     #- найдите значения, которые не встречаются в обоих множествах
     #- проверьте являются ли эти множества подмножествами друг друга
