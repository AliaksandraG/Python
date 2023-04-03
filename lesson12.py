# a = int(input('введите первое число:'))
# b = int(input('введите второе число:'))
# if a-b == 135:
#     print('yes')
# if b-a ==135:
#     print('yes')
# else:
#     print('no')
import random

# a = int(input('введите число:'))
# if a > 100 or a < -100:
#     print('-')
# else:
#     print('+')

# a = int(input('введите число:'))
# b = int(input('введите число:'))
# c = int(input('введите число:'))
# if a>10 and b>10 and c>10 :
#     print('yes')
# else:
#     print('no')

# otr = 0
# pol = 0
# for i in range(1,6):
#     a = int(input('введите число:'))
#     if a>0:
#         pol = pol + 1
#     else:
#         otr = otr + 1
# print('кол-во отрицательных:', otr, 'кол-во положительных:',pol)

# ss = []
# while True:
#     a = int(input('введите число:'))
#     if a < 10:
#         continue
#     if a > 100:
#         break
#     else:
#         ss.append(a)
# print(ss)


# import random
# a = [random.randint(-100,100) for i in range(10)]
# b = []
# print('изначальный список:', a)
# for i in a:
#     if i > 0 and i % 2 ==0:
#         b.append(i)
# print('список положительных четных чисел:', b)
# print('сумма четных положительных чисел:', sum(b))


# a = int(input('введите число a:'))
# b = int(input('введите число b:'))
# c = []
# for i in range(a,b):
#     if i % 3 ==0:
#         c.append(i)
# print('числа кратные 3:',c)
# d = len(c)
# s = sum(c)
# e = s/d
# print('средние арифмитическое:', e)

# a = int(input('введите целое семизначное число:'))
# b = 0
# while a!= 0:
#     b = b + a % 10
#     a = a//10
# print(b)

# a = input('введите строку:')
# b = len(a)
# if b >= 10:
#     print('!!!')
# else:
#     print(a[1])


# a = 'my name is Aleksandra'
# print(a)
# c = a.split()
# b = []
# for i in c:
#     b.append(i + '!')
# print(b)

# a = str(input('введите слова:'))
# c = a.split()
# b = []
# for i in c:
#     b.append(i + '_world')
# s = ','.join(b)
# print(s)

# a = [random.randint(0,100) for i in range(10)]
# print('рандомный список 10 чисел:', a)
# b = []
# for x in a:
#     if x % 2 != 0:
#         b.append(x)
# print('новый список нечётных чисел', b)


# a = [random.randint(50,70) for i in range(10)]
# print('список чисел между 50 и 70:',a)
# b = []
# for i in a:
#     if i > 65:
#        b.append(i)
# kor = tuple(b)
# print('числа более 65:', kor)
# print(type(kor))

def sum(a,b): return a+b
print(sum(1,5))