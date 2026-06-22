# #1. Write a Python program to print all odd and even numbers from 1 to 20.
# for i in range(1,10):
#     if i % 2 != 0:
#         print(i,"Odd")
#     if i % 2 == 0:
#         print(i,"Even")

# #2. Write a Python program to generate all multiples of 12.
# for i in range(12,100,12):
#     print(i)

# #3. Write a Python program to generate a table of a number provided by the user. 
# num1 = int(input("Enter Your Table : "))
# for i in range(1,11):
#     print(num1,"*",i,"=",num1*i)

# #4. Write a Python program to check if a number provided by the user is prime or not. 
# num1 = int("enter your number :")    
# check = 0
# for i in range(1,num1 + 1):
#     if num1 % i == 0:
#         check = i + check
# if check == 2:
#     print("prime number") 
# else:
#     print("Not a prime number")      

# # 5. Write a Python program to calculate the sum of numbers between a starting and 
# # ending point provided by the user. 
# start =int(input("Enter your Num : "))
# end = int(input("Enter your Num : "))
# add = 0
# for i in range(start,end +1):
#     add = i + add
# print(add)

# #6. Write a Python program to calculate the product of numbers between a starting and ending point provided by the user.
# start =int(input("Enter your number : "))
# end = int(input("Enter Your number : "))
# product = 1
# for i in range(start,end,+1):
#     product = i * product
# print(product)


# # 7. WAP to generate Fibonacci sequence up to a specified number of terms
# n = int(input("Enter the number : "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
# print("Fibonacci Sequence:")

# #8. Write a Python program to calculate the factorial of a number provided by the user.
# num1 =int(input("Enter your Number : "))
# fac = 1
# for i in range(1,num1 + 1):
#     fac = i + fac
# print(fac)

# #9. Write a Python program to find the greatest character from the string "python"
# str1= "PYTHON"
# grater = str1[0]
# for i in str1:
#     if i > grater:
#         grater = i
# print(grater)

# #10. Write a Python program to display all letters except 'm' and 'i' from the string "Dreamer infotech". 
# word = "Dreamer infotech"
# for i in word:
#     if i == "m" or i == "i":
#         continue
#     print(i, end="")

# #11. Write a Python program to print alternate characters from a given string. 

# str1 = input("Enter your Str : ")
# for i in range(0,len(str1),2):
#     print(str1[i],end="")

# # 12. Write a Python program to reverse a string entered by the user.
# name = "rajnish"   # donot use (-)sub
# rev = ""
# for i in name:
#    rev = i + rev
# print("Reversed Name:", rev)

# # 13.Write a Python program to display all letters except 'm' and 'i' from the string "Dreamer infotech".

# char1="Dreamer infotech"
# for i in char1:
#    if i == "m" or i =="i":
#        continue
#    print(i,end="")

# # 14.Write a Python program to print alternate characters from a given string.
# #alternate ---- always print second number
# cha1 = "Rajnish"
# for i in range(1,len(cha1),2):
#     print(cha1[i],end="")
# #12. Write a Python program to reverse a string entered by the user. 

# char1 ="Python"
# rev = ""
# for i in char1:
#     rev = i + rev
# print("Revsered =",rev)

# #. Write a Python program to count the total number of characters in a string entered by the user. 
# hello =input("Enter your char :")
# count = 0
# for i in hello:
#     count += 1
# print(count)

# #14. Write a Python program to check whether a string entered by the user is a palindrome. 
# #palindrome  ----- it mean read same forward to backward
# char1 = input("Enter your char : ")
# rev = ""
# for i in char1:
#     rev = i + rev
# if char1 == rev:
#      print("palindrome")
# else:
#     print("Not palindrome")

# #15. Write a Python program that allows the user to search for a character within a given string.
# char1 =input("Enter your Charecter :")
# take =input("Fill your Charrr :")
# for i in char1:
#     if i == take:
#         print("Found")
#         break
# else:
#     print("Not Found...")

# #16. Write a Python program to filter out all vowels and consonants from a string entered by the user. 
# stt1 = input("Enter your String : ")

# print("Vowel:")
# for i in stt1:
#     if i in "aeiouAEIOU":
#         print(i,end="")

# print("\nconsonant:")
# for i in stt1:
#     if i not in "aeiouAEIOU":
#         print(i,end="")

# #17. Write a Python program to filter out duplicate characters from a string entered by the user. 
# str2 = input("Enter your String :")
# result = ""
# for i in str2:
#     if i not in result:
#         result += i
# print("No dublicate :",result)


# #18. Write a Python program to display all possible pairs of 3. Example: 1:3, 2:3, 3:3 , 2:1 , 2:2 ,2:3 , 3:1 ,3:2 ,3:3 
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,":",j)


# #19.Write a Python program to generate the pattern of the letter H
# n = 7
# for i in range(n):  #row
#     for j in range(n):  #columns
#         if j==0 or j==n-1 or i==n//2:   #j==o mean first columns,  j==n mean last line(columns),   i==n// middle line
#             print("❤️",end=" ")
#         else:
#             print(" ",end=" ")
#     print() 

# #20. Write a Python program to find duplicate letters between two strings.
# #  Example: In "virat" and "rohit", the duplicate letter is "r".
# name1 = "virat"   
# name2 = "rohit"
# for i in name1:
#     if i in name2:
#         print(i)

# #21. Write a Python program to display the squares of numbers from 1 to 10.
# for i in range(1,11):                    
#     print(i**2)

# #22. Given a string text = "python", calculate the sum of the indices of its characters without using the range() or len() functions. 
# text = "python"
# sum1 = 0
# index =  0
# for i in text:
#     sum1 += index
#     index +=  1
# print(sum1)

# #23.Given: text = "python programming" Goal: Count how many vowels are in the string. Constraint: Do not use indexing (text[i]) or slicing (text[:]). 
# text = "python programming"
# count = 0
# for i in text:
#     if i in "aeiouAEIOU":
#         print(i,end="")
#         count += 1
# print("\ncount =",count)

# # 24.Given: text = "programming" Goal: Print all characters that repeat in the string. 
# text = "programming"
# dot = ""
# for i in text:
#     if text.count(i) > 1 and i not in dot: # text.count(i) ka mtlb ye hai ki text me count kar raha hai kitne bar aaye hai 
#         print(i)
#         dot += i

# 25. Given : 01275623 
# # Write a Python program to find and print the greatest character in the string. 

# Given = "01275623"
# print("Greatest number =",max(Given))
# #--------2nd ways------------
# text = "01275623"
# greatest = "0"
# for i in text:
#     if i > greatest:
#         greatest = i
# print(greatest)


# #26. Given: text = "knowyourself" Goal: Find and print the first character that repeats. 
# text = "knowyourself"
# rep = ""
# for i in text:
#     if i in rep:
#         print(i)
#         break
#     rep += i

# 27. Give : text=”if you think you can not do, you can not show think wisely”  
# Goal: Print the alternate words  
# Constraint: Do not use space between words more than once . 

# text = "if you think you can not do, you can not show think wisely"
# word = text.split() #break into list 

# for i in range(0,len(word),2):
#     print(word[i],end="")

# # 28. Given: text = "knowyourself" Goal: Find and print the alternate characters.
# text = "knowyourself"
# for i in range(0,len(text),2):
#     print(text[i],end="")

# #29  Take two numbers from the user: start and end. Print a string labeling each number in that range as Odd or Even. 
# num1 = int(input("Enter your number  :"))
# num2 = int(input("ENter your number : "))
# for i in range(num1,num2 +1):
#     if i % 2 ==0:
#         print(i,"Even",end="")
#     else:
#         print(i,"ODD")

# #30.Find the sum of string “198765456412”. 
# string = "198765456412"
# total = 0
# for i in string:
#     total += int(i)
# print(total)
# print(type(total))

# # 31.Count how many digits in the string are greater than 5 from text = "1234567890".
# text = "1234567890"
# count = 0
# for i in text:
#     if int(i) > 5:
#         count += 1
# print(count)

# # 32.Task: Replace Character in String Write a program that takes a string input from the user, then asks for a character 
# # to replace and the character to replace it with. The program should output the 
# # modified string where all occurrences of the specified character are replaced by 
# # the replacement character.

# text = input("Enter your string : ")
# old = input("ENter yoour old string :")
# new = input("ENter your new string : ")
# result = ""
# for i in text:
#     if i == old:
#         result += new
#     else:
#         result += i
# print(result)


# #33.Replace Spaces with Underscores Replace all spaces in a string with underscores (_) 

# text = input("Enter your string : ") 
# res = ""

# for i in text:
#     if i == "":
#         res += "_"
#     else:
#         res += i
# print(res)

# #34.Remove Duplicate characters from the string given by the user then print the final output. 

# text = input("Enter your string :")
# res = ""
# for i in text:
#     if i not in res:
#         res += i
# print(res)

# #35.Take string from user and Replace every vowel in the string with an asterisk *. 

# text = input("String : ")
# res = ""
# for i in text:
#     if i.lower() in "AEIOUaeiou":
#         res += "*"
#     else:
#         res += i
# print(res)

# # 36..Count only words not spaces. Entered a string: Hello coders from Success24 Number of words: 4

# text = input("String : ")
# words = text.split()
# count = 0
# for i in words:
#     count += 1
# print("Words =",count)

# #37.Task: Count how many uppercase and lowercase letters are in a string.

# text = input("String : ")
# upar = 0
# lower = 0
# for i in text:
#     if i.isupper():
#         upar += 1
#     elif i.islower():
#         lower += 1
# print(upar)
# print(lower)

#38.Task: Print all characters from the string that are at odd indices. 
text = input("String : ")
for i in text(1, len(text),2):
    print(text[i],end="")