import operator
#.add(23) - добавить
# .remove() - удалить
# .pop() - удалить случайное значение
# .update([]) -работает как extend()
# .clear() - полностью удаляет значения в множестве
# a.intersection(b) - возращает объект который есть в обоих множествах
# a.intersection_update(b) - сохраняет объекты которые есть в обоих множествах
# a.difference(b) - показывает не похожие 
# .discard() - удаление если не найдет значение то не выдаст ошибку


# dict
# a['new'] = 145 - добавит ключ/значение
# a.update({'run' : True }) - добавить ключ/значение можем добавить сразу много значений 
# a.get('key') - получение из "а" значение key == a['key'] 
# .keys() - получить ключи ключи
# .values() - получить все значения
# .items() - получить все ключи и значения 
# .clear() - очистить словарь 


# #1
# dates_of_birth = {3, 10, 11, 7, 31, 21, 1, 10, 3, 5, 6, 6,}
# dates_of_birth.remove(7)
# print(dates_of_birth)

# #2
# farm_1 = {'cow', 'horse', 'donkey', 'cat', 'dog'}
# farm_2 = {'dog', 'cat', 'mouse', 'sheep'}
# farm_3 = farm_1.intersection(farm_2)
# print(farm_3)

#3
# farm_1 = {'cow', 'horse', 'donkey', 'cat', 'dog'}
# farm_2 = {'dog', 'cat', 'mouse', 'sheep'}
# farm_3 = farm_2.difference(farm_1)
# print(farm_3)

#4
# set_1 = {1, 2, 3, 4, 5}
# set_1.add(10)
# print(set_1)
# set_1.pop()
# print(set_1)

#000
# menu = {'lagman': 120, 
#     'plov': 120,
#     'borsh': 100
#     }
# menu['besh_barmack'] = 130
# menu['lagman'] = 135
# menu.pop('borsh')

# #010 
# drink = ['fanta', 'cola', 'sprite']
# menu['drinks'] = drink
# print(menu)

# #3
# set_1 = {'add', 'remove', 'pop', 'update', 'clear', 'intersection', 'intersection_update', 'different', 'differernt_update', 'card'}
# set_dict = {'update', 'get', 'keys', ' values', 'items', 'clear'}
# print(set_1.intersection(set_dict))


# #4
# user = {}
# count = 0
# while count < 3:
#     a = input("Ваше имя: ")
#     b = input("Ваш пароль: ")
#     user[a] = b
#     count += 1

# print(user)

#5
# users = {'Alex': 'programming', 
#     'Denis': 'doctor',
#     'Pasha': 'teacher',
#     'Sasha': 'driver',
#     'Igor': 'manager'
#     }

# for i in users:
#     print(f'Здравствуйте, {i} прекрасная профессия: {users[i]}')
    

# #6
# set_1 = set()
# count = 0
# while count < 4:
#     a = int(input(">>"))
#     set_1.add(a)
#     count += 1

# b = tuple(set_1)

# print(type(b))
# print(b)


#7
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# set_country = set(south_american_countries)
# print(set_country)

#8
# suitsbags = []
# a = input("Положите вещь: ")
# b = input("Положите вещь: ")
# c = input("Положите вещь: ")
# d = input("Положите вещь: ")
# e = input("Положите вещь: ")
# suitsbags.append(a)
# suitsbags.append(b)
# suitsbags.append(c)
# suitsbags.append(d)
# suitsbags.append(e)
# print(suitsbags)
# suitsbags.pop(-1)
# print(suitsbags)

# suits_bags = []
# count = 0
# while count < 5:
#     a = input("Положите вещь: ")
#     suits_bags.append(a)
#     count += 1

# print(suits_bags)
# suits_bags.pop(-1)
# print(suits_bags)

# #9
# my_friends = {
#     'Joomart': "+77555246810",
#     'Adinali': '+77555013579',
#     'Ermek': '+77777013579',
#     'Atai': '+777777246810',
#     'Alymbek': '+77555501234'
# }

# his_her_friends = {
#     'Lyazat': '+77551123456',
#     'Salavat': '+77552234567',
#     'Danyar': '+77553345678',
#     'Bolot': '+77554456789',
#     'Alymbek': '+77555501234',
#     "Dastan": '+775566789012',
#     'Maksat': '+77557789012',
#     'Adinail': '+77555013579'
# }

# our_friends = my_friends.copy()
# our_friends.update(his_her_friends)
# print(our_friends)

#10
# my_friends = {'Joomart','Adinali', 'Ermek', 'Atai','Alymbek'}

# his_her_friends = {'Lyazat', 'Salavat', 'Danyar', 'Bolot','Alymbek', "Dastan", 'Maksat', 'Adinail'}

# our_friends = my_friends.copy()
# our_friends.update(his_her_friends)
# print(our_friends)

#11
# users = {}
# count = 0
# while count < 5:
#     a = input("Введите логин: ")
#     b = input("Введите пароль: ")
#     count += 1
#     if a  in users:
#         print("Пользователь с таким именем существует")
#     else:
#         users[a] = b

# print(users)
# print(len(users))

#12
# dictionary = {}
# count = 0
# while count < 5:
#     a = input('Введите слово: ')
#     dictionary[a] = len(a)
#     count += 1

# a = sorted(dictionary.items(), key=operator.itemgetter(1))
# b = a[-1][0]

# print(b)