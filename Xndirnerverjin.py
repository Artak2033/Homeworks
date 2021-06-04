'''1.'''
# import math
# from math import pi

# class Covid:
# 	def __init__(self,celsius):
# 		self.celsius = celsius

# 	def result(self):
# 		res = math.ceil(self.celsius * pi)
# 		print(res)

# 		if 120 <= res <= 128:
# 			return 'Coronavirus'
# 		else:
# 			return 'No Coronavirus'

# x = Covid(36.6)
# print(x.result())




'''2.'''
# import math
# class Name:

# 	def __init__(self,var_name):
# 		self.var_name = var_name

# 	def result(self):
# 		name_dict = {1:'a,j,s',2:'b,k,t',3:'c,l,u',4:'d,m,v',5:'e,n,w',6:'f,o,x',7:'g,p,u',8:'h,q,z',9:'i,r'}

# 		count = 0

# 		for i in self.var_name:
# 			for j,h in name_dict.items():
# 				if i in h:
# 					count += j
# 		res = (math.sqrt(count))

# 		if res < 5:
# 			return 'Count: ',count,'Sqrt of count: ',res,'result: ','Yes' 
# 		else:
# 			return 'Count: ',count,'Sqrt of count: ',res,'result: ','No' 
			

# x = Name('ani')
# print(x.result())



'''3.'''
import random

class Harry:

	def __init__(self):
		self.my_count = 0
		self.pc_count = 0


	def result(self):

		while True:

			l = ['Avada Kedavra','Crucio','Imperio']

			harry = input('\nMagic word: ')
			pc = random.choice(l)
			print('Voldemort: ',pc)

			
			if harry == pc:
				self.my_count += 1
				print('Harry: ',self.my_count)
			else:
				self.pc_count += 1
				print('Voldemort: ',self.pc_count)


			if self.my_count == 2:
				print('Win Harry')
				break
			if self.pc_count == 2:
				print('Win Voldemort')
				break

x = Harry()
x.result()