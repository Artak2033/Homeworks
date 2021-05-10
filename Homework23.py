# '''Calculator'''

def calculator():

	while True:
		try:
			a = int(input('Input first number: '))
			b = int(input('Input second number: '))
			operation = input('Choose operation + - / * : ')
		except ValueError:
			print('Input only number.')
			continue
		except KeyboardInterrupt:
			print("\nProgram closed.")
			break


		if operation == '+':
			print('Result: ',a + b)

		elif operation == '-':
			print('Result: ',a - b)	

		elif operation == '/':
			try:
				print('Result: ',a / b)	
			except ZeroDivisionError:
				print('Only positive number.')

		elif operation == '*':		
			print('Result: ',a * b)
					
calculator()




'''Password'''

# password = input('Input password: ')


# number_count = 0
# char_count = 0

# char = ('!@#$%^&*')

# try:
# 	if len(password) < 8:
# 		raise Exception ("Password len must be 8+")
# except Exception as r:
# 	print(r)

# try:
# 	if not password[0].isupper():
# 		raise Exception ("First letter must be upper.")
# except Exception as r:
# 	print(r)


# for i in password:
# 	try:
# 		if i.isdigit():
# 			number_count += 1		
# 		if number_count < 2:				
# 			raise Exception ("In password must be 2 number.")
# 	except Exception as r:
# 		print(r)

# 	try:
# 		if i in char:
# 			char_count += 1
# 		if char_count < 2:
# 			raise Exception ("In password must be 2 char.")
# 	except Exception as r:
# 		print(r)
