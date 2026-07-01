# with open("Demo.txt","r") as f:
#     r=f.read()

# seen = ""
# for i in r:
#     if not i.isdigit():
#         seen += i
# print(seen)

# #Read one line=========================== 
# # Note = Count Only First Line 
# with open("Demo.txt","r") as file:
#     data = file.readline()
#     print(data)

# # This is read all line with count---------------------------------
# with open("Demo.txt","r") as file:
#     count = 0
#     for i in file:
#         count += 1
#         print(f"{count}: {i}", end="")
# print("\nTotal lines",count)

# # Read the entire file--------------------------------
# # remove all number------
# with open("Demo.txt", "r") as file:
#     data = file.read()

#     result=""
#     for ch in data:
#         if not ch.isdigit():
#             result += ch
#     print(result)

# ## READ ALL LINE---------------
# with open("Demo.txt","r") as file:
#     data = file.readlines()
#     print(data)

# # Every Line in Row -----------------
# # remove number-------------
# with open("Demo.txt","r") as file:
#     data=file.readlines()

#     for i in data:
#          count = ""
#          if not i.isdigit():
#             count += i
#     print(count,end="")


# #Print only the digits
# with open("Demo.txt","r") as file:
#     data=file.readlines()

#     for i in data:
#          number = ""

#          for ch in i:
#             if ch.isdigit():
#                  number += ch
#          print(number)

# #-----------------------------------------------------------
# emp_list = ['Sanjeev', 'Aman', 'Deepak', 'Rudra']

# with open("Demo.txt", "w") as file:
#     for name in emp_list:
#         file.write(name + "\n")

# print("Text file created successfully.")

# Create a file .txt ---------------------------------
# import os
# emp_list = ["Sanjeev", "Aman", "Deepak", "Rudra"]

# for name in emp_list:
#     file_check = os.path.exists(f"{name}.txt")
#     if not file_check:
#         with open(name + ".txt", "w") as file:
#             file.write(f"This is {name}'s file.👍")
#     else:
#         print(f"{name} -- file Already Exixts..👍")

# # make a folder --------------------------------
# folder = "Employee_detail"
# os.makedirs(folder)


# emp_list = ["Sanjeev", "Aman", "Deepak", "Rudra"]
# for i in emp_list:
#     os.remove(f"{i}.txt")
#     print(i,"Remove SUccesFully...")


# # create a folder and add all .txt file in this folder..............
# import os

# emp_list = ["Sanjeev", "Aman", "Deepak", "Rudra"]
# folder = "employee_details"
# os.makedirs(folder)
# for i in emp_list:
#     file_path = os.path.join(folder, i + ".txt")
#     with open(file_path, "w") as file:
#         file.write(f"Employee Name: {i}")

# print("All files created successfully.")

# def write_data():
#     Name = input("Enter Your Name :")
#     age = input("Enter Your Age :")

#     file = open("Rajnish.txt","w")

#     file.write("Name" ":" + Name + "\n")
#     file.write("Age" ":" + age)

#     file.close()
#     print("SuccesFully....")

# write_data()

# # Read Data of Rajnish.txt-------------------------
# def read_data():
#     file = open("Rajnish.txt","r")
#     data = file.read()
#     print(data)
#     file.close
# read_data()

# # # Append New Data -------------------------------------
# # def add_student():
# #     name = input("Fill Your name :" )
# #     age = input("Fill your Age :")

# #     file = open("Rajnish.txt","a")
# #     file.write("\n")
# #     file.write("Name :" + name)
# #     file.write("\nAge :" + age)
# #     file.write("\n")

# #     file.close()
# #     print("Added Your Data")

# # add_student()

# # Search Student -------------------------
# def search_student():
#     name = input("Enter Search Name :")
#     file = open("Rajnish.txt","r")
#     data = file.read()
#     if name in data:
#         print(f"{name} : Yes,This is found!!")
#     else:
#         print(f"{name} : No, Found !!!")
# search_student()

# # Remove file form folder
# import os
# path = "E:/python_IQ/Pyhton_class/filehandling/demo.txt"
# os.remove(path)
# print("Remove That")


# # Count Line How many line in your Txt-----------------------------------
# def count_lines():
#     file = open("Rajnish.txt","r")
#     lines = file.readlines()
#     print("Total Line =",len(lines))
#     file.close()
# count_lines()