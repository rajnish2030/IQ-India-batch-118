# comparsion operation (>,<,>=,<=,==,!=)
# logical operator(and,or,not)
# membership operator(in,not in)
# identity operator(is,is not)
# assigement operator(+=,~=,*=)
# bitwise operator() not require


# comparsion operation (>,<,>=,<=,==,!=)  
# aman_age = 34
# raj_age = 30
# if(aman_age <= raj_age) :
#     print("yes")
# else:
#     print("no")

# # 1. Marks Check
# marks = 50
# if marks >= 80 :
#     print("A")
# elif marks >= 60 :
#     print("B")
# else:
#     print("Fail")

# #-----------------------------------#

# # 2. wap to check odd and even by taking number from user 
# num = int(input("Enter Your Number : "))
# if num % 2 == 0 :
#     print("Even")
# else:
#     print("Odd")

# #-----------------------------------#

# # 3. find the average of 5 subject marks
# sub1 = int(input("Enter your Number of Hindi :  "))
# sub2 = int(input("Enter your Number of computer :  "))
# sub3 = int(input("Enter your Number of Math :  "))
# sub4 = int(input("Enter your Number of English :  "))
# sub5 = int(input("Enter your Number of Science :  "))
# res = (sub1+sub2+sub3+sub4+sub5) / 5
# print(f"average of 5 sub {res}")

# #-----------------------------------#

# # 4. Able to Vote
# age = 20
# if age >= 18:
#     print("Able to vote ...😍😍")
# else:
#     print("He is not able to Vote right Now ..😒😒")

# #-----------------------------------#

# # 5. Leap Year Check
# year = int(input("Enter your Year : "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("This is leap year ..👌")
# else:
#     print("No, This is not leap year...💕")

# #-----------------------------------#

# # 6. check password  
# Pass =input("Enter Your Password : ")
# if Pass == "Rajnish" :
#     print("Yes, This is Your Password 😎")
# else:
#     print("No, This is Wrong Password 😒😒")

# #-----------------------------------#

# # 7. Number Check (Country)
# num =input("Enetr Your Code ")
# if num == "+91" :
#     print("Indian Country Code ")
# elif num == "+1" :
#     print("USA Country Code ")
# elif num == "+44":
#     print("Canada Country Code")
# elif num == "+52 " :
#     print("Mexico Country Code")
# else:
#     print("No Any Country Code .......")

# #-----------------------------------#

# # 8. Price of mobiles
# cell =int(input("Enter your (GB) :"))
# if cell >= 8 :
#     print("Mobile Price : 25000")
# elif cell >= 6:
#     print("Mobile Price : 20000")
# else:
#     print("Mobile Price : 15000")

# #-----------------------------------#

# # 9. Cricket Score
# score = int(input("What is Your Score : "))
# if score >= 100:
#     print("century 🏏🏏")
# elif score >=50:
#     print("Half century 😊")
# else:
#     print("No Thing ..😒😒")

# #-----------------------------------#
# # 10. wheather Hottness
# temp =int(input("Fill Temp : "))
# if temp >= 40 :
#     print("Wheather Is Too Much Hottyyyyy ...")
# elif temp >= 25 :
#     print("Normal Hotty ...")
# else :
#     print("Chilllllllll.......")



# | Operator | Meaning          
# | -------- | ------------------------
# | `>`      | Greater Than             
# | `<`      | Less Than                
# | `>=`     | Greater Than or Equal To 
# | `<=`     | Less Than or Equal To    
# | `==`     | Equal To                
# | `!=`     | Not Equal To      
       

# logical operator(and,or,not) 
# and -- only return True If all condition are true,other wise false
# or -- returns True if any condition are true , otherwise false
# not -- reverse the result true becomes false and false true 

# num1 = 40
# num2 = 30
# if num1 >= 30 and num2 >= 30 :
#     print("Yes")
# else:
#     ("No") 

# math = 40
# hindi = 60
# english = 70
# if math >= hindi and hindi <= english  or english == math :
#     print("Pass")
# else:7

#     print("Fail")

#-------------------------------#
# age = 30
# if not(age >= 30 and age <= 30 or age == 30):
#     print("Votedddd")
# else:
#    print("Not Vote")

# # wap to check number given by user is completely divide by 2 and 3 

# num1 = int(input("Enter your number : "))
# if num1 % 2 and 3 :
#     print("Number is completely divide ")
# else:
#     print("Number is not divide")


#-------------------------------------------#

#length 
# name1 = "Rajnish"
# print(len(name1))

# #------------------------#
# #index -- start from 0 and negtive -1
# name1 = "rajnish"
# i = len(name1)
# print(name1[2])

# #--------------------------------------#
# # wap a program to check mob number given by user is valid or not valid.

# user_num = int(input("Fill your mobile no.."))
# if len(str(user_num)) == 10 :
#     print("valid")
# else:
#     print("invalid")

#---------------------------------------------------------#
# membership operator(in,not in)

  # - not work in integer
  # - In Sequence important

# name = "Rajnish"
# find = "ni"
# if find in name :
#     print("Yes")
# else:
#     print("No")

# wap to check is the string contain vowels or not.
# String = "this is python class"

# char = "this is my python class"
# if ("a" in char or
#     "e" in char or
#     "i" in char or
#     "o" in char or
#     "u" in char):
#     print("Vowels is here..")
# else:
#     print("Not Here Vowels..")

#-----------------------------#
# str = "this is my laptop"
# vowels = input("Enter your Vowels (a,e,i,o,u) :")
# if vowels in str:
#     print("yes vowels is here...")
# else:
#     print("No vowels is not here....")

#wap a program valid email "@gmail.com" else invalid email

# email = input("enter your email..: ")
# find = "@gmail.com"
# if find in email:
#     print("Valid ...")
# else:
#     print("invalid")

# # url website
# url =input("Enter Your Website Url : ")
# valid = "https://"
# if valid not in url : 
#     print("This is not secure website ..")
# else:
#     print("url")

#-----------------------#

#check password
# pass1 = input("Enter Your Password : ")
# if ("A-Z" in pass1 or
#     "1-9" in pass1 or 
#     "@" in pass1 ):
#     print("Password Created SuccessFully...💕💕")
# else:
#     print("Something is wrong..")

# # identity operator(is,is not) 

# if user in None:
#     print("Action 1")
#     if user is not None :
#         print("Action 2")


# assigement operator(+=,~=,*=)



