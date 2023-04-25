#import os
#os.mkdir('C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2')
# a = open('C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\test_1.txt','w')
# b = open('C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\test_2.txt','w')
# c = open('C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\test_3.txt','w')
#os.rename('C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\test_1.txt','C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\rename_1.txt')
#os.rename('C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\test_2.txt','C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\rename_2.txt')
#os.rename('C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\test_3.txt','C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\rename_3.txt')
#os.remove('C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\rename_1.txt')
#os.remove('C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\rename_2.txt')
#os.remove('C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2\\rename_3.txt')
#os.rmdir('C:\\Users\\Александра\\OneDrive\\Рабочий стол\\Exam2')
import random

# import random
#
# a = ([random.randint(0,100) for i in range(10)])
# print('изначальный рандомный список(10 чисел):', a)
# print('сумма чисел в списке:', sum(a))
# b = sum(a)/10
# print('среднее арифметическое списка:',b )
# for i in a:
#     if i < b:
#        print('числа меньше среднего арифмитического:',i)

# import random
# a = {random.randint(0,50) for i in range(5)}
# print('первое множество:',a)
# b = {random.randint(0,50) for i in range(5)}
# print('второе множество:', b)
# if a == b:
#     print('множества равны')
# else:
#     print('множества неравны')
# if a.issubset(b):
#     print('множество 1 состоит из множества 2')
# if b.issubset(a):
#     print('множество 2 состоит из множества 1')
# if (a&b):
#     print('элементы пересечения', (a&b))
# else:
#     print('множества не пересекаются')


# str = 'An apple a day keeps the doctor away'
# str2 = ''.join(str.split(' '))
# dict1 = {i: str2.count(i) for i in str2}
# print(dict1)

# a = input('введите 10 чисел')
# a1 = ''.join(a.split(' '))
# x = set(a1)
# print(x)

# a = 0
# a1 = set([])
# while a < 10:
#     b = input('введите число:')
#     a = a + 1
#     a1.add(b)
# print(a1)



# songsdict = { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
# 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88,
# 'Blue Dress': 4.18, 'Clean': 5.68, }
# songs5 = []
# songs_in1word = {}
# print('общее время звучания:', sum(songsdict.values()))
# for i in songsdict:
#     if songsdict[i] >= 5:
#         songs5.append(i)
# print('список песен,звучание которых больше 5 минут:',songs5)
# for x in songsdict:
#     y = x.split()
#     if len(y) < 2:
#         songs_in1word[x] = songsdict.get(x)
# print('песни, названия которых состоят из одного слова:',songs_in1word)


# a = 'i love my cat because he is very cute'
# a1 =[]
# for i in a:
#     if a.count(i) > 1:
#         continue
#     else:
#         a1.append(i)
# a2 = tuple(a1)
# print(a2, type(a2))

# import random
# massiv = [random.randint(1,100) for i in range (10)]
# print('изначальный массив:',massiv)
# a = int(input('введите начало интервала: '))
# b = int(input('введите конец интервала:'))
# for i in range (a, b+1):
#     if i in massiv:
#         massiv.remove(i)
#         massiv.append(0)
# print('сжатый массив:',massiv)

#
# import random
# a = int(input('введите количество строк матрицы:'))
# b = int(input('введите количество столбцов матрицы:'))
# matrix = [[random.randint(-20,20) for x in range(a)] for i in range(b)]
# z = 0
# print('матрица:')
# for i in range (b):
#     print(matrix[i])
#     for x in range(1+1,a):
#         if matrix [i][x] < 0:
#             z = z + 1
# print('количество отрицательных элементов под главной диагональю матрицы:',z)
#
# import random
# a = [random.randint(0,100) for i in range (10)]
# print('список чисел:', a)
# a1 = max(a)
# a2 = min(a)
# print ('самый максимальный элемент:', a1)
# print('самый минимальный элемент:',a2)
# for x in a:
#     if x == a1 or x == a2:
#         a.remove(x)
# print('список без максимального и минимального элемента:',a)
# print('cумма элементов между минимальным и максимальным элементами(не включающая их):',sum(a))






