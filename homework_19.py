#1------------------------------------------

# def summa_n(num:int) -> int:
#     summ = 0
#     for i in range(num+1):
#         summ += i
#     return summ
# def main() -> None:
#     num = int(input("Enter a number: "))
#     print(f"sum of numbers up to {num} = {summa_n(num)}")
# if __name__ == "__main__":
#     main()

#2------------------------------------------

# def positive_or_negative(num:int) -> int:
#     if num > 0:
#         return "Положительное"
#     else:
#         return "Отрицательное"
# def main() -> None:
#     num = int(input("Enter a number: "))
#     print(positive_or_negative(num))
# if __name__ == "__main__":
#     main()

#3------------------------------------------

# num1 = []

# def summ():
#     summm = 0
#     for i in num1:
#         summm += i
#     return summm

# def minus():
#     summm = 0
#     for i in num1:
#         summm -=i
#     return summm

# def mult():
#     summm = 0
#     for i in num1:
#         summm *= i
#     return summm

# def div():
#     summm = 0
#     for i in num1:
#         summm /= i
#     return summm

# def maxx():
#     num1.sort()
#     return num1[-1]

# def main() -> None:
#     action = input("What should it do ? ")

#     while True:
#         num = input("Enter a number(Enter to exit): ")
#         if num == "":
#             break
#         else:
#             num = float(num)
#             num1.append(num)

#     if action == "+":
#         print(summ())
#     elif action == "-":
#         print(minus())
#     elif action == "*":
#         print(mult())
#     elif action == "/":
#         print(div())
#     elif action == "max":
#         print(maxx())

# if __name__ == "__main__":
#     main()

#4------------------------------------------

# def rev(num:int) -> str:
#     return num[::-1]

# def main() -> None:
#     while True:
#         num = input("Введите число: ")
#         if num == "":
#             print("Программа завершена!")
#             break
#         else: 
#             print(f"Число наоборот: {rev(num)}")

# if __name__ == "__main__":
#     main()

#5------------------------------------------

# def count_letters(sentence:str) -> int:
#     number = input("Какую цифру ищем ? ")
#     letter = input("Какую букву ищем ? ")
#     sentence_list = [i for i in sentence]
#     count_number = sentence_list.count(number)
#     count_letter = sentence_list.count(letter)
#     return f"Количество цифр {number}: {count_number}\nКоличество букв {letter}: {count_letter}"

# def main() -> None:
#     sentence = input("Введите текст: ")
#     print(count_letters(sentence))

# if __name__ == "__main__":
#     main()

#6------------------------------------------

# def find_coin(x:int, y:int) -> str:
#     if (-1 <= x <= 1) and (-1 <= y <= 1):
#         return "Монетка где-то рядом"
#     else:
#         return "Монетки в области нет"

# def main() -> None:
#     x = int(input("Введите координату x: "))
#     y = int(input("Введите координату y: "))
#     print(find_coin(x,y))

# if __name__ == "__main__":
#     main()

#7------------------------------------------

# number= []

# def minimal(*args) -> int:
#     number.sort()
#     return number[0]

# def main():
#     while True:
#         num = input("Введите число: ")
#         if num == "":
#             print(minimal())
#             break
#         else:
#             number.append(int(num))

# if __name__ == "__main__":
#     main()

#8------------------------------------------

# def gcd(a:int, b:int) -> int:
#     while b:
#         a, b = b, a % b
#     return a

# def main() -> None:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     print(gcd(a,b))

# if __name__ == "__main__":
#     main()

#9------------------------------------------

# import random

# def rock_paper_scissors():
#     print("----Rock, paper, scissors----")
#     user_choice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ")
#     computer_choice = random.choice(['r', 'p', 's'])
#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif user_choice == 'r' and computer_choice == 's':
#         print("You win!")
#     elif user_choice == 'p' and computer_choice == 'r':
#         print("You win!")
#     elif user_choice == 's' and computer_choice == 'p':
#         print("You win!")
#     else:
#         print("You lose!")

# def guess_the_number():
#     print("----Guess the number game----")
#     guess = 0
#     target_number = random.randint(1, 100)
#     while guess != target_number:
#         guess = int(input("Enter a number between 1 and 100: "))
#         if guess < target_number:
#             print("Too low")
#         elif guess > target_number:
#             print("Too high")
#     print(f"You win! The number was {target_number}")


# def main():
#     game = input("1.Rock, paper, scissors\n2.Guess the number game\nSelect game: ")
#     if game == "1":
#         rock_paper_scissors()
#     elif game == "2":
#         guess_the_number()
#     else:
#         print("There is no such game")

# if __name__ == "__main__":
#     main()
