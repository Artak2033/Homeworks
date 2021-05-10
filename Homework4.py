'''1. You have one input where you write
number (Celsius) and your program will say
how much fahrenheit is your Celsius.'''

# Celsius = float(input('Enter the Celsius: '))

# Fahrenheit = 32 + Celsius * 1.8

# print('Celsius in Fahrenheit: ',Fahrenheit)



'''2. You have one input where you write
number (Fahrenheit) and your program will
say how much Celsius is your Fahrenheit.'''

# Fahrenheit = float(input('Enter the Fahrenheit: '))

# Celsius = (Fahrenheit - 32) / 1.8

# print('Fahrenheit in Celsius: ', Celsius)



'''3. Convert Minutes into Seconds you have one input.
5 ------->> 300'''

# Minutes = int(input("Enter minutes: "))

# Seconds = Minutes * 60

# print('Minutes in Seconds: ',Seconds)



'''4. Convert Day into Minutes and Seconds you have one
input.
And check the type of result'''

# Day = int(input("Enter day: "))

# Minutes = Day * 24 * 60 
# Seconds = Minutes * 60

# print('Day in Minutes: ',Minutes,type(Minutes))
# print('Day in Seconds: ',Seconds,type(Seconds))



'''5. Write a python program which have 2 input (float or
int) and two of them less than 90 you will check that
triangle have 90 degree angle.'''

# var1 = int(input("Enter first less: "))
# var2 = int(input("Enter second less: "))

# res = 180 - (var1 + var2)
# Triangle = res == 90

# print('Result: ',Triangle)



'''6. Write a python program which have 2 input (angle of
triangle) and calculate the size of the third angle.
30, 60, ---> 90'''

# angle1 = int(input('Enter first angle: '))
# angle2 = int(input('Enter second angle: '))

# Res = 180 - angle1 - angle2

# print('Third angle: ',Res)



'''7.Write a python program which have one
input(int or float) and check this number is
more than 100 or less than 100 ? If Great
True otherwise False.'''

# Number = float(input('Enter the number: '))

# Res = Number >= 100

# print('Result: ',Res)



'''8.Write a python program which have one
input(int or float) and check ,
if modulo 400 is 0 True, otherwise False.'''

# Num = int(input('Enter the number: '))

# Zero = Num != 0
# Res = Num % 400 == 0

# print('Result: ',Res==Zero)



'''9. You have a wheel: and have one input the
radius of wheel and calculate how much
meter it will pass after 5 turn.'''

# Radius = int(input('Enter radius of wheel: '))

# T = 3.14 * Radius * 2 

# Meter = T * 5

# print("Result: ",Meter)



'''10.Write a python program to check how much odd
and even number have your number.
For example 103 have 52 odd and 51 even'''

# Number = int(input('Enter the number: '))

# Even = Number // 2 
# Odd = Number - Even

# print('Even numbers: ',Even)
# print('Odd numbers: ',Odd)



'''11.Create a python program to check if your
letter is upper or not you have one input.'''

# Word = input('Enter the word: ')

# Res = Word == Word.upper()

# print(Res)




'''EXERCISES'''


'''You have a one input(int,float).Enter salary and write a program 
to calculate the salary for the year, if you receive 15% of the salary 2 times a year.'''

# Salary = int(input('Enter the salary: '))

# Procent = Salary * 15 / 100
# Year = 12 * Salary + (Procent * 2)

# print ('The salary in year with procents: ',Year)



'''You have 3 inputs(name, surname and age). Write a program if age 18 or above (True), else (False)'''

# Name = input('Enter the name: ')
# Surname = input('Enter the surname: ')
# Age = int(input('Enter the age: '))

# Res = Age >= 18

# print(Res)



'''You have three input, parametres sides of triangle.You should see can you create 
triangle with this parametres'''

# First = int(input("Enter first side: "))
# Second = int(input("Enter second side: "))
# Third = int(input("Enter third side: "))

# Triangle = First + Second + Third == 180

# print('Triangle: ',Triangle)



'''You have two input(int,float).Write a program, that will calculate their percent to each other.'''

# Number1 = int(input('Enter first number: '))
# Number2 = int(input('Enter second number: '))

# res = (Number1 / Number2) * 100
# res2 = (Number2 / Number1) * 100

# print('Number1 %  of Number2: ',res)
# print('Number2 %  of Number1: ',res2)