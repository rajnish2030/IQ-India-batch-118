# ------ Nested Condition -------
marks = 80
name = "rajnish"
if marks >= 90:
    if name == "rajnish":
        print("Pass")
    else:
        print("Not match this ")
else:
    print("Fail..")

# UPSC Exam : pre ,mains ,inetrview
pre_marks =int(input("Enter Your Marks : "))
if pre_marks >= 300:
    print("Pre Pass")
    main_makrs = int(input("Enter Your Marks : "))
    if main_makrs >= 500:
        print("Pass MAin")
    else:
        print("Fail in MAin")
        inter_makrs = int(input("fill your inter marks.. "))
        if inter_makrs >= 700:
            print("your selected...")
        else:
            print("Fail.....")
else:
    print("Your marks is less than pree marks ...😒")

# btech exam process 

name =input("Enter Your Name : ")
if name == "rajnish":
    print(f"His name : {name}")
    Rollno =int(input("Enter your rollno :"))
    if Rollno >= 1:
        print("This is your roll no :")
    else:
        print("Your are not here")
        marks_12 = int(input("Enter Your 12th class marks : "))
        if marks_12 >=60:
            print("Yes data is here..")
else:
    print("Your data is not save")

# marks of pass and fail
marks =int(input("Enter your mark : "))
if marks >= 300:
    print("Your next process is Done ")
    marks1=int(input("Enter your Second score : "))
    if marks1 >=400:
        print("Your Second level is pass ")
        marks3 = int(input("Enter Your 3rd level score : "))
        if marks3 >= 600:
            print("You are passed..")
        else:
            print("Your 3rd level is not clear")
    else:
        print("Your is not good for 3rd level. Try Again 2nd Level.")
else:
    print("This is not good score for next process..")







