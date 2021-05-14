'''1.You have two list convert it in dictionary and add in (mydict.txt) and show result'''

# first = ['Ani', 'Jessy', 'Ben']
# second = [1,2,3]

# res = {i:j for i,j in zip (second,first)}


# with open('mydict.txt','w') as f:
# 	f.write(f"{res}")

# with open('mydict.txt','r') as file:
# 	print(file.read())



'''2.Create json file and save them lyrics (song) and print in cmd word this song.'''

# import json

# song = {'Minor':'Я сам будто себя наказал\
# Этим непониманием йейейе\
# Перестал себе тупо доверять\
# И без устали жаловался на людей\
# Караван гаремел и негодяй\
# Потешал себя баснями о воде\
# Но то были миражи - ты покаяние моё\
# Найдика меня скорей\
# Пустынями верными я кочевал\
# Да песок глотал следы\
# И не надо быть тут пророком\
# Чтобы понимать суету беды\
# Сам приволок эти пули\
# Чё мыслями выстрелами судьбы\
# Убивали во мне этого Бога\
# Чё по сути был поводырь'}


# song_name = input('Song name: ')

# with open('song.json','w') as f:
# 	json.dump(song,f)

# file = open('song.json')
# play = json.load(file)


# if song_name in play:
# 	print(play[song_name])



'''3.Write a python program which have one input an
integer, representing the sum of all the multiples of
3 and 5 below the given input. and save this result
in json file.'''

# import json

# number = int(input('Enter number: '))

# c = 0

# for i in range(1,number):	
# 	if i % 3 == 0 or i % 5 == 0:
# 		c += i
# print('Result',c)

# with open('Num.json','w') as f:
# 	json.dump(c,f)



'''4.Write a program that takes in a string as input,
counts and outputs the number of vowels.
And add result in json file.'''

# import json

# vowels = ('a','e','i','o','u','y')

# vowels_count = 0
# user = input('Enter word: ')

# for i in user:
# 	if i in vowels:
# 		vowels_count += 1
# print(vowels_count)

# with open('Word.json','w') as file:
# 	json.dump(vowels_count,file)



'''5.You have text.txt file and contains such text:
Another pause and more eying and siding around
each other
You can create one dict where you have.
‘’Another’’:1
‘’and’’:2'''


# with open('text.txt','w') as text:
# 	text.write('Another pause and more eying and siding around each other')

# with open('text.txt','r') as file:
# 	read = file.read().split()

# word_count = {}

# for i in read:
# 	word_count[i] = read.count(i)
# print(word_count)



'''6.Write a python function which get a new list
from a given list, consisting of the first
repeating elements.'''

# my_list = ['a','b','a','c','b']

# def elements(my_list):
# 	new_list = []	
# 	for i in my_list:
# 		if i not in new_list:
# 			new_list.append(i)
# 	return(new_list)

# print(elements(my_list))



'''7.You have word.txt file and in them you have
one story.
Write a Python function that accepts this
story and calculate the number of uppercase
letters and lowercase letters.'''

# import string

# def story():

# 	uppercase = string.ascii_uppercase
# 	lowercase = string.ascii_lowercase
# 	numbers = string.digits

# 	upper_count = 0
# 	lower_count = 0
# 	number_count = 0

# 	with open('word.txt','w') as f:
# 		f.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')

# 	with open('word.txt','r') as file:
# 		read = file.read()
# 	print(read)

# 	for i in read:
# 		if i.isupper():
# 			upper_count += 1
# 		if i.islower():
# 			lower_count += 1
# 		if i.isdigit():
# 			number_count += 1
# 	print('\nUppercase: ',upper_count,'\nLowercase: ',lower_count,'\nNumbers: ',number_count)

# story()


'''8.You have test.txt file and in them you have
one story overwrite this story in another file.'''

# with open('word.txt','r') as f:
# 	read = f.read()

# with open('test.txt','w') as file:
# 	file.write(read)




'''********** Music ************'''

# from playsound import playsound

# try:
# 	user = input('Your mood (Fine,Normal,Sad): ').title()
# 	if user == 'Fine':
# 		playsound('miyagi.mp3')
# 	if user == 'Normal':
# 		playsound('Samurai.mp3')
# 	if user == 'Sad':
# 		playsound('miyagi.mp3','Samurai.mp3')
# except KeyboardInterrupt:
# 	print("\nMusic OFF.")


