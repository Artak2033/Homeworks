from random import randint as r

# x = None
# print(x)
# print(type(x))

# print(True + True)
# print(True + False)
# print(False + False)

# print(True + True == 2)

# print(None == False)
# print(None == 0)
# print(None == True)
# print(None == '')

# print(None is None)
# print(None == None)

# print('Ani')
# print(None)


# a = 27
# b = 14

# if b > a:
# 	print('b is big')
# elif a > b:
# 	print('a is big')


# a = 34
# b = 14

# if b > a:
# 	print('b is big')
# else:
# 	print('a is big')

# pc = r(1,6)
# user = int(input('User '))

# if pc > user:
# 	print('pc',pc,'>',user,'user')
# elif pc == user:
# 	print('pc',pc,'=',user,'user')
# else:
# 	print('pc',pc,'<',user,'user')



# user = int(input('Age '))

# if user > 16 and user < 30:
# 	print('Entered')
# else:
# 	print('Sorry')



# user = int(input('Age '))

# if user > 16:
# 	if user < 30:
# 		print('Entered')
# 	else:
# 		print('Meceq 30')
# else:
# 	print('Poqr eq 16')


# num = float(input('Enter a number: '))

# if num >= 0:
# 	if num == 0:
# 		print('Zero')
# 	else:
# 		print('Positive number')
# else:
# 	print('Negative number')


# res = None

# if res is True:
# 	print('Do you think None is True?')
# elif res is False:
# 	print('Do you think None is False?')
# else:
# 	print('None is not True, or False, None is just None...')



# name = input('name ')

# if name.isalpha():
# 	print('Good!')
# else:
# 	print('Name only')



# age = input('Age: ')

# if age.isdigit():
# 	print('OK')
# else:
# 	print('Only age')



# password = input('Password: ')

# if password.istitle():
# 	print('OK')
# else:
# 	print('First letter Upper must be in password')


# name = input('name ')

# if name.isupper():
# 	print('Name is upper')
# else:
# 	print('Name is lower')


# name = input('name ')

# if name.islower():
# 	print('Name is lower')
# else:
# 	print('Name is upper')


# word = input('Word: ')

# word = word.capitalize()
# print(word)


# a = input()
# print(a.capitalize())



# phone = 'iphone samsung'
# color = 'black red green'

# user = input('Choose phone: ')
# user1 = input('Choose phone color: ')

# if user in phone:
# 	if user1 in color:
# 		print('phone exists Color arka')
# 	else:
# 		print('heraxosy unenq Color arka che')
# else:
# 	print('Phone arka che')



# dog_age = input('Dog age: ')

# if dog_age.isdigit():
# 	dog_age = int(dog_age)
# 	if dog_age < 0:
# 		print('Please input positiv number')
# 	elif dog_age >= 0 and dog_age <= 2:
# 		human_age = dog_age * 5.25
# 		print('Human age: ',human_age)
# 	else:
# 		human_age = 10.5 + (dog_age - 2) * 4
# 		print('Human age:',human_age)
# else:
# 	print('Please input only numbers')



# num = int(input('Enter number: '))

# if num % 2 == 0:
# 	print('Number zuyg')
# else:
# 	print('Number zuyg che')


user = input('Enter word: ')

if user.isalpha():
	print('Enter str')
	if user == user.capitalize():
		print('Good')
	else:
		print('Error')
else:
print('Norm')	
