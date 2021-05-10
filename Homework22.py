'''1.Write a python function which conversion kilometer to miles.'''

# def kmconvert(km):
# 	res = km / 1.6
# 	return res
# km = int(input('Input Km: '))

# print(kmconvert(km))



'''2.Write a python function which conversion days to seconds.'''

# def dayconvert(day):
# 	result = day * 24 * 60 * 60
# 	return result

# day = int(input('Input day: '))
# print(dayconvert(day))



'''3.Write a python function which generate a valid password.'''

# import random
# import string

# def valid_pass():

# 	letter = string.ascii_letters
# 	numbers = string.digits
# 	chars = string.punctuation

# 	password = ''

# 	for i in range(4):
# 		x = random.choice(letter)
# 		password += x
# 	for i in range(2):
# 		x = random.choice(numbers)
# 		password += x
# 	for i in range(2):
# 		x = random.choice(chars)
# 		password += x

# 	password = list(password)
# 	random.shuffle(password)
# 	return ''.join(password)\

# print(valid_pass())



'''4.Factorial'''

# from functools import reduce

# user = int(input('Enter number: '))

# res = reduce(lambda x,y: x * y, range(1,user+1))
# print('Factorial = ',res)



'''5.Given an list of numbers.Find the maximum element in
list.Without use max function.'''


# def max(num_list):

# 	count = 0
# 	for i in num_list:
# 		if i > count:
# 			count = i
# 	return count

# num_list = [2,4,5,1,48,3,7,8,25]
# print(max(num_list))



'''6.Write a Python program which will remove all zeros from an IP address.
ip = "216.008.094.196"'''

# def ipzero(ip):
	 
# 	ip_list = []

# 	for i in ip:
# 		if i != '0':
# 			ip_list.append(i)
# 	print(ip_list)

# ipzero("216.008.094.196")	



'''7.Imagine you and the computer are playing tennis.
write a program where you have a sheet where victory
points are kept and you need to figure out who is the
winner.A set is won by the first side to win 6 games.
You should to show the result of the match. If game
win you in list add “a” if pc “b”.'''

# results = ['b','a','a','a','a','a','a','a','a','a','a','a','b','b','b','b','b','b','a','a',
# 'a','a','a','b','b','b','b','b','a','a','a','a','a','b','a','a','a','a','a','a','a','a','a','a']

# pc = 0
# user = 0 

# pc_count = 0
# user_count = 0

# num = 6

# for i in results:
# 	if i == "a":
# 		user_count += 1
# 	else:
# 		pc_count += 1

# 	if user_count == pc_count and user_count > 4:
# 		num += 1

# 	if user_count == 6:
# 		print('User win!',user_count,'Pc: ',pc_count)
# 		user += 1
# 		user_count = 0
# 		num = 6

# 	if pc_count == 6:
# 		print('Pc win!',pc_count,'User: ',user_count)
# 		pc += 1
# 		pc_count = 0
# 		num = 6

# print('User: ',user,'Pc: ',pc)

