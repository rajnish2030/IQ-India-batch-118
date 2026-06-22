#Question 1
num1 = 20 
num2 = 30
print("Befor swaping  :", num1,num2)
swap = num1
num1=num2
num2=swap
print("After swaping : ", num1 , num2)

# Question 2
char1 = "hello"
char2 = "java"
print("Before swaping : ", char1,char2)
swap = char1
char1=char2
char2 = swap
print("After swaping : ", char1,char2)

#Question 3
num1 = 200
cha1 = "Java"
print("before swaping : ",num1,cha1)
swap = num1
num1 = cha1
cha1 = swap
print("After swaping : ",num1,cha1)

#Question 4
#Update balance after deposit Initial balance: current_balance = 10000 Deposit amount: deposit_balance = 5000 Output
current_balance = 10000
deposit_balance = 5000
print("Before deposit:", current_balance)
current_balance += deposit_balance
print("After deposit:", current_balance)

# Question 5
 #Update balance after withdrawal Before: balance = 12000 Withdrawal: 3000 After: ?
balance = 12000
withdrawal = 3000
print("Before withdrawal:", balance)
balance -= withdrawal
print("After withdrawal:", balance)

# Increase shopping cart items by 3 Before: cart_items = 5 After: ?
cart_items = 5
print("Before:", cart_items)
cart_items += 3
print("After:", cart_items)

# Apply a 20% discount to a price Before: price = 1000 After: ?
price = 1000
print("Before discount:", price)
price -= price * 20 / 100
print("After discount:", price)

#9.Calculate student percentage Input: obtain_marks = 430, out_of = 500 Output: Percentage = ?
obtain_marks = 430
out_of = 500
percentage = (obtain_marks / out_of) * 100
print("Percentage =", percentage)

#10. Calculate total and average of 4 subjects Input Example:
# ● Subject 1: 80 
# ● Subject 2: 75 
# ● Subject 3: 90 
# ● Subject 4: 85
subject1 = 80
subject2 = 75
subject3 = 90
subject4 = 85
total = subject1 + subject2 + subject3 + subject4
average = total / 4
print("Total =", total)
print("Average =", average)

# 11.Calculate average of 3 numbers Input: num1 = 25, num2 = 35, num3 = 45 Output: Average = ?
num1 = 25
num2 = 35
num3 = 45
average = (num1 + num2 + num3) / 3
print("Average =", average)

#13 .Calculate simple interest Input: principal = 10000, rate = 5, time = 2 Output: Simple Interest = ?
principal = 10000
rate = 5
time = 2
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)

# Calculate compound interest Input: principal = 10000, rate = 5, time = 2 Output: Compound Interest = ?
principal = 10000
rate = 5
time = 2
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal
print("Compound Interest =", compound_interest)

# 15. Calculate tax on income Input: income = 500000, tax_rate = 10 Output: Tax = ?
income = 500000
tax_rate = 10
tax = (income * tax_rate) / 100
print("Tax =", tax)

# 16.Convert boolean to integer Input: True Output: ? 
value = True
result = int(value)
print(result)

# 17 .  Convert float to string Input: 45.67 Output: ? 
value = 45.67
result = str(value)
print(result)

#19. Convert 20°C to Fahrenheit Input: 20°C Output: ?
celsius = 20
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit =", fahrenheit)

#20. Convert 50°F to Celsius Input: 50°F Output: ? 
fahrenheit = 50
celsius = (fahrenheit - 32) * 5 / 9
print("Celsius =", celsius)

#21-----
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("Area of Triangle =", area)

#21. Convert integer to binary Input: 25 Output: ?        
#26.Square of sum: (x + y)² Input: x = 5, y = 7 Output: ?
x = 5
y = 7
sum = (x + y)** 2
print(sum)

#27.Simplify expression: x² - 4x + 4 Input: x = 3 Output: ? 
x = 3
sum = (x**3 - 4*x + 4)
print(sum)

#25.Evaluate: (a + b)(a - b) Input: a = 6, b = 2 Output: ?
a = 6
b = 2
sum = (a+b)*(a-b)
print(sum)

#29.Sum of cubes: a³ + b³ Input: a = 1, b = 2 Output: ?
a = 1
b = 2
sum = (a**1 + b**2)
print(sum)

#30.Simplify: (x - y)² Input: x = 10, y = 6 Output: ?
x =10
y = 6
sum = (x-y)**2
print(sum)

#31.Difference of cubes: x³ - y³ Input: x = 4, y = 1 Output: ?
x = 4
y = 1
sum = (x**3 - y**3)
print(sum)

#32.If user input is: Name: Dev Age: 25 City: Jaipur Hobby: Cooking 
name = "Rajnish"
age = 24
city = "Bihar"
hobby = "Playing cricket"
print(f"Meet {name}, a {age}-year-old enthusiast from {city}.")
print(f"When not busy with daily tasks, {name} loves spending time {hobby.lower()}.")
print(f"Life in {city} keeps {name} energetic and curious every single day.")
print(f"With coding as a passion, the future looks creative and inspiring for {name} in the {city} City.")

# 33.Create a Python program that asks the user for the following: 
# ● Full Name 
# ● Profession 
# ● Favorite Quote 
# ● Years of Experience

Name = input("Fill Your Name : ")
Profession = input("Fill your profession : ")
FQ = input("Your Fav Quote : ")
YOE = input("Your Experience .. : ")
print(f"Name : {Name}")
print(f"Profession : {Profession}")
print(f"Experience : {YOE} Years")

#34.Ask the user: 
# ● Movie Name 
# ● Viewer Name 
# ● Seat Number 
# ● Show Time 
# Output format: 
# �
# �
# Movie Ticket 
# �
# �
#  ------------------------ 
# Movie   : <Movie Name> 
# Name    : <Viewer Name> 
# Seat No : <Seat Number> 
# Time    : <Show Time> 
# Enjoy the show! 

Movie_Name = input("Movie Name :")
Your_Name = input("Your Name :")
Seat_No = int(input("Seat No :"))
Time = float(input("Show time :"))
print("/n 🎟️ Movies Ticket 🎞️") #(yaha me icons use kiaa Window + .)
print("------------------")
print(f"Movie : {Movie_Name}")
print(f"Name : {Your_Name}")
print(f"Seat No : {Seat_No}")
print(f"Show Timw : {Time}")
print("Enjoy the Show ..!")