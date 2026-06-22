
# n = 8
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==n//2:
#             print("*",end="")
#         else:print(" ",end="")
#     print()

# n = 7
# for i in range(n):  #row
#     for j in range(n):  #columns
#         if j==0 or i==0 or i==n//2 or i==n-1:
#             print("😊",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

n = 7
for i in range(n):  #row
    for j in range(n):  #columns
        if j==0 or j==n-1 or i==0 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  