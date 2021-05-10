# students = {'Aram':5,'Ann':6,'Yana':10,'Sona':7,'Karen':3,'Ashot':9,'Zara':10,'Kara':9,'Suren':5,'Sara':6}

# c = 0
# for i in students.values():
# 	c += i
# print('Mijin: ',c / len(students))



# z = sorted(students.values())

# for i in students:
# 	if students[i] == z[-1]:
# 		print(i,z[-1])
# 	elif students[i] == z[0]:
# 		print(i,z[0])



# for i in students:
# 	if students[i] > 5:
# 		print(i,students[i])



# user = input('Enter student name:')

# if user in students:
# 	print('True')
# else:
# 	print('False')



# s = 'a,2,b,5,c,8,a,4,e,11'.split(',')
# res = {}

# for i in range(0,len(s),2):
# 	if s[i] in res:
# 		res[s[i]] += int(s[i+1])
# 	else:
# 		res[s[i]] = int(s[i+1])
# print(res)



# word = 'exercises'

# c = {}

# for i in word:
# 	c[i] = word.count(i)
# print(c)



# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]

# c = []

# for i in old_list:
# 	if i not in c:
# 		c.append(i)
# print(c) 



# my_list = ['1','2','3','4','5','6','7','8']

# res = []

# for i in range(0,len(my_list),2):
# 	res.append(my_list[i] + my_list[i+1])
# print(res)



my_list = ['Aram','Ann','Yana','Sona','Karen','Ashot','Zara','Kara','Suren','Sara']

c = []

for i in range(0,len(my_list),2):
	c.append(my_list[i])
print(c)