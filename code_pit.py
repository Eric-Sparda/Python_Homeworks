#------------------------------------1-10------------------------------------
# num = int(input("number: "))
# numbers = ""
# rev = ""
# rev_numbers = ""
# bigger = ""
# for i in range(num,0,-1):
#     if i < 10:

#         numbers += str(i)
#         rev_numbers += str(i)
#         print(numbers +(i-1)*"." +(i-1)*"."+ rev_numbers[::-1])
#     elif i >= 10:
#         rev += str(i)
#         rev = rev[::-1]
#         numbers += rev
#         rev_numbers += numbers
#         numbers = numbers[::-1]
#         print(numbers +(i-1)*"." +(i-1)*"."+ rev_numbers[::-1])
#         rev_numbers = ""
#         numbers = ""
#     else:
#         pass
#------------------------------------Divided------------------------------------
#---------------------------------------------------------------------------PART_1---------------------------------------------------------------------------
# n = int(input("number: "))
# for i in range(n):
#     for j in range(i+1):
#         print(n-j,end="")
#     print((n-i-1)*".")
#---------------------------------------------------------------------------PART_2---------------------------------------------------------------------------
# for i in range(n):
#     for j in range(n-i-1):
#         print(".",end="")
#     for j in range(i+1):
#         print(j+1,end="")
#     print()
#---------------------------------------------------------------------------wrong direction---------------------------------------------------------------------------
# n = int(input("num: "))
# for i in range(n):
#     for j in range(i+1):
#         print(n-j,end="")
#     for k in range(n-i-1):
#         print(".",end="")
#     for l in range(i+1):
#         print(n-l,end="")
#     print()

