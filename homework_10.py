#63---------------------------------------------------------------------------------

# numbers = float(input("Enter a number(Enter 0 to exit): "))
# s = 0
# s += numbers
# quantity = 0
# while numbers != 0:
#     numbers = float(input("Enter a number(Enter 0 to exit): "))
#     s += numbers
#     quantity += 1

# avr = s / quantity
# print(avr)

#64---------------------------------------------------------------------------------

# for item in range(0,5):
# 	original = 5*item + 4.95
# 	discounted = original / 0.4
	
# 	print(f"Original: ${round(original, 2)} | Discounted: $ {round(discounted,2)} ")

#65---------------------------------------------------------------------------------

# for celsius in range(0, 100, 10):    
#     fahrenheit = (celsius * (9/5)) + 32
#     print(fahrenheit)

#66---------------------------------------------------------------------------------

# import math

# summ_number = 0

# while True:
#     number = input("Enter number: ")
#     if number == "":
#         if summ_number % 5 >= 2.5:
#             print(math.ceil(summ_number))
#             break
#         else:
#             print(math.floor(summ_number))
#             break
#     else:
#         summ_number += float(number)

#67---------------------------------------------------------------------------------

# x1 = input("Enter the x part of the coordinate(Enter to exit): ")
# y1 = input("Enter the y part of the coordinate(Enter to exit): ")
# x2 = input("Enter the x part of the coordinate(Enter to exit): ")
# y2 = input("Enter the y part of the coordinate(Enter to exit): ")
# i = 1

# while i > 0:

#     if x1 != "" and x2 != "" and y1 != "" and y2 != "":
#         x1 = input("Enter the x part of the coordinate(Enter to exit): ")
#         y1 = input("Enter the y part of the coordinate(Enter to exit): ")
#         x2 = input("Enter the x part of the coordinate(Enter to exit): ")
#         y2 = input("Enter the y part of the coordinate(Enter to exit): ")
        
#         if x1 != "" and x2 != "" and y1 != "" and y2 != "":
#             x1 = int(x1)
#             x2 = int(x2)
#             y1 = int(y1)
#             y2 = int(y2)
#         else:
#             break
#     else:
#         break
#     distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
# print(distance)

#68---------------------------------------------------------------------------------

# grade = input("Enter the grade(press Enter to quit): ").upper()
# fin_grade = 0
# count = 0
# avrg = 0

# while grade != "":
#     count += 1
#     if grade =="A" or grade == "A+":
#         gr = 4.0
#     elif grade == "A-":
#         gr = 3.7
#     elif grade == "B+":
#         gr = 3.3
#     elif grade == "B":
#         gr = 3.0
#     elif grade == "B-":
#         gr = 2.7
#     elif grade == "C+":
#         gr = 2.3
#     elif grade == "C":
#         gr = 2.0
#     elif grade == "C-":
#         gr = 1.7
#     elif grade == "D+": 
#         grade = 1.3
#     elif gr == "D":
#         grade = 1
#     elif grade =="F":
#         gr = 0    
#     grade = input("Enter the grade: ").upper()
#     fin_grade += gr
#     avrg = fin_grade/count

# print(avrg)

#69---------------------------------------------------------------------------------

# total = 0
# price = 0
# while True:

#     age = input("Enter your age(press Enter to quit): ")
#     try:
#         number = int(age)
#     except:
#         break

#     if number <= 2:
#         price = 0

#     elif 3 <= number <= 12:
#         price = 14.00

#     elif number >= 65:
#         price = 18.00

#     else:
#         price = 23.00
#     total += price
# print(total)

#70---------------------------------------------------------------------------------

# while True:
#     bit = input("Enter 8 bit: ")
#     if bit == "":
#         break
#     else:
#         if len(bit) == 8:
#             if int(bit)%2 == 0:
#                 print("Even")
#             else:
#                 print("Odd")
#         else:
#             print("ERROR!!! Enter 8 bit")

#71---------------------------------------------------------------------------------

# n1 = 2
# n2 = 3
# n3 = 4

# pi = 3

# for i in range (15):
#     if i % 2 ==0:
#         pi % 2 == 0
#         pi += (4/(n1*n2*n3))
#         n1 = n3
#         n2 += 2
#         n3 += 2

#     else:
#         pi -= (4/(n1*n2*n3))
#         n1 = n3
#         n2 += 2
#         n3 += 2

# print(pi)

#72---------------------------------------------------------------------------------

# for i in range(0,101):
#     if i % 3 == 0:
#         print("Fizz")
        
#     elif i % 5 == 0:
#         print("Buzz")
        
#     elif i % 3 == 0 and i % 5 ==0:
#         print("Fizz - Buzz")
        
#73---------------------------------------------------------------------------------

# message = input("Enter a mesage: ")
# word = ""

# for i in message:
#     letter = ord(i) +3
#     new_letter = chr(letter)
#     word += new_letter
# print(word)

#74---------------------------------------------------------------------------------



#75---------------------------------------------------------------------------------

# text = input("Enter a word: ")
#
# for i, j in zip(range(0, len(text)), range(len(text) - 1, -1, -1)):
#     if text[i] != text[j]:
#         print("Word is not Palindrome")
#         break
# else:
#     print("Word is a Palindrome")

#76---------------------------------------------------------------------------------

# while True:
#     text = input("Enter a sentence: ")
#     replace = [" ", ",", ".", "!", "`", "~", ":", ";", """, "?"]
#     for char in replace:
#         text = text.replace(char, "")
#     if text == "":
#         break
#     else:
#         for i, j in zip(range(0,len(text)),range(len(text)-1, -1,-1)):
#             if text[i] != text[j]:
#                 print("Not a Palindrome")
#                 break
#             else:
#                 print("Palindrome")
#                 break

#77---------------------------------------------------------------------------------


#78---------------------------------------------------------------------------------

# number = input("Enter a number(Press Enter to exit): ")

# while True:
#     if number == "":
#         break
#     else:
#         number = int(number)
#         if number % 2 == 0:
#             number = number / 2
#             print(number)
#         else:
#             number = 3* number + 1
#             print(number)
#         if number == 1:
#             number = input("Enter a number(Press Enter to exit): ")
#             if number == "":
#                 break
#             else:
#                 number = int(number)
#         else:
#             continue

#79---------------------------------------------------------------------------------

# a =  int(input("Enter the first number: ")) #578438543
# b =  int(input("Enter the second number: ")) #48735678346534

# if a > b:
#     greater = a
#     lesser = b
# else:
#     greater = b
#     lesser = a

# for i in range(greater, (greater*lesser)+1,greater):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break

#80---------------------------------------------------------------------------------



#81---------------------------------------------------------------------------------

# binary  = input("Enter a binary number: ")
# count = len(binary)
# decimal = 0
# for i in range(len(binary)):
#     count -= 1
#     decimal += (int(binary[i]) * 2**(count))
# print(decimal)

#82---------------------------------------------------------------------------------

# decimal = int(input("Enter a decimal number: "))

# binary = ""
# while decimal > 0:
#     r = str(decimal % 2)
#     binary += r
#     decimal = decimal //2
# print(binary[::-1])

#83---------------------------------------------------------------------------------

# import random

# count = 0
# change = 0
# l = []

# for i in range(10):
#     number = random.randint(1,99)
#     number1 = random.randint(1,99)
#     l.append(number)
#     l.append(number1)
# for j in range(len(l)):
#     count += 1
#     if l[j+1] > l[j]:
#         change += 1
#         print(l[j])
#         print(l[j+1], "<====== Update")
#     if count == 10:
#         break

# print("The maximum value found was 100")
# print(f"The maximum value was updated {change} times")


#84---------------------------------------------------------------------------------

# import random
# tries = 0
# heads = 0
# tail = 0
# st_heads = ""
# st_tail = ""
# flips = ""
# while tries < 10:
#     coin = random.randint(0, 1)
#     tries += 1
#     if coin > 0:
#         heads +=1
#         st_heads += "H"
#     else:
#         tail += 1
#         st_tail += "T"
#     flips += st_tail
#     flips += st_heads
#     if "TTT" in flips:
#         print(flips, f"({tail} flips)")
        
#     if "HHH" in flips:
#         print(flips, f"({heads} flips)")
        


