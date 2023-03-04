#-------------------------------------------------------------------11.Введение в ООП-------------------------------------------------------------------
#1-------------------------------------------------------------------

# from random import randint

# class game:
#     def __init__(self) -> None:
#         self.warrior1 = 100
#         self.warrior2 = 100

#     def fight(self):
#         while True:
#             turn = randint(0,1)

#             if turn == 0:
#                 self.warrior2 -= 20
#             else:
#                 self.warrior1 -= 20

#             if self.warrior1 <= 0:
#                 return f"Warrior 2 won"
#             elif self.warrior2 <= 0:
#                 return f"Warrior 1 won"
            
# print(game().fight())

#2-------------------------------------------------------------------

# students = []

# class Student:
#     def __init__(self, name, group, grades):
#         self.name = name
#         self.group = group
#         self.grades = grades

#     def average_grade(self):
#         avrg = round(sum(self.grades) / len(self.grades), 2)
#         return f"{self.name}, группа {self.group}, средний балл {avrg}"

# while len(students) < 3:    
#     name = input("Введите ФИ студента: ")
#     group = input("Введите номер группы: ")
#     grades = input("Введите успеваемость: ").split()
#     grades = [int(i) for i in grades]
#     student = Student(name, group, grades)
#     students.append(student.average_grade())

# for i in students:
#     print(i)

#3-------------------------------------------------------------------

# class Circle:
#     def __init__(self, x=0, y=0, r=1):
#         self.x = x
#         self.y = y
#         self.r = r

#     def area(self):
#         return 3.14 * self.r ** 2

#     def perimeter(self):
#         return 2 * 3.14 * self.r

#     def increase(self, k):
#         self.r *= k

#     def intersect(self, x2,y2,r2):
#         d = ((self.x - x2) ** 2 + (self.y - y2) ** 2)**0.5
#         return d < self.r + r2
    

# x2 = float(input("Введите координату X центра второго круга: "))
# y2 = float(input("Введите координату Y центра второго круга: "))
# r2 = float(input("Введите радиус второго круга: "))
# k = float(input("Введите коэффициент увеличения для первого круга: "))
# circle1 = Circle()
# circle2 = Circle(x2,y2,r2)  

# print(circle1.area())
# print(circle1.perimeter())
# print(circle1.r)
# circle1.increase(k)

# print(circle1.intersect(x2, y2, r2))

#6-------------------------------------------------------------------

# class Element:
#     def __init__(self, element1, element2):
#         self.element1 = element1
#         self.element2 = element2

#     def combine_elements(self):
#         if self.element1 == 'Вода' and self.element2 == 'Воздух' or self.element1 == 'Воздух' and self.element2 == 'Вода':
#             return f"Шторм"
#         elif self.element1 == 'Вода' and self.element2 == 'Огонь' or self.element1 == 'Огонь' and self.element2 == 'Вода':
#             return f"Пар"
#         elif self.element1 == 'Вода' and self.element2 == 'Земля' or self.element1 == 'Земля' and self.element2 == 'Вода':
#             return f"Грязь"
#         elif self.element1 == 'Воздух' and self.element2 == 'Огонь' or self.element1 == 'Огонь' and self.element2 == 'Воздух':
#             return f"Молния"
#         elif self.element1 == 'Воздух' and self.element2 == 'Земля' or self.element1 == 'Земля' and self.element2 == 'Воздух':
#             return f"Пыль"
#         elif self.element1 == 'Огонь' and self.element2 == 'Земля' or self.element1 == 'Земля' and self.element2 == 'Огонь':
#             return f"Лава"
#         else:
#             return None

# element1 = input("Введите первый элемент: ").title()
# element2 = input("Введите второй элемент: ").title()
# print(Element(element1,element2).combine_elements())

#7-------------------------------------------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# from random import randint

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.hunger = 50
#         self.freezer = 50
#         self.money = 0

#     def life(self):
#         count = 0
#         while count != 365:
#             count += 1
#             action = randint(1,3)
#             if self.hunger >= 1:
#                 if self.freezer <= 10:
#                     self.money -= 40
#                     self.freezer += 40
#                 elif self.money <= 50:
#                     self.hunger -= 20
#                     self.money += 10
#                 else:
#                     self.hunger -= 10
#                     self.freezer -= 10
                
#                 if action == 1:
#                     self.hunger += 20
#                     self.freezer -= 20
#                 elif action == 2:
#                     self.hunger -= 10
#                     self.money += 30
#                 elif action == 3:
#                     self.hunger -= 20
#             else:
#                 return f"{self.name} умер от голода!"
#         if self.hunger < 0:
#             return f"{self.name} умер от голода!"
#         else:
#             return f"{self.name} прожил год и остался жив!"


# person1 = Person("Артём")
# person2 = Person("Ольга")

# print(person1.life())
# print(person2.life())


