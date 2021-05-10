'''Password'''

# c = '!@#$%^&*()-_+'

# while True:
# 	number_c = 0
# 	char_c = 0

# 	password = input('Enter your password.')

# 	if len(password) < 8:
# 		print('Your password length must be great than 8.')
# 		continue

# 	if not password[0].isupper():
# 		print('First letter must be upper.')
# 		continue
# 	for i in password:
# 		if i.isdigit():
# 			number_c += 1
# 		elif i in c:
# 			char_c += 1

# 	if number_c < 2 and char_c < 2:
# 		print('Your password must be have two numbers and chars.')
# 		continue
# 	print('Strong!')
# 	break



# link = 'https://www.youtube.com/watch?v=RRw45gt4sd4print'
# print(link[link.index('=')+1:]) 


# user = input('Enter word:')

# if user == user[::-1]:
# 	print('OK')
# else:
# 	print('NO')



# l = [1,2,3,5,4,1,1]

# c = 0

# for i in range(len(l)):
# 	if l.count(l[c]) > 1:
# 		l.remove(l[c])
# 		c -= 1
# 	c += 1
# print(l)



# l = [1,2,3,5,4,1,1]

# c = []

# for i in l:
# 	if i not in c:
# 		c.append(i)
# print(c)




l = [1,2,4,5,7,8,9,10,12,14,19,21]

c = []
z = 0

for i in range(len(l)):
	if l[z] % 2 == 0:
		del l[z]
		z -= 1
	z += 1
print(l)