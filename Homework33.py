'''1.Write a python class to find max, min num and
and sum in your list:'''

# class Number:

# 	def __init__(self,count):
# 		self.count = count

# 	def result(self):
# 		minimum = self.count[0]
# 		maximum = self.count[0]
# 		zero = 0

# 		for i in self.count:
# 			if i < minimum:
# 				minimum = i

# 			if i > maximum:
# 				maximum = i

# 		print('Minimum: ',minimum,'\nMaximum: ',maximum)


# 		for j in self.count:
# 			zero += j
# 		print('Sum: ',zero)

# x = Number([1,2,7,10,5,6])
# x.result()



'''2.Write a python class to find two highest values in your dict:'''

# class Find:

# 	def __init__(self,dictionary):
# 		self.dict = dictionary

# 	def result(self):
# 		return sorted(self.dict.values()) [-2:]


# x = Find({'Ani':5,'John':6,'Mary':10,'Ashot':2,'Ruben':15})
# x.result()
# print(x.result())


'''3.Write a python class where your child class takes
all methods in parent class and print them.'''

# class Person:

# 	def __init__(self,name,surname,age):
# 		self.name = name
# 		self.surname = surname
# 		self.age = age

# 	def result(self):
# 		return self.name,self.surname,self.age

# class Child(Person):
# 	def __init__(self,name,surname,age):
# 		super().__init__(name,surname,age)

# x = Child('Ani','Sahakyan',18)
# x.result()
# print(x.result())



'''4.Write a Python class named Rectangle
constructed by a length and width and a method
which will compute the area of a rectangle.'''

# class Rectangle():

# 	def __init__(self,length,width):
# 		self.length = length
# 		self.width = width

# 	def area(self):
# 		return self.length * self.width

# res = Rectangle(4,5)
# print('Area of rectangle: ',res.area())



'''5.Write a python class where we use polymorphism:
Example:
a.country() - Erevan   b.country() - Paris'''


class Armenia:
	def country(self):
		print('Erevan')


class France:
	def country(self):
		print('Paris')

a = Armenia()
b = France()

a.country()
b.country()		