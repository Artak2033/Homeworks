# my_list = ["Asus","HP","Dell","Mac","Samsung","Lenovo"]
# if "Mac" in my_list:
#     print(True,my_list.index("Mac"))
# else:
#     print(False)


# import string
# char = string.punctuation
# while True:
#     number_c = 0
#     char_c = 0
#
#     password = input('Input password:')
#
#     if len(password) < 8:
#         print("Input password more than 8 characters")
#         continue
#
#     if password[0].islower():
#         print("First letter must be upper")
#         continue
#
#     for i in password:
#         if i in char:
#             char_c += 1
#         elif i.isdigit():
#             number_c += 1
#
#     if char_c < 2 or number_c < 2:
#         print("Your passwor must be have two characters and two numbers")
#         continue
#     print("Your password is STRONG")
#     break


# link = 'https://www.youtube.com/watch?v=4jf75E4dTDY'
# print(link[(link.index("=")+1):])

# word = input("Input word: ")
# if word == word[::-1]:
#     print("word is palindrom")
# else:
#     print("word is NOT palindrom")

# txt = "Loren Ipsum dolor sit amed"
# print(list(txt))
# print(txt.split())

# txt = '21 32 45 8 7'
# l = txt.split()
# for i in l:
#     if int(i) % 2 == 0:
#         print(i,end=" ")

# l = [5,2,8,7,6,9]
# c = 0
# for i in range(len(l)):
#     if l[c] % 2 == 0:
#         l.remove(l[c])
#         c -= 1
#     c += 1
# print(l)


# group = ["Tom","Kate","Bob","Mari","Gor"]
# for i in range(len(group)):
#     name = input("Input name: ")
#     if name in group:
#         group.remove(name)
# print(group)

# l = [1,5,2,3,1,5,9,8,3,6,3,3]
# c = 0
# for i in range(len(l)):
#     if l.count(l[c]) > 1:
#         l.remove(l[c])
#         c -= 1
#     c +=1
# print(l)


