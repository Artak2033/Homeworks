'''1.Take two int values from user and print greatest among them.'''

# user1 = int(input('Enter value: '))
# user2 = int(input('Enter value: '))

# if user1 > user2:
# 	print('Greatest value is User1: ',user1)
# elif user1 == user2:
# 	print('The values is equal')
# else:
# 	print('Greatest value is User2: ',user2)



'''2.Take input of age of 3 people by user and determine oldest
and youngest among them.'''

# user1 = int(input('User1 age: '))
# user2 = int(input('User2 age: '))
# user3 = int(input('User3 age: '))

# if user1 == user2 == user3:
# 	print('The values is equal.')
# elif user1 > user2 and user1 > user3:
# 	print('User1 is oldest.')
# elif user2 > user1 and user2 > user3:
# 	print('User2 is oldest.')
# elif user3 > user1 and user3 > user2:
# 	print('User3 is oldest.') 
# 	if user1 < user2 and user1 < user3:
# 		print('User1 is youngest.')
# 	elif user2 < user1 and user2 < user3:
# 		print('User2 is youngest.')
# 	elif user3 < user1 and user3 < user2:
# 		print('User3 is youngest.') 



'''3.You have number. Write a python program which to print a
new number with digits reversed as of original one.
For example:
INPUT : 1234 OUTPUT : 4321'''




'''4.Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using
following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
And any other input of age should print "ERROR".'''

# age = int(input('Your age: '))
# sex = input('M or F: ').upper()
# status = input('Y or N: ')

# if sex == 'F':
# 	print('Only in urban areas.')
# elif sex == 'M' and 20 < age < 40:
# 	print('Work in anywhere.')
# elif sex == 'M' and 40 < age < 60:
# 	print('Only in urban areas.')
# elif sex == 'F' or sex == 'M' and age < 20 or age > 60:
# 	print('ERROR')


'''5.Chingachoong'''

# import random

# pc = 'RPS'
# user = 'RPS'


# var_pc = random.choice(pc)
# var_user = input('Choose R,P,S: ').upper()


# print(var_pc)
# print(var_user)

# if var_pc == var_user:
# 	print('Nichya')
# elif var_pc == 'R' and var_user == 'P' or var_pc == 'S' and var_user == 'R' or var_pc == 'R' and var_user == 'P':
# 	print('User win')
# else:
# 	print('Pc win')




'''6.You (input) and pc have followers (pc have random followers) if your followers
is great 20 % than pc you are blogger otherwise pc is blogger.'''

# import random

# pc = random.randint(1,50000)
# print('Pc follower: ',pc)
# user = int(input('Followers: '))
# print('User followers: ',user)

# proc = user * 20 / 100

# if proc > pc:
# 	print('You are blogger.')
# else:
# 	print('Pc are blogger.')



'''7.You and the Pc take part in the rally, You must pass 12 km. PC passed in 3 minutes and You are
10% later than Pc.How much is the speed of your car.'''

# km = 12

# pc = 3
# v1 = 12 / pc
# print('Pc time: ',pc)
# print('Pc speed: ',v1)

# proc = pc * 10 / 100

# user = pc + proc
# v2 = 12 / user
# print('Your time: ',user)
# print('Your speed: ',v2)



'''8.The given number is of one digited or two digited or three digited or more than three digited.
input >> 176
output >> 3 Digit'''

# user = int(input('Enter number: '))

# if user < 10:
# 	print('One digited.')
# elif user > 9 and user < 100:
# 	print('Two digited.')
# elif user > 99 and user < 1000:
# 	print('Three digidet')
# else:
# 	print('More than three digited.')



'''9.The given character is an uppercase letter or
lowercase letter or a digit or a special character.
Use ord().
input >> @
output >> @ - Special character'''

# user = input('Enter char: ')

# if ord(user) > 64 and ord(user) < 90:
# 	print('Mecatar')
# elif ord(user) > 31 and ord(user) < 65:
# 	print('Char')
# elif ord(user) > 96 and ord(user) < 123:
# 	print('Poqratar')
# else:
# 	print('Number')