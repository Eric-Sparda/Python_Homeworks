#35---------------------------------------------------------------------------------

#number =int(input("Enter a number: "))
#if number % 2 == 0:
#    print("Number is even")
#else:
#    print("Number is odd")

#36---------------------------------------------------------------------------------

#age = float(input("How old is your dog ? "))

#if (age > 2):
#    print(f"Your dog is {10.5 + (age*4)} years old")
#elif (0 < age <= 2):
#    print("Your dogs age is in 10.5 years")
#else:
#    print("Wrong input")

#37---------------------------------------------------------------------------------

#letter = input("Enter a letter: ").lower()
#if letter in ("a", "e","i","o","u"):
#    print("This letter is a vowel")
#elif letter == "y":
#    print("This letter can be either a vowel or a consonant")
#else:
#    print("Consonant is entered")

#39---------------------------------------------------------------------------------

#month = input("Enter the current month: ").lower()

#if month in ("september","april","june","november"):
#    print("You have 30 days in", month)
#elif month in ("january","march","may","july","august","october","december"):
#    print("You have 31 days in", month)
#elif month == "february":
#    print("You have 28 or 29 days in", month)

#42---------------------------------------------------------------------------------

# note_name = input("Enter a note: ").lower().replace(" ", "")

# note = note_name[0]
# octave = int(note_name[1])

# C4 = 261.63
# d4 = 293.66
# e4 = 329.63
# f4 = 349.23
# g4 = 392.00
# a4 = 440.00
# b4 = 493.88

# if note  == "C":
#    hertz = C4
# elif note == "D":
#    hertz = d4
# elif note == "E":
#    hertz = e4
# elif note == "F":
#    hertz = f4
# elif note == "G":
#    hertz = g4
# elif note == "A":
#    hertz = a4
# elif note == "B":
#    hertz = b4
# else:
#    print("Enter a valid musical note")

# hertz =  float(hertz) / 2  ** (4 - octave)
# print(f"The {note_name} note is the {hertz} hertz")


#43---------------------------------------------------------------------------------
# import math

# notes = ["A","B","C","D","E","F","G"]
# hertz = float(input("Please enter a hertz in Hertz: "))
# note = ""
# #if hertz <= 500 use the formula that allows us to get 16.35, 18.35, 20.60, etc.
# octave = math.floor((12*math.log2(hertz/440) + 49)/10)

# if octave == -1:
#     octave = 0
# if hertz == 16.35:
#     note = notes[2]
# elif hertz == 18.35:
#     note = notes[3]
# elif hertz == 20.60:
#     note = notes[-3]  
# elif hertz == 21.83:
#     note = notes[-2]
# elif hertz == 24.50:
#     note = notes[-1]
# elif hertz == 27.50:
#     note = notes[0]
# elif hertz == 30.87:
#     note = notes[1]

# print(f"The note is {note} {octave}")


