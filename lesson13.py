# def a_function():
#     print('вы создали функцию')
# a_function()
# a_function()
# a_function()
import random


# def empty_function():
#     pass

# def new_function():
#    a = [1,2,3]
#    print(sum(a))
# new_function()

# def add(a,b):
#     return a+b
# print(add(1,2))
# print(add(2,5))
# add(3,8)

# def add(a,b):
#     print(a+b)
# print(add(1,2))

# def add(a,b):
#     return a+b
# print(add(a=2,b=3))
# total = add(b=4, a=5)
# print(total)

# def keyword(a=1, b=2):
#     return a+b
# print(keyword(a=5,b=4))
# print(keyword())


# def mixed(a, b=2, c=3):
#     return a+b+c
# #mixed(b=4,c=5)  error
# print(mixed(1,b=4,c=5))
# print(mixed(1))


# def many(*args, **kwargs):
#     print(args)  кортежи
#     print(kwargs)  словарь
# many(1,2,3,name='sasha', age='21')


# def abcd():
#     a=1
#     b=2
#     return a+b
# print(abcd())

# def fun():
#     global a
#     a = 1
#     b = 2
#     return a+b
# def fun1():
#     c = 3
#     return a+c
# print(fun())
# print(fun1())


# def func1(a,b):
#     def in_func1(x):
#         return x*x*x
#     return in_func1(a)+in_func1(b)
# print(func1(4,5))


# def sum(a,b): return a+b
# print(sum(2,3))


# def is_year_leap(x):
#     return x % 4 ==0 and x % 100 != 0 or x % 400 == 0
# print(is_year_leap(int(input('год на проверку:'))))


# import math
# def square(x):
#     a = x*4
#     b =  x*x
#     c = math.sqrt(2)*x
#     return a,b,c
# print(square(int(input('введите сторону квадрата:'))))


# def season(x):
#     if x <=2 or x == 12:
#         print('это зима')
#     elif x == 3 or x == 4 or x ==5:
#         print('это весна')
#     elif x == 6 or x ==7 or x ==8:
#         print('это лето')
#     else:
#         print('это осень')
#     return x
# print(season(int(input('введите номер месяца:'))))

# import random
# def sr_ar():
#     sum = 0
#     a = [random.randint(0,100) for i in range(10)]
#     for z in a:
#         sum += z
#     return a,sum/10
# print(sr_ar())


# def dlina(a):
#     return a, len(a)
# print(dlina(input('введите строку:')))


# def chislo(x):
#     if x < 0:
#         print('число отрицательное')
#     elif x > 0:
#         print('число положительное')
#     else:
#         print('введен 0')
#     return x
# chislo(int(input('введите число:')))


# def n_ch():
#     a = int(input('введите число:'))
#     b = int(input('введите число:'))
#     c = int(input('введите число:'))
#     if a>b and a>c:
#         print('наибольшее число:',a)
#     elif b>a and b>c:
#         print('наибольшее число',b)
#     else:
#         print('наибольшее число',c)
# n_ch()


# def umn(x):
#     for i in range(1,11):
#         print(x*i,' ',end=' ')
#     return x,x*i
# umn(int(input('введите число')))


# def mass():
#     a = int(input('введите начало диапозона:'))
#     b = int(input('введите конец диапозона:'))
#     c = [random.randint(a,b) for i in range(5)]
#     print(c)
# mass()


# def rasr(x):
#     s = 0
#     while x>0:
#         x = x//10
#         s += 1
#     return s
# q = abs(int(input('введите число:')))
# print('кол-во разрядов:', rasr(q))

# дз по функции1

def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def division(a,b):
    if b==0:
        return 'на ноль делить нельзя'
    else:
        return a/b
def multiply(a,b):
    return a*b
while True:
    a = float(input('введите первое число:'))
    b = float(input('введите второе число:'))
    x = input('введите знак для операции(+,-,/,*)(используйте 0 для выхода):')
    if x == '0':
        print('до свидания!')
        break
    elif x == '+' :
        print('=', plus(a, b))
    elif x == '-' :
        print('=', minus(a, b))
    elif x == '/' :
        print('=',division(a, b))
    elif x == '*' :
        print('=',multiply(a, b))