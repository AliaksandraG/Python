# def factorial(n):
#     if n != 0:
#         return  n* factorial(n-1)
#     else:
#         return 1
# print(factorial(4))

# def add(a,b):
#     return a+b
# cake = add(1,2)
# cake1 = add(2,3)
# print(cake)
# print(cake1)


# def func(x): return x
# a1 = func
# a2 = a1
# print(a2(10))


# def sq(x): return x*x
# square = sq

# product = lambda x=3,y=2 : x**y
# square = product
# print(product(5))
# print(type(product))

#
# def mul(a):
#     def helper(b):
#         return a*b
#     return helper
# print(mul(3)(2))


# def simple(fn):
#     def wrapper():
#         print('start function')
#         fn()
#         print('stop function')
#     return wrapper
#
# def first():
#     print('test function 1')
# def second():
#     print('test function 2')


# def simple(fn):
#     def wrapper():
#         print('start function')
#         fn()
#         print('stop function')
#     return wrapper
#
# @simple
# def first():
#     print('test function 1')
# @simple
# def second():
#     print('test function 2')
# first()
# second()


# def circle(x):
#     s1 = 3.14*x**2
#     print('площадь круга', s1)
# circle(int(input('введите радиус круга:')))

# def rectangle(y,z):
#     s2 = y*z
#     print('площадь прямоугольника:',s2)
# y = (int(input('введите длину прямоугольника')))
# z = (int(input('введите ширину прямоугольника:')))
# rectangle(y,z)

# def triangle(a,b,c):
#     p = a+b+c
#     p2 = p/2
#     s3 = p2*(p2-a)*(p2-b)*(p2-c)
#     s4 = s3**0.5
#     print('площадь треугольника:',s4)
# a = float(input('введите сторону треугольника:'))
# b = float(input('введите сторону треугольника:'))
# c = float(input('введите сторону треугольника:'))
# triangle(a,b,c)

# дз по функциям 2

# def function(x):
#     if type(x) == tuple:
#         print('длина всех слов:', len(x))
#     elif type(x) == list:
#         numbers = 0
#         letters = 0
#         for i in x:
#             if type(i) == int:
#                 numbers += 1
#             if type(i) == str:
#                 letters +=1
#         print('кол-во букв:', letters)
#         print('кол-во цифр:', numbers)
#     elif type(x) == int:
#         nech = 0
#         for i in str(x):
#             i = int(i)
#             if i%2 != 0:
#                     nech += 1
#         print('кол-во нечётных цифр:', nech)
#     elif type(x) == str:
#         print('кол-во букв:', len(x))
#     else:
#         print('неизвестный тип')
# function(135246)


# def del_from_tuple(tuple1,element):
#     x = list(tuple1)
#     if element in tuple1:
#         x.remove(element)
#     return tuple(x)
# print(del_from_tuple((1,2,3,4,5),3))


