#1---------------------------------------------------------

# def count(num:int) -> int:
#     if num == 0:
#         return 0
#     else:
#         print(num)
#         return count(num-1)


# def main():
#     num = int(input("Enter a number: "))
#     print(count(num))

# if __name__ == "__main__":
#     main()

#2---------------------------------------------------------

# new_list = []

# def zip(item:list, count = 1):
#     if len(item) == 0:
#         return new_list
#     else:
#         string = f"{str(count)} - {item[0]}"
#         new_list.append(string)
#         return zip(item[1:], count+1)

# def main():
#     item = input("Enter an items name: ")
#     print(zip(item))

# if __name__ == "__main__":
#     main()

#3---------------------------------------------------------

# def fib(num:int) -> int:
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fib(num-1) + fib(num-2)
# def main():
#     num = int(input("Enter position in fibonacci series: "))
#     print(fib(num))

# if __name__ == "__main__":
#     main()

#5---------------------------------------------------------

# def calculating_math_func(num:int,fact = 1) -> int:
#     for i in range(1,num+1):
#         fact *= i
#     new_num = fact / (num**3)
#     return (new_num ** 10)

# def main():
#     num = int(input("Enter a number: "))
#     print(calculating_math_func(num))

# if __name__ == "__main__":
#     main()

#7---------------------------------------------------------

# def my_sum(*args):
#     total = 0
#     for i in args:
#         if type(i) == list:
#             for j in i:
#                 total += j
#         else:
#             total += i
#     return total

# def main():
#     nums = input("Enter a list of numbers: ").split()
#     nums = [int(num) for num in nums]
#     print(my_sum(nums))

# if __name__ == "__main__":
#     main()

