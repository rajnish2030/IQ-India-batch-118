#1. Write a program that takes input for the cost price and selling price of an item.
cp = float(input("Enter Your Cost Price: "))
sp = float(input("Enter Your Sell Price: "))

#profit
if cp < sp:
    profit = sp - cp
    profit_per = (profit/cp)*100
    print("Profit =", profit)
    print("Profit Percentage =",profit_per)
 #loss   
elif cp > sp :
    loss = cp - sp
    loss_per = (loss/cp)*100
    print("loss =",loss)                    
    print("Loss Percentage =",loss_per)
else:
    print("Here is not any profit")

# 2. Write a script to analyze cricket stats for a team. 
Virat = int(input("Enter Virat Runs : "))
Rohit = int(input("Enter Rohit Runs : "))
Ishan = int(input("Enter Ishan Runs : "))
Hardik = int(input("Enter Hardik Runs : "))
Vaibhaw = int(input("Enter Vaibhaw Runs : "))
Runs = (Virat+Rohit+Ishan+Hardik+Vaibhaw)
average = Runs/5
print(Runs)
print(average)

# 3.Write a program that prompts the user for their age and tells them how many years until they reach retirement age (65).
age = int(input("Enter your Age : "))
retiement_age = 65
if age <= retiement_age:
    final_age = retiement_age - age
    print("Final age =",final_age)
elif age >= retiement_age:
    over = retiement_age - age
    print("Your already reached retirement age. =",over)
else:
    print("No Age ")

# 4. Write a program to calculate the area of a circle.
radius =float(input("Enter Your Radius : "))
area = 3.14159 * radius ** 2
print("Area = ",area)

# 5.You have to calculate an employee's salary by computing the gross salary tax and net salary based on the given parameters. 
bass_salary = float(input("Enter your salary : "))
bouns_salary = float(input("Enter your bous salary : "))
tax = float(input("Enter your tax : "))
other_salary =float(input("Enter your other Salary : "))

gross_salary = bass_salary + bouns_salary
if gross_salary > 0:
    tax = gross_salary * tax / 100
    if tax > 0:
         net_salary = gross_salary - tax - other_salary
         print("Gross salary = ",gross_salary)
         print("Net Salary = ",net_salary)

# 6. Task: Bank Loan Approval System
age = int(input("Enter your Age : "))
monthly_income = int(input("Enter Your Monthly : "))
credit_score = int(input("Enter Your Credit Score : "))
outstanding_debts = int(input("Enter your Outstanding :"))
if age >=18 and age <= 60:
    if monthly_income >= 25000:
        if credit_score >= 700:
            if outstanding_debts >= 10000:
                print("Loan Approved")
            else:
                print("Loan Rejected")

# 7. Task: Students Interview Eligibility Checker
# Objective: You have to create a javascript script that checks whether an user is eligible for a bank loan based on various criteria. 

Academic_Score = float(input("Enter Your academic score : "))
Attendance_Percentage = float(input("Enter your Attendance Percentage : "))
if Academic_Score >= 70 and Attendance_Percentage >= 85:
        print("Eligible for Interview")
else:
        print("Not Eligible for Interview")

#8. Task: Validating Email Domain
email = input("Enter Your Email : ")
if "gamil.com" in email:
       print("Email is correct....👌")
else:
       print("Email is not correct ...😊")
    
# 10.Task : Student Grading System 
# Create a javascript program to calculate a student's grade based on their marks. 
# Task: 
# 1. Input: Prompt the user to enter their marks. 
# 2. Criteria: 
# ○ Grade A: 90–100 
# ○ Grade B: 80–89 
# ○ Grade C: 70–79 
# ○ Grade D: 60–69 
# ○ Grade E: 50–59 
# ○ Grade F: 0–49 
# ○ Invalid marks: Outside the range 0–100. 
# 3. Output: Display the grade or an error message for invalid marks. 
# Example Outputs: 
# ● Marks: 85 → Grade: B 
# ● Marks: 45 → Grade: F 
# ● Marks: 105 → Invalid marks

num1 = int(input("Enter your Marks : "))
if num1 >=90 and num1 <= 100:
        print("Grade A")
elif num1 >= 80 and num1 <= 89:
       print("Grade B")
elif num1 >= 70 and num1 >= 79:
        print("Grade C")
elif num1 >= 60 and num1 <= 69:
        print("Grade D")
elif num1 >= 50 and num1 <= 59:
        print("Grade E")
elif num1 >= 0 and num1 <= 49:
     print("Grade F")
else:
       print("Invalid marks.")



#12.Employee Salary Based on Experience. 
bouns = 5000
experience = int(input("Enter your Experience : "))
if experience >= 15:
       salary = 80000 + bouns
       print("Senior Employees")
       print("Senior Employees salary :",salary)
elif experience >= 5 and experience <= 9:
       salary = 50000
       print("5 and 9 years Experience salary :",salary)
       print("Mid-Level Employee")
elif experience <= 3:
       salary3 = 30000
       print("Junior Employee")
       print("Junior level salary :",salary3)
else:
       print("Your are fresher")


# 13. Library Charge Calculation
day = int(input("Enter the number of days the book has been borrowed: "))
if day <= 5:
    library_charge = day * 2
elif day >= 6 and day <= 10:
    library_charge = day * 3
elif day >= 11 and day <= 15:
    library_charge = day * 4
else:
    library_charge = day * 5
print("Library charge =", library_charge)

#  14 .Arranging Three Numbers in Descending Order
a =int(input("Enter your number : "))
b = int(input("Enter your number : "))
c = int(input("Enter your number : "))
if a >= b and b >= c:
    print(a,b,c)
elif a >= c and c >= b:
    print(a,c,b)
elif b >=a and a >= c:
    print(b,a,c) 
elif b >= c and c >= a:
    print(b,c,a)
elif c >= a and c >= b:
    print(c,a,b)
else:
    print(c,b,a)


#15. Tax Calculation for Car Purchase 
price = float(input("Enter Your Car Price : "))
brand = input("Enter Your Brand Car : ")

if brand == "Mahindra" and price >= 7 and price <= 10:
    tax = price * 0.05
elif brand == "Audi" and price >= 10 and price <= 15:
    tax = price * 0.10
elif brand == "Jaguar" and price >= 15 and price <= 20:
    tax = price * 0.25
elif brand == "Mercedes" and price >= 20 and price <= 25:
    tax = price * 0.30
else:
    tax = 0
    print("no tax")
print("Tax on purchase = ",tax, "lakh")

#16.Finding the Middle Number
num1 = int(input("Enter your First Number : "))
num2 = int(input("Enter your second Number : "))
num3 = int(input("Enter your Third Number : "))
if num1 > num2 and num1 < num3:
    print("This is Middle Number : ",num1)
elif num2 > num1 and num2 < num3:
    print("This is Middle Number : ",num2)
else:
    print("This is middle Number : ",num3)

# 17.Find the greatest number. 

num1 = int(input("This is Your Highest Number : "))
num2 = int(input("This is Your Highest Number : "))
num3 = int(input("This is Your Highest Number : "))

if num1 > num2 and num1 > num3:
    print("Highest Number : ",num1)
elif num2 > num1 and num2 > num3:
    print("Highest Number : ",num2)
else:
    print("Highest Number : ",num3)

#11. #Write a javascript program that authenticates a user by checking their username and 
# password. The program should compare the entered credentials with predefined valid 
# credentials. 
# ● Predefined valid usernames and corresponding passwords 
# username1 = "user1"  
# username1_password1 = "pass@123" 
# Instructions: 
# 1. Input: 
# ○ Prompt the user to input their username and password. 
# 2. Processing: 
# ○ Check if the username and password match 
# 3. Output: 
# ○ If both the username and password match the predefined valid credentials 
# display "Authentication successful." 
# ○ If either the username or the password does not match display 
# "Authentication failed."

username1 = "user1"
user_password = "pass@123"

user = (input("Enter Your USER Name : "))
password = input("Enter Your Password : ")

if user == username1 and password == user_password:
       print("Authentication successful....😍😍😍")
else:
       print("Authentication failed....😒😒")

       
#21.UPSC Selection Process  
age = int(input("Enter Your Age : "))
Graduate_status  = input("Enter Your Graduate status ? (yes/no): ")
nationality = input("Enter Your Nationality : ")
if age >= 21 and age <= 32:
    if Graduate_status == "yes":
        if nationality == "Indian":
            print("If eligible, for upsc exam ")
            print("Proceeding to Prelims..")
            #Prelims
            Prelims_Exam = int(input("Enter Your Prelims exam score : "))
            prelims_cutoff = int(input("Enter Prelims Cut-off: "))
            if Prelims_Exam >= prelims_cutoff:
                print("You passed the Prelims.")
                print("Process in main...")
                #Mains Exam 
                Mains_Exam =int(input("Enter Your Main Score :"))
                main_cutoff = int(input("Enter Your Cutoff Marks : "))
                if Mains_Exam >= main_cutoff:
                    print("proceed to Interview >>")
                    print("Enter Interview Cut-off")
                    #interview
                    interview_score = int(input("Enter Interview Score: "))
                    interview_cutoff = int(input("Enter Interview Cut-off: "))
                    if interview_score >= interview_cutoff:
                        print("Congratulations😍😍 You have cleared the UPSC👌👌")
                    else:
                        print("You failed the Interview.")
                else:
                    print("You failed the Prelims...")
            else:
                print("You failed the Prelims")
            
        else:
            print("Ineligible: Age must be between 21 and 32 years.")
