# m = int(input("Minute: "))
# s = m * 60
# print(s)

# day = int(input("Input day: "))
# mv = day * 24 * 60 * 60
# print (mv)

# e = int(input ("Input 1 angle: "))
# e1 = int(input ("Input 2 angle: "))
# e2 = 180 - (e + e1)
# print (e2)

# tiv = int(input("Input number = "))
# if tiv <= 100:
# 	print("True")
# else:
# 	print("False")

# tiv = int(input("Input number: "))
# if tiv % 400 == 0:
# 	print("True")
# else: 
# 	print("False")

# r = int(input("Input radius: "))
# s = 3.14 * r **2 / 2
# l = s * 5
# print(l)





# def summ(my_list):

# 	count = 0
# 	for i in my_list:
# 		count += i
# 	return count

# my_list = [8,2,3,0,7]

# print(summ(my_list))



def multyply(my_list):

	count = 1

	for i in my_list:
		count *= i
	return count

my_list = [8, 2, 3, -1, 7]

print(multyply(my_list))