'''1.Given three numbers a, b (a ≤ b) and step. Create an list of
evenly spaced elements starting from a to b spaced by
step. you have 3 argument'''

# def numbers():

# 	a = int(input('First number: '))
# 	b = int(input('Last number: '))
# 	step = int(input('Step: '))

# 	c = []

# 	for i in range(a,b+1,step):
# 		c.append(i)
# 	print(c)

# numbers()



'''2.Write a function. Create the list which elements are
products between two neighbours.'''

# def func():

# 	my_list = [3, 7, 12, 5, 20, 0]
# 	new_list = []

# 	res = [my_list[i] * my_list[i + 1] for i in range(len(my_list) - 1)]

# 	new_list.append(res)

# 	print(res)

# func()



'''3.Given a sentence with missing words and an array ofwords.
Replace all ‘_’ in a sentence with the words from the array.'''

# sentence = '_ , we have a _ .'.split(' ')
# word = ['Ashot','problem']

# c = 0


# for i in range(len(sentence)):
# 	if sentence[i] == '_':
# 		sentence[i] = word[c]
# 		c += 1
# print(' '.join(sentence))



'''4.Given a list of strings. Find the strings with maximum and
minimum lengths in array. Print the sum of their lengths.'''

# sentence = ['anymore', 'raven', 'me', 'communicate']

# res = [len(i) for i in sentence]
# print(min(res) + max(res))



'''5.Given a list of numbers and a number. Find the index of a
first element which is equal to that number. If there is not
such a number, that find the index of the first element
which is the closest to it.'''

# def num():

# 	my_list = [21,-9,15,2116,-71,33]
# 	new_list = []

# 	number = int(input('Number: '))

# 	for i in range(len(my_list)):
# 		res = abs(number - my_list[i])
# 		new_list.append(res)

# 	print(new_list.index(min(new_list)))

# num()



'''6.Define a function which can generate a dictionary where
the keys are numbers between 1 and N (both included) and
the values are square of keys. The function should print the
dict.'''


# def gen():

# 	num = int(input('Number: '))
# 	return {i:i**2 for i in range(1,num+1)}

# print(gen())



'''7.Given an dict. Invert it (keys become values and values
become keys). If there is more than key for that given value
create an list.'''


# my_dict = {'a':'1', 'b':'2', 'c':'2'}
# new_dict = {value:key for (key,value) in my_dict.items()}

# print(new_dict)



'''8.Write a function using recursion to find fibonacci numbers:'''

# def fibo(num):

# 	if num == 1:
# 		return 0
# 	elif num == 2:
# 		return 1
# 	else:
# 		return fibo(num - 1) + fibo(num - 2)

# print(fibo(7))