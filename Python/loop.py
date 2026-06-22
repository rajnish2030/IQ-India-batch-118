# loop in python -- For and while
# for -- range based loop
# while -- condition based loop

# for i in range(10):
#     print("Rajnish")

# range(start -0,stop-1,step-1)
# range only support integer values.

# for i in range(1,10,3):
#     print(i)

# for i in range (1,21,2):
#     print(i)

# for i in range (1,21):
#     if i / 2 != 0:
#         print(i,end="")


# Adding 1 to 100 number 
# total = 0
# for num1 in range(1,101):
#     total = total + num1
#     print("Sum of 1 to 21 =",total)

# wap a program to product the range given by user 

# start_point = int(input("Enter your Number : "))
# end_point = int(input("enter your number : "))
# total = 0
# for point in range (start_point,end_point+1):
#     total = total + point
#     print("total number of = ",total)

# # table show 
# num = int(input("Enter your no : "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# # Traversing on Strings.
# str1 = "Pyhton programming"
# size = len(str1)
# for i in range(size):
#     print(str1[i],end="") 

# str1 = "Python"
# size = len(str1)
# for i in range(size):
#     print(str1[i],i)

# # WAP to count total number of vowels
# str2 = "Python Programming"
# v = 0
# vc = "aeiouAEIOU"
# for i in str2:
#     if i in vc:
#         v += 1
# print("Total vowels:", v)

# # wap to reverse the string pass by user.
# name = "rajnish"   # donot use (-)sub
# rev = ""
# for i in name:
#     rev = i + rev
# print("Reversed Name:", rev)

# #wap to find char from string "This is python programming".
# char1 = "This is python programming"
# search = "j"
# for i in char1:
#     if i == search:
#         print("Found",i)
#         break
# else:
#     print("No found")

#break -- this is stop when its use on any line.....
#continue --- drop it if any want to removes....

# # wap to count how many consonants "this is python programming"

# text = "this is python programming"
# count = 0

# for ch in text:
#     if ch.isalpha() and ch not in "aeiou":    # isalpha--check to character in latter  ....
#         count += 1

# print("Consonants =", count)


# str1 = "PYTHON"
# size =(len(str1))
# for i in range(size):
#     print(str1[i],"PYTHON",i)


# name = "Rajnish"
# size = (len(name))
# for ch in range(size):
#     print(name[ch],"Rajnish",ch)


# name = "Rajnish"
# rev = ""
# for i in name:
#     rev = i + rev
# print(rev)

# str1 = "PYTHON"
# count = 0
# for i in str1:
#     count += 1
# print("Length =", count)

# str1 = "Rajnish"
# for i in range(len(str1)):
#     print(i,str1[i])

# str1 = "Rajnish"
# size =(len(str1))
# for i in range(size):
#     print(str1[i],i)
   
# name = "Rajnish"
# size = -1
# for i in name:
#     size += 1
#     print(i,size)

# name = "Harshita Gupta"
# count = -1
# for i in name:
#     count += 1
#     print(i,"=",count)

# name = "Rajnish"
# for i in  range(len(name)):
#     print(i,name[i])


# # enumerate() — Loop with Index----------------
# languages = ["Python", "SQL", "Tableau", "Power BI"]
# for index, lang in enumerate(languages):
#     print(f"{index}: {lang}")



# # Check membership efficiently (O(1) thanks to lazy evaluation)
# print(500 in range(1000))  # True
# print(1001 in range(1000)) # False
# # Get length
# print(len(range(0, 100, 3)))  # 34
# # Convert to list when you need actual values
# print(list(range(5)))  # [0, 1, 2, 3, 4]

# for i in range(10, 0, -1):
#     print(i)
# # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# # Countdown
# for i in range(5, 0, -1):
#     print(f"{i}...")
# print("Liftoff!")

# -----------enumerate-----------------------

# liii = ["Rajnish","Harshita","Manisha","Nisha"]
# for index, lang in enumerate(liii,start=1): 
#     print(index,":",lang)

#---------------ZIP---------------

# # names = ["Priya", "Rahul", "Ananya"]
# # scores = [95, 82, 90]
# # grades = ["A", "B", "A"]

# # for name, score, grade in zip(names, scores, grades):
# #     print(f"{name}: {score} ({grade})")

# from itertools import zip_longest

# a = [1, 2, 3, 4, 5]
# b = ["x", "y", "z"]

# for num, letter in zip_longest(a, b, fillvalue="-"):
#     print(num, letter)
# # 1 x
# # 2 y
# # 3 z
# # 4 -
# # 5 -
# pairs = [("Priya", 95), ("Rahul", 82), ("Ananya", 90)]
# names, scores = zip(*pairs)

# print(names)   # ('Priya', 'Rahul', 'Ananya')
# print(scores)  # (95, 82, 90)

# keys = ["name", "age", "city"]
# values = ["Rahul", 25, "Mumbai"]

# info = dict(zip(keys, values))
# print(info)  # {'name': 'Rahul', 'age': 25, 'city': 'Mumbai'}
