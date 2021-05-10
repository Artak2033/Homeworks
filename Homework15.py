'''1.Create new list which have 6 different data types.
For example: str, int'''

# my_list = [21,12.23,'OK',True,(1,2),[5,6]]
# print(my_list)



'''2.Create new list which have data notebooks and you want check if the data have Mac?
For example: my_list = [“Hp”, “Asus”, “Dell”, “Mac”, ”Lenovo”]
output: True'''

# my_list = ['Hp','Asus', 'Dell', 'Mac','Lenovo']

# user = input('Choose notebook: ')

# if user == 'Mac':
# 	print(user,'True')
# else:
# 	print(user,'False')



'''3.Create python program which will check if your password is strong
or no. if Len your password is great than 8 and if your password have
2 numbers and 2 of the following special characters ('!', '@', '#', '$', '%',
'&', '*') Sample Input: Python@$World11
 Sample Output: Strong'''

# char = '!@#$%^&*()-=+_'

# num_c = 0
# char_c = 0

# while True:
# 	password = input('Create password: ')

# 	if len(password) < 8:
# 		print('Strong password len is 8+')
# 		continue

# 	if not password[0].isupper():
# 		print('Write first letter upper')
# 		continue

# 	for i in password:
# 		if i.isdigit():
# 			num_c += 1
# 		elif i in char:
# 			char_c += 1

# 	if num_c < 2 and char_c < 2:
# 		print('Write 2 numbers and 2 chars in your password.')
# 		continue
# 	print('Strong password.')
# 	break



'''4.Create python program where you want to find id in link if link have id print id.
Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU
Sample Output: RWW2aUSwvU '''

# link = 'https://www.youtube.com/watch?v=RRW2aUSw5vU'

# print(link[link.index('=')+1:]) 



'''5.Create python program where you want to check if input word is
palindrome or no .if yes print Open otherwise Trash
Sample Input: RACECAR
Sample Output: Open'''

# user = input('Enter word: ')

# if user == user[::-1]:
# 	print('Palindrome.',user)
# else:
# 	print('Non palindrome.')



'''6.Create python program to convert string to a list.'''

# string = 'Hello world'

# c = []

# c.append(string)
# print(type(c))



'''7.Create python program which will show all even numbers in your string. Note: you have input where have 5 numbers:
Sample Input: 12 21 15 19 8
Sample Output: 12 8'''

# user = [12,21,15,19,8]

# x = 0

# for i in range(len(user)):
# 	if user[x] % 2 != 0:
# 		user.remove(user[x])
# 		x -= 1
# 	x += 1
# print('Result',user)



'''8.Write a Python program to select the odd items of a list. And delete even items.'''

# num_list = [1,2,3,4,5,6,7,8,9,10]
# print(num_list)

# z = 0

# for i in range(len(num_list)):
# 	if num_list[z] % 2 == 0:
# 		del num_list[z]
# 		z -= 1
# 	z += 1
# print('Odd numbers.',num_list)



'''9.Your group have 5 people and each of them can take one name and when take this name is delete
from this list.And he can not take his name:'''

# group = ['Ann','Aram','Ani','Artak','Lili']

# while True:
# 	name = input('Enter name: ')

# 	if group == []:
# 		print('All name')
# 		break
# 	if name not in group:
# 		print('No name.')
# 	if name in group:
# 		group.remove(name)
# 		print(group)	