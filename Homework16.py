'''1.Write a Python program to sort a dictionary by value.'''

# dictionary = {'a':3,'b':9,'q':7}

# print(sorted(dictionary.values()))



'''2.Write a Python program to add a key to a dictionary.'''

# my_dict = {'Ani':5,'Aram':6}

# my_dict['Ann'] = 7

# print(my_dict)



'''3.Write a Python program to check whether a given key already exists in a dictionary.'''

# dictionary = {'Ani':5,'John':6,'Mary':10,'Ashot':2,'Ruben':10}

# user = input('Enter key: ')

# if user in dictionary.keys():
# 	print('True')
# else:
# 	print('False')



'''4.Write a Python program to merge two Python dictionaries.
dict1 = {'a': 50, 'b': 700}
dict2 = {'c': 400, 'd': 600}
output: {'a': 50, 'b': 700, 'c': 400, 'd': 600}'''

# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}

# dict1.update(dict2)

# print(dict1)



'''5.Write a Python program to multiply all the values in a dictionary.
For example:
mydict = {'a':1,'b':2,'c':12} output: 24'''

# mydict = {'a':1,'b':2,'c':12}

# c = 1

# for i in mydict.values():
# 	c *= i
# print('Result: ',c)



'''6.Create a Python program to find the highest 3 values in a dictionary.
{'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
output: {'F': 69, 'A': 67, 'D': 56}'''

# dictionary = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}

# c = sorted(dictionary.values()) [-3:]

# for i in c:
# 	for j in dictionary:
# 		if i == dictionary[j]:
# 			print(j,i)