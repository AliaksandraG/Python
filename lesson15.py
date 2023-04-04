# class Human:
#
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self,km):
#         if km > 5:
#             return f'я не могу пройти {km} км'
#         else:
#             return f'я могу пройти {km} км'
#
#
# my_human = Human('sasha',21)
# my_human2 = Human('stas',22)
#
#
# class Car:
#     #статические поля(переменные класса)
#     default_color = 'grey'
#     default_weight = 5000
#     def __init__(self,color,model):
#         #динамические поля(переменные объекта)
#         self.color = color
#         self.model = model
#     def turn_on(self):
#         pass
# print(dir(Car))


# class TheExample:
#     a = 2
#     b = 3
#     def __init__(self,t,r):
#         self.t = t  #привязываем к классу переменную
#         self.r = r
#     def func1(self):
#         self.c = 5
#         print(self.c)
#     def func2(self):
#         return self.a + self.b
#     def func3(self):
#         return self.t ** self.r
# example = TheExample(4,2)
# print(example.a)
# print(example.func3())
# print(example.func2())
# example.func1()

# дз ооп
class Homework:
    def __init__(self):
        self.g = 0
        self.s = 0
        self.n = 0
        self.sogl = []
        self.gl = []
    def function(self,x):
        if type(x) is str:
            for i in x:
                if i in 'ёуеыаоэяию':
                    self.g += 1
                    self.gl.append(i)
                else:
                    self.s += 1
                    self.sogl.append(i)
            if self.g * self.s <= self.function1(x):
                print('гласные:',self.gl)
            else:
                print('согласные:',self.sogl)
        else:
            for i in str(x):
                i = int(i)
                if i%2 == 0:
                    self.n += i
            print('произведение:',self.n * self.function1(x))
    def function1(self,x):
        return len(str(x))

zadanie = Homework()
z = input('введите слово или число:')
if z.isalpha():
    zadanie.function(z)
else:
    zadanie.function(int(z))