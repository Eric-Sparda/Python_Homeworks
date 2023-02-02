#110----------------------------------------------------------------------------------

# listt = []

# while True:
#     num = input("Enter a number(Enter to exit): ")
#     if num == "":
#         break
#     else:
#         listt.append(int(num))
# listt.sort()
# for i in listt:
#     print(i)

#111----------------------------------------------------------------------------------

# listt = []

# while True:
#     num = input("Enter a number(Enter to exit): ")
#     if num == "":
#         break
#     else:
#         listt.append(int(num))
# listt.sort()
# for i in listt[::-1]:
#     print(i)

#112----------------------------------------------------------------------------------******************

# import random
# listt = []
# for i in range(10):
#     listt.append(random.randint(1,100))
# listt.sort
# print(f"Original list: {listt}")
# listt.pop(0)
# listt.pop(-1)
# print(f"Outliers Removed: {listt}")

#113----------------------------------------------------------------------------------

# words = []
# new_words = []

# while True:
#     word = input("Enter a word(Enter to exit): ")
#     if word == "":
#         break
#     else:
#         words.append(word)
# for i in words:
#     if i not in new_words:
#         new_words.append(i)
# print(new_words)

#114----------------------------------------------------------------------------------

# nums = []

# while True:
#     num = input("Enter a number(Enter to exit): ")
#     if num == "":
#         break
#     else:
#         nums.append(int(num))
# nums.sort()
# for i in nums:
#     print(i)

#115----------------------------------------------------------------------------------

# div = []

# while True:
#     num = input("Enter a number(Enter to exit): ")
#     if num == "":
#         break
#     else:
#         num = int(num)
#         for i in range(1,int(num/2)+1):
#             if num % i == 0:
#                 div.append(i)
#         print(f"List of proper divisors of {num} is: {div}")
#         div = []

#116----------------------------------------------------------------------------------

# perf_nums = []

# for i in range(1,10000):
#     summ = 0
#     for j in range(1, i):
#         if i % j == 0:
#             summ += j
#     if(summ == i):
#         perf_nums.append(i)
# print(f"The perfect numbers from 1 to 10000 are: {perf_nums}")

#119----------------------------------------------------------------------------------

# avr = []
# lower = []
# higher = []
# summ = 0
# while num != "":
#     num = input("Enter a number(Enter to exit): ")
#     if num == "":
#         break
#     else:
#         avr.append(int(num))

# for i in avr:
#     summ += i
#     avr_num = summ / len(avr)

# print(f"The average is: {avr_num}")

# for i in avr:
#     if i < avr_num:
#         lower.append(i)
#     else:
#         higher.append(i)

# print(f"The values below the average are : {lower}")
# print(f"The values above the average are: {higher}")

#121----------------------------------------------------------------------------------

# import random
# lottery = []
# lottery_nodup = []

# while len(lottery) != 12:
#     lottery.append(random.randint(1,49))

# for i in lottery:
#     if i not in lottery_nodup:
#         lottery_nodup.append(i)
#     if len(lottery_nodup) == 6:
#         break
# print(lottery_nodup)

#122----------------------------------------------------------------------------------

# word = input("Enter a word: ")
# vow = ["a","e","i","o","u"]
# letter = []
# if word[0] in vow:
#     print(word + "way")
# else:
#     word.split()
#     con = []
#     for i in word:
#         letter.append(i)
#     for i in letter:
#         if i not in vow:
#             con.append(i)
#         elif i in vow:
#             letter.index(i)
#             break
#     print("".join(letter[letter.index(i):] + con )+"ay")

#124----------------------------------------------------------------------------------

# x = []
# y = []
# xy = []

# sum_x = 0
# sum_y = 0
# sum_xy = 0
# sum_x2 = 0

# while True:
#     x1 = input("Enter x: ")

#     if x1 == "":
#         break
#     else:
#         y1 = float(input("Enter y: "))
#         x.append(float(x1))
#         y.append(y1)

# for i in x:
#     sum_x += i

# for i in y:
#     sum_y += i

# for i in xy:
#     sum_xy += i

# for i in x:
#     sum_x2 += (i**2)

# m = (sum_xy - ((sum_x*sum_y)/len(x)))/(sum_x**2 - ((sum_x)**2)/len(x))
# b = (sum_y/len(y)) - m*(sum_x/len(x))

# print(f"y = {m}x + {b}")

#127----------------------------------------------------------------------------------

# listt = []
# while True:
#     item = input("Enter value: ")
#     if item == "":
#         break
#     else:
#         listt.append(item)
# copy = listt.copy()
# copy.sort()
# print(copy)
# if listt == copy:
#     print("True")
# else:
#     print("False")

#128----------------------------------------------------------------------------------

# numbers = []
# minimal = int(input("Enter the minimum number: "))
# maximum = int(input("Enter the maximum number: "))
# # count = 0
# while True:
#     item = input("Enter value: ")
#     if item == "":
#         break
#     else:
#         numbers.append(float(item))

# print(f"There are {numbers.count(minimal)} minimal numbers and {numbers.count(maximum)} maximum")

    
# # for i in numbers:
# #     if minimal <= i < maximum:
# #         count += 1
# # print(f"There are {count} elements between {minimal} and {maximum}")

