# a = open('file1 for lesson 11.txt', 'r')
# print(*a)
# a.close()

# with open('file1 for lesson 11.txt') as a:
#     print(*a)

# a = open('file1 for lesson 11.txt', 'r')
# print(a.read(8))
# print(a.read(8))


# a = open('file1 for lesson 11.txt', 'r')
# print(a.readline())
# print(a.readline())

# a = open('file1 for lesson 11.txt', 'r')
# print(a.readlines())

# a = open('xyz.txt', 'w')
# a.write('hello my kitten')
# a.close()
# a = open('xyz.txt', 'r')
# print(*a)
# a.close()
# import os
# os.rename('xyz.txt','zzz.txt')

# import os
# print('текущая директория:', os.getcwd())
# os.mkdir('cats') при повторном запуске ошибка


# import os
# os.chdir('cats') #изменение название
# print(os.getcwd())

# import os
# os.chdir('cats')
# os.chdir('..')
# os.makedirs('cat1,2/cat1/cat2')
#
# import os
# os.remove('xyz.txt')

# import os
# os.removedirs('cat1/cat2/cat3')


# with open('file1 for lesson 11.txt') as f:
#     a = f.readlines()
#     print(a)
# for i in a:
#     i = i.replace('_', ' ')
#     b = i.split(' ')
# print(b)
# sum = 0
# for i in b:
#     if i.isdigit():
#         i = int(i)
#         sum += i
# print(sum)

# with open('file1 for lesson 11.txt') as f:
#     a = f.readlines()
#     print(a)
# for i in a:
#     if i.isdigit():
#         print(a.sort())



# дз по файлам
a = [1,7,'cats',2,'dog',5,'hamster']
f = open('dz10les','w')
words = []
numbers = []
for i in a:
    if type(i) is int:
        numbers.append(i)
        numbers.sort()
    else:
        words.append(i)
        words1 = sorted(words, key=len)
mas =words1 +numbers
print(mas)
x = str(mas)
f.write(x)
f.close()