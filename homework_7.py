#44---------------------------------------------------------------------------------
# money = int(input("Enter the dollar note money: "))

# if money == 1:
#     face = "George Washington" 
# elif money == 2:
#     face = "Thomas Jefferson"
# elif money == 5:
#     face = "Abraham Lincoln"
# elif money == 10:
#     face = "Alexander Hamilton"
# elif money == 20:
#     face = "Andrew Jackson"
# elif money == 50:
#     face = "Ulysses S. Grant"
# elif money == 100:
#     face = "Benjamin Franklin"

# print(f"The face on the ${money} bill is {face}")

#45---------------------------------------------------------------------------------

# month = input("Enter a month of the year: ").lower()
# day = int(input("Enter a day of the month: "))

# if month == "january" and day == 1:
#     print("It"s New Year"s Day")
# elif month == "july" and day == 1:
#     print("It"s Canada Day")
# elif month == "december" and day == 25:
#     print("Christmas")
# else:
#     print("Error:entered month and day do not correspond to a fixed-date holiday")

#46---------------------------------------------------------------------------------

# position = input("Enter position on the chessboard: ").lower().replace(" ", "")
# letter = position[0]
# number = int(position[1])
# if letter in ["a", "c", "e", "g"]:
#     black = True
# else:
#     black = False

# if black:
#     if number%2 == 0:
#         white = True
#     else:
#         white = False
# else:
#     if number%2 == 0:
#         white = False
#     else:
#         white = True
# if white:
#     print("White")
# else:
#     print("black")

#47---------------------------------------------------------------------------------

# month = input("Enter the name of a month: ").lower()
# day = int(input("Enter day: "))

# if month == "march" or month == "april" or month == "may" or month == "june":
#     if month == "march" and day >= 20:
#         print("The date falls in spring")
#     elif month == "april" or month == "may":
#         print("The date falls in spring")
#     elif month == "june" and day <=21:
#         print("The date falls in spring")

# if month == "june" or month == "july" or month == "august" or month == "septemper":
# 	if month  == "june" and day > 21:
# 		print("The date falls in summer")	
# 	elif month == "july" or month == "august":
# 		print("The date falls in spring")	
# 	elif month == "semptember" and day <= 22:
# 		print("The date falls in spring")

# if  month == "septemper" or month == "october" or month == "november" or month == "december":
# 	if month == "september" and day > 22:
# 		print("That date falls in fall")	
# 	elif month == "october" or month == "november":
# 		print("That date falls in fall")	
# 	elif month == "december" and day < 21:
# 		print("That date falls in fall")

# if month == "december" or month == "january" or month == "february" or month == "march":
# 	if month == "december" and day > 21:
# 		print("The date falls in winter")
		
# 	elif month == "january" or month == "february":
# 		print("The date falls in winter")
		
# 	elif month == "march" and day < 20:
# 		print("The date falls in winter")

# else:
#     print("Enter a valid month or day")

#48---------------------------------------------------------------------------------		

# month = (input("Enter your birth month: ")).lower()
# day = int(input("Enter the day you were born: "))

# if month == "december" and 22 <= day <= 31 or month == "january" and 1 <= day <= 19:
#     print("Your zodiac sign is Capricon")
# elif month ==  "january" and 20 <= day <= 31 or month == "february" and 1 <= day <= 18:
#     print('Your zodiac sign is Aquarius ')
# elif month == 'february' and  19 <= day <= 29 or month == 'march' and 1 <= day <= 20:
#     print('Your zodiac sign is Pisces')
# elif month == 'march' and  21 <= day <= 31 or month == 'april' and 1 <= day <= 19:
#     print('Your zodiac sign is Aries')
# elif month == 'april' and  20 <= day <= 30 or month == 'may' and 1 <= day <= 20:
#     print('Your zodiac sign is Taurus')
# elif month == 'may' and  21 <= day <= 31 or month == 'june' and 1 <= day <= 20:
#     print('Your zodiac sign is Gemini')
# elif month == 'june' and  21 <= day <= 30 or month == 'july' and  1 <= day <= 22 :
#     print('Your zodiac sign is Cancer')
# elif month == 'july' and  23 <= day <= 31 or month == 'august' and 1 <= day <= 22:
#     print('Your zodiac sign is Leo')
# elif month == 'august' and  23 <= day <= 31 or month == 'september' and 1 <= day <= 22:
#     print('Your zodiac sign is Virgo')
# elif month == 'september' and  23 <= day <= 30 or month == 'october' and 1 <= day <= 22:
#     print('Your zodiac sign is Libra')
# elif month == 'october' and  23 <= day <= 31 or month == 'november' and 1 <= day <= 21:
#     print('Your zodiac sign is Scorpio')
# elif month == 'november' and  22 <= day <= 30 or month == 'december' and 1 <= day <= 21:
#     print('Your zodiac sign is  Sagittarius')

#49---------------------------------------------------------------------------------

# year = int(input("Enter a year: "))

# if year%12 == 8:
#     print("Dragon")
# elif year%12 == 9:
#     print("Snake")
# elif year%12 == 10:
#     print("Horse")
# elif year%12 == 11:
#     print("Sheep")
# elif year%12 == 0:
#     print("Monkey")
# elif year%12 == 1:
#     print("Rooster")
# elif year%12 == 2:
#     print("Dog")
# elif year%12 == 3:
#     print("Pig")
# elif year%12 == 4:
#     print("Rat")
# elif year%12 == 5:
#     print("Ox")
# elif year%12 == 6:
#     print("Tigre")
# elif year%12 == 7:
#     print("Hare")

#50---------------------------------------------------------------------------------

# magnitude = float(input("Enter the magnitude: "))

# if magnitude < 2.0:
# 	print(f"The magnitude {magnitude} earthquake is considered to be Micro earthquake")
# elif magnitude >= 2.0 and magnitude < 3.0:
# 	print(f"The magnitude {magnitude} earthquake is considered to be Very Minor earthquake") 
# elif magnitude >= 3.0 and magnitude < 4.0:
# 	print(f"The magnitude {magnitude} earthquake is considered to be Minor earthquake") 
# elif magnitude >= 4.0 and magnitude < 5.0:
# 	print(f"The magnitude {magnitude} earthquake is considered to be Light earthquake") 
# elif magnitude >= 5.0 and magnitude < 6.0:
# 	print(f"The magnitude {magnitude} earthquake is considered to be Moderate earthquake")
# elif magnitude >= 6.0 and magnitude < 7.0:
# 	print(f"The magnitude {magnitude} earthquake is considered to be Strong earthquake") 
# elif magnitude >= 7.0 and magnitude < 8.0:
# 	print(f"The magnitude {magnitude} earthquake is considered to be Major earthquake") 
# elif magnitude >= 8.0 and magnitude < 10.0:
# 	print(f"The magnitude {magnitude} earthquake is considered to be Great earthquake") 
# else:
# 	print(f"The magnitude {magnitude} earthquake is considered to be Meteoric earthquake") 

#51---------------------------------------------------------------------------------

# a = float(input("Please enter a value for a: "))
# b = float(input("Please enter a value for b: "))
# c = float(input("Please enter a value for c: "))

# discriminant = (b**2) - (4*a*c)

# if discriminant == 0:
#     root = (-b) / (2*a)
# elif discriminant < 0:
#     print("The quadratic equation does not have any real roots")
# else:
#     root = (-b) + discriminant / (2*a)
#     root2 = (-b) - discriminant / (2*a)
#     print(f"The roots are {root} and {root2}")

#52---------------------------------------------------------------------------------

# grade = input("Enter letter grade: ").upper()

# points = -1

# if grade == "A+":
# 	points = 4.0
# elif grade == "A":
# 	points = 4.0
# elif grade == "A-":
# 	points = 3.7
# elif grade == "B+":
# 	points = 3.3
# elif grade == "B":
# 	points = 3.0
# elif grade == "B-":
# 	points = 2.7
# elif grade == "C+":
# 	points = 2.3
# elif grade == "C":
# 	points = 2.0
# elif grade == "C-":
# 	points = 1.7
# elif grade == "D+":
# 	points = 1.3
# elif grade == "D":
# 	points = 1.0
# elif grade == "F":
# 	points = 0
	
# else:
# 	print("Invalid grade entered")

# if points >= 0:
#     print(f"Your grade equivalent in number of grade points is {points}")

#54---------------------------------------------------------------------------------

# rating = float(input("Enter rating for the employee's performance: "))

# if rating == 0.0:
# 	perfomance = "unacceptable performance"
# elif rating == 0.4:
# 	perfomance = "acceptable performance"
# elif rating >= 0.6:
# 	perfomance = "meritorious performance"

# print(f"The employee performance is {perfomance} and raise is {rating*2400}")

#55---------------------------------------------------------------------------------

# length = int(input("Enter a value for a wavelength: "))

# if length >= 350 and length < 450:
# 	print("Violet")
# elif length >= 450 and length < 495:
# 	print("Blue")
# elif length >= 495 and length < 570:
# 	print("Green")
# elif length >= 570 and length < 590:
# 	print("Yellow")
# elif length >= 590 and length < 620:
# 	print("Orange")
# elif length >= 620 and length <= 750:
# 	print("Red")
	
# else:
# 	print("This wavelength is outside the spectrum of visible light")

#57---------------------------------------------------------------------------------

# calls = int(input("Enter the number of minutes: "))
# messages = int(input("Enter the number of text messages: "))

# additional_messages_charge = (messages - 50) * 0.15
# additional_calls_charge = (calls - 50) * 0.25

# total = (additional_calls_charge + additional_messages_charge + 0.44)
# tax = total * 0.05
# total = total + tax

# print(f"Base charge is 15$\n911 charge is $0.44\nTax is {round(tax,4)}")

# if additional_calls_charge > 0:
#     print(f"Additional minutes charge is {additional_calls_charge}$")
# elif additional_calls_charge <= 0:
#     print("There is no additional charge")
# if additional_messages_charge > 0:
#     print(f"Additional messages charge is {additional_messages_charge}$")
# elif additional_messages_charge <= 0:
#     print("There is no additional charge")

#58---------------------------------------------------------------------------------
    
# year =  int(input("Enter a year: "))

# if year % 400 == 0:
# 	print("That year is a leap year.")
# elif year % 100 == 0 and not year % 400 == 0:
# 	print("That year is not a leap year.")
# elif year % 4 == 0 and not year % 100 == 0 and not year % 400 == 0:
# 	print("That year is a leap year.")
# else:
#     print("That year is not a leap year.")

#60---------------------------------------------------------------------------------

# import math
# year = int(input("Enter a year: "))

# day_of_the_week = (year + math.floor((year - 1)/4) - math.floor((year - 1)/100) 
# + math.floor((year - 1)/400))%7.
# if day_of_the_week == 0:
#     day = "Sunday"
# elif day_of_the_week == 1:
#     day = "Monday"
# elif day_of_the_week == 2:
#     day = "Tuesday"
# elif day_of_the_week == 3:
#     day = "Wednesday"
# elif day_of_the_week == 4:
#     day = "Thursday"
# elif day_of_the_week == 5:
#     day = "Friday"
# elif day_of_the_week == 6:
#     day = "Saturday"


# print(f"The day of the week for January 1 is {day}")

#61---------------------------------------------------------------------------------

# licensePlate = input("Enter a license plate: ")

# if len(licensePlate) == 6:
#     print("This is an old style plate")
# elif len(licensePlate) == 7:
#     print("This is a new style plate")
# else:
#     print("Invalid license plate")

#62---------------------------------------------------------------------------------

# import random

# red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]

# spin = random.randint(0,37)
# if spin == 0:
#     spin = random.randint(0,1)
    
#     if spin == 0:
#         print("Pay 0")
#     else:
#         print("Pay 00")

# else:
#     print(f"The spin resulted in {spin}...")
#     print(f"Pay {spin}")

#     if spin in red:
#         print("Pay Red")
#     else:
#         print("Pay Black")

#     if spin % 2 == 0:
#         print("Pay Even")
#     else:
#         print("Pay Odd")

#     if 1 <= spin <= 18:
#         print("Pay 1 to 18")
#     else:
#         print("Pay 19 to 36")