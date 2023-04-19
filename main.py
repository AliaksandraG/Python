# d = {1:2, 2:4, 3:9}
# d[4]= 4**2
# print(d[1])
# print(d)

# months = {1:'Jan', 2:'Feb', 3:'Mar'}
# count = len(months)
# print(count)
#
# fruit = {'cherry': 5.0,
#          'orange':8.5,
#          'apple':2.5}
# print(fruit)
# del fruit['orange']
# print(fruit)


# position = {'manager':{'director',
#                        'mini Director'}
#             'staff': {'cleaner',
#                         'porter',
#                         'watchman'}
#             'teacher': {'specialist',
#                         'methodist',
#                         'Lecturer'}}
# count1 = len(position)
# count2 = len(position['manager'])
# count3 = len(position['staff'])
# print(position, 'len:', count1)

# fruit = {'cherry': 5.0,
#          'orange':8.5,
#          'apple':2.5}
# print(fruit)
# key = 'orange'
# if key in fruit:
#     del fruit['orange']
# print(fruit)

# numbers = dict(zip([1,2,3], ['one', 'two','three']))
# print(numbers)


# months = {1:'Jan', 2:'Feb', 3:'Mar'}
# for i in months:
#     print(i, ':', months[i])

# person = {'name': 'sasha',
#           'age': '21',
#           'city': 'minsk'}
# print(person['age'])




#дз
#
# a = ('я изучаю новый язык програмированния ')
# print(a)
# b = a.split()
# print(max(b, key=len))


# a = 'в любом, тексте, много, много, запятых, не бывает.'
# a1 = ''
# for i in a:
#     if i != ',' and i != '.':
#       a1 = a1 + i
# print(a)
# print(a1)
# print(a1.split())



# #дз
# print('приветствуем в нашем магазине!')
# print('товар - цена - количество')
# my_dict = {'яблоко': [3.5, 6],
#            'банан': [4.5, 5],
#            'апельсин': [5.5, 4]}
#
# for key, value in my_dict.items():
#     print(key, '-', value[0], '-', value[1])
# summa = 0
# while True:
#     fruit = input('введите название товара(если ничего - введите "n"):')
#     if fruit == 'n' or fruit not in my_dict.keys():
#         print('До свидания!')
#         break
#     piece = int(input('введите количество:'))
#     if piece > my_dict[fruit][1]:
#         print('к сожалению столько нет')
#         continue
#         summa += my_dict[fruit][0] * piece
#         my_dict = my_dict[fruit][1] - piece
# print('к оплате:', summa)
# for key, value in my_dict.items():
#     print('остаток:')
#     print(key, '-', value[0], '-', value[1])


f1 = open('C:/Users/Александра/Downloads/Telegram Desktop/Проект-7-2/Проект-7-2/online/sms.py' ,'t')
# f1.readline()