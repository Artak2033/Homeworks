'''1. Write a Python program to count the elements in a list until an element is a tuple.'''

# var_tuple = (123,'Yes','Aram',2021,('ok','no'))

# c = 0

# for i in var_tuple:
# 	if type(i) != tuple:
# 		c+=1
# 		print(i,c)
		


'''2.Write a Python program to reverse a tuple.'''

'''1 Tarberak'''
# num = (1,2,3,4,5,6)
# x = reversed(num)
# print(tuple(x))


'''2 Tarberak'''
# print(num[::-1])



'''3.Write a Python program to find the length of a tuple.'''

''' 1 Tarberak '''
my_tuple = ('Mac','Apple',1154,'Hi',('adaf','asfaf'),('OK','NO'))
# print(len(my_tuple))


''' 2 Tarberak '''
c = 0
for i in my_tuple:
	c+=1
print('Length of tuple: ',c)



'''4.Write a Python program to convert a tuple to a string.'''

# var_tuple = ('a','b','c')

# var_str = "".join(var_tuple)
# print(var_str)
# print(type(var_str))



'''5.Write a Python program which calculate the count of item in
tuple for example: my_tuple = (1,12,15) output:28.'''

'''1 Tarberak'''
# my_tuple = (1,12,15)
# print(sum(my_tuple))

'''2 Tarberak'''
# my_tuple = (1,12,15)
# c = 0
# for i in my_tuple:
# 	c += i
# print(c)



'''6.Write a Python program to find name in tuple'''

# name_tuple = ('Ani','Aram','Ann')

# name = input('Enter name: ')

# if name in name_tuple:
# 	print('ok')
# else:
	# print('no')