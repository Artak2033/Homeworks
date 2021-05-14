'''*********************************'''

# first = ['Ani','Jessy','Ben']
# second = [1,2,3]

# c = {i:j for i,j in zip(second,first)}
# print(c)


# file_name = 'Art.txt'

# with open(file_name,'w') as f:
# 	f.write(f"{c}")


'''*********************************'''

# import json

# song = {'test':
# 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book'	
# }

# user = input('Song name: ')

# with open('Art.json','w') as f:
# 	json.dump(song,f)

# file = open('Art.json')
# song_play = json.load(file)

# print(song_play)


# if user in song_play:
# 	print(song_play[user])



'''*********************************'''

# string = 'Another pause and more eying and siding around each other'.split(' ')

# c = {}

# for i in string:
# 	c[i] = string.count(i)

# with open('Art.txt','w') as file:
# 	file.write(str(c))

# with open('Art.txt','r') as file_read:	
# 	read = file_read.read()
# 	print(read)



'''*********************************'''

# import json

# file_name = 'about_users.json'

# user_num = int(input('Enter number: '))

# count = 0

# for i in range(1,user_num):
# 	if i % 3 == 0 or i % 5 == 0:		
# 		count += i
# print(count)

# c = {'num':count}

# with open(file_name,'w') as file:
# 	json.dump(c,file)


'''*********************************'''

user = input('Enter word ')

vowels = ('a','e','i','o','u','y')

count_vowels = 0

for i in user:
	if i in vowels:
		count_vowels += 1
print(count_vowels)
