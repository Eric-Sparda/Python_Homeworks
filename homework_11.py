#----------------------------------------6.Цикл while----------------------------------------
#1-----------------------------------------------------------
# count = 0
# number = int(input("Введите число: "))

# while count < number:
#     count+=1
#     power = count **3
#     print(power)

#2-----------------------------------------------------------

# money = int(input("Сколько ваша задолженность составляет ?: "))

# while True:
#     pay = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?: "))
#     money -= pay
#     if money == 0:
#         print("Отлично! Вы погасили долг. Спасибо!")
#         break
#     else:
#         print("Маловато. Давайте ещё раз")

#3-----------------------------------------------------------

# number = int(input("Введите число: "))
# count = 0

# while True:
#     if number > 0:
#         count+=1
#         number = number//10
#     else:
#         break

# print(count)

#4-----------------------------------------------------------

# pos = 0
# neg = 0
# zero = 0
# while True:
#     number = input("Поставьте оценку(Нажмите Enter чтобы выйти): ")
#     if number == "":
#         break
#     else:
#         number = int(number)
#         if number > 0:
#             pos+=1
#         elif number < 0:
#             neg+=1
#         else:
#             zero+=1
# print(f"Кол-во положительных чисел:{pos}\nКол-во отрицательных чисел:{neg}\nКол-во нулей:{zero}" )

#5-----------------------------------------------------------

# import random

# count = 0
# task = 0
# all_tasks = 0
# yes_no = 0

# print("Начался восьмичасовой рабочий день.")

# while count < 8:
#     count += 1
#     task = random.randint(1,5)
#     all_tasks += task
#     print(f"Сколько задач решит Максим ? {task}")
#     question = input("Звонит жена. Взять трубку ?: ").lower() 
#     if question == "да":
#         yes_no = 1
#         print("Зайди вечером в магазин.")
#     elif question == "нет":
#         continue
# print(f"Рабочий день закончился. Всего выполнено задач: {all_tasks}")
# if yes_no == 1:
#     print("Нужно зайти в магазин")
# else:
#     pass

#6-----------------------------------------------------------

# x = int(input("Сколько хотите вложить ?: "))
# p = int(input("Под какой процент ?: "))
# y = int(input("Введите сумму цели: "))
# year = 0

# while x < y:
#     year += 1
#     x = x + (x*(p/100))
#     x = (2 * x)//2
#     print(x)
# print(f"Понадобится {year} года")

#7-----------------------------------------------------------

# import random

# num = random.randint(1,10)
# count = 0
# while True:
#     count+=1
#     guess = int(input("Введите число: "))
#     if guess != num:
#         print("Число меньше, чем нужно. Попробуйте ещё раз!")
#     else:
#         print(f"Вы угадали! Число попыток: {count}")
#         break

#8-----------------------------------------------------------


#----------------------------------------7.For_ циклы со счётчиком----------------------------------------
#1-----------------------------------------------------------

# count = 0
# for i in range(10):
#     number = int(input("Введите номер должника: "))
#     if number % 2 == 0 and number > 0:
#         count+=1

# print(count, "Являются должниками")

#2-----------------------------------------------------------

# avrg_salary = 0
# for i in range(12):
#     monthly_salary = int(input("Введите зарплату сотрудника: "))
#     avrg_salary += monthly_salary

# print("средняя зарплата за год. = ", (avrg_salary/12))

#3-----------------------------------------------------------

# number = int(input("Введите число: "))
# factorial = 1
# for i in range(1,number+1):
#     factorial *= i
# print(factorial)

#4-----------------------------------------------------------

# a = 0
# b = 0
# c = 0

# students = int(input("Сколько учеников в классе ?: "))
# for i in range(students):
#     grade = int(input("Введите оценку: "))
#     if grade == 5:
#         a+=1
#     elif grade == 4:
#         b+=1
#     elif grade == 3:
#         c+=1
# print(f"В классе\n{a} отличников\nхорошистов {b}\nтроечников {c}")

#5-----------------------------------------------------------

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# count = 0
# avrage = 0

# for i in range(a,b+1):
#     if i % 3 == 0:
#         count += 1
#         avrage += i
# print(avrage/count)

#6-----------------------------------------------------------

# num = 0
# for i in range(10, 100):
#     num = (i//10) * (i%10)
#     if num*3 == i:
#         print(i, end= ", ")

#7-----------------------------------------------------------

# stack = int(input("Введите количество карточек: "))
# summ = 0
# for i in range(stack+1):
#     summ += i
# for i in range(stack-1):
#     card_number = int(input("Введите номер оставшейся карточки: "))
#     summ -= card_number
# print(summ)

#----------------------------------------8.For: циклы со счетчиком. Часть 2----------------------------------------
#1-----------------------------------------------------------

# g = 100
# month  = 0
# for i in range(g, -4, -4):
#     month  += 1
# print((f"через {month} месяцев останется {i} кг гречки"))

#2-----------------------------------------------------------

# debtor = int(input("Введите количество должников: "))
# debtor_number = 0
# summ = 0

# for i in range(debtor):
#     question = int(input(f"Должник c номером {debtor_number} \nСколько должны? "))
#     debtor_number += 5
#     summ += question
# print(summ)

#3-----------------------------------------------------------

# import time

# reverse_timer =  int(input("введите сколько должна готовится еда: "))

# for i in range(reverse_timer, -1, -1):
#     time.sleep(i)
#     if i == 0:
#         print("Ваша еда готова, осторожно горячo!")
#         break
#     ready = int(input("Ваша еда готова, можете забрать ?\n 1 - да\n 0 - нет\t: "))
#     if ready == 1:
#         print("Ваша еда готова, осторожно горячo!")
#         break
#     elif ready == 0:
#         continue

#4-----------------------------------------------------------

# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# c = int(input("Введите число c: "))
# count = 0
# sum_ = 0

# for i in range(a,b+1):
#     if i % c == 0:
#         count += 1
#         sum_ += i
# print (sum_/count)

#5-----------------------------------------------------------


# a = int(input("Введите начало отрезка: "))
# b = int(input("Введите конец отрезка: "))
# c = int(input("Введите шаг: "))
# c = ((-1)*c)
# y = 0

# for x in range(b, a-1, c):
#     y = x**3 + 2*x**2 - 4*x + 1
#     print(f"B точке {x} функция равна {y}")

#6-----------------------------------------------------------

# letter = int(input("Введите размер листа: "))

# count = 0

# for i in range(letter//12):
#     count += 1
# print(f"лист нужно сложить {2*(count - 1)} раз")

#7-----------------------------------------------------------***********************

# educational_grant = int(input("Введите размер степендии: "))
# expenses = int(input("Введите расходы на проживание: ")) 

# for i in range(2, 11):
#     expenses = expenses + (expenses * 0.03)
# print("у родителей попросить:",expenses-educational_grant)

#8-----------------------------------------------------------************************

# num =  int(input("number: "))
# summ = 0
# div = 1
# for i in range(num +1):
#     summ += div
#     div /= (-2)
#     if i % 2:
#         pass
#     else:
#         summ = (-1)*summ
# print(summ)

#9-----------------------------------------------------------

# x = int(input("Введите число x: "))
# nums1 = 2
# nums2 = nums1 - 1
# summ1 = 1
# summ2 = 1
# summ1 *= (x - nums2)
# summ2 *= (x - nums1)

# for i in range(1,65):
#     nums1 *= 2
#     nums2 = nums1 - 1
#     summ1 *= (x - nums2)
#     summ2 *= (x - nums1)

# if summ2 == 0:
#     print("Нельзя делить на 0")
# else:
#     print(f"RES = {summ1/summ2}")

#10-----------------------------------------------------------

# boys = int(input("Введите количество мальчиков: "))
# girls = int(input("Введите количество девочек: "))

# moreboys = ""
# equal= ""

# if boys == girls:
#     for i in range(boys):
#         equal += "BG"
#     print(equal)

# elif boys > girls:
#     for i in range(boys - girls):
#         moreboys += "BGB"
#     print(moreboys)

# elif (boys > 2 * girls) or (girls > 2 * boys):
#     print("Нет решения.")

#----------------------------------------9.Цикл for_ работа со строками----------------------------------------
#1-----------------------------------------------------------

# day = input("Введите день недели: ").lower()
# count = 0

# for i in ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"):
#     count+=1
#     if i == day:
#         print(f"Номер дня недели: {count}")
#         break

#2-----------------------------------------------------------

# count = 0

# for i in range(10):
#     word = input("Введите текст: ").lower()
#     if word == "карамба":
#         count+=1
# print(f"Слово Карамба было сказано {count} раза")

#3-----------------------------------------------------------

# text = input("Введите текст: ")
# count = 0
# num = 0
# new_text = ""

# for i in text:
#     count+=1
#     num+=1
#     if count ==1:
#         num = 0
#     new_text += i
#     if text[num] == "*":
#         break
# print(f"Символ '*' стоит на позиции {count}")

#4-----------------------------------------------------------

# row = int(input("Введите кол-во рядов: "))
# seats = int(input("Введите кол-во сидений в ряду: "))
# distance = int(input("Введите кол-во метров между рядами: "))
# print("Сцена")
# for i in range(row):
#     print(seats*"=", distance*"*",seats*"=")

#5-----------------------------------------------------------

# move = input("Марсоход находится на позиции 8, 10 введите команду: ").lower()
# x = 8
# y = 10

# while x != -1 and y != -1:
#     if move == "":
#         break
#     else:
#         if move == "w" and y != 20:
#             y+=1
#             move = input(f"Марсоход находится на позиции {x,y} введите команду: ").lower()
#         elif move == "s" and y != 1:
#             y-=1
#             move = input(f"Марсоход находится на позиции {x,y} введите команду: ").lower()
#         elif move == "a" and x != 1:
#             x-=1
#             move = input(f"Марсоход находится на позиции {x,y} введите команду: ").lower()
#         elif move == "d" and x != 15:
#             x+=1
#             move = input(f"Марсоход находится на позиции {x,y} введите команду: ").lower()
#         elif x == 1 or x == 15:
#             move = input(f"Марсоход находится на позиции {x,y} введите команду: ").lower()
#         elif y == 1 or y == 20:
#             move = input(f"Марсоход находится на позиции {x,y} введите команду: ").lower()

#6-----------------------------------------------------------

# text = input("Введите текст: ")
# count = 0
# fin_count = 0

# for i in text:
#     if i == "s":
#         count +=1
#     if count > fin_count:
#         fin_count=count
#     if i != "s":
#         count = 0
# print(f"Самая длинная последовательность: {fin_count}")

#7-----------------------------------------------------------

# text = input("Введите текст: ")
# count = 0
# fin_count = 0

# for i in text:
#     count +=1
#     if i == " ":
#         count = 0
#     if count > fin_count:
#         fin_count = count
# print(f"Самое длинное слово: {fin_count} букв")

#8-----------------------------------------------------------*******************************************

# sign = int(input('Введите кол-во знаков в колонтитуле: '))
# exc = int(input('Введите кол-во восклицательных знаков: '))


# row = sign*"~"
# row = row + '!'*exc + row
# print(row)

#9-----------------------------------------------------------

# text = input("Введите строку из букв a и b: ")
# milk = 0
# if len(text) < 10:
#     for j in range(len(text)):
#         if len(text) != 10:
#             print("Введите 10 символов")
#             text = input("Введите строку из букв a и b: ")
# if len(text)==10:
#     for i in range(10):
#         if text[i] == "b":
#             milk += (2 * (i+1))
# print(f"Всего молока: {milk}")

#10-----------------------------------------------------------

# text = input('Введите зашифрованное сообщение: ')

# even = ""
# odd = ""
# count = 0
# deciphered = ""

# for i in text:
#     count +=1
#     if count % 2 == 0:
#         even += i
#     else:
#         odd += i 
# print(odd+(even[::-1]))

#----------------------------------------10.Вложенные циклы----------------------------------------
#1-----------------------------------------------------------

# for i in range(6):
#     for j in range(1,11,2):
#         print(i + j, end="\t")
#     print()

#2-----------------------------------------------------------

# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()

#5-----------------------------------------------------------

# from math import sqrt

# steps = int(input("Введите кол-во ходов: "))
# count = 0

# for i in range(steps):
#     number = int(input("Введите число: "))
#     for j in range(2,number+1):
#         if number % j == 0:
#             count +=1
# print("Количество простых чисел в последовательности: ",count)

#6-----------------------------------------------------------

# num = int(input('Введите число N: '))
# sum_factorials = 1
# counter = 1

# for i in range(2, num + 1):
#   counter *= i
#   sum_factorials += counter
# print(f"Сумма факториалов: {sum_factorials}")

#7-----------------------------------------------------------

# step = int(input("step: "))
# number = int(input("Введите число: "))
# summ = 0
# count = 0
# maxx = 0 
# while count != step:
#     count += 1
#     number = int(number)
#     summ += number % 10
#     print(summ)
#     number //= 10
#     if summ > maxx:
#         maxx = summ
# print(maxx)

