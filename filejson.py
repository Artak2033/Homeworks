import json

file_name = 'about_users.json'

# player1 = {
# 	'id': 12,
# 	'Name':'Aram',
# 	'Age':18,
# 	'Height':180,
# 	'Awards':['Master',3,2,1,]
# }


# player2 = {
# 	'id':13,
# 	'Name':'Ani',
# 	'Age':14,
# 	'Height':178,
# 	'Awards':[3,2,1,]
# }

player1 ={12: {
	'Name':'Aram',
	'Age':18,
	'Height':180,
	'Awards':['Master',3,2,1,]}
}

player2 = {13:{
	'Name':'Ani',
	'Age':14,
	'Height':178,
	'Awards':[3,2,1,]}
}


player1.update(player2)
my_players = dict(player1)


# question = input('1 Km to meter? ') == '1000'
id_user = int(input('Your id: '))
id_name = input('New name: ')
my_players[id_user]['Name'] = id_name

# if question:
# 	if 'Senior' not in my_players[id_user]['Awards']:
# 		my_players[id_user]['Awards'].append('Senior')


# if question:
# 	for data in my_players:
# 		if data['id'] == 12:
# 			if 'General' not in data['Awards']:
# 				data['Awards'].append('General')
# 				break


# name_question = input('New name ')

# for name in my_players:	
# 	if name['id'] == 13:
# 		name['Name'] = name_question


with open(file_name,'w') as file:
	json.dump(my_players,file) 

file = open(file_name)
json_date = json.load(file)
for data in json_date:


	print('\nPlayer name is',json_date[data]['Name'])
	print('Player age is',json_date[data]['Age'])
	print('Player height is',json_date[data]['Height'])
	print('Player awards is',json_date[data]['Awards'])

