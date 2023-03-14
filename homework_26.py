#-----------------------------------------------------TASK N1-----------------------------------------------------

# def generate_parentheses(n):
#     def backtrack(combination, left, right):
#         if len(combination) == 2*n:
#             result.append(combination)
#             return
#         if left < n:
#             backtrack(combination + "(", left + 1, right)
#         if right < left:
#             backtrack(combination + ")", left, right + 1)
    
#     result = []
#     backtrack("", 0, 0)
#     return result

# def main():
#     n = int(input("Enter the number of brackets: "))
#     print(generate_parentheses(n))

# if __name__ == "__main__":
#     main()

#-----------------------------------------------------TASK N2-----------------------------------------------------

# def climb(n, steps=[]):
#     if n == 0:
#         print(steps)
#         return 1
#     if n < 0:
#         return 0
#     count = climb(n-1, steps + [1]) + climb(n-2, steps + [2])
#     return count

# def main():
#     n = int(input("Enter how many steps till top: "))
#     print(f"All possible solutions:")
#     res = climb(n)

# if __name__ == "__main__":
#     main()

#-----------------------------------------------------TASK N3-----------------------------------------------------

# def num(n):
#     numbers = [int(i) for i in str(n)]
#     while len(numbers) > 1:
#         total = 0
#         for i in numbers:
#             total += i
#         numbers = [int(i) for i in str(total)]
#     return numbers[0]

# def main():
#     n = int(input("Enter a number: "))
#     print(num(n))

# if __name__ == "__main__":
#     main()
