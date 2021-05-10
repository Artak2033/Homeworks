'''1.Write a python program to check have your
name ‘a’ or no.You have 2 input.'''

name = input('Your name: ').lower()
letter = input('Letter in your name: ').lower()

res = letter in name

print('Name: ',name,'\nLetter in your name: ',res)



'''2.Write a python program to check if there
are bananas, oranges and apples in your
fridge։'''

# banana = input("Do you have bananas: ").lower() == 'y'
# orange = input("Do you have oranges: ").lower() == 'y'
# apple = input("Do you have apples: ").lower() == 'y'

# print('You have banana:',banana)
# print('You have oranges:',orange)
# print('You have applees:',apple)



'''3.Given a number x. Check following conditions:
 x is less or equal to -8 or x is greater than 12
 x is greater than 10 and is less or equal to 50
 x is greater than -10 and is less than 10
 x isn’t equal to 20 or x is greater than 50
 Print the results (they should be True or False)'''

# x = int(input('Enter number:'))

# x1 = x <= -8 or x > 12
# x2 = x > 10 and x <= 50
# x3 = x > -10 and x < 10
# x4 = x != 20 or x > 50

# print("X1 result:",x1)
# print("X2 result:",x2)
# print("X3 result:",x3)
# print("X4 result:",x4)



'''4. Write a python program to check if there
are bananas, oranges and apples in your
fridge, and if you don’t have one of them you
should go buy this , and check have you at
home light if not, take those items out of the
fridge։'''

# import datetime
# start = datetime.datetime.now()

# banana = input('Do you have bananas: ').lower() == 'y'
# orange = input('Do you have oranges: ').lower() == 'y'
# apple = input('Do you have apples: ').lower() == 'y'

# light = input('Do you have a light: ').lower() =='y'

# var_banana = not banana 
# print('Buy bananas: ',var_banana,)
# out_banana = not light
# print('Take off:',out_banana)

# var_orange = not orange
# print('Buy oranges: ',var_orange)
# out_orange = not light
# print('Take off:',out_orange)

# var_apple = not apple
# print('Buy apples: ',var_apple)
# out_apple = not light
# print('Take off:',out_apple)

# end = datetime.datetime.now()
# print('Code working: ',end-start)


'''5. Write a python program to create a
histogram in one print from given number. You
know that your number have three-digit.
Example:
>>> input 254
>>> output **
 *****
 ****'''

# number = int(input('Number: '))

# num1 = number // 100
# num2 = number // 10 % 10  
# num3 = number % 10


# res = num1 * '*'
# res1 = num2 * '*'
# res2 = num3 * '*'

# print('\n',res,'\n',res1,'\n',res2)
