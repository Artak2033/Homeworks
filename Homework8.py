'''1.Write a Python program to calculate a dog's age in human years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that,
each dog year equals 4 human years.'''

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



'''2.Write a Python program to check whether an alphabet is a vowel or
consonant.'''

# vowels = 'aeiou'
# const = 'bcdfghjklmnpqrstvwxyz'

# user = input('Enter a letter: ').lower()

# if user in vowels:
# 	print('This letter is vowel.')
# else:
# 	print('This letter is constant.')



'''3. Write a Python program to check this year is leap year or no.'''

year = int(input("Year: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
	print(year," Leap year")
else:
    print(year," Non leap year")


'''4.Write a Python program to check if your number is odd or even.'''

# num = int(input('Number: '))

# if num % 2 == 0:
# 	print('The number is even.')
# else:
# 	print('The number is odd.')



'''5. Write a python program which will say who win in game.
The winner is the one which have 2 point.You should try to find pc number(0-5):
if find (your point +=1) otherwise (pc point +=1):'''

# from random import randint as r

# pc = r(0,5)
# user = int(input('Enter first number 0-5: '))
# pc1 = r(0,5)
# user1 = int(input('Enter second number 0-5: '))

# pc_score = 0
# user_score = 0

# if user == pc and user1 == pc1: 
# 	user_score += 2
# if user != pc or user1 != pc1:
# 	pc_score += 2
	
# print('First Pc number: ',pc)
# print('Second Pc number: ',pc1)
# print('Pc score: ',pc_score)
# print('User score: ',user_score)


'''6.Write a python program to Check if a Number is Positive, Negative or 0.'''

# user = float(input('Enter a number: '))

# if user > 0:
# 	print('The number is Positive.')
# if user == 0:
# 	print('The number is Zero.')
# if user < 0:
# 	print('The number is Negative.')