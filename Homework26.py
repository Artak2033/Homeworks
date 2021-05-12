'''1.Write a Python program to add info in JSON file about you.'''

import json

# file_name = 'firsthomework.json'

# dict_info = {1:{
# 	'Name':None,
# 	'Age':None,
# 	'Sex':None,
# 	'Country':None}
# }

# dict_user = dict(dict_info)


# user_name = input('Name: ')
# user_age = int(input('Age: '))
# user_sex = input('Sex: ')
# user_country = input('Country: ')

# dict_user[1]['Name'] = user_name
# dict_user[1]['Age'] = user_age
# dict_user[1]['Sex'] = user_sex
# dict_user[1]['Country'] = user_country


# with open(file_name,'w') as file:
# 	json.dump(dict_info,file)

# file = open(file_name)
# json_date = json.load(file)
# for data in json_date:

# 	print('\nMy name is',json_date[data]['Name'])
# 	print('Age is',json_date[data]['Age'])
# 	print('Sex is',json_date[data]['Sex'])
# 	print('Country is',json_date[data]['Country'])



'''*********************************'''

# file_name = 'firsthomework.json'

# dict_info = {
# 	'Name':'Artak',
# 	'Age':22,
# 	'Sex':'Male',
# 	'Country':'Armenia'
# }

# user = [dict_info]

# with open(file_name,'w') as file:
# 	json.dump(user,file)

# file = open(file_name)
# json_date = json.load(file)
# for data in json_date:
# 	print(data)




'''2.Write a Python program to get info in JSON file about you.'''

# file_name = 'firsthomework.json'

# with open(file_name,'r') as f:
# 	file = json.load(f)
# 	print(file)



'''3.Write a Python program to check if your json file have this info.'''

# file_name = 'firsthomework.json'

# name = input('Name: ')

# with open(file_name,'r') as file:
# 	file = json.load(file)
# 	print(file)

# for i in range(len(file)):
# 	if file[i]['Name'] == name:
# 		print('True')
# 	else:
# 		print('False')