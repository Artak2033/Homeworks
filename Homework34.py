'''1.Create a class which given a year, return the
century it is in. The first century spans from the
year 1 up to and including the year 100, the
second - from the year 101 up to and including the
year 200, etc.
For year = 1900, the output should be = 19'''


# class Century:

# 	def __init__(self,year):
# 		self.year = year


# 	def result(self):
# 		if self.year % 100 == 0:
# 			dar = self.year // 100
# 		else:
# 			dar = self.year // 100 + 1
# 		print(dar)

# res = Century(2021)
# res.result()



'''2.Create a class given the string, check if it is a palindrome.
word should be lowercase and 1 ≤ inputString.length ≤ 105'''

# class Palindrome:

# 	def __init__(self,word):
# 		self.word = word


# 	def result(self):
# 		if 1 < len(self.word) < 105 and self.word.islower():
# 			if self.word == self.word[::-1]:
# 				print(self.word,'Palindrome')
# 			else:
# 				print(self.word,'Non palindrome.')

# res = Palindrome('acca')
# res.result()



'''3.Create a Class which given an list of integers, find the pair
of adjacent elements that has the largest product and
return that product.'''

# class Find:

# 	def __init__(self,my_list):
# 		self.my_list = my_list


# 	def result(self):
# 		x = [self.my_list[i] * self.my_list[i+1] for i in range(len(self.my_list)-1)]
# 		return max(x)


# res = Find([3, 6, -2, -5, 7, 3])
# res.result()
# print(res.result())



'''4.Create a class which given a list of strings, return another list
containing all of its longest strings.'''

# class Long:

# 	def __init__(self,my_list):
# 		self.my_list = my_list

# 	def result(self):

# 		x = 1
# 		c = []

# 		for i in self.my_list:
# 			if len(i) >= x:
# 				x = len(i)
# 				c.append(i)
# 		print('Longest words: ',c)


# res = Long(["aba", "aa", "ad", "vcd", "aba"])
# res.result()




'''5.Ticket numbers usually consist of an even number of digits.A ticket number is
considered lucky if the sum of the first half of the digits is equal to the sum of the
second half.Given a ticket number n, determine if it's lucky or not.'''

# class Luck:
# 	def __init__(self,number):
# 		self.number = number

# 	def result(self):
# 		list1 = []
# 		list2 = []

# 		l = len(self.number) + 1
# 		var = self.number[0:l//2]
# 		var2 = self.number[l//2:]

# 		list1.append(var)
# 		list2.append(var2)
# 		print(list1,list2)

# 		list1_count = 0
# 		list2_count = 0

# 		for i in list1:
# 			for j in i:
# 				list1_count += int(j)
# 			print('List1: ',list1_count)


# 		for i in list2:
# 			for j in i:
# 				list2_count += int(j)
# 			print('List2: ',list2_count)

# 		if list1_count == list2_count:
# 			print('Luck')
# 		else:
# 			print('No luck')


# res = Luck('123051')
# res.result()



'''6.Create a class: Some people are standing in a row in a park. There are trees
between them which cannot be moved. Your task is to rearrange the people by
their heights in a non-descending order without moving the trees. People can be
very tall!
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].'''

# class Park:
# 	def __init__(self,my_list):
# 		self.my_list = my_list

# 	def result(self):
# 		x = sorted([i for i in self.my_list if i != -1])

# 		count = 0
		
# 		for i in range(len(self.my_list)):
# 			if self.my_list[i] == -1:
# 				continue
# 			else:
# 				self.my_list[i] = x[count]
# 				count += 1
# 		return self.my_list


# res = Park([-1, 150, 190, 170, -1, -1, 160, 180])
# res.result()
# print(res.result())


'''7.Several people are standing in a row and need to be divided into two teams. The
first person goes into team 1, the second goes into team 2, the third goes into
team 1 again, the fourth into team 2, and so on.You are given an array of positive
integers - the weights of the people. Return an array of two integers, where the
first element is the total weight of team 1, and the second element is the total
weight of team 2 after the division is complete.
a = [50, 60, 60, 45, 70]
Sums(a) = [180, 105]'''


# class People:
# 	def __init__(self,a):
# 		self.a = a

# 	def result(self):
# 		team1 = []
# 		team2 = []
# 		sums = []

# 		for i in range(len(self.a)):
# 			if i % 2 == 0:
# 				team1.append(self.a[i])
# 			if i % 2 == 1:
# 				team2.append(self.a[i])
# 		sums.append(sum(team1))
# 		sums.append(sum(team2))
# 		return sums


# res = People([50, 60, 60, 45, 70])
# print(res.result())