#---------------------------------------------------------------------Lesson13---------------------------------------------------------------------
#1-----------------------------------------------------

# l = [10,20,30,(10,20), 40]
# for i in range(len(l)):
#     if type(l[i]) == tuple:
#         break
#     else:
#         print(l[i],end=" ")

#2-----------------------------------------------------

# x = (5, 10, 15, 20)
# y = reversed(x) 
# print(tuple(y))

#3-----------------------------------------------------

# x = (5, 10, 15, 20)
# print(len(x))

#4-----------------------------------------------------

# tuple1 = ("e", "x", "a", "m", "p", "l", "e")
# tuple2 =  "".join(tuple1)
# print(tuple2)

#5-----------------------------------------------------

# my_tuple = (1,12,15)
# summ=0
# for i in range(len(my_tuple)):
#     summ += my_tuple[i]
# print(summ)

#6-----------------------------------------------------

# name = int(input("Which name you want to find ?(Enter a number): "))

# my_tuple = ("John", "Mark", "Peter")

# for i in range(len(my_tuple)):
#     if i == name:
#         print(my_tuple[i])
#         break
# else:
#     print("No name under this number")

#---------------------------------------------------------------------Lesson14---------------------------------------------------------------------
#1-----------------------------------------------------

# list1=[]
# summ = 0
# while True:
#     number = input("Enter a number(Press enter to exit): ")
#     if number == "":
#         break
#     else:
#         number = int(number)
#         list1.append(number)
# for i in range(len(list1)):
#     summ += list1[i]
# print(summ)

#2-----------------------------------------------------

# list1=[]
# summ = 1
# while True:
#     number = input("Enter a number(Press enter to exit): ")
#     if number == "":
#         break
#     else:
#         number = int(number)
#         list1.append(number)
# for i in range(len(list1)):
#     summ *= list1[i]
# print(summ)

#3-----------------------------------------------------

# list1=[]
# summ = 1
# while True:
#     number = input("Enter a word(Press enter to exit): ")
#     if number == "":
#         break
#     else:
#         list1.append(number)
# list1 = sorted(list1, key=len)
# print(list1[-1])

#4-----------------------------------------------------

# list1=[]
# list2 = []
# summ = 1
# while True:
#     number = input("Enter a number/word for list 1(Press enter to exit): ")
#     if number == "":
#         break
#     else:
#         list1.append(number)

# while True:
#     number = input("Enter a number/word for list 2(Press enter to exit): ")
#     if number == "":
#         break
#     else:
#         list2.append(number)

# for i in range(len(list2)):
#     for j in range(len(list1)):
#         if list2[i] == list1[j]:
#             print("Ture")
#             break
#         else:
#             continue

#---------------------------------------------------------------------Lesson15---------------------------------------------------------------------
#2-----------------------------------------------------

# name = input("What kind of laptop do you want?: ").lower()
# my_list =["hp", "asus", "dell", "mac", "lenovo"]

# if name in my_list:
#     print("True")
# else:
#     print("False")

#3-----------------------------------------------------

# password = input("Create a password: ")
# symbols = ["!","@","#","$","%","&","*"]
# digits= ["0","1","2","3","4","5","6","7","8","9"]

# low = 0
# upper = 0
# syb = 0
# num = 0
# while True:
#     if len(password) < 8:
#         password = input("Passwords length at least should be 8 symbols, try again: ")
#     for i in password:
#             if "a" <= i <= "z":
#                 low += 1
#             if "A" <= i <= "Z":
#                 upper += 1
#             if i in symbols:
#                 syb += 1
#             if i in digits:
#                 num += 1
#     if low >= 2 and upper >=2 and syb >= 2 and num >=2:
#         print("Strong Password")
#         break
#     else:
#         password = input("Weak Password, try again: ")

#5-----------------------------------------------------

# word = input("Enter a word: ")
# listt = list(word)
# rev = listt.copy()
# rev_list = rev.reverse()

# if listt == rev:
#     print("Open")
# else:
#     print("Trash")

#6-----------------------------------------------------

# word = input("Enter a word: ")
# print(list(word))

#7-----------------------------------------------------

# listt = []

# for i in range(5):
#     number = int(input("Enter a number: "))
#     if number % 2 != 0:
#         listt.append(number)
# string = " ".join(str(x) for x in listt)
# print(string)

#8-----------------------------------------------------****************

# listt = []

# while True:
#     ayt= input("anything: ")
#     if ayt == "":
#         break
#     else:
#         listt.append(ayt)

# for i in range(len(listt)):
#     if i % 2 == 0:
#         listt.remove(listt[i])
#     else:
#         pass
# print(listt)

#short way after while just write - del lst[1::2]

#9-----------------------------------------------------

# people=[]
# while True:
#     person=input("Enter a person participating(Enter to exit): ")
#     if person=="":
#         break
#     else:
#         people.append(person)

# for i in range(len(people)):
#     print(people[i],"buys for",people[(i+1)%(len(people))])

