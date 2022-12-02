#Задание 2.1
#Напишите программу, которая проверяет здоровье персонажа в игре.
#Если оно равно или меньше нуля, выведите на экран False, в противном случае Tru

x = int(input("Health?"))
if x>0: print("True")
else:print("False")
#Задание 2.2
#Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
x = int(input("Number?"))
if x%2: print("Нечетное")
else:print("Четное")
#Задание 2.3
#Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
year = int(input("Year?"))
if not year%4 and year%100 or not year%400:print("Високосный")
else:print("Невисокосный")


#Задание 2.4
#Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью inpit()
i=0
text=str(input("Text?") )
n=int(input("How many?"))
while i<n:
    print(text)
    i=i+1

#i=0
#while i<5:
#    print("HELOO!")
#   i=i+1
#    if i==3:
#        continue
#name= input("What is your name?")
#for letter in name:
#    letter=letter.upper()
#    print(letter)
#def narcissistic(value):
 #   value = str(value)
  #  size = len(value)
   # sum = 0
    #for i in value:
     #   sum += int(i) ** size
   # return sum == int(value)
#print(narcissistic(1000))
#print('a' 'b' 'c' 'd')
#x=int(input("Number?"))
#if x%2:
#    print(x)
#else: print(x)
#print(" Robert\n","Stannis\n","Renly")