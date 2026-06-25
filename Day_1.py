# print("Hello")

# name = "Rajnish"
# Age = 24

# print(name)
# print(Age)

# name = input("Enter Your Name : ")
# print("Welcome" , name)

# age = int(input("Enter Your Age : "))
# if age >= 18:
#     print("Your Are Able to Vote....")
# else:
#     print("Your Are not Able to vote in this time....")

# for i in range(5):
#     print(i)     #0 1 2 3 4  

# count = 1
# while count <= 5:
#     print(count)   #1 2 3 4 5 
#     count += 1

# Movie_Name = input("Movie Name :")
# Your_Name = input("Your Name :")
# Seat_No = int(input("Seat No :"))
# Time = float(input("Show time :"))
# print("/n Movies Ticket")
# print("------------------")
# print(f"Movie : {Movie_Name}")
# print(f"Name : {Your_Name}")
# print(f"Seat No : {Seat_No}")
# print(f"Show Timw : {Time}")
# print("Enjoy the Show ..!")

# numbers = [10, 20, 30, 40]

# for num in numbers:
#     print(num) 
# value = 45.67
# result = str(value)
# print(result)
# print(type(result))

# for i in range(1,100):
#     if i % 2 == 0:
#         print(i)

# # Even NUMBER
# for u in range(1,100):
#     if u % 3 == 0:
#         print(u)

# # Odd Number 
# for u in range(2,50):
#     if u % 2 !=0:
#         print(u)

# name = "Rajnish"  #Print a string character by character
# for  i in name:
#     print(i)      

#Reverse Counting   
# i = 20
# while i >= 1:
#     print(i)
#     i -= 1       

# name = "Rajish"
# rev = ""
# for i in name:
#     rev = i + rev
# print(rev)

# # wap to reverse the string pass by user.
# name = "rajnish"   # donot use (-)sub
# rev = ""
# for i in name:
#     rev = i + rev
# print("Reversed Name:", rev)

#   # For Loop
# for i in range(5):
#     print(i)

# # While Loop
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# #for
# name = "rajnish"   # donot use (-)sub
# rev = ""
# for i in name:
#     rev = i + rev
# print("Reversed Name:", rev)

# #while
# name = "rajnish"
# rev = ""
# i = 0
# while i < len(name):
#     rev = name[i] + rev
#     i += 1

# print("Reversed Name:", rev)

#------
#Print numbers from 1 to 10 using a for loop.
# Print numbers from 10 to 1 using a while loop.
# Print all even numbers from 1 to 50.
# Print all odd numbers from 1 to 50.
# Find the sum of numbers from 1 to 100.
# Print the multiplication table of a given number.
# Count how many digits are in a number.
# Reverse a string using a loop.
# Count the vowels in a string.
# Count the consonants in a string.


# #Print numbers from 1 to 10 using a for loop.
# for i in range (1,10):
#     print(i)
# # Print numbers from 10 to 1 using a while loop.
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1


# # Print all even numbers from 1 to 50.
# for i in range(1,50):
#     if i % 2 ==0:
#         print(i)

# Print all odd numbers from 1 to 50.
# for i in range(1,50,2):
#     if i != 0:  #(if i % 2 != 0)
#         print(i)

# Find the sum of numbers from 1 to 100.
# sum1 = 0

# for i in range(1, 101):
#     sum1 += i
# print("Sum Of =",sum1)
# #----------------------------------while-----
# total = 0
# i = 1

# while i <= 100:
#     total += i
#     i += 1

# print("Sum =", total)



# num1 = int("enter your number :")
# check = 0
# for i in range(1,num1 + 1):
#     if num1 % i == 0:
#         check = i + check
# if check == 2:
#     print("prime number0") 
# else:
#     print("Not a prime number")  


# hhhh = int(input("Enter your num :"))
# count = 0
# for i in range(1,hhhh+1):
#     if hhhh % i == 0:
#         count += 1
# if count == 2:
#       print("Prime number")
# else:
#       print("NOt PRime nUmber")

# char1 = input("Enter your char : ")
# rev = ""
# for i in char1:
#     rev = i + rev
# if char1 == rev:
#      print("palindrome")
# else:
#     print("Not palindrome")


# name = "Rajnish"
# for i in range(len(name)):
#     print(i,":",name[i])

# name = "Rajnish"
# for index, ch in enumerate(name):
#     print(index, ":",ch)

# name = "python"
# index = 0
# for i in name:
#     index += 1
#     print(i,"::",index)

# mame =[10,20,40,30]
# mame.append(25)
# mame.insert(3,35)
# print(mame)

# str1 = ["ram","roihan","jishu"]
# cap = []
# for i in str1:
#     if i in str1:
#         cap.uppar(i)
#     print(cap)


# str1=[90,30,60,45]
# odd = []
# even = []
# for i in str1:
#     if i % 2 == 0:
#         even.append(f"{i} : Even")
#     else:
#         odd.append(f"{i} : Odd")
# print(odd,even)

# str1 = ["python"]
# for i in str1:
#     print(i[::-1])


