# a= {'one', 'two',2.0, 'three',(1,2,3), 'four'}
# print(a)


# a = set([1, 2, 3, 2, 1])
# print(a)
# a1 = {1, 2, 3, 2, 1}
# print(a1)

# x = {} будет словарь, а так множество х=()
# print(type(x))

# numbers = {'one', 'two', 'three', 'four'}
# for i in numbers:
#     print(i)


# numbers = {'one', 'two', 'three', 'four'}
# print('two' in numbers)
# print('five' in numbers)
#
# numbers = {'one', 'two', 'three', 'four'}
# numbers.add('five')
# print(numbers)

# numbers = {'one', 'two', 'three', 'four'}
# numbers.discard('five')
# print(numbers)

#
# numbers = {'one', 'two', 'three', 'four'}
# numbers.remove('five')
# print(numbers)

# numbers = {'one', 'two', 'three', 'four'}
# numbers.pop()
# print(numbers)

# numbers = {'one', 'two', 'three', 'four'}
# numbers.clear()
# print(numbers)

# numbers = {'one', 'two', 'three', 'four'}
# numbers2 = {'five', 'six', 'seven'}
# all_numbers  = numbers.union(numbers2)
# print(all_numbers)

# x = {2, 1, 3}
# y = {3, 4, 5}
# z = {5, 6, 7}
# all = x.union(y,z)
# print(all)

# numbers = {'one', 'two', 'three', 'four'}
# numbers2 = {'five', 'six', 'seven'}
# print(numbers | numbers2)

# a = { 1, 2, 3}
# b = {3, 4, 5}
# print(a & b)

# a = { 1, 2, 3}
# b = {3, 4, 5}
#
# print(a-b)
# print(b-a)


# numbers = {'one', 'two', 'three', 'four'}
# numbers2 = {'five', 'six', 'seven'}
# x = numbers.isdisjoint(numbers2)
# print(x)

# a = [1, 2, 3, 4, 5, 5, 4]
# a1 = set(a)
# b = len(a)
# b1 = len(a1)
# if b > b1:
#     print('есть дубликаты')
# else:
#     print('дубликатов нет')

# a = {1: 'one',
#      2: 'two',
#      3: 'three'}
# print('исходный словарь:', a)
# a['four']= 4
# print('добавили ключ', a)
# a[('it', 'number')] = [1, 2, 3]
# print('добавили ключ', a)
# b = a[1]
# print(b)
# del a[1]
# print(a)
# print(a.keys())

# a = {1, 2, 3, 4}
# b = frozenset([5, 6, 7])
# print(a)
# print(b)
# print(a|b)
# print(a&b)




