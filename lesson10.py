# try:
#     a = 100 / 0
# except BaseException:
#     a = 1
# print(a)

# my_dict = {'a':1, 'b':2, 'c':3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('ключа нет')

# a = [1, 2, 3]
# try:
#     a[5]
# except IndexError:
#     print('no')

# my_dict = {'a':1, 'b':2, 'c':3}
# try:
#     value = my_dict['d']
# except IndexError:
#     print('индекса нет')
# except KeyError:
#     print('ключа нет')
# except:
#     print('другая ошибка')


# my_dict = {'a':1, 'b':2, 'c':3}
# try:
#     value = my_dict['d']
# except (IndexError, KeyError):
#     print('произошла ошибка IndexError или KeyError')

# my_dict = {'a':1, 'b':2, 'c':3}
# try:
#     value = my_dict['b']
# except KeyError:
#     print('error KeyError')
# finally:
#     print(' operator finally done')


# my_dict = {'a':1, 'b':2, 'c':3}
# try:
#     value = my_dict['b']
# except KeyError:
#     print('error KeyError')
# else:
#     print(' error is not')


# my_dict = {'a':1, 'b':2, 'c':3}
# try:
#     value = my_dict['b']
# except KeyError:
#     print('error KeyError')
# else:
#     print(' error is not')
# finally:
#     print(' operator finally done')

# a = int(input('введите делимое'))
# b = int(input('введите делитель'))
# try:
#     c = a / b
# except ZeroDivisionError:
#     print('на ноль делить нельзя')
# else:
#     print(c**2)
# finally:
#     print('оператор finally выполнен')


# a = int(input('введите делимое'))
# b = int(input('введите делитель'))
# try:
#     c = a / b
# except ZeroDivisionError:
#     print('на ноль делить нельзя')
# except Exception:
#     print('ошибка общего исключения')
# except ValueError:
#     print('ошибка преобразования')

# дз по исключениям
try:
    a = int(input('введите первое значение:'))
    b = int(input('введите второе значение: '))
    c = a / b
except ValueError:
    print('введены не цифры')
except ZeroDivisionError:
    print('на ноль делить нельзя')
    if b == 0:
        d = int(input('введите первое значение заново:'))
        e = int(input('введите второе значение заново:'))
        w = d/e
        print('деление =', w)
else:
     c = a / b
     print('деление =', c)





