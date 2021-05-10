'''1.Write a Python program to check if pc
number is great than 10. random(1,20)
when True break.'''

# import random

# while True:
# 	pc = random.randint(1,20)
# 	if pc <= 10:
# 		print(pc)
# 		continue
# 	if pc > 10:
# 		print(pc)
# 		break



'''2.Create a program that will display the numbers
from 1 to 50 which is divisible by 5.'''

# for i in range (1,51):
# 	if i % 5 == 0:
# 		print(i)



'''3.Display the numbers from 1 to 10 except 5.
Expected Output: 1 2 3 4 5 7 8 9 10 '''

# for i in range(1,11):
# 	if i == 5:
# 		continue
# 	print(i)	



'''4.ChingaChung'''

# import random

# pc = 'QTM'
# user = 'QTM'

# pc_score = 0
# user_score = 0

# while True:
# 	var_user = input('User QTM: ').upper()
# 	var_pc = random.choice(pc)
# 	print('Pc QTM: ',var_pc)
# 	if user_score == 3 or pc_score == 3:
# 		print('User score: ',user_score)
# 		print('Pc score: ',pc_score)
# 		break
# 	if var_pc == 'Q' and var_user == 'M' or var_pc == 'T' and var_user == 'Q' or var_pc == 'M' and var_user == 'T':
# 		pc_score+=1
# 		print('Pc score: ',pc_score)
# 		continue
# 	elif var_pc == var_user:
# 		print('Voch voqi:')
# 		continue
# 	elif var_user == 'Q' and var_pc == 'M' or var_user == 'T' and var_pc == 'Q' or var_user == 'M' and var_pc == 'T':
# 		user_score+=1
# 		print('User score: ',user_score)
# 		continue
	
		