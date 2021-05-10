'''1.Write a Python program to sum all the items in a list.'''
 
''' Tarberak 1'''
# num_list = [5,10,65]
# print(sum(num_list))


'''Tarberak 2'''
# num_list = [5,10,65]
# c = 0
# for i in num_list:
# 	c+=i
# print('Sum: ',c)



'''2.Write a Python program to multiplies all the items in a list.'''

# num_list = [2,5,3,5,2]
# c = 1
# print(num_list)

# for i in num_list:
# 	c*=i
# print('Multiplies result: ',c)



'''3.Write a Python program to get the largest text from a list.'''

text_list = ['I','asdfgh','day','school','py',]

c = 0

for i in text_list:
	if len(i) > c:
		c = len(i)
		res = i
print('Largest word: ',res)



'''4.Write a Python program that have two lists and returns True if they have at least
one common member.'''

# list1 = ['apple','orange','red','black']
# list2 = ['banana','red','green','yellow']

# for i in list1:
# 	if i in list2:
# 		print('Repeat word: ',i)
# 		break	
# else:
# 	print('No Repeat')



'''5.Write a Python program to Sort Words in Alphabetic Order'''

# my_list = ['Ann','Ford','Down','Case','Ball','English']
# print(my_list)

# my_list.sort()
# print(my_list)