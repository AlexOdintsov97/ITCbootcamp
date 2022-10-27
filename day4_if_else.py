#1
# a = 2 ** 3
# b = 3 ** 2
# if a > b:
#     print('a больше чем b')
# else:
#     print('b больше a')

#2
# a = int(input('введите число от 0 до 100: '))
# if a > 0 and a < 21:
#     print("число разрешенное")
# elif a > 57 and a < 100:
#     print("число разрешенное 2")
# else:
#     print("число из запрещенного диапазона")


#3
# a = int(input('Введите число: '))
# if a % 2 ==0:
#     print("число четное")
# else:
#     print('Число не четное')

# if a % 3 == 0:
#     print("число делится на 3 без отстатка")
# else:
#     print("Число не делится на 3 без остатка")

# if a ** 2 > 1000:
#     print("число больше 1000")
# else:
#     print("чило меньше 1000")

#4
# a = True
# if a == True:
#     print("Работает")
# else:
#     a = True
#     print("aga")

#5
# a = 10 // 5
# b = 10 / 5
# if a == b:
#     c = a + b
#     print("Сумма чисел", c)
# else:
#     print("переменные не равны")

#6
# a = int(input("vvedite chislo: "))
# if a > 0:
#     b = a * -1
#     print("pomenyali znak", b)
# else:
#     print("good")


#7
# a = 10 
# b = 5

# if a > 0 and b > 0:
#     print('Числа положительные')
# else:
#     print("числа отрицательные")

#8
# a = 10
# b = 5
# if a > b:
#     a += 2
#     print(a)
# else:
#     b += 2
#     print(b)

#9
# a = int(input("Введите положительное или отрицательное число: "))
# if a > 0:
#     print("Положительное число")
# elif a < 0:
#     print("Число отрицательное")
# else:
#     print(a)

# 10
# age = int(input("Введите ваш возраст: "))
# if age > 18:
#     print("Совершеннолетний")
# elif age <= 4:
#     print("Ребенок")
# else:
#     print("Несовершеннолетний")

#11
# a = 45
# b = 6
# if a % b == 0:
#     print('число нацело делится')
# else:
#     print('чило не делилится')
#     print(a % b)

#12 
# year = int(input('Введите год: '))
# if year == 2022:
#     print("Текущий год")
# elif year > 2022:
#     print("Год еще не наступил")
# else:
#     print("Год уже прошел")


# 13
# year = int(input("Введите год рождения: "))
# age = 2022 - year
# if age > 18:
#     print("Совершеннолетний")
# elif age <= 4:
#     print("Ребенок")
# else:
#     print("Несовершеннолетний")

#14
# a = 1
# b = 5678
# c = 4
# max = 0
# min = 0

# if a > max and a > min:
#     max = a
#     min = a
# else:
#     min = a

# if c > max:
#     max = c
# else:
#     min = c

# if b > max:
#     max = b
# else: 
#     min = b

# print(max)
# print(min)

#15
# a = 17391 % 17
# b = 546 % 17
# c = 934 % 17
# min = 0
# if a < b:
#     print("a min", a)
#     min = a
# else: 
#     print("b min")
#     min = b

# if c < min:
#     min = c
# else:
#     print(min)


#16

# b = 13 
# x = b ** 2
# if x >= 172:
#     print("число больше")
# else:
#     a = x ** 2
#     print(a)

#17
# f = 10
# r = 10.5
# j = 13.7

# if r > j:
#     print("r > j")
# elif r < j:
#     print("r < j")
# else:
#     print("r = j")


#18
# a = 4
# b = 7
# if a % 2 == 0:
#     print("число четное")
# else:
#     print("число не четное")

# if a % 2 == 1 and a < 4:
#     print("Число простое")
# else:
#     print("Число не простое ")


#19
# a = 123
# b = 321
# x = 0
# if (a + b) % 2 == 0:
#     x = (a + b) // 2
# else:
#     print("число не четное")

# if x < b and x > a:
#     print('b > sum/2 > a')

#20
a = 35
b = 25
c = 75
max = 0 
min = 0
if a > b:
    max = a
    min = b
else:
    print('fd')

if c > max:
    max = c
else:
    print("df")

if b < c:
    min = b
else:
    min = c

print(max, min)