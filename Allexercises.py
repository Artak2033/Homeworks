'''1.Write a python program which have two input and compute the area of a rectangle.'''

# a = int(input('Koxm 1: '))
# b = int(input('Koxm 2: '))\

# res = a * b

# print('Result: ',res)



'''2.Write a python program which have one input and compute the area of a square.'''

# user = int(input('Enter side of square: '))

# res = user * user

# print(res)



'''3.Write code to print pypypypython'''

# print(4 * 'py' + 'thon')



'''4.Write code to print 7p7p7p79'''

# print(3 * '7p' + '79')



'''5.Write code to print 9999999'''

# print(7 * '9')



'''6.Write a Python program that checks how much money you have on your card.
At first, your balance is 0, and you have 3 inputs and add each of them to the card.'''

# balance = 0

# user1 = int(input('Enter money: '))
# user2 = int(input('Enter money: '))
# user3 = int(input('Enter money: '))


# balance += user1 + user2 + user3

# print('Result: ',balance)



'''7.Create a python program which convert the pound in kilograms.'''

# user = float(input('Enter kilograms: '))

# res = user / 2.205

# print('Pound in Kg: ',res)



'''8.Create a python program which convert the miles in kilometers.'''

# user = float(input('Enter mile: '))

# res = user * 1.6

# print('Miles in km: ',res)



'''9.You have one input where you write number (Celsius) and your program will say
how much fahrenheit is your Celsius.'''

# Celsius = float(input('Celsius: '))

# fahrenheit = 32 + Celsius * 1.8

# print('Celsius to fahrenheit: ',fahrenheit)



'''10.You have one input where you write number (Fahrenheit) and your program will
say how much Celsius is your Fahrenheit.'''

# Fahrenheit = float(input('Fahrenheit: '))

# Celsius = (Fahrenheit - 32) / 1.8

# print('Fahrenheit to Celsius: ',Celsius)



'''11.Convert Minutes into Seconds you have one input.5 ------->> 300'''

# Minutes = float(input('Enter Minutes: '))

# Seconds = Minutes * 60

# print('Minutes into Seconds: ',Seconds)



'''12.Convert Day into Minutes and Seconds you have one input.
And check the type of result'''

# Day = int(input('Day: '))

# Minutes = Day * 24 * 60
# Seconds = Minutes * 60

# print('Day in Minutes: ',Minutes,'\nDay in Seconds: ',Seconds)



'''13.Write a python program which have 2 input (float or int) and two of them less than 90 you will check that
triangle have 90 degree angle.'''

# a = float(input('First less: '))
# b = float(input('Second less: '))

# res = 180 - (a + b)
# Triangle = res == 90

# print('Result: ',Triangle)



'''14.Write a python program which have 2 input (angle of triangle) and calculate the size of the third angle.
30, 60, ---> 90'''

# angle1 = int(input('Enter first angle: '))
# angle2 = int(input('Enter second angle: '))

# res = 180 - angle1 - angle2

# print('Third angle =',res)



'''15.Write a python program which have one input(int or float) and check this number is
more than 100 or less than 100 ? If Great True otherwise False.'''

# num = int(input('Enter number: '))

# res = num >= 100

# print(res)



'''16.Write a python program which have one input(int or float) and check ,
if modulo 400 is 0 True, otherwise False.'''

# number = int(input('Enter number: '))

# zero = number != 0
# res = number % 400  == 0

# print(res==zero)



'''17.You have a wheel: and have one input the radius of wheel and calculate how much
meter it will pass after 5 turn.'''

# radius = int(input('Raidus: '))

# x = 3.14 * radius * 2
# meter = x * 5

# print(meter)



'''18.Write a python program to check how much odd
and even number have your number.
For example 103 have 52 odd and 51 even'''

# num = int(input('Enter number: '))

# zuyg = num // 2
# kent = num - zuyg

# print('Zuyg: ',zuyg,'Kent: ',kent)


import random

print(random.randint(1,10))