#173-------------------------------------------

# def total():
#     number = input("Enter a number: ")
#     if number == "":
#         return 0
#     else:
#         return float(number) + total()

# def main():
#     print(f"Sum = {total()}")

# if __name__ == "__main__":
#   main()

#174-------------------------------------------

# def gcd(a:int, b:int) ->int:
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# def main():
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     print(f"GCD = {gcd(a,b)}")

# if __name__ == "__main__":
#   main()

#175-------------------------------------------

# def dec_to_bin(number:int) -> str:
#     if number == 0:
#         return "0"
#     elif number == 1:
#         return "1"
#     else:
#         next_digit = str(number % 2)
#         return dec_to_bin(number // 2) + next_digit

# def main():
#     number = int(input("Enter the first number: "))
#     print(f"{number} in binary is: {dec_to_bin(number)}")

# if __name__ == "__main__":
#   main()

#176-------------------------------------------

# def nato(word:str) -> str:
#     phonetic_alphabet = {
#     'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
#     'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
#     'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
#     'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
#     'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
#     'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
#     'Y': 'Yankee', 'Z': 'Zulu'
#     }

#     if word == "":
#         return ""
#     else:
#         if word[0] in phonetic_alphabet:
#             return phonetic_alphabet[word[0]] + " " + nato(word[1:])
#         else:
#             return nato(word[1:])
# def main():
#     word = input("Enter the first number: ").upper()
#     print(f"{nato(word)}")

# if __name__ == "__main__":
#   main()

#178-------------------------------------------

# def palindrome(word:str) -> str:
#     if len(word) == 2:
#         return True
#     if word[0] != word[-1]:
#         return False
#     else:
#         return palindrome(word[1:-1])

# def main():
#     word = input("Enter word: ").upper()
#     print(f"{palindrome(word)}")

# if __name__ == "__main__":
#   main()

#179------------------------------------------- 

# def sqrt(num:int, guess:float = 1) -> float:
#     if abs(guess**2 - num) < 10**(-12):
#         return guess
#     else:
#         return sqrt(num,round((guess + (num/guess))/2))

# def main():
#     num = int(input("Enter a number: "))
#     print(f"{sqrt(num)}")

# if __name__ == "__main__":
#   main()

#181-------------------------------------------

# def change(money:float, num_coins:int) -> bool:
#     coins = [0.25, 0.10, 0.05, 0.01]
#     if money == 0:
#         return True
#     if num_coins == 0:
#         return False
#     return change(money - coins[0], num_coins - 1)
        

# def main():
#     money = float(input("Enter the amount of money: "))
#     num_coins = int(input("Enter the number of coins: "))
#     print(f"{change(money,num_coins)}")

# if __name__ == "__main__":
#   main()

