'''1.Write a recursive function to determine whether all
digits of the number are odd or not.'''

# def odd_num(num):

# 	for i in str(num):
# 		if int(i) % 2 == 0:
# 			print('False')
# 		else:
# 			print('True')

# odd_num(123456789)



'''2.Write a python function all even number in
10.000 use threading and print time.'''

# import threading
# import time


# def even_num(start,end):
# 	with open('evennumbers.txt','a') as f:
# 		for i in range(start,end):
# 			if i % 2 == 0:
# 				f.write(str(i) + '\n')

# start = time.time()

# num1 = threading.Thread(target=even_num, args=(0,5000))
# num2 = threading.Thread(target=even_num, args=(5000,10000))

# num1.start()
# num2.start()

# num1.join()
# num2.join()

# print('Time: ',time.time()-start)



'''3.Given N number. Write a recursive function that
should print from 1 to N numbers.'''

# def numbers(n):
# 	if n > 0:	
# 		numbers(n-1)
# 		print(n)
# numbers(5)



'''4.Write a python program to find the longest word from the file content.Need to use
<try-except> block in the file reading process and print time. example:'''

# import time

# start = time.time()

# def longest_word(file_name):

# 	x = 0

# 	try:
# 		with open(file_name,'r') as file:
# 			words = file.read().split()
# 			print(words)
# 		for i in words:
# 			if len(i) > x:
# 				x = len(i)
# 				res = i
# 		print('\nLongest word is: ',res,'\nLength: ',x)
# 		print('Time: ',time.time()-start)
# 		raise Exception ('END')
# 	except Exception as r: 
# 		print(r)	

# longest_word('test.txt')