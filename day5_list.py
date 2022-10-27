#0
# list = []
# a = (1, 2)
# b = (3, 4)
# c = (5, 6)
# d = (7, 8)
# e = (9, 10)
# list.append(e)
# list.append(a)
# list.append(d)
# list.append(c)
# list.append(b)
# print(list)

#1
# tu = (1, 2, 4)
# print(tu[0])
# print(tu[1])
# print(tu[2])

#2
# list = []
# list.append(1)
# list.append("odin")
# list.append(1.0)
# list.append(True)
# list.append([1, 2, 3])

#3
# list = ['Sasha', 'misha', 'Pasha', 'Lesha', 'grisha']
# a = ' '
# print(a.join(list))
# print(list)

#4
# list_a = ['Odin', 'dva']
# list_b = ['Tri', 'chetyre']
# list_a.extend(list_b)
# print(list_a)

#5
# list_1 = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon', 'Jimmy', 'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jimmy', 'Jackson', 'Jhon']
# print(list_1.count('Jack'))

#6
# list_1 = ['Jack', 'Oscar', 'Jackson', 'Jhon', 'Jackson', 'Jhon', 'Jimmy', 'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jimmy', 'Jackson', 'Jhon']
# list_1.remove('Oscar')
# print(list_1)

# #7
# info = []
# name = 'Alex'
# age = 1997
# lan = "python"
# info.append(name)
# info.append(age)
# info.append(lan)
# print(info)

#8
# python_list = ['int', 'str', 'bool', 'if', 'else', 'elif', 'loop', 'tuple', 'list', 'None', True, False]
# a = python_list.index('loop')
# python_list.pop(a)
# print(python_list)

# 9
# list_3 = [123, 321, 2, 543]
# sum = list_3[0] * list_3[1] * list_3[2] * list_3[3]
# print(sum)

#10
# list_1 = []
# list_2 = []
# a = input('>> ')
# b = a.split()
# for i in b:
#     i = int(i)
#     if i % 2 == 0:
#         list_1.append(i)
#     else:
#         list_2.append(i)
# print('list1>',list_1)
# print('list2>', list_2)

#11
# list_1 = []
# a = input(">> ")
# b = a.split()
# for i in b:
#     i = int(i)
#     list_1.append(i)
# ma = max(list_1)
# mi = min(list_1)
# print('max', ma)
# print('min', mi)

#12
# products = ['яблоко', "груша", "арбуз", "банан", "мандарин"]
# print(products)
# user = int(input(">> "))
# products.pop(user)
# if user > len(products):
#     print("Вы ввели большое число")
# else:
#     print(products)

# #13
# points = 0
# user = int(input("Вас зовут Саша? 1. Да 2. Нет: " ))
# if user == 1:
#     points += 1
# else:
#     pass
# user = int(input("Вам 25 лет? 1. Да 2. Нет: " ))
# if user == 1:
#     points += 1
# else:
#     pass
# user = int(input("Вы из России? 1. Да 2. Нет: " ))
# if user == 1:
#     points += 1
# else:
#     pass
# user = int(input("Вы казах? 1. Да 2. Нет: " ))
# if user == 2:
#     points += 1
# else:
#     pass
# if points >= 3:
#     print("Вы прошли тест")
# elif points > 0 and points < 3:
#     print("вы набрали два балла")
# else:
#     print("не прошли тест")

#14
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# user = int(input(">> "))
# print(lis[user:])

# #15
# from curses.ascii import isdigit


# login = input("Введите логин: ")
# passwor = input("Введите пароль: ")
# passwor1 = input("подтвердите пароль")
# users = []
# if  not login.isdigit() and not login.isalpha():
#     if passwor == passwor1:
#         users.append((login, passwor))
#     else:
#         print("Пароль не совпадает")
# else:
#     print("Логин должен состоять из букв и цифр")

# print(users)

