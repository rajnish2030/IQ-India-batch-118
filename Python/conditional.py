# # Multiple IF statment ---
marks = 90
if marks >= 70:
    print("c")
    if marks >=90:
        print("B")
        if marks >= 95:
            print("A")
        else:
            print("Fail")

# # If-elif-else
marks= int(input("Fill Marks :"))
if marks >= 90:
    print("Grad-A")
elif marks >=70:
    print("Grad-B")
elif marks >60:
    print("Grad-C")
else:
    print("Fails")


# # wap to find the greatest number between 3 number -- 4 9 3
num1 = 4
num2 = 9
num3 = 3
if num1 > num2 and num1 > num3:
    print("The Greatest Number : ",num1)
elif num2 > num1 and num2 > num3:
    print("this is greatest number : ",num2)
else:
    print("this is greatest number : ",num3)

# # wap to find middle number bwtween 3 number 4,9,3
a = 4
b = 9
c = 3
if (a > b and a < c) or (a < b and a > c):
    print("Middle number here:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Middle No here:", b)
else:
    print("Middle no here:", c)

# # wap to find first number from 3 number 
# # wap to find last number from 3 number 
num1 = 3
num2 = 4
num3 = 7

if num1 < num2 and num1 < num3:
    print("This is smallest number:", num1)

elif num2 < num1 and num2 < num3:
    print("This is smallest number:", num2)

else:
    print("This is smallest number:", num3)

# #=======================================================================#
# # greatest numebr through i/o

num1 = int(input("fill num1 :" ))
num2 = int(input("fill num2 :"))
num3 = int(input("Fill num3 :"))
if num1 > num2 and num1 > num3:
    print("This is greatest number : ",num1)
elif num2 > num1 and num2 > num3:
    print("This is Greatest Number : ",num2)
else:
    print("this is greatest number : ",num3)

# # smallest number through i/o

num1 = int(input("Fiil your number : "))
num2 = int(input("Fiil your number : "))
num3 = int(input("Fiil your number : "))
if num1 < num2 and num1 < num3:
    print("This is your smallest number : ",num1)
elif num2 < num1 and num2 < num3:
    print("This is your smallest number : ",num2)
else:
    print("This is your smallest number : ",num3)




