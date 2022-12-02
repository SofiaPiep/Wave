#Лекция1:
# 1) Установите Python и PyCharm
# 2) Напишите и запустите программу.которая выводит строку "Hello world!"
#print('Hello, World!')
# 3) Напишите программу, которая на входе получает имя пользователя, cохраняет его в переменную user_name и
# выводит строку "Hello {user_name}!"
#user_name = input('What is your name?')
#print('Hello, ', user_name)
# 4) Напишите программу, чтобы вывести:
n = '**'
n1 = '*'
n2=' '
print(n,n2,n,n2,n,n2,n,n2,n1)
print(n1,n2,n2,n2,n2,n2,n2,n2,n2,n2,n1)
print(n1,n2,n2,n2,n2,n2,n2,n2,n2,n2,n1)
print(n,n2,n,n2,n,n2,n,n2,n1)
print('*********\n*       *\n*       *\n*********')
# ** ** ** ** *
# *           *
# *           *
# ** ** ** ** *
User_name = input('Your name?\n')
User_birth_year = input('What is your year of birth?\n')
User_birth_year=User_birth_year.isdigit()
print(User_birth_year)
User_birth_year1 = int(input('Confirm your year of birth\n'))
User_age = 2022-User_birth_year1
User_name=User_name.capitalize()
print(f'Hello, {User_name}. Your age is {User_age}')
m="You are awesome!"
m=m.upper()
print(m)
print("You are great,{0} {1}".format(User_name, User_age))
print("You are great,{1} {0}".format(User_name, User_age))
print(f'Hello, {User_name}. Your age is {User_age}')
print("Hello, " + User_name + ". " + "Your age is " + str(User_age))

#num = int(input("Number?"))
#sum1 = 0
#while (num != 0):
#   sum1 = sum1 + num % 10
#    num = num // 10
#print(sum(map(int,str(sum1))))