email = input("Enter your email  : ")
password = input("Enter Your Password : ")
if email == "Rajnish@gamil.com" and password == "Rajnish":
    print("Login Success !! ")
elif password != "Rajnish":
    print("Fill Correctly please !!!!")
    password = input("Fill Password Again : ")
    if password == "Rajnish":
        print("Welcome Yaar Finaly .... !!")
    else:
        print("Rahne De Bhai ... phir kahi !")
else:
    print("Not Correct !!")

#-----------------------------

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
