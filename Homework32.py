'''Calculator'''

# class Calculator:

# 	def __init__(self,a,b):
# 		self.a = a
# 		self.b = b

# 	def plus(self):
# 		return self.a + self.b

# 	def minus(self):
# 		return self.a - self.b

# 	def multy(self):
# 		return self.a * self.b

# 	def div(self):
# 		return self.a / self.b


# while True:

# 	try:
# 		a = int(input('\nFirst number: '))
# 		choice = input('Choose (+,-,*,/):  ')
# 		b = int(input('Second number: '))
# 		res = Calculator(a,b)
# 	except ValueError:
# 		print('Only number.')
# 		continue
# 	except KeyboardInterrupt:
# 		print('\nCalculator OFF.')
# 		break		

# 	if choice == '+':
# 		print(res.plus())

# 	elif choice == '-':
# 		print(res.minus())

# 	elif choice == '*':
# 		print(res.multy())
		
# 	elif choice == '/':
# 		try:
# 			print(res.div())
# 		except ZeroDivisionError:
# 			print('Only positive number.')




'''2.Create a class for Car and Person'''

# class Car:
# 	def __init__(self,mark,color,hp):
# 		self.mark = mark
# 		self.color = color
# 		self.hp = hp

# car1 = Car('BMW','Black','500')
# car2 = Car('Audi','Red','480')


# print('Car mark: ',car1.mark,'\nColor: ',car1.color,'\nHP: ',car1.hp)
# print('\nCar mark: ',car2.mark,'\nColor: ',car2.color,'\nHP: ',car2.hp)



# class Person:

# 	def __init__(self,name,age,gender):

# 		self.name = name
# 		self.age = age
# 		self.gender = gender

# pers1 = Person('Artak',22,'Male')
# pers2 = Person('Ann',19,'Female')

# print('\nName: ',pers1.name,'\nAge: ',pers1.age,'\nGender: ',pers1.gender)
# print('\nName: ',pers2.name,'\nAge: ',pers2.age,'\nGender: ',pers2.gender)



'''3.Create a class Change:You have 3 methods in your class:'''

# class Change:

# 	def __init__(self,USD):
# 		self.USD = USD

# 	def usd_euro(self):
# 		return self.USD * 0.82

# 	def usd_amd(self):
# 		return self.USD * 520

# 	def usd_ru(self):
# 		return self.USD * 72


# while True:

# 	try:
# 		user = int(input('\nUSD: '))
# 		choice = input('EUR, AMD, RU:	').upper()
# 		res = Change(user)
# 	except ValueError:
# 		print('Only number.')
# 		continue
# 	except KeyboardInterrupt:
# 		print('\nChange converter OFF.')
# 		break



# 	if choice == 'EUR':
# 		print(res.usd_euro())
# 	elif choice == 'AMD':
# 		print(res.usd_amd())

# 	elif choice == 'RU':
# 		print(res.usd_ru())
