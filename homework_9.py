# even = 0 

# for i in range(11):
#     numbers = int(input("Enter a number: "))
#     if numbers % 2 == 0 and numbers > 0:
#         even += 1
# print(even)
#--------------------------------------------------

# salary = int(input("Enter the salary "))
# money = 0
# for i in range (12):
#     money += salary
# print(money/12)

#--------------------------------------------------

# number = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, number +1):
#     factorial = factorial * i
# print(factorial)
    
#--------------------------------------------------

# a = 0
# b = 0 
# c = 0
# while True:
#     grade = int(input("Enter the greade(Enter 0 to exit): "))
#     if grade == 0:
#         break
#     else:
#         if grade == 5:
#             a += 1
#         elif grade == 4:
#             b += 1
#         elif grade == 3:
#             c += 1
# print(a,b,c)

#--------------------------------------------------

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# div = 0
# mid = 0
# for i in range(a,b+1):
#     if i % 3 == 0:
#         div += 1
#         mid += i
# print(mid/div)

#--------------------------------------------------

# for i in range(10,100):
#     if i % 3 == 0:
#         print(i)

#--------------------------------------------------

# card = int(input("Введите количество карточек: "))
# su =int((n+1)*n/2)
# for i in range (1,card):
#     su -= int(input("Введите номера оставшихся карт: "))
# print(su)

#--------------------------------------------------

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# i = 1

# if(a>b):
#     greater = a
# else:
#     greater = b
# while i > 0 :
#     if(greater % a == 0 and greater % b == 0):
#         print("LCM is:",greater)
#         break
#     greater = greater+1

#--------------------------------------------------

# for i in range(101):
#     if i % 2 == 0:
#         print(i,"number is even")
#     if i % 2 != 0:
#         print(i,"number is odd")

#--------------------------------------------------

# n1 = 0
# n2 = 1
# n_fin = 0
# while n_fin < 40:
#     n_fin = n1 + n2
#     n1 = n2
#     n2 = n_fin
#     print(n_fin)

#--------------------------------------------------

# string = input("Enter a word: ")
# number = 0
# for i in string:
#     number += 1
# print(number) 

#--------------------------------------------------

# number = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, number +1):
#     factorial = factorial * i
# print(factorial)

#--------------------------------------------------

# g = 100
# month  = 0
# for i in range(g, -4, -4):
#     month  += 1
# print((f"через {month} месяцев останется {i} кг гречки"))

#--------------------------------------------------

# debtor = int(input("Введите количество должников: "))

# sum_= 0

# for i in range(debtor):
#     question = int(input("Должник c номером 0\n Сколько должны? "))
#     sum_ += question
# print(sum_)

#--------------------------------------------------

# import time

# reverse_timer =  int(input("введите сколько должна готовится еда: "))

# for i in range(reverse_timer, -1, -1):
#     time.sleep(reverse_timer)
#     ready = int(input("Ваша еда готова, можете забрать ?\n 1 - да\n 0 - нет\t: "))
#     if ready == 1:
#         print("Ваша еда готова, осторожно горячo!")
#         break
#     elif ready == 0:
#         continue
    
#--------------------------------------------------

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

#--------------------------------------------------

# a = int(input("number1: "))
# b = int(input("number2: "))
# c = int(input("step "))
# y = 0

# for x in range(b, a-1, c):
#     y = x**3 + 2*x**2 - 4*x + 1
#     print(f"B точке {x} функция равна {y}")

#--------------------------------------------------

# letter = int(input("size: "))

# count = 0

# for i in range(letter//12):
#     count += 1
# print(f"лист нужно сложить {count - 1}раз")

#--------------------------------------------------

# num =  int(input("number: "))
# summ = ((-1)**num) * (1/(2**num))
# print(summ)

#--------------------------------------------------

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
#     print('Нет решения.')

#--------------------------------------------------