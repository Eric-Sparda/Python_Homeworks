#------------------------------------------------------------------2.Базовые коллекции 1 - list------------------------------------------------------------------
#1------------------------------------------------------------------
# listt = []
# num = int(input("Enter a number: "))
# for i in range(num+1):
#     if i % 2 != 0:
#         listt.append(i)
# print(listt)

#2------------------------------------------------------------------

# listt = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
# listt2 = []

# for i in range(0,len(listt),2):
#     listt2.append(listt[i])

# print(listt2)

#3------------------------------------------------------------------

# import random
# listt = []
# num = int(input("Количество клеток: "))

# while True:
#     for i in range(num):
#         listt.append(random.randint(0,num))
#     break

# for i in range(len(listt)):
#     print(f"Эффективность {i+1} клетки: {listt[i]}")

#4------------------------------------------------------------------

# old_listt = [3070, 2060, 3090, 3070, 3090]
# new_listt = []
# for i in range(len(old_listt)):
#     print(f"{i+1} Видеокарта: {old_listt[i]}")
#     if old_listt[i] != max(old_listt):
#         new_listt.append(old_listt[i])
# print(f"Старый список видеокарт: {old_listt}")
# print(f"Новый список видеокарт: {new_listt}")

#5------------------------------------------------------------------

# films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
# num = int(input("Сколько фильмов хотите добавить? "))
# user = []
# for i in range(num):
#     movie_name = input("Введите название фильма: ").title()
#     if movie_name in films:
#         user.append(movie_name)
#     else:
#         print(f"Ошибка: фильма {movie_name} y нас нет :(")
# print(f"Ваш список любимых фильмов: {user}")

#6------------------------------------------------------------------

# word = input("Введите слово: ")
# word_listt = list(word)
# unique_letters = []

# for i in word_listt:
#     letter = word_listt.count(i)
#     if letter < 2:
#         unique_letters.append(i)
#     else:
#         pass
# print(f"Количество уникальных букв: {len(unique_letters)}")

#7------------------------------------------------------------------

# amount = int(input("Количество контейнеров: "))
# listt = []
# count = 1
# for i in range(amount):
#     mass = int(input("Введите вес контейнера: "))
#     listt.append(mass)
# num = int(input("Введите вес нового контейнера: "))
# listt.append(num)
# listt.sort()
# for i in listt:
#     if i == num:
#         print(count)
#         break
#     else:
#         count += 1
# print(f"Номер, который получит новый контейнер: {listt}")

#9------------------------------------------------------------------

# word = input("Enter a word: ")
# listt = list(word)
# rev = listt.copy()
# rev_list = rev.reverse()

# if listt == rev:
#     print("Слово является палиндромом")
# else:
#     print("Слово не является палиндромом")

#10------------------------------------------------------------------

# listt = []
# while True:
#     num = input("Введите число: ")
#     if num == "":
#         break
#     else:
#         num = int(num)
#         listt.append(num)
# listt.sort()
# print(listt)

#------------------------------------------------------------------3.Методы для работы со списками------------------------------------------------------------------
#1------------------------------------------------------------------

# listt1 =  [1, 5, 3]
# listt2 =  [1, 5, 1, 5]
# listt3 =  [1, 3, 1, 5, 3, 3] 

# for i in listt2:
#     listt1.append(i)
    
# print(f"Кол-во цифр 5 при первом объединении: {listt1.count(5)}")

# listt1 =  [1, 5, 3]

# for i in listt3:
#     listt1.append(i)
# print(f"Кол-во цифр 3 при втором объединении: {listt1.count(3)}")
# listt1.sort()
# print(listt1)

#2------------------------------------------------------------------

# class1 = []
# class2 = []

# for i, j in zip(range(162,177,2), range(162,181,3)):
#     class1.append(i)
#     class2.append(j)
# for i in class2:
#     class1.append(i)
# class1.sort
# print(f"Отсортированный список учеников: {class1}")

#3------------------------------------------------------------------**********************************************************

# shop = [["каретка", 1200], ["шатун", 1000], ["седло", 300], ["педаль", 100], ["рама", 12000], ["обод", 2000]]
# summ =0 
# name = input('Название детали: ').lower()
# amount = int(input("Кол-во деталей: "))
# for i in shop:
#     if name == i[0]:
#         summ = amount * i[1]

# print("Общая стоимость:",summ)

#4------------------------------------------------------------------

# guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

# while True:
#     print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
#     come_go = input("Гость пришёл или ушёл? ").lower()
#     if come_go == "пора спать":
#         break
#     elif come_go == "пришёл":
#         new_guest = input("Имя гостя: ")
#         if len(guests) < 6:
#             guests.append(new_guest)
#         else:
#             print(f"Прости, {new_guest}, но мест нет.")
#     elif come_go == "ушёл":
#         new_guest = input("Имя гостя: ").title()
#         guests.remove(new_guest)
#         print(f"Пока, {new_guest}!")

#5------------------------------------------------------------------

# violator_songs = [['World in My Eyes', 4.86],['Sweetest Perfection', 4.43],['Personal Jesus', 4.56],['Helo', 4.9],['Waiting for the Night', 6.07],['Enhoy the Silence', 4.20],['Policy of Truth', 4.76],['Blue Dress', 4.29],['Clean', 5.83]]

# quantity = int(input("Скодько песен выбрать? "))
# minn = 0

# for i in range(quantity):
#     name = input(f'Название {i + 1}-й песни: ').title()
#     for j in violator_songs:
#         if name == j[0]:
#             minn += j[1]
# print(f"Общая время звучания песен: {round(minn,2)} минуты")

#6------------------------------------------------------------------

# listt = []
# listt2 = []
# unique = []
# for i in range(3):
#     num = int(input(f"Введите {i + 1}-е число для первого списка: "))
#     listt.append(num)
# for i in range(7):
#     num2 = int(input(f"Введите {i + 1}-е число для второго списка: "))
#     listt2.append(num2)

# print(f"Первий список: {listt}")
# print(f"Второй список: {listt2}")

# for i in listt2:
#     listt.append(i)


# for i in listt:
#     if i not in unique:
#         unique.append(i)
# print(f"Новый первый список с уникальными элементами: {unique}")

#7------------------------------------------------------------------***************************************

# skates_size = []
# feet = []
# skates = int(input("Коль-во коньков: "))
# count = 0
# for i in range(skates):
#     feet_size = int(input("Размер 1-й пары: "))
#     skates_size.append(feet_size)
# skates_size.sort()
# print(skates_size)
# ppl = int(input("Кол-во людей: "))
# for i in range(ppl):
#     size= int(input(f"Размер ноги {i+1}-го человека: "))
#     feet.append(size)
# feet.sort()
# print(feet)
# for k in skates_size:
#     print(k)
#     for j in feet:
#         if k == j:
#             count += 1

# print(f"Наибольшее кол-во людей, которые могут взять ролики: {count}")

#10------------------------------------------------------------------******************************************

# listt = []
# iterations = int(input("Кол-во чисел: "))
# listt2 = []
# for i in range(iterations):
#     num = int(input("Число: "))
#     listt.append(num)
# print(f"Последовательность {listt}")

# for i in range(len(listt)-1):
#     listt2.append(listt[i])
# print(f"Нужно приписать чисел {len(listt2)}")
# listt2.reverse()
# print(f"Сами числа {listt2}")