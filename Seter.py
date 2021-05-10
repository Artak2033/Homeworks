# my_list = [100,2,3,5,10,25,15]
# c = set(my_list)
# print(c)



# my_set = {'Ani','Aram','Arsen','Ani'}
# print(my_set)



# import random 

# my_list = [100,2,3,5,10,25,15]
# random.shuffle(my_list)
# print(my_list)



# my_set = {'Ani','Aram','Arsen','Ani'}
# print(len(my_set))



# my_set = {'Ani','Aram','Arsen','Ani'}
# for i in my_set:
# 	print(i)



# my_set = {'Ani','Aram','Arsen','Ani'}
# my_set1 = {1,2,3,4,5,6,7}

# my_set.add('Art')
# my_set.update(my_set1)
# print(my_set)



# my_set = {'Ani','Aram','Arsen','Ani'}

# my_set.remove('Ann')
# my_set.discard('Ann')
# print(my_set)



# my_set = {'Ani','Aram','Arsen','Ani'}
# my_set2 = {'Suren','Karen','Anna'}

# print(my_set.isdisjoint(my_set2))



# my_set = {'Ani','Aram','Arsen','Ani'}
# my_set2 = {'Suren','Karen','Anna','Aram'}

# print(my_set.intersection(my_set2))



# my_set = {'Ani','Aram','Arsen','Ani'}
# my_set2 = {'Suren','Karen','Anna','Aram'}

# print(my_set.symmetric_difference(my_set2))



# my_set = {'Ani','Aram','Arsen','Ani'}
# my_set2 = {'Suren','Karen','Anna','Aram'}

# c = my_set.intersection(my_set2)

# my_set.update(my_set2)

# for i in c:
# 	my_set.discard(i)
# print(my_set)



print('Millionaire')

question = {
	'When was the battle of Avarayrs\na)459 b)436\nc)451 d)561':'c',
	'When is the biggest mounthain \na)Everest b)Mauna Kea\nc)Ararat d)Tapa':'b'
}

a = ('a','b','c','d')
counter = 1
start = 500
balance = 0

for quest,answer in question.items():
	print(quest)

	while True:
		ans = input('Answer ').strip().lower()
		if ans in a:
			break
		else:
			print('Please input correct answer a, b, c, d')
	if ans == answer:
		counter += 1
		balance += start
		start *= 2
	else:
		balance = 0
		break

if balance > 0:
	print('You win',balance)
elif counter > 0:
	print('Loser',500)
else:
	print('Loser')