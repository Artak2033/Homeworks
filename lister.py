# my_string = 'Hi my friend, thanks'
# 
# my_string = list(my_string)

# my_string = my_string.split(' ')
# print(my_string)



# fruits = ['banana','apple','cherry']
# fruits[1] = 'kiwi'
# print(fruits)



# l = list(range(0,1000,2))
# print(l)



# fruits = ['banana','apple','cherry']
# fruits.append('orange')
# print(fruits)



# fruits = ['banana','apple','cherry']
# fruits.insert(1,'orange')
# print(fruits)



# l = ['Ani','Anna','Sona','Ani']
# l.remove('Ani')
# print(l)



'''1 Tarberak'''

# my_list = [1,2,3,5,6,9,8,10,12]
# length = len(my_list)
# count = 0

# for i in range(length):	
# 	if my_list[count] % 2 == 0:
# 		my_list.remove(my_list[count])
# 		count -= 1
# 	count += 1
# print(my_list)



'''2 Tarberak'''

# my_list = [1,2,3,5,6,9,8,10,12]
# res = []

# for i in my_list:
# 	if i % 2 != 0:
# 		res.append(i)
# print(res)



# my_list = [1,2,3,5,6,9,8,10,12]

# c = my_list.pop()

# print(c)
# print(my_list)



# fruits = ['banana','apple','cherry']
# del fruits[2]
# del fruits
# print(fruits)



fruits = ['banana','apple','cherry']
numbers = [12,45,-454,7.23]
fruits.extend(numbers)
print(fruits)



# my_list = [123,21,32,5,6,9,8,10,12]

# my_list.sort()

# print(sorted(my_list))
# print(my_list)



# my_list = [i for i in range(10)]
# print(my_list)

# my_list = [i ** 2 for i in range(100) if i % 2 == 0]



# my_list = [i for i in range(1000) if i % 2 != 0]
# print(my_list)