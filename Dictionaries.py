# thisdict = {'name':'Aram','year':1994}
# print(thisdict)



# test = {'Name':'Ani',"A":3}

# x = test.popitem()
# print(x)

# print(test)


# import datetime

# students = {'id':12345,'Name':'Aram','Email':None}

# name = input('Name: ')
# email = input('Email: ')
# date = datetime.date.today()

# if students['id'] == 12345:
# 	students['Name'] = name
# 	students['Email'] = email
# 	students['Create date'] = str(date)
# 	print(students)
	


# test = dict(brand = 'Gucci', price=1900, date = 2021)
# print(test)


# thisdict = {'name':'Aram','year':1994}
# del thisdict['year']

# print(thisdict)



# test = dict(brand = 'Gucci', price=1900, date = 2021)

# test.clear()
# print(test)
# c = test.copy()
# print(c)

# for i in test:
# 	print(i,test[i])

# for i in test.values():
# 	print(i)

# for i in test.keys():
# 	print(i)

# for i,j in test.items():
# 	print(i,j)	



# users = ('Ani','John','Mary')

# c = dict.fromekeys(users)
# print(c)




# users = ('Ani','John','Mary','Ashot','Ruben')
# raitings = (5,6,7,8,9)


'''my_students = dict.fromekeys(users,0)
print(my_students)'''

# c = {}
# for i,j in zip(users,raitings):
# 	c[i] = j
# print(c)



# dictionary = {'z':18,'b':10,'c':11,'g':17}

# print(sorted(dictionary.values()))
# print(sorted(dictionary.keys()))
# print(sorted(dictionary.items()))



# dictionary = {'Ani':5,'John':6,'Mary':10,'Ashot':2,'Ruben':10}

# l = max(dictionary.values())

# for  i in dictionary:
# 	if dictionary[i] == l:
# 		print(i,l)


dictionary = {'Ani':5,'John':6,'Mary':10,'Ashot':2,'Ruben':10}
reversed_dictionary = {value : key for (key, value) in dictionary.items()}

print(reversed_dictionary)

