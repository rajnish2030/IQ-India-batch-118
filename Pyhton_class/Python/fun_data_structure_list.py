# marks = [90,55,33,54,75,88,77,30]
# first_element = marks[0]
# last_elemet = marks[-1]
# marks[0]= last_elemet
# marks[-1] = first_element
# print(marks)

# traversing-------------------------------------------------

# marks = [90,55,33,54,75,88,77,30]
# for i in range(len(marks)):
#     if marks[i]%2==0:
#         print(marks)


# # ======== All Sum Element =========
# marks = [90,55,33,54,75,88,77,30]
# count = 0
# for i in marks:
#     count += i
# print(count)


# #======odd number =====
# marks = [90,55,33,54,75,88,77,30]
# for i in marks:
#     if i % 2 != 0:
#         print(i)


# #  greate tha 60  -----------
# marks = [90,55,33,54,75,88,77,30]
# for i in marks:
#     if i > 60:
#         print(i)

# # max ------
# marks = [90,55,33,54,75,88,77,30]
# greater = marks[0]
# for i in marks:
#     if i > greater:
#         greater = i
# print(greater)

# # min ----------------
# marks = [90,55,33,54,75,88,77,30]
# mini = marks[0]
# for i in marks:
#     if i < mini:
#         mini = i
# print(mini)

# # second largest number--------------
# marks = [90,55,33,54,75,88,77,30]
# greater = marks[0]

# for i in marks:
#     if i > greater:
# # second_marks = marks[0]
# # for num1 in marks:
# #     if num1 > second_marks and num1 != greater:
# #         second_marks = num1

# print("Largest:", greater)
# # print("Second Largest:", second_marks)

# # --------Nasted List -----------
# data = [10,20,30,[30,40,50],50,50]
# print(data)


# #---------traversing---------
# marks = [90,30,20,30]
# for i in range(len(marks)):
#     print(i,":",marks[i])

# marks = [30,49,49,30,50]
# for i in marks:
#     print(i)

# #slicing ----------------------------
# num1 = [10,20,30,40,50,60]
# print(num1[1:5])

# # Adding Element --------(Append())

# marks = [10,30,40,50,60,70]
# marks.append(20)
# print(marks)

# # Insert ---------------
# data = [102,203,400,500,600]
# data.insert(1,150)
# print(data)

# # Extend()-----------
# a = [10,20,30]
# b = [40,50,60]
# a.extend(b)
# print(a)

# #POP() -----------------------
# num1 = [10,30,40,50]
# num1.pop(2)
# print(num1)

# #count ------------
# num1 = [10,20,30,40,50]
# print(num1.count(10))

# #Index-----------------
# num1 = [10,20,30,40]
# print(num1.index(20))

# # Reverse ----------
# num1 = [10,20,30,40]
# num1.reverse()
# print(num1)

# # short ------------
# num1 = [40,30,20,10]
# num1.sort()
# print(num1)


# #---------------covert into Zero
# marks =[10,20,30,40,50,60,70]
# for  i in range(len(marks)):
#     marks[i] = 0
# print(marks)

# marks =[10,20,30,40,50,60,70]
# marks = [0] * len(marks)
# print(marks)

# #wap to check 
# emp_name =["raj","harshit","rohan","kamal"]
# vowel = ""
# fal_str  = ""

# for i in emp_name:
#     fal_str  +=  i
# for  j in fal_str:
#     if j in "AEIOUaeiou":
#         vowel += j
# print(vowel)

# # Question ----------------------
# marks =[10,20,30,40,50,60,70]
# makrs_tag = ['55 : pass','22 : fail']

# data_list = ["aman",78,True,False,[5,10],68,10.5]
# print(data_lis_type)

# #---- Append ----
# marks =[10,20,30,40,50,60,70]
# marks_list = []
# for i in marks:
#     if i >= 40:
#          marks_list.append(f"{i} : Pass")
#     else:
#          marks_list.append(f"{i} : Fail")
# print(marks_list)

# #----Simple-----use condition and loop----
# marks =[10,20,30,40,50,60,70]
# for m in marks:
#     if m >= 40:
#         print(m,":","Pass")
#     else:
#         print(m,":","Fail")

# #  data type check  ---------------------
# data_list = ["aman",78,True,False,[5,10],68,10.5]

# for i in data_list:
#      print(i,":",type(i))

# #waf to generate only odd number and store in list using compr.

# def odd(a,b):
#     odd_num=[]
#     for i in range(a,b+1):
#         if i % 2 != 0:
#             odd_num.append(i)
#     return odd_num
# print(odd(10,19))

# #lis con
# def odd(a,b):
#     odd_num=[[i for i in range(a,b) if i% 2 != 0],[i for i in range(a,b) if i% 2 == 0]]
#     return odd_num
# print(odd(10,30))


# # string search -----------------------------------------------------------------------
# def search(name,user):
#     return [i for i in emp_name if user in i]
# emp_name = ["rajnish","harshita","kamal"]
# res = search(emp_name,"h")
# if res==[]:
#     print("Result not found")
# else:
#     print(res)





