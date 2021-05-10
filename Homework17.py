'''1.Create new dictionary where you have 10 students and each of them have rating(1-10).'''

# students = {'Aram':5,'Ann':7,'Ani':3,'Ashot':9,'Yana':10,'Karen':6,'Mane':10,'Artur':4,'Kara':6,'Narek':3}
# print(students)



'''2.Create python program which will calculate the arithmetic average of rating students.'''

# students = {'Aram':5,'Ann':7,'Ani':3,'Ashot':9,'Yana':10,'Karen':6,'Mane':10,'Artur':4,'Kara':6,'Narek':3}

# c = 0

# for i in students.values():
# 	c += i
# print('Arithmetic average of raitings: ',c / len(students))



'''3.Create a python program which says good and bad students names and ratings.'''

# students = {'Aram':5,'Ann':7,'Ani':3,'Ashot':9,'Yana':10,'Karen':6,'Mane':10,'Artur':4,'Kara':6,'Narek':3}

# c = sorted(students.values())

# for i in students:
# 	if students[i] == c[-1]:
# 		print('Good students: ',i,c[-1])
# 	elif students[i] == c[0]:
# 		print('Bad students: ',i,c[0])



'''4.Create a python program which says whose grades are greater or equal to 5. '''

# students = {'Aram':5,'Ann':7,'Ani':3,'Ashot':9,'Yana':10,'Karen':6,'Mane':10,'Artur':4,'Kara':6,'Narek':3}

# for i in students:
# 	if students[i] >= 5:
# 		print(i,students[i])



'''5.Create a python program which will say who have 5 or little rating in your Students.'''

# students = {'Aram':5,'Ann':7,'Ani':3,'Ashot':9,'Yana':10,'Karen':6,'Mane':10,'Artur':4,'Kara':6,'Narek':3}

# for i in students:
# 	if students[i] <= 5:
# 		print(i,students[i])



'''6.Create a python program which will say if your dictionary have this name print name and rating.'''

# students = {'Aram':5,'Ann':7,'Ani':3,'Ashot':9,'Yana':10,'Karen':6,'Mane':10,'Artur':4,'Kara':6,'Narek':3}

# user = input('Enter student name: ')

# for i in students.keys():
# 	if user == i:
# 		print(i,students[i])


'''7.Create a new dictionary:For example…
s = 'a,2,b,5,c,8,a,4,e,11'
{“a”:6,”b”:5,”c”:8,”e”:11}'''

# s = 'a,2,b,5,c,8,a,4,e,11'.split(',')

# res = {}

# for i in range(0,len(s),2):
# 	if s[i] in res:
# 		res[s[i]] += int(s[i+1])
# 	else:
# 		res[s[i]] = int(s[i+1])
# print(res)	




'''8.Create a dictionary from a string.Get the count of the letters from the string.
word = ‘exercises’
output: {“e”:3,”x”:1,”r”:1,”c”:1,”s”:2}'''

# word = 'exercises'

# c = {}

# for i in word:
# 	c[i] = word.count(i)
# print(c)



'''9.Remove all duplicate items in list.
old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
output:
new_list = [{'key1':'value1'},{},{'key2':'value2'}]'''

# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]

# new_list = []

# for i in old_list:
# 	if i not in new_list:
# 		new_list.append(i)
# print('New list: ',new_list)



'''10.Write a Python program to join adjacent members of a given list.
Original list:
['1', '2', '3', '4', '5', '6', '7', '8']
Join adjacent members of a given list:
['12', '34', '56', '78']'''

# my_list = ['1','2','3','4','5','6','7','8']

# res = []

# for i in range(0,len(my_list),2):
# 	res.append(my_list[i] + my_list[i+1])
# print(res)



'''11.Create a python game Millionaire.'''

print('\n\t\t***** MILLIONAIRE GAME *****')

count = 0

while True:

	quest1 = input('\nQuestion 1: 500 AMD \n\n24 + 5 = \na)28\tb)29\nc)30\td)27\n\nYour answer: ').lower()
	if quest1 == 'b' or quest1 == '29':
		count += 500
		print('Right answer: ',count,'AMD')
	else:
		print('You lose, Your score is 0')
		break

	quest2 = input('\n\nQuestion 2: 1500 AMD \n\nFactorial of 0 = \na)1\tb)0\nc)10\td)2\n\nYour answer: ').lower()
	if quest2 == 'a' or quest2 == '1':
		count += 1500
		print('Right answer: ',count,'AMD')
	else:
		print('You lose, Your score is 0')
		break

	quest3 = input('\n\nQuestion 3: 5000 AMD \n\n5 * 4 - 5 = \na)16\tb)14\nc)15\td)17\n\nYour answer: ').lower()
	if quest3 == 'c' or quest3 == '15':
		count += 5000
		print('Right answer: ',count,'AMD')
	else:
		print('You lose, Your score is 0')
		break

	quest4 = input('\n\nQuestion 4: 10.000 AMD \n\nMath PI = \na)1\tb)3.13\nc)3\td)3.14\n\nYour answer: ').lower()
	if quest4 == 'd' or quest4 == '3.14':
		count += 10000
		print('Right answer: ',count,'AMD')
	else:
		print('You lose, Your score is 0')
		break

	quest5 = input('\n\nQuestion 5: 20.000 AMD \n\nCapital of Russia :  \na)Moscow\tb)Saints-Peterburgs\nc)Kiev\td)Kazan\n\nYour answer: ').lower()
	if quest5 == 'a' or quest5 == 'Moscow':
		count += 20000
		print('Right answer: ',count,'AMD')
	else:
		print('You lose, Your score is 0')
		break

	user = input('\n\nYou chose the correct answer 5 times,\nYou can take money or continue the game.Continue?   (Y or N)\n').upper()

	if user == 'N':
		print('Your choice are money: ',count,'AMD')
		break
	elif user == 'Y':
		quest6 = input('\n\nQuestion 6: 35.000 AMD \n\nHow many colors are on a flask of Armenia :  \na)2\tb)3\nc)4\td)1\n\nYour answer: ').lower()
		if quest6 == 'b' or quest6 == '3':
			count += 35000
			print('Right answer: ',count,'AMD')
		else:
			print('You lose, Your score is 0')
			break

		quest7 = input('\n\nQuestion 7: 50.000 AMD \n\nHow many players are on the basketball team :  \na)5\tb)7\nc)9\td)8\n\nYour answer: ').lower()
		if quest7 == 'a' or quest7 == '5':
			count += 50000
			print('Right answer: ',count,'AMD')
		else:
			print('You lose, Your score is 0')
			break

		quest8 = input('\n\nQuestion 8: 100.000 AMD \n\nMain mach time in football:  \na)45\tb)90\nc)40\td)80\n\nYour answer: ').lower()
		if quest8 == 'b' or quest8 == '90':
			count += 100000
			print('Right answer, Your score: ',count,'AMD')
		else:
			print('You lose, Your score is 0')
			break

		quest9 = input('\n\nQuestion 9: 250.000 AMD \n\nHow many letters are in the english alphabet :  \na)27\tb)25\nc)26\td)28\n\nYour answer: ').lower()
		if quest9 == 'c' or quest9 == '26':
			count += 250000
			print('Right answer: ',count,'AMD')
		else:
			print('You lose, Your score is 0')
			break


		user1 = input('\n\nYou have reached the last question.The game will end if you take money.If the answer is wrong you will lose all your money.\n Continue? : Y or N\n\n').upper()	

		if user == 'Y':
			print('Your choice are money: ',count,'AMD')
			break
		elif user == 'N':
			quest10 = input('\n\nFinally question: 1.000.000 AMD \n\nHow many letters are in the English alphabet :  \na)27\tb)25\nc)26\td)28\n\nYour answer: ').lower()
		if quest10 == 'c' or quest10 == '26':
			print('\t\t\t*** You win the game,your score: 1.000.000 AMD ***')
			break
		else:
			print('You lose, Your score is 0')
			break