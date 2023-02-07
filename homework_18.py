#85-----------------------------------------------------------------

# def right_triangle(a:float, b:float) -> float:
#     c = (a**2 + b**2)**0.5
#     if a <= 0 or b <= 0:
#         print("Both catheti should be positive.")
#     else:       
#         return c

# def main():
#     a = float(input("Enter the first cathetus of the triangle: "))
#     b = float(input("Enter the second cathetus of the triangle: "))
#     print(f"Hypotenuse = {right_triangle(a,b)}")

# if __name__ == '__main__':
#     main()

#86-----------------------------------------------------------------

# def taxi():
#     fares = int(input("Enter the base fare: "))
#     distance = float(input("Enter the distance traveled in kilometers: "))
#     fare = fares + ((distance * 1000) / 140) * 0.25
#     return fare


# def main():
#     print(f"The total fare is {taxi()}$")

# if __name__ == '__main__':
#     main()

#87-----------------------------------------------------------------

# def shipping():
#     items = int(input("Enter the number of items: "))
#     first_item_charge = 10.95
#     additional_item_charge = 2.95
#     return first_item_charge + (items - 1) * additional_item_charge

# def main():
#     print(f"The shipping charge is {shipping()}$")

# if __name__ == "__main__":
#     main()

#88-----------------------------------------------------------------

# def median():
#     median = []
#     for i in range(3):
#         num = int(input(f"Enter the {i+1} number: "))
#         median.append(num)
#         median.sort()
#     return median[1]

# def main():
#     print(median())

# if __name__ == "__main__":
#     main()

#89-----------------------------------------------------------------

# def ordinal():
#     ordinal_numbers = {
#         1:"First",
#         2: "Second",
#         3: "Third",
#         4: "Fourth",
#         5: "Fifth",
#         6: "Sixth",
#         7: "Seventh",   
#         8: "Eighth",
#         9: "Ninth",
#         10: "Tenth",
#         11: "Eleventh",
#         12: "Twelfth"}

#     num = int(input("Enter a number from 1 to 12: "))

#     if num in ordinal_numbers:
#         return ordinal_numbers[num]
#     else:
#         return "The number is outside of the range 1 to 12."

# def main():
#     print(ordinal())

# if __name__ == "__main__":
#     main()

#90-----------------------------------------------------------------

# def song():
#     ordinal_numbers = {
#         1:"first",
#         2: "second",
#         3: "third",
#         4: "fourth",
#         5: "fifth",
#         6: "sixth",
#         7: "seventh",   
#         8: "eighth",
#         9: "ninth",
#         10: "tenth",
#         11: "eleventh",
#         12: "twelfth"}
#     gifts = {
#         1:"A partridge in a pear tree.",
#         2:"Two turtle doves",
#         3:"Three French hens",
#         4:"Four calling birds",
#         5:"Five gold rings",
#         6:"Six geese a-laying",
#         7:"Seven swans a-swimming",
#         8:"Eight maids a-milking",
#         9:"Nine ladies dancing",
#         10:"Ten lords a-leaping",
#         11:"Eleven pipers piping",
#         12:"Twelve drummers drumming"
#     }
#     for i in range(12):
#         lyr = f"On the {ordinal_numbers[i+1]} day of Christmas\nmy true love sent to me\n"
#         for j in range(i+1,0,-1):
#             lyr += gifts[j] + "\n"
#         print(lyr)


# def main():
#     song()

# if __name__ == "__main__":
#     main()

#91-----------------------------------------------------------------


# def date():
#     days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     day = int(input("Enter the day as a number: "))
#     month = int(input("Enter the month as a number: "))
#     year = int(input("Enter the year: "))
#     if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
#         days_in_month[1] = 29
#     for i in range(1, month):
#         day += days_in_month[i]
#     return day

# if __name__ == "__main__":
#         print(f"The day within the year is: {date()}")

#94-----------------------------------------------------------------

# def triangle():
#     a = int(input("Enter the first side of the triangle: "))
#     b = int(input("Enter the second side of the triangle: "))
#     c = int(input("Enter the third side of the triangle: "))
#     if a <= 0  or b <= 0 or c <= 0:
#         return False
#     if a + b > c:
#         return False
#     else:
#         return True 

# if __name__ == "__main__":
#         print(f"{triangle()}")

#95-----------------------------------------------------------------**************************

# def text():
#     result = ""
#     message = input("Write a message: ")
#     message = message.capitalize()
#     for i in range(len(message)):
#         if message[i] == "i" and message[i+1] == " ":
#             result += "I"
#         elif message[i] == ".":
#             result += message[i]
#             result += message[i+1].upper()
#         elif message[i-1] !=".":
#             result += message[i]
#     return result   
# print(text())

#96-----------------------------------------------------------------*******************************

# def isInteger():
#     num = input("Enter a number: ")
#     if num[0] == "+" or num[0] == "-" and num[1].isdigit():
#         print("The string represents an integer")
#     elif len(num) == 1 and num[0].isdigit():
#         print("The string represents an integer")
#     else:
#         print("The string does not represent an integer")

# def main():
#     isInteger()

# if __name__ == "__main__":
#     main()


#97-----------------------------------------------------------------

# def precedence():
#     operator = input("Enter an operator: ")
#     if operator == "+" or operator == "-":
#         print("1")
#     elif operator == "*" or  operator == "/":
#         print("2")
#     elif operator == "^":
#         print("3")
#     else:
#         print("-1")
    
# def main():
#     precedence()

# if __name__ == "__main__":
#     main()

#98-----------------------------------------------------------------

# def prime():
#     num = int(input("Enter a number: "))
#     if num == 2 or num == 3:
#         return True
#     for i in range(2,(num//2)+1):
#         if num % i == 0:
#             return False
#             break
#         else:
#             return True
    
# def main():
#     print(prime())

# if __name__ == "__main__":
#     main()

#99-----------------------------------------------------------------

# def nextprime():
#     num = int(input("Enter a number: "))
#     while True:
#         for i in range(2,(num//2)+1):
#             if num % i != 0:
#                 return(f"The next prime number is {num}") 
#             else:
#                 num += 1

# def main():
#     print(nextprime())

# if __name__ == "__main__":
#     main()

#100-----------------------------------------------------------------

# import random

# def generate_password():
#     ascii_codes = [chr(i) for i in range(33, 127)]
#     password = ''.join(random.choice(ascii_codes) for i in range(random.randint(7, 10)))
#     return password

# if __name__ == "__main__":
#     print(f"Random password: {generate_password()}")

#101-----------------------------------------------------------------

# import random

# def plate():
#     letter = [chr(i) for i in range(97, 122)]
#     plate = "".join(str(random.randint(1,9)) for i in range(4))
#     plate_letters = "".join(random.choice(letter)for i in range(3))
#     return plate + plate_letters

# if __name__ == "__main__":
#     print(f"Random license plate: {plate()}")

#102-----------------------------------------------------------------

# def password_check():
#     password = input("Enter your password: ")
#     if len(password) >=8:
#         for i in password:
#             if i.isdigit():
#                 has_num = True
#             elif i.isupper():
#                 has_upper = True
#             elif i.islower():
#                 has_lower = True
#         if has_num and has_lower and has_upper:
#             return True
#     else:
#         return False
    

# if __name__ == "__main__":
#     print(password_check())

# #-----------------------------------------------

# def password_check():
#     password = input("Enter your password: ")
#     letter = 0
#     cap = 0
#     digit = 0
#     for i in password:
#         if "A" <= i <= "Z":
#             cap += 1
#         elif "a" <= i <= "z":
#             letter += 1
#         elif i.isdigit():
#             digit += 1
#     if len(password) >= 8 and letter >= 1 and cap >= 1 and digit >=1 :
#         return True
#     else:
#         return False

# if __name__ == "__main__":
#     print(password_check())

#103-----------------------------------------------------------------*****************************

# import random

# def generate_password():
#     ascii_codes = []
#     for i in range(random.randint(3,5)):
#             ascii_codes.append(chr(random.randint(65,90)))
#             ascii_codes.append(chr(random.randint(97,122)))
#             ascii_codes.append(str(random.randint(1,9)))
#     password = ''.join(ascii_codes)
#     return password 

# if __name__ == "__main__":
#     print(f"Random password: {generate_password()} len {len(generate_password())}")

#105-----------------------------------------------------------------

# def days():
#     year = int(input("Enter a year: "))
#     month = int(input("Enter a month as a number: "))
#     if month not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
#         return "Error: Invalid month."
#     if month in [4, 6, 9, 11]:
#         return 30
#     if month == 2:
#         if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#             return 29
#         else:
#             return 28
#     return 31

# def main():
#     print(f"Days in the month: {days()}")

# if __name__ == "__main__":
#     main()

#106-----------------------------------------------------------------

# def lowest():
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     if numerator > denominator:
#         greater = numerator
#     else:
#         greater = denominator

#     while True:
#         if((greater % numerator == 0) and (greater % denominator == 0)):
#             lcm = greater
#             break
#         else:
#             greater += 1
         
#     gcm = (numerator * denominator)/ lcm
#     numerator /= gcm
#     denominator /= gcm

#     return f"{int(numerator)} / {int(denominator)}"

# print(lowest())

#109-----------------------------------------------------------------

# def magic_date():
#     day = int(input("Enter day: "))
#     month = int(input("Enter month: "))
#     year = int(input("Enter a year: "))
#     if month * day == year % 100:
#         return "Date is a magic date"
#     else:
#         return "Date is not a magic date"

# def main():
#     print(magic_date())

# if __name__ == "__main__":
#     main()