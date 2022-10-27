# #Задача №1
# a = []
# a1 = input('Введите слово1: ')
# a.append(a1)
# a2 = input('Введите слово2: ')
# a.append(a2)
# a3 = input('Введите слово3: ')
# a.append(a3)
# b = a1 + a2 + a3
# if len(b) > 20:
#     if b.isalpha():
#         c = (a.index(max(a)))
#         a.pop(c)
#         d = str(a)
#         print(d.upper())
#     else:
#         print("слова должно состоять только из букв")    
# else: 
#     print("Длина меньше 20 символов")

#2

# user = input('Введите почту: ')
# a = user.endswith('@gmail.com')
# b = user.endswith('@mail.ru')
# if a or b == True: 
#     pasford = 123456
#     print(pasford)
# else:
#     print('Не верный формат почты')

# past = int(input('Подвердите пароль: '))

# if past == pasford:
#     print('Подверждение прошло успешно!')  
# else:
#     print('Не удалось подвердить почту ')


# # Задача 3
# a = 2897607
# if a % 3 == 0:
#     d = a * a
#     number = str(d)
#     a = len(number)
#     print(f'Длина int - {a}')
#     if len(number) > 10:
#         print(f"До изменения {number[:6]}")
#         a = number.replace('3','0')
#         print(f'Окончательное решение {a[:6]}')
        
#     else:             
#         print('Меньше  или ровно 10')      
# else: 
#     print('Не делится без остатка')

           
     
  
#Задача №4
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = (1, 2, 3, 4, 5, 6, 7)
# b = list(b)
# a.extend(b)
# print(a)
# print(a[0])
# print(a[len(a)//2])
# print(a[-1])


# #Exe5

# a = input('Имя: ')
# b = input('Фамилия: ')
# e  = int(input('Год рождения: '))
# d = input('Страна проживания: ')
# f = 2022 - e
# print(f"Hello {a} {b}. You are {f} years old. You are living in {d}.")
# if e in range(1910, 2019):
#     my_dict = {}
#     my_dict ['Name'] = a
#     my_dict ['Last_name'] = b
#     my_dict ['Born'] = e
#     my_dict ['From'] = d
#     my_dict ['Age'] = f
#     print(my_dict)
    




#6


# user = int(input('Введите первое число: '))
# user2 = int(input('Введите второе  число: '))
# summ = user * user2
# num = '123456789'
# if str(user) in num and str(user2) in num:
#     otv = int(input('Введите ответ: ')) 
#     if summ == otv:
#         print('Correct')
#     else:
#         print('not correct')
# else:
#     print("Введите число от 1 до 9")


#exe7
# a = input('slovo: ')
# b = input('slovo2: ')
# c = len(a)
# d = len(b)
# if c > d:
#     print(f'{a} больше чем a на {c - d} символов')
# elif c < d:
#     print(f'{b} больше чем a на {d - c} символов')
# elif c == d:
#     print ('равны', c == d )

#8
# 1.False or True == True
# 2. false and True or True ==  True 
# 3. False  or  True and true = True
# 4.  False and False and False = False  

# Задача №9
# yoda = ['on Python', 'programming ', 'I like ']
# a = yoda[2] + yoda[1] + yoda[0]
# print(a)


# #10
# marks = {}
# marks ['Bill']=int(input('Enter mark for Bill:'))
# marks ['Jane']=int(input('Enter mark for Jane:'))
# marks ['john']=int(input('Enter mark for John:'))
# marks ['Mary']=int(input('Enter mark for Mary:'))

# a = sum(marks.values())/len(marks.values())
# sum_m = math.ceil(a)
# print(f"Enter mark for Bille {marks['Bill']}")
# print(f"Enter mark for Jane {marks['Jane']}")
# print(f"Enter mark for John {marks['john']}")
# print(f"Enter mark for Mary {marks['Mary']}")
# print('average mark :', sum_m)

#Exe11
# a = int(input('number: '))
# b = input("Знак ('+', '-', '*', '/', '//', '%'): ")
# c = int(input('number2: ')) 
# if b == "+":
#     r = a + c
#     print(f'{a}+{c}={r}')
# elif b == "-":
#     r = a - c
#     print(f'{a}-{c}={r}')
# elif b == "*":
#     r = a * c
#     print(f'{a}*{c}={r}')
# elif b == "/":
#     r = a / c
#     print(f'{a}/{c}={r}')
# elif b == "%":
#     r = a % c
#     print(f'{a}%{c}={r}')
# elif b == "//":
#     r = a // c
#     print(f'{a}//{c}={r}')


# № 12
# У нас есть wather_dict
# тут хранятся все данные о сегоднешней погоде
# Вам необходимо его расспоковать 
# тоесть взять данные и записать как показано ниже

# вывода на экран:
# Дата: 2022-10-26
# Время: 11:33
# Погода в городе: Almaty 
# Температура:  9.18 °C  
# Описание: moderate rain
# Облачность: 100
# Влажность: 71
# Давление: 1022  мм.рт.ст
# Скорость ветра: 4.99




# wather_dict = {'base': 'stations',
#  'clouds': {'all': 100},
#  'datetime': '2022-10-26 11:33:21.774524',
#  'main': {'feels_like': 6.57,
#           'grnd_level': 925,
#           'humidity': 71,
#           'pressure': 1022,
#           'sea_level': 1022,
#           'temp': 9.18,
#           'temp_max': 9.18,
#           'temp_min': 9.18},
#  'name': 'Almaty',
#  'rain': {'1h': 1.26},
#  'sys': {'country': 'KZ', 'sunrise': 1666747131, 'sunset': 1666785198},
#  'timezone': 21600,
#  'visibility': 10000,
#  'weather': [{'description': 'moderate rain',
#               'icon': '10d',
#               'id': 501,
#               'main': 'Rain'}],
#  'wind': {'deg': 262, 'gust': 9.09, 'speed': 4.99}}

# data = wather_dict['datetime'].split()
# time = data[1].split('.')

    
# print("Дата", data[0])
# print("Время", time[0])
# print('погода в городе: ', wather_dict['name'])
# print(f"Температура: {wather_dict['main']['temp']} °C ")
# print('Описание: ', wather_dict['weather'][0]['description'] )
# print('Облачность:',wather_dict['clouds']['all'] )
# print('Влажность:', wather_dict['main']['humidity'] )
# print(f"давление: {wather_dict['visibility']} мм.рт.ст")
# print(f"Скорость ветра: {wather_dict['wind']['speed']}")