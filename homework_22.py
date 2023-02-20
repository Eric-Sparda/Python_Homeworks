#152-------------------------------------------------------

# count = 0
# name = input("Enter the name of the file: ")
# end_file = input("Enter the name of the output file: ")
# with open(name, "a") as f_in:
#     while True:
#         string = input("Enter a word: ")
#         if string == "":
#             break
#         else:
#             f_in.write(f"{string}\n")

# with open(name, "r") as f_in:
#     res = f_in.readlines()

# with open(end_file, "a") as f_out:
#     for i in res:
#         count += 1
#         f_out.write(f"{count} - {i}")

#154-------------------------------------------------------

# maxx = 0
# letters = []
# with open("text.txt", "w") as file:
#     while True:
#         word = input("Enter a word: ")
#         if word == "":
#             break
#         else:
#             file.write(word)
# with open("text.txt", "r") as file:
#     res = file.readline()
#     for i in res:
#         letters.append(i)
    
# for i in letters:
#     num = letters.count(i)
#     if num > maxx:
#         maxx = num
#         letter = i

# print(f"Letter - {letter}, Frequency - {maxx}")

#155-------------------------------------------------------

# maxx = 0

# with open("text.txt", "w") as file:
#     while True:
#         word = input("Enter a word: ")
#         if word == "":
#             break
#         else:
#             file.write(f"{word} ")
# with open("text.txt", "r") as file:
#     content = file.read()
#     words = content.split()

# for i in words:
#     num = words.count(i)
#     if num > maxx:
#         maxx = num
#         letter = i

# print(f"Word - {letter}, Frequency - {maxx}")

#156-------------------------------------------------------

# summ = 0

# with open("text.txt", "w") as file:
#     while True:
#         word = input("Enter: ")
#         if word == "":
#             break
#         else:
#             file.write(f"{word} ")
# with open("text.txt", "r") as file:
#     content = file.read()
#     digits = content.split()

# for i in digits:
#     if i.isdigit():
#         summ += int(i)

# print(summ)

#160-------------------------------------------------------

# i_before = []
# e_before = []
# with open("text.txt", 'r') as f:
#     for i in f:
#         words = i.split()
#         for j in words:
#             if 'ei' in j or 'ie' in j:
#                     if 'cei' in j:
#                         i_before.append(j)
#                     elif 'cie' in j:
#                         e_before.append(j)
#                     elif 'ei' in j:
#                         i_before.append(j)
#                     elif 'ie' in j:
#                         e_before.append(j)

# print(f"Words that follow the 'I before E except after C' rule: {i_before}")
# print(f"Words that violate the 'I before E except after C' rule: {e_before}")

#The ceiling in the chief's office was a relief to see after the fierce storm. 
#He had a receipt for the repairs, but it was weird how the price had increased. 
#She tried to believe that the thief had left her things alone, but she couldn't be sure. 
#The friends decided to hike through the field, and saw a piece of pie lying on the ground. 
# They both wanted to try it, but decided to leave it there for fear of getting sick.

#162-------------------------------------------------------

# letters = []
# letters_nodub = []
# with open("text.txt", "r") as file:
#     res = file.readline()
#     for i in res:
#         letters.append(i)
# for i in letters:
#     if i not in letters_nodub:
#         letters_nodub.append(i)
#     if i == " ":
#         letters_nodub.remove(i)
#     elif i == ",":
#         letters_nodub.remove(i)
#     elif i == "!":
#         letters_nodub.remove(i)
#     elif i == "?":
#         letters_nodub.remove(i)
#     elif i == ".":
#         letters_nodub.remove(i)
#     elif i == "'":
#         letters_nodub.remove(i)
# for i in letters_nodub:
#     print(f"Letter - {i}, count - {letters.count(i)}")

