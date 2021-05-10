'''1.Write a python program which will check is your number equal the random
number of computer (1-10) if yes print True otherwise False.'''

import math
import random
import calendar

# Me = random.randint(1,10)
# Pc = random.randint(1,10)

# Res = Me == Pc

# print(Me)
# print(Pc)
# print('Result: ',Res)



'''2. Write a python program which will check is your number great or equal
the random number of computer (10-100) if yes print True otherwise False.'''

# User = random.randint(1,100)
# Pc = random.randint(1,100)

# Res = User >= Pc

# print('User:',User)
# print('Pc:',Pc)
# print('Result: ',Res)



'''3.Write a python program which will show your birthday using calendar.'''


# bday_y = int(input('Enter your born year: '))
# bday_m = int(input('Enter your born month: '))
# bday_d = int(input('Enter your born day: '))

# print(calendar.month(bday_y,bday_m))



'''4.Write a python program where we use sqrt (definition discriminant):6x2+10x−1=0    D=b^2-4ac'''

a = 6
b = 10
c = -1

D = (b ** 2) - 4 * a * c

print('D =',D)

x1 = (-b + math.sqrt(D)) / (2 * a)
x2 = (-b - math.sqrt(D)) / (2 * a)

print('X1 =',x1)
print('X2 =',x2)



'''5.Write a python program where we use pi (calculate the area of circle)
you have one input (radius circle).'''

# Rad = int(input("Enter Radius of circle: "))

# Res = math.pi * Rad ** 2

# print('Result: ',Res)