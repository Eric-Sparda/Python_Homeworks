#1-----------------------------------------------------------------------------

# class YeartoCentury:
#     def __init__(self, year):
#         self.year = year
    
#     def calculate_century(self):
#         if self.year <= 0:
#             return "Not a valid year"
#         elif self.year <= 100:
#             return "1st century"
#         elif self.year % 100 == 0:
#             return f"{self.year//100}th century"
#         else:
#             return f"{self.year//100 + 1}th century"
        
# year = int(input("Enter the year: "))
# obj = YeartoCentury(year)
# print(obj.calculate_century())

#2-----------------------------------------------------------------------------

# class Palindrome:
#     def __init__(self, input_string):
#         self.input_string = input_string.lower()
    
#     def is_palindrome(self):
#         nochar = ""
#         for i in self.input_string:
#             if i.isalnum():
#                 nochar += i
#         return nochar == nochar[::-1]
    
# input_string = input("Enter a word: ")
# obj = Palindrome(input_string)
# print(obj.is_palindrome())

#3-----------------------------------------------------------------------------

# class Largest:
#     def __init__(self,numlist):
#         self.numlist = numlist

#     def maxx(self):
#         maximum = 0
#         for i in range(len(self.numlist) - 1):
#             product = int(self.numlist[i]) * int(self.numlist[i + 1])
#             if product > maximum:
#                 maximum = product
#         return f"Maximum product = {maximum}"
# numlist = input("Enter a list of numbers: ").split()
# obj = Largest(numlist)
# print(obj.maxx())

#Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# class Largest:
#     def __init__(self,numlist):
#         self.numlist = numlist

#     def maxx(self,maximum = 0):
#         if not self.numlist:
#             return maximum
#         num = int(self.numlist[0]) * int(self.numlist[1])
#         if num > maximum:
#             maximum == num
#         return self.maxx(self.numlist[1:],maximum)
            

# numlist = input("Enter a list of numbers: ").split()
# obj = Largest(numlist)
# print(obj.maxx())

#4-----------------------------------------------------------------------------

# class Longest:
#     def __init__(self,inputList):
#         self.inputList = inputList

#     def longest(self):
#         long = []
#         self.inputList.sort(key=len, reverse=True)
#         long.append(self.inputList[0])
#         for i in self.inputList:
#             if i == long[0]:
#                 long.append(i)
#         return f"{long}"

# inputList = input("Enter a list: ").split()
# obj = Longest(inputList)
# print(obj.longest())

#5-----------------------------------------------------------------------------

# class LuckyTicket:
#     def __init__(self, numbers):
#         self.numbers = numbers
    
#     def checkLuckyTicket(self):
#         stringNumbers = str(self.numbers)
#         firsthalf = sum(int(i) for i in stringNumbers[:len(stringNumbers) // 2])
#         secondhlaf = sum(int(i) for i in stringNumbers[len(stringNumbers) // 2:])
#         if firsthalf == secondhlaf:
#             return True
#         else:
#             return False

# number = input("Enter your ticket: ")
# obj = LuckyTicket(number)
# print(obj.checkLuckyTicket())

#6-----------------------------------------------------------------------------

# class ListSort:
#     def __init__(self, height):
#         self.height = height

#     def height_list(self):
#         (self.height).sort()
#         return f"{self.height}"

# height = input("Enter a list: ").split()
# height = [int(i) for i in height]
# obj = ListSort(height)
# print(obj.height_list())

#7-----------------------------------------------------------------------------

# class Weight:
#     def __init__(self, weightlist):
#         self.weightlist = weightlist
    
#     def summary(self):
#         team1 = sum([i for i in weightlist[::2]])
#         team2 = sum([i for i in weightlist[1::2]])
#         return f"{team1,team2}"

# weightlist = input("Enter a list: ").split()
# weightlist = [int(i) for i in weightlist]
# obj = Weight(weightlist)
# print(obj.summary())
