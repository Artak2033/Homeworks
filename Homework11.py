'''1.Write a Python program to find the smallest number which are
divisible by 12 and 15.'''

# a = int(input('First number: '))
# b = int(input('Second number: '))

# res = a * b

# for i in range(b,res):
# 	if i % a == 0 and i % b == 0:
# 		print(i)
# 		break



'''2.Write a Python program to count the number of even and odd
numbers from a series of numbers(1-100).'''

# num = int(input('Enter number: '))

# zuyg = 0
# kent = 0

# for i in range(1,num+1):
# 	if i % 2 == 0:
# 		zuyg += 1
# 	else:
# 		kent += 1
# print('Even numbers: ',zuyg,'\tOdd numbers: ',kent)

'''2 tarberak'''
# x = int(input('Enter number: '))
# zuyg,kent = x // 2, x // 2 + x % 2
# print('Zuyg: ',zuyg,'Kent',kent)


'''3.Write a Python program to get the Fibonacci series between 0
to 40:
Fib_num = 0,1,1,2,3,5,8 …..'''

# x = 0 
# y = 1
# print(x)

# while y < 40:
# 	print(y)
# 	x,y = y,x+y



'''4.Write a Python program that accepts a string and calculate
the number of digits and letters.
string = ‘python 3.9’'''

# digits = 0
# letters = 0

# string = 'python 3.9'

# for i in string:
# 	if i.isdigit():
# 		digits += 1
# 	if i.isalpha():
# 		letters += 1

# print('String:',string,'\nDigits:',digits,'\nLetters:',letters)



'''5.Write a Python program which have number (73421):
You should calculate (7 + 3 + 4 ….):'''

# num = input('Enter number: ')	
# count = 0	
	
# for i in str(num):
# 	if i.isdigit():
# 		count+=int(i)
# print(count)
	
	

'''6.Write a loop to find the factorial of any number. You have one input.'''

# num = int(input('Number: '))

# count = 1

# for i in range(1,num+1):
# 	count *= i
# print('Result: ',count)



'''7.Write a python program to compute the greatest
common divisor of two positive integers.
Example:
>>> input 14 8
>>> output 4'''

# x = int(input('First number: '))
# y = int(input('Second number: '))

# if x > y:
# 	res = y
# else:
# 	res = x

# for i in range(res,1,-1):
# 	if y % i == 0 and x % i == 0:
# 		print(i)
# 		break



'''8.Write a python program to compute the smallest
number that is divisible by both integer a and b.
Example:
>>> input 14 8
>>> output 2'''

# x = int(input('First number: '))
# y = int(input('Second number: '))

# if x > y:
# 	res = y
# else:
# 	res = x

# for i in range(2,res,+1):
# 	if y % i == 0 and x % i == 0:
# 		print(i)
# 		break



'''9.Write a python program to check if user age in (18-20) and if sex is male.'''

# age = int(input('Age: ')) 
# sex = input('Male or Female: ')


# if 17 < age < 21 and sex == 'Male':
# 	print('Age: ',age,'\nSex: ',sex)
# else:
# 	print('Your age is not 18-20 or sex is not male.')	