'''1.Create 5 file (.txt) and write messages in them.'''

# file_name = 'Test1.txt'

# def create_file(file_name):
# 	file = open(file_name,'w')
# 	file.write('Homework')
# 	file.close()
# create_file(file_name)



# file_name2 = 'Test2.txt'

# def create_file(file_name):
# 	file = open(file_name,'w')
# 	file.write('Homework2')
# 	file.close()
# create_file(file_name2)


# file_name3 = 'Test3.txt'

# def create_file(file_name):
# 	file = open(file_name,'w')
# 	file.write('Homework3')
# 	file.close()
# create_file(file_name3)


# file_name4 = 'Test4.txt'

# def create_file(file_name):
# 	file = open(file_name,'w')
# 	file.write('Homework4')
# 	file.close()
# create_file(file_name4)


# file_name5 = 'Test5.txt'

# def create_file(file_name):
# 	file = open(file_name,'w')
# 	file.write('Homework5')
# 	file.close()
# create_file(file_name5)



'''2.Write a Python program to read first n lines of a file.'''

# file_name5 = 'Test5.txt'

# file = open(file_name5,'r')
# print(file.readline())	



'''3.Write a Python program to append text to a file and display the text.'''

# file_name = 'Test1.txt'

# file = open(file_name,'a')
# file.write('Append')

# file2 = open(file_name,'r')
# print(file2.read())




'''4.Write a python program to find the longest words.'''

# file_name = 'Test1.txt'

# def longest_words(file_name):

# 	x = 0
# 	c = []

# 	with open(file_name,'r') as f:

# 		words = f.read().split()
# 		print(words)

# 		for i in words:
# 			if len(i) > x:
# 				x = len(i) 
# 		print(i)

# longest_words(file_name)





'''5..Write a python program to find numbers in txt.'''

# file_name = 'Test1.txt'
# c = []


# file = open(file_name,'r')
# read = file.read()

# for i in read:
# 	if i.isdigit():
# 		c += i

# print(read)
# print('Numbers in text: ',c)



'''6.Write a python program to get login and password.'''

# with open('Test3.txt','a') as f:

# 	login = input('Input Login: ')
# 	password = input('Input Password: ')

# 	result = f"Login: {login}	 Password: {password}\n"

# 	f.write(result)
# print(f.closed)