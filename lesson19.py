# class Student:
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#
# student1 = Student('Petya', 100)
# student2 = Student('Kolya',200)
# student3 = Student('Vasya', 100)
# students = [student1,student2,student3]
# moneys = []
# for student in students:
#     moneys.append(student.money)
# print(moneys)
# if max(moneys) == min(moneys):
#     print('all')
# else:
#     max_money = 0
#     name_student = ''
#     for student in students:
#         if student.money > max_money:
#             max_money = student.money
#             name_student = student.name
#     print(f'Студент с наибольшим количеством денег {name_student} ---> {max_money}')



# class Calculator:
#
#     def validate_numbers(self,a,b):
#         is_valid_a = isinstance(a,int) or isinstance(a,float)
#         is_valid_b = isinstance(b,int) or isinstance(b,float)
#         if is_valid_a and is_valid_b:
#             print('valid')
#         else:
#             raise Exception('not valid')
#     def sum(self, a,b):
#         self.validate_numbers(a,b)
#         return a+b
#
#     def minus(self, a,b):
#         self.validate_numbers(a,b)
#         return a-b
#
#     def mul(self, a,b):
#         self.validate_numbers(a,b)
#         return a*b
#
#     def delenie(self, a,b):
#         self.validate_numbers(a,b)
#         if b == 0:
#             return 'ERROR'
#         else:
#             return a/b
# calc = Calculator()
# print(calc.sum(2,5))

#
# class Orange:
#     def __init__(self, sort, vitamins, price, name):
#         self.sort = sort
#         self.vitamins = vitamins
#         self.price = price
#         self.name = name
#
#     def clear(self):
#         return f'{self.name} is clear'
#
#     @property
#     def __repr__(self):
#         return f'sort{self.sort}, vitamins{self.vitamins}, price{self.price}, name{self.name}'
#
# class Apple(Orange):
#     def cut(self):
#         return f'{self.name}is cut'
#
# class Mandarin(Orange):
#     pass
#
# class Banana(Orange):
#     def __init__(self,sort,vitamins,price,name,num_of_kalium):
#         super().__init__(sort,vitamins, price, name)
#         self.num_of_kalium = num_of_kalium
#
#     def __repr__(self):
#         return f'sort{self.sort}, vitamins{self.vitamins}, price{self.price}, name{self.name},num of kalium{self.num_of_kalium}'
#
# orange = Orange('Verna',['a','b1','c'], 100, 'Orange')
# apple  = Apple('Antonovka',['a','b','c'],120, 'Apple')


class Student:
    def __init__(self, name, group,progress):
        self.name = name
        self.group = group
        self.progress = progress

class School:
            def __init__(self, students):
                self.students = students

            def add_students(self, student):
                self.students.append(student)

            def get_list_of_students(self):
                return self.students

            def remove(self, student, group):
                if student.group == group:
                    self.students.remove(student)

            def print_names(self):
                for student

            def print_group(selfs):