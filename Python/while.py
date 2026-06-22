# while loop
# 1. initializatio
# 2.condition
# 3. decrement/increament

# #1 to 10
# i = 1
# while  i<=10:
#     print(i)
#     i += i

# # 10 to 1
# i=10
# while i>=1:
#     print(i)
#     i -= 1

#  In While loop when use one thing always use break..

# wap to take start point and stop point by user print all even number
# start_point =int(input("Ënter your start :"))
# end = int(input("Enter your end :"))
# while start_point <= end:
#     if start_point % 2 == 0:
#         print("start = ",start_point)
#     start_point += 1

# #apply the while loop traversing
# name = "Python-programming"
# i = 0
# while i < len(name):
#     print(name[i],end=" ")
#     i += 1

# name = "python-programming"
# rev = ""
# i = 0
# while i < len(name):
#     rev = name[i] + rev
#     i += 1
# print(rev)

# i = 1
# while  i<=10:
#     print(i)
#     i += 1

# # find the vowel
# str2 = "Python Programming"
# i=0
# size =len(str2)
# vowel = 0
# while i < size:
#     if str2[i] in "aeiouAEIOU":
#         vowel +=1
#     i += 1
# print("Total Number :",vowel)

# #consonant
# str2 = "Python Programming"
# i=0
# size =len(str2)
# cons = 0
# while i < size:
#     if str2[i] not in "aeiouAEIOU":
#         cons +=1
#     i += 1
# print("Total Number :",cons)

# # sum of indexes
# str2 = "Python Programming"
# i = 0
# size = len(str2)
# while i < size:
#     sum = +i
#     i+= 1
# print("Sum of Index", sum)

# # make some pattern 
# for i in range(1,6):
#     print("*" * i)

# count = 0
# while count <= 5:
#     print("Rajish", count)
#     count += 1

# # print 1 to 6 number
# i = 1
# while i <= 100:
#     print(i)
# #     i += 1
# # revered number 
# i = 100
# while i >=1:
#     print(i)
#     i -= 1

# i = 1
# while i <=10:
#     print(4*i)
#     i += 1

    
# def palindrome(s):
#     rev = ""

#     for i in s:
#         rev = i + rev

#     if s == rev:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")

# palindrome("madam")


# def even():
#     for i in range(2,21,2):
#         print(i)
# even()

# def even(n):
#     for i in n:
#         if i % 2 == 0:
#             print("Even")
#         else:
#             print("Not even")
# even([1,2,3,4,5,6,6,6,7,8,8,76,8])

def even(h):
    if h % 2 == 0:
        print("Even")
    else:
        print("Not Even")
even(30)


h = 30
def even_odd(h):
    if h % 2 == 0:
        print("Even")
    else:
        print("Not even")
even_odd(h)