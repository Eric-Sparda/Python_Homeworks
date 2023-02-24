#1------------------------------------------------------------------

# mylist = []

# def sep(a,b,c):
#     if a >= b:
#         return mylist
#     else:
#         mylist.append(a)
#         return sep(a+c,b,c)

# def main():
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     c = int(input("Enter steps: "))
#     b +=1
#     print(sep(a,b,c))

# if __name__ == "__main__":
#     main()

#2------------------------------------------------------------------

# mylist = input("List: ").split()
# newlist = []
# copy = mylist.copy()

# def prod(copy):
#     if len(copy) <= 1:
#         return newlist
#     else:
#         c = int(copy[0]) * int(copy[1])
#         newlist.append(c)
#         return prod(copy[1:])

# def main():
#     print(prod(copy))

# if __name__ == "__main__":
#     main()


#3------------------------------------------------------------------

# new_text = []

# def replace(text, replacement_words):
#     for i in text:
#         if i == "_":
#             i = replacement_words[0]
#             new_text.append(i)
#             replacement_words = replacement_words[1:]
#         else:
#             new_text.append(i)
#     return " ".join(new_text)

# def main():
#     text = input("Enter a sentence: ").split()
#     replacement_words = input("Enter the replacement words : ").split()
#     print(replace(text, replacement_words))


# if __name__ == "__main__":
#     main()

#4------------------------------------------------------------------

# mylist = input("Enter the words: ").split()
# mylist.sort(key = len)
# summa = len(mylist[0]) + len(mylist[-1])
# print(summa)

#5------------------------------------------------------------------

# mylist = input("Enter numbers: ").split()
# n = int(input("Enter a number: "))

# def rec(start,stop,mid):
#     if n == int(mylist[mid]):
#         return mid
#     elif n > int(mylist[mid]):
#         return rec(start = mid + 1, stop = len(mylist), mid = ((start+stop)//2))
#     elif n < int(mylist[mid]):
#         return rec(start = 0, stop = mid - 1, mid = ((start+stop)//2))
    
# def main():
#     start = 0
#     stop = len(mylist)
#     mid = (start + stop) //2
#     print(rec(start,stop,mid))

# if __name__ == "__main__":
#     main()

#6------------------------------------------------------------------

# def sqrt(n):
#     sqrt_dict = {}
#     for i in range(1, n+1):
#         sqrt_dict[i] = i**2
#     return sqrt_dict

# def main():
#     n = int(input("Enter a value for N: "))
    
#     print(f"Dictionary of squares:\n{sqrt(n)}")

# if __name__ == "__main__":
#     main()

#8------------------------------------------------------------------

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
    
# def main():
#     n = int(input("Enter a value for N: "))
#     print(fib(n))

# if __name__ == "__main__":
#     main()