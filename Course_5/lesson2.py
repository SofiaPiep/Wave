# HW 2.1
# health = 0
# if health > 0:
#     print(True)
# else:
#     print(False)
#
# #HW 2.2
# number = int(input('Enter the number: '))
# if number % 2:
#     print('Nechetnoe')
# else:
#     print('Chetnoe')

#HW 2.3
# year = int(input('Enter the year: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('Visokosnii')
# else:
#     print(False)

#HW 2.4
# text = input('What should I print? ')
# i = int(input('How many times? '))
# for x in range(i):
#    print(text)

#FizzBuzz
'''
loop from 1 to 10 (for/while)
-if value is multiple of 3
    display value
    ...
'''
# for number in range(1, 16):
#     if number % 3 == 0 and number % 5 == 0:
#         print('FizzBuzz')
#     elif number % 5 == 0:
#         print('Buzz')
#     elif number % 3 == 0:
#         print('Fizz')
#     else:
#         print(number)


#Fibonacci
'''0 1 1 2 3 5 8 13.....
n = target(how many fib numbers)
F0 = 0
F1 = 1
loop 1 to n
    fib = F0 + F1
    F0 = F1
    F1 = fib
    display(fib)'''
# n = 5
# f0 = 0
# f1 = 1
# print(f0)
# print(f1)
# for i in range(n + 1):
#     fib = f0 + f1
#     f0 = f1
#     f1 = fib
#     print(fib)


