'''1.Write a python function to create a simple Calculator.'''

# def test(num1,num2):
# 	res = f"{num1} + {num2} = {num1 + num2}"
# 	print(res)

# num1 = float(input('Input first number: '))
# num2 = float(input('Input second number: '))

# test(num1,num2)



'''2.Write a python function to find max of two numbers.'''

# def number(num1,num2):
# 	if num1 > num2:
# 		return num1
# 	else:
# 		return num2

# num1 = float(input('Input number: '))
# num2 = float(input('Input number: '))

# print(number(num1,num2))



'''3.Write a python function to sum all numbers.'''

# def num(numbers):
# 	count = 0
# 	for i in numbers:
# 		count += i
# 	return count
# print(num((1,2,3,4,5)))



'''4.Write a python function to multiply all numbers.'''

# def multy(numbers):
# 	count = 1
# 	for i in numbers:
# 		count *= i
# 	return count
# print(multy((1,2,5,5,2)))



'''5.Write a python program to sum all letter and number in your string.'''

# def text(user):
# 	letters = 0
# 	number = 0
# 	for i in user:
# 		if i.isdigit():
# 			number += 1
# 		if i.isalpha():
# 			letters += 1
# 	return('Letters; ',letters,'Numbers: ',number)

# user = input('Input text: ')

# print(text(user))



'''6.You are given a program that takes all 3
passengers ages as inputs and inserts them in
a list. Complete the program so that if it
finds a value less than 16, it breaks the
loop and outputs "Too young! ".
If the age requirement is satisfied, the
program outputs "Get ready!".'''


def people(*args):

	for i in my_list:
		if i < 16:
			return('Too young!')
		else:
			print('Get ready!')
age1 = int(input('How old are you? '))
age2 = int(input('How old are you? '))
age3 = int(input('How old are you? '))

my_list = [age1,age2,age3]

print(people(my_list))
