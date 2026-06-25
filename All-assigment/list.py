# #1.Write a Python program to find the sum of all elements in the list [10, 20, 30,40, 50].
# # -- Function ---
# def sum_list(num):
#     total = 0
#     for i in num:
#         total += i
#     return total
# list_number = [10, 20, 30,40, 50]
# print("Sum of all number =",sum_list(list_number))

# # -- list Comprehension--
# list_num = [10,20,30,40,50]
# print("Sum -",sum([i for i in list_num]))

# # ---Loop---
# list_num = [10,20,30,40,50]
# total = 0
# for i in list_num:
#     total += i   
# print("Sum =",total)

# # conditional statement 
# num = [10,20,30,40,50]
# total = 0
# for i in num:
#     if i > 0:
#         total += i
# print("Sum =",total)

# # 2. Write a Python program to display the odd and even elements from the list [10,23, 11, 12, 33, 44, 2, 5, 6].
# # function
# def odd_even(number):
#     for i in number:
#         if i % 2 == 0:
#             print(i,":" "Even")
#         else:
#             print(i,":","Odd")
#     return number
# number = [10,23, 11, 12, 33, 44, 2, 5, 6]
# print(odd_even(number))

# # -- list Comprehension--
# list_even_odd =[10,23, 11, 12, 33, 44, 2, 5, 6]
# print("Even -",[i for i in list_even_odd if i % 2 == 0],"\n""Odd =",[i for i in list_even_odd if i % 2 != 0])

# # loop
# even_odd =[10,23, 11, 12, 33, 44, 2, 5, 6]
# for i in even_odd:
#     if i % 2 == 0:
#         print(i,"= Even")
#     else:
#         print(i,"= Odd")

# #3.Write a Python program to count the odd and even numbers in the list [10, 23,11, 12, 33, 44, 2, 5, 6]. 
# def count_even_odd(number):
#     count_even = 0
#     count_odd = 0
#     for i in number:
#         if i % 2 == 0:
#             count_even += 1
#         else:
#            count_odd += 1
#     print("Odd =",count_odd)
#     print("Even =",count_even)
# number = [10, 23,11, 12, 33, 44, 2, 5, 6]
# count_even_odd(number)

#  # -- list Comprehension--
# num = [10, 23,11, 12, 33, 44, 2, 5, 6]
# count_even = 0
# count_odd  = 0
# print('Even -',len([i for i in num if i % 2 ==0]),"\n""odd",len([i for i in num if i % 2 != 0]))

# # Loop  
# num = [10, 23,11, 12, 33, 44, 2, 5, 6]
# count_even = 0
# count_odd = 0
# for i in num:
#     if i % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1      
# print("Even = ",count_even)  
# print("Odd =",count_odd)        

# # 4. Write a Python program to interchange the first and last elements in the list [10,23, 11, 12, 33, 44, 2, 5, 6].
# simple
# num = [10,23, 11, 12, 33, 44, 2, 5, 6]
# num [0], num[-1] = num[-1], num[0]
# print(num)

# #loop  --
# num = [10,23, 11, 12, 33, 44, 2, 5, 6]
# first_num = num[0]
# second_num = num[-1]
# for i in range(len(num)):
#     if i == 0:
#         num[i] = second_num
#     elif i == len(num) - 1:
#         num[i]= first_num
# print(num)

# # Function----
# def interchange(num):
#     first_num = num[0]
#     second_num = num[-1]
#     for i in range(len(num)):
#          if i == 0:
#                num[i] = second_num
#          elif i == len(num) - 1:
#               num[i]= first_num
#     return num
# num = [10,23, 11, 12, 33, 44, 2, 5, 6]
# print(interchange(num))

# # list comperihance
# num = [10, 23, 11, 12, 33, 44, 2, 5, 6]
# print([num[-1] if i == 0 else num[0] if i == len(num) - 1 else num[i] for i in range(len(num))])

# # 5. Write a Python program to duplicate all the items in the list li = [1, 2, 3], such that the result is: output = [1, 2, 3, 1, 2, 3, 1, 2, 3].
# li=[1,2,3]
# show=[]
# for i in range(3):
#     show.extend(li)
# print(show)

# #_-----2nd method-----------------
# li=[1,2,3]
# show = []
# for i in range(len(li)):
#     show.append(li)
#     show.extend(li)
# print(show)

# # 6. Find the smallest element in the list [10, 23, 11, 12, 33, 44, 2, 5, 6]. 
# li = [10, 23, 11, 12, 33, 44, 2, 5, 6]
# small = min(li)
# print(small,"- Smallest Number")

# #loop
# l2 = [10, 23, 11, 12, 33, 44, 2, 5, 6]
# smallest = l2[0]
# for i in l2:
#     if i < smallest:
#         smallest = i
# print(smallest,"- Smallest Number")


# # 7. Find the greatest element in the list [89, 23, 24, 2, 55, 54, 64].
# num = [89, 23, 24, 2, 55, 54, 64]
# greate = max(num)
# print(greate," : Greatest Number")

# #loop
# num = [89, 23, 24, 2, 55, 54, 64]
# greater = num[0]
# for i in num:
#     if i > greater:
#         num = i
# print("Greatest Number -",greater)

# # 8. Find the repetitive elements in the list [1,2,3,4,56,1,22,23,33,23, 56]. (dublicate)
# li = [1,2,3,4,56,1,22,23,33,23, 56]
# dublicate = []
# for i in li:
#     if li.count(i) > 1 and i not in dublicate:
#         dublicate.append(i)
        
# print(dublicate)

# #list 
# li = [1,2,3,4,56,1,22,23,33,23, 56]
# dublicate = []
# [dublicate.append(i) for i in li if li.count(i)> 1 and i not in dublicate]
# print(dublicate)


# # 9. Remove all the odd elements from the list [10, 23, 11,12,33,44,2,5, 6]. 
# list1 = [10, 23, 11,12,33,44,2,5, 6]
# even_list = []
# for i in list1:
#     if i % 2 == 0:
#         even_list.append(i)
# print(even_list)

# #function
# def even_list(num):
#     even_list = []
#     for i in num:
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list
# num = [10, 23, 11,12,33,44,2,5, 6]
# print(even_list(num))

# # 10. Find all non-repetitive elements in the list[1,2,3,4,56,1,22,23,33,23,56]. 
# def non_repetitive(num):
#     show = []
#     for i in num:
#         if num.count(i) == 1:
#             show.append(i)
#     return show
# num = [1,2,3,4,56,1,22,23,33,23,56]
# print(non_repetitive(num))

# # list
# num = [1,2,3,4,56,1,22,23,33,23,56]
# print("non_repetitive -",[i for i in num if num.count(i) == 1])

# #  Write a Python program to duplicate all items in the list l = [1, 2, 3] to produce the result: result = [1, 2, 3, 1, 2, 3, 1, 2, 3].
# def duplicate(num):
#     show = []
#     for i in num:
#         show.extend(num)
#     return show
# num = [1,2,3]
# print(duplicate(num))

# # list
# l1 = [1,2,3]
# print("seen -",[i for i in range(3) for i in l1])


# #12. Find the second greatest element in the list [89, 23, 24, 2, 55, 54, 64]
# def second_greatest(list1):
#     first_sg=max(list1)
#     second_sg=min(list1)
#     for i in list1:
#         if i != first_sg and i > second_sg:
#             second_sg = i
#     return second_sg
# list1 = [89, 23, 24, 2, 55, 54, 64]
# print(second_greatest(list1))

# # loop
# li = [89, 23, 24, 2, 55, 54, 64]
# first_highest = []
# second_highest = [] 
# for i in li:
#     if i != first_highest and i > second_highest:
#         second_highest = i
# print("Second highest =",second_highest)

# # #13. Reverse the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56].
# def reverse(li):
#     rev = []
#     for i in li:
#         rev = [i] + rev
#     return rev
# li = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# print(reverse(li))

# # reverse list  (insert)
# li = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# rev = []
# for i in li:
#     rev.insert(0,i) 
# print(rev)   

# #list
# li = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# print("reverse",[i for i in li[::-1]])

# # loop
# li = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# rev = []
# for i in li:
#     rev = [i] + rev
# print(rev)

# # 14. Arrange the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] in ascending order. 
# def asss_order(num):
#     return sorted(num)

# num = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# print(asss_order(num))

# # #loop
# num = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         if num[i]> num[j]:
#             num[i],num[j] = num[j],num[i]
# print(num)

# # 15. Arrange the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] in descending order. 
# #   function
# def descending_order(num):
#     return sorted(num,reverse=True)
# num =[1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# print(descending_order(num))

# # loop with function
# def descending_order(num):
#     for i in range(len(num)):
#         for j in range(i+1,len(num)):
#             if num[i] < num[j]:
#                 asc = num[i]
#                 num[i] = num[j]
#                 num[j] = asc
#         return num
# num = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# print(descending_order(num))

# #simple 
# num1 =  [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# num1.sort(reverse=True)
# print(num1)

# #16. Write a Python program to print all the vowels present in the given list of strings ["Dreamer", "infotech"].
# def vowel_check(str):
#     vowel = "aeiouAEIOU"
#     for i in str:
#         for ch in i:
#             if ch in vowel:
#                 print(ch , "is vowel")

# str = ["Dreamer", "infotech"]
# vowel_check(str)


# #list
# str = ["Dreamer", "infotech"]
# print("vowel",[ch for i in str for ch in i if ch.lower()in "aeiou"])

# # 17. Write a Python program to take input from the user to create a list of elements.
# # The user should input each element of the list one by one. 
# # Create a list with these elements (maximum of 5 elements).
# def list_el():
#     my_list =[]
#     for i in range(5):
#         element = int(input("Enter your Element "))
#         my_list.append(element)
#     return my_list
# show = list_el()
# print("List of Element = ",show)

# list_1 =[]
# for i in range(5):
#     show = int(input("Enter your element: "))
#     list_1.append(show)
# print("My element =",list_1)


# #18. Write a Python program to generate a list of numbers in reverse order from 10 to 1 using list comprehension. 
# #fuction
# def reverse():
#     for i in range(10, 0, -1):
#         print(i)

# reverse()

# #  second ways
# def revser_order():
#     return list(range(10,0,-1))
# print(revser_order())

# # third method
# list_num = []
# for i in range(10,0,-1):
#     list_num.append(i)
# print(list_num)

# #lc
# list_num = [i for i in range(10,0,-1)]
# print(list_num)

# #19. Create a list of square numbers from 1 to 10 using list comprehension. 
# num = []
# for i in range(1,11):
#     if i > 0 and i<= 10:
#         print(i**2)

# #list comp
# square = [i**2 for i in range(1,11)]
# print(square)

# # function
# def square():
#     for i in range(1,11):
#         print(i**2)
# square()

# # second method
# def square_num():
#     square = []
#     for i in range(1,11):
#         square.append(i**2)
#     return square
# print(square_num())


# #20. Create a list of even numbers from 1 to 10 using list comprehension. 
# num = []
# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)

# #list comprehension. 
# num = [i for i in range(1,11) if i % 2 == 0 ]
# print(num)

# # function
# def even_number():
#     even = []
#     for i in range(1,11):
#         if i % 2 == 0:
#             even.append(i)  
#     return even
# print(even_number())


# 21. Filter strings from the list language = ['python', 'php', 'java', 
# 'c++', 'javascript', 'ruby'] that contain a specific letter provided by 
# the user, using list comprehension. 

