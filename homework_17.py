#137----------------------------------------------------

# import random 
# from collections import Counter

# dice = {}
# for i in range(50):
#     x = random.randint(1,1000)
#     dice[x] = x

# count_d = Counter(dice.values())

# print("Total:")
# for key, value in count_d.items():
#     print(f"\n{key}: {value} ({(value/50) * 100}%)",end = "")

#139----------------------------------------------------

# sentence = input("Enter a message: ")
#morse_code = { 
#    "A":".-", "B":"-...", 
#    "C":"-.-.", "D":"-..", "E":".", 
#    "F":"..-.", "G":"--.", "H":"....", 
#    "I":"..", "J":".---", "K":"-.-", 
#    "L":".-..", "M":"--", "N":"-.", 
#    "O":"---", "P":".--.", "Q":"--.-", 
#    "R":".-.", "S":"...", "T":"-", 
#    "U":"..-", "V":"...-", "W":".--", 
#    "X":"-..-", "Y":"-.--", "Z":"--..", 
#    "1":".----", "2":"..---", "3":"...--", 
#    "4":"....-", "5":".....", "6":"-....", 
#    "7":"--...", "8":"---..", "9":"----.", 
#    "0":"-----"
#}
# ciphered = ""
# for i in sentence:
#     if i != " ":
#         if i.upper() in morse_code:
#             ciphered += morse_code[i.upper()] + " "
#     else:
#         ciphered += " <New Word> "

# print(ciphered)

#140----------------------------------------------------

# postal_code = input("Enter your postal code: ").upper()

# province_codes = {

#     "Newfoundland": "A",
#     "Nova Scotia": "B",
#     "Prince Edward Island": "C",
#     "New Brunswick": "E",
#     "Quebec": ["G", "H", "J"],
#     "Ontario": ["K", "L", "M", "N", "P"],
#     "Manitoba": "R",
#     "Saskatchewan": "S",
#     "Alberta": "T",
#     "British Columbia": "V",
#     "Nunavut": "X",
#     "Northwest Territories": "X",
#     "Yukon": "Y"
# }

# for key,val in province_codes.items():
#     if postal_code[0] == val:
#         print(key)
#     else:
#         print("We don't know where you are located")

#141----------------------------------------------------


# number = int(input("Enter salary: "))

# number_words = {
#     1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
#     6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
#     11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
#     15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 
#     19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 
#     50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 
#     90: "ninety", 100: "hundred"
# }

# if number < 20:
#     print(number_words[number])
# elif number < 100:
#     tens = number // 10 * 10
#     units = number % 10
#     if units == 0:
#         print(number_words[tens])
#     else:
#         print(number_words[tens] + ' ' + number_words[units])
# else:
#     hundreds = number // 100
#     number = number % 100
#     tens = number // 10 * 10
#     units = number % 10
#     if number > 0:
#         if units == 0:
#             print(number_words[hundreds] + ' hundred and ' + number_words[tens])
#         else:
#             print(number_words[hundreds] + ' hundred and ' + number_words[tens] + ' ' + number_words[units])
#     else:
#         print(number_words[hundreds] + ' hundred')

#142----------------------------------------------------

# word = input("Enter a word: ")

# uniq = []
# for i in list(word):
#     if i not in uniq:
#         uniq.append(i)

# print(f"Number of unique characters: {len(uniq)}")

#143----------------------------------------------------

# word = input("Enter the first word: ").lower()
# word2 = input("Enter the second word: ").lower()
# list1 = list(word).sort()
# list2 = list(word2).sort()

# if list1 == list2:
#     print("The words are anagrams")
# else:
#     print("The words are not anagrams")

#144----------------------------------------------------

# sen = input("Enter the first sentence: ").lower()
# sen2 = input("Enter the second sentence: ").lower()
# list1 = sorted([i for i in sen if i != " "])
# list2 = sorted([i for i in sen2 if i != " "])

# if list1 == list2:
#     print("The sentences are anagrams")
# else:
#     print("The sentences are not anagrams")



