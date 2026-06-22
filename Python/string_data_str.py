# #strig  ==----------------------
# name = "Rajnish"
# print(name.isupper())
# print(name.islower())
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
#----------------------------------------------
# # replace ===============
# user = "This is my Python code"
# new_user = user.replace("T","H")  # T is value of that can replace By H 
# print(new_user)
#----------------------------------------------
# #Join ===============
# user = "rajnish"
# new_user = "".join(user)
# print(new_user)
#-----------------------------------------
# # strip() ================
# user_name = "This is my strip code "
# print(user_name.endswith(" "))
# print(user_name.startswith("T"))
#----------------------------------------
# # Find ==============================
# user = "This is my find code"
# print(user.find('f'))
#--------------------------------------------------
# # Index ==================
# user = "This is my Index code"
# print(user.index('m'))

#-----------------------------------------------
# # split =======================
# name = "My code is Split-code"
# print(name.split(" "))
# print(name.split(","))
# print(name.split("-"))
#---------------------------------------
# # break all alphbeta in string
# name = "My code is Split-code"
# list = list(name)
# print(list)
#-----------------------------------------------------
# # split-line============================
# name = """ this is my splite-line
# code from string
# and i want split this line
# """
# print(name.splitlines())
#----------------------------------------------
# # isdigit====================================
# num = "12345"
# print(num.isdigit())
#------------------------------------------------
# #isalnum==================================
# num = "raji123"
# print(num.isalnum())

#-----------------------------------
# #isalpha
# name = "jsjndi123"
# print(name.isalpha())

# string = "this is python for data-science"
# remove duplicate chr
# string alternate upar

# string1 = "this is python for data-science"
# dup = ""
# for i in string1:
#     if i not in dup:
#         dup += i
# print(dup)

# def duplicate(text):
#     dup = ""
#     for n in text:
#         if n not in dup:
#             dup += n
#     return dup
# string1 = "Helo is my function code for string"
# print(duplicate(string1))


#---------data masking =========================

# num = "28273737737373"
# new_num = num.replace('28273737737373','xxxxxxxxx7373')
# print(new_num)

# # function --------------------------------
# def masking_num(data,visible=4):
#     mask ='X' * (len(data)- visible)
#     visible=data[-visible:]
#     return mask + visible
# print(masking_num('838484848948'))

# # loop --------------------------------
# mask = "384059595"
# mask_list = []
# for i in range(len(mask)):
#     if i < len(mask)-4:
#         mask_list.append("X")
#     else:
#         mask_list.append(mask[i])
# print("".join(mask_list))

# # list compeherince ----------------------------
# mask = "373983939837983739873"
# print("".join(["X" if i < len(mask) - 4 else mask[i] for i in range(len(mask))]))

# #remove vowel
# string1 = "this is python for data-science"
# vowel = "aeiouAEIOU"
# vowel_list = []
# for i in string1:
#     if i in vowel:
#         if i in vowel:
#             print(i)

# #remove vowel
# string1 = ["this is python for data-science"]
# emp_list = []
# vowel = "aeiou"
# for i in string1:
#     for v in vowel:
#         i = i.lower().replace(v,'')
#     emp_list.append(i)
# print(emp_list)


# #remove vowel
# string1 = ["this is python code in vs"]
# emp_list = []
# vowel = "aeiou"
# for i in string1:
#     for v in vowel:
#         i = i.lower().replace(v,'')
#     emp_list.append(i)
# print(emp_list)

#  break all alphbeta in string
name = "My pyhton code is vs"
list = list(name)
print(list)

# regex opertion     -----------------------