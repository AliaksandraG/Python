# class Car:
#     def start(self):
#         print('двигатель запущен')
# car_a = Car()
# print(car_a)

# class Car:
#     def __str__(self):
#         return 'car class object'
#     def start(self):
#         print('двигатель запущен')
# car_a = Car()
# print(car_a)

# class Phone:
#     @staticmethod
#     def model_hash(model):
#         if model == 'I785':
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
# print(Phone.model_hash('I785'))

class Human:
    # статические поля
    default_name = 'Sasha'
    default_age = 21

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 1000
        self.__house = 'home'

    def info(self):
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
        print(f'House:{self.__house}')
        print(f'Money:{self.__money}')

    @staticmethod
    def default_info():
        print(f'Default Name:{Human.default_name}')
        print(f'Default Age:{Human.default_age}')

    def earn_money(self, plus_money):
        self.__money += plus_money
        return self.__money

Human.default_info()
Aleksandra = Human('Stas', 22)
Aleksandra.info()
Aleksandra.earn_money(2000)
Aleksandra.info()