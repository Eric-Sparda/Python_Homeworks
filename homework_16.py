#----------------------------------------------------[Lesson16][Dictionary]----------------------------------------------------
# 3------------------------------------------------------

# key = input("Enter a key: ")
# dic = {
#     "name": "Headset",
#     "price": 15,
#     "ship": "Everywhere"
# }
# for i in dic:
#     if i == key:
#         print("True")
#         break
# else:
#     print("False")

# 5------------------------------------------------------

# summ = 1
# dic = {
#     "a": 1,
#     "b": 2,
#     "c": 12
# }
# for i in dic.values():
#     summ *= i
# print(summ)

# 6------------------------------------------------------
# dic = {
#     "d": 56,
#     "e": 12,
#     "f": 69,
#     "c": 45,
#     "b": 23,
#     "a": 67
# }
# for i in list(sorted(dic, key = dic.get, reverse=True))[:3]:
#     print(i,dic[i])

#----------------------------------------------------[Lesson18][Exercises]----------------------------------------------------
# 1------------------------------------------------------

# uni = {
#     }
# for i in range(10):
#     uni[input("Enter a student name: ")] = int(input("Enter student's rating: "))
# print(uni)

# 2------------------------------------------------------

# summ = 0
# uni = {
#     }
# while True:
#     name = input("Enter a student name: ")
#     if name == "":
#         break
#     else:
#         rate = int(input("Enter a rate: "))
#         uni[name] = rate
# for i in uni.values():
#     summ += i
# print(f"Arithmetic average of students = {summ/len(list(uni))}")

# 3,4,5------------------------------------------------------

# uni = {}
# bad = {}
# good = {}
# while True:
#     name = input("Enter a student name: ")
#     if name == "":
#         break
#     else:
#         rate = int(input("Enter a rate: "))
#         uni[name] = rate
# for i in uni:
#     if uni[i] < 5:
#         bad[i] = uni[i]
#     else:
#         good[i] = uni[i]
# print(f"Good students: {good}\nBad students: {bad}")

#7,8------------------------------------------------------

# s = "a,2,b,5,c,8,a,4,e,11"
# s_list = s.split(",")
# dic = {}

# for i in range(0, len(s_list), 2):
#     key = s_list[i]
#     value = int(s_list[i + 1])
#     if key in dic:
#         dic[key].append(value)
#     else:
#         dic[key] = [value]
# dic["a"] = sum(dic["a"])
# print(dic)

#10------------------------------------------------------

# questions = {
#     1: {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
#     2: {"question": "What is the largest ocean in the world?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "answer": "Pacific Ocean"},
#     3: {"question": "What is the currency of Japan?", "options": ["Yen", "Dollar", "Euro", "Pound"], "answer": "Yen"},
#     4: {"question": "What is the tallest mammal in the world?", "options": ["Giraffe", "Elephant", "Hippopotamus", "Rhinoceros"], "answer": "Giraffe"},
#     5: {"question": "What is the longest river in the world?", "options": ["Nile", "Amazon", "Yangtze", "Yellow"], "answer": "Nile"}
# }

# money = [0, 100, 500, 10000, 20000, 1000000]

# print("Welcome to Who Wants to be a Millionaire!")
# print("Answer 5 questions correctly to win $1 million!")

# for i in range(5):
#     current_question = questions[i+1]
#     print(current_question["question"])
#     for j, option in zip(range(1,5),current_question["options"]):
#         print(f"{j}. {option}")
#     answer = input("Enter your answer: ")
#     if answer == current_question["answer"]:
#         print(f"Correct! You won ${money[i+1]}")
#     else:
#         print(f"Incorrect! You won ${money[i - 1]}")
#         break

# print("Thank you for playing Who Wants to be a Millionaire!")


