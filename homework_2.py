#1--------------------------------------------------------------------

#name = "Eric Yeghiazaryan"
#mail = "roy.sec@bk.ru"
#print(f"{name}\n{mail}")

#2--------------------------------------------------------------------

#name = input("Enter your name: ")
#print(f"Hello {name}" )

#3--------------------------------------------------------------------

#width = int(input("Enter rooms width: "))
#length = int(input("Enter rooms length: "))
#print(f"Room area = {length * width}")

#4--------------------------------------------------------------------

#length = int(input("Enter length: "))
#width = int(input("Enter  width: "))
#print(f"Area of the field = {(length*width)/43.560}")

#5--------------------------------------------------------------------

#bottle1 = int(input("Enter how many bottles of 1 liter or less: "))
#bottle2 = int(input("Enter how many bottles of over 1 liter: "))
#SUM = bottle1*0.10 + bottle2*0.25
#print("Sum = ", round(SUM, 2)"$")

#6--------------------------------------------------------------------

#order= float(input("Enter order price: "))
#tax = order * 20 / 100
#tip = order * 18 / 100
#total = order + tax + tip
#print(f"
#Tax = {round(tax, 2)} Tip = {round(tip, 2)} Total = {round(total, 2)}"
#) 

#7--------------------------------------------------------------------

#num = int(input("Enter a number: "))
#print(f"Sum = {(num * (num + 1)) / 2}")

#8--------------------------------------------------------------------

#widgets = int(input("Enter the widgets number: "))
#gizmos = int(input("Enter the gizmos number: "))
#print(f"Total weight = {widgets*75+gizmos*112} gram")

#9--------------------------------------------------------------------

#card_ballance = float(input("Enter your ballance: "))
#card_ballance += card_ballance * (4 / 100)
#print(f"Card ballance for the first year = ",round(card_ballance,3))
#card_ballance += card_ballance * (4 / 100)
#print(f"Card ballance for the second year = ",round(card_ballance,3))
#card_ballance += card_ballance * (4 / 100)
#print(f"Card ballance for the third year = ",round(card_ballance, 3))

#10--------------------------------------------------------------------

#import math
#a = float(input("Enter the first number : "))
#b = float(input("Enter number b: "))
#print(f"sum a and b = {a+b}")
#print(f"The difference between a and b = {a-b}")
#print(f"The product of a and b = {a*b}")
#print(f"The quotient of a divided by b = {a // b}", )
#print(f"The remainder after dividing a by b = {math.fmod(a, b)}")
#print(f"The remainder after dividing a by b = {a % b}", )
#print(f"The decimal logarithm of a = {math.log10(a)}", )
#print(f"The result of raising the number a to the power b = {math.pow(a,b)}")

#11--------------------------------------------------------------------

#mpg = float(input("Enter the mpg: "))
#print(f"L/100 = ", round((235.21/mpg), 2), "MPG")

#12--------------------------------------------------------------------

#import math
#t1 = float(input("Enter latitude1: "))
#g1 = float(input("Enter longitude1: "))
#t2 = float(input("Enter latitude12: "))
#g2 = float(input("Enter longitude2: "))
#rt1 = math.radians(t1)
#rg1 = math.radians(g1)
#rt2 = math.radians(t2)
#rg2 = math.radians(g2)
#distance = 6371.01*math.acos(math.sin(rt1) * math.sin(rt2) + math.cos(rt1) * math.cos(rt2) * math.cos(rg1 - rg2))
#$print(f"Distance = ", round(distance, 2))

#13--------------------------------------------------------------------

#cents = int(input("Please enter a number of cents: "))
#loonie = cents / 100
#toonies = cents / 200
#print(f"The change using the smallest amount of change is {toonies} toonies, {loonie} loonies")

#14--------------------------------------------------------------------

#ft = float(input("Enter foot : ))
#inches = float(input("Enter inches"))
#print(f"Your Height= ", round(ft * 30.48 + inches * 2.54))

#15--------------------------------------------------------------------

#distance = float(input("Enter the distance in foots : "))
#print(f"Inches = {distance * 12}, Yards = {distance * 3}, Miles = {distance * 0.000189}")

#16--------------------------------------------------------------------

#import math
#r = float(input("Please enter the radius r: "))
#area = math.pi*(r*r)
#vol = (4/3)*math.pi*(r*r*r)
#print(f"Area = ",round(area, 3), "Volume = ", round(vol, 3))

#17--------------------------------------------------------------------

#mass = float(input("Please enter the mass of some water in grams: "))
#tempChange = float(input("Please enter the temperature changein degrees in Celsius: "))  
#joules = mass*4.186*tempChange
#print(f"Total amount of energy used in Joules is {joules}")
#watt = joules*2.7778e-7
#cost = 8.9*watt
#print(f"The cost for all this = {cost}")

#18--------------------------------------------------------------------

#import math
#radius = float(input("Please enter the radius: "))
#height = float(input("Please enter the height: "))
#volume = math.pi * (radius*radius) * height
#print(f"The volume of this cylinder = ", round(volume,3))

#19--------------------------------------------------------------------

#import math
#height = float(input("Please enter the height from which an object is dropped in meters: "))
#vf = math.sqrt(2*9.8*height)
#print(f"The velocity when the object hits the ground = ", round(vf,3))

#20--------------------------------------------------------------------

#p = int(input("Please enter a pressure in Pascals: "))
#v = int(input("Please enter a volume in liters: "))
#t = int(input("Please enter a temperature in Kelvin: "))
#n = (p*v)/(8.314*t)
#print("The amount of gas in moles for a SCUBA tank = ", round(n,4))

#21--------------------------------------------------------------------





