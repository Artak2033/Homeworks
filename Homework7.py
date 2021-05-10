'''Dembel Program'''

import datetime
import calendar

print('\n\t\t*** Dembel Program ***')

print('Name: Artak')
print('Surname: Chobanyan')

x = datetime.datetime.now()
y = datetime.datetime(2020,3,1)

res = x - y

print('Time passed: ',res)
print('Today: ',datetime.date.today())
print(x.strftime("%A"))



'''1.You wrote a test.If test score 0-40 print(Bad!),40-80(Normal!),80-100(Good!).
Test score with Random().'''


# import random

# test = random.randint(1,100)

# res = 79 < test < 100 
# res1 = 39 < test < 80 
# res2 = 0 < test < 40 

# print('Test Score: ',test)

# print('Test result Good! ',res,'\nTest result Normal! ',res1,'\nTest result Bad! ',res2)



'''2.You want to buy a sneakers.You have 2 inputs(brand,size).If you have sneakers print(True,False) and size(True,False).
For example. Sneakers(Nike): True    Size(40): True'''

# sneakers = 'Nike Adidas Puma'
# size = '36 37 40 41'

# user = input('Choose the brand: ') == 'Nike'
# user_size = int(input('Choose the size of sneakers: ')) == 40


# print('Sneakers(Nike): ',user,'\nSize(40): ',user_size)




