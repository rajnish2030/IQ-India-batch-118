#   ------------------  Tuple  ----------
# 1.Tuple is a data structure in python used to store multiple data of different type with comma(,) in round braces.
# 2. Inmutable
# 3. Support indexing slicing and ordered

# # ----creation of tuple ----
# ti =(30,40,50,50,60) 
# print(type(ti)) # "str"
# print(ti)

# #---- Tuple unpacking---------'
# t1,t2,t3 = (40,50,60)
# print(type(t1)) # "Int convert if tuple unpacking"
# print(t1)
# print(t2)
# print(t3)

# # ----Indexing and Sclicing --------
# mark_tuple = (40,50,60,70)
# print(mark_tuple[0])  # 40
# print(mark_tuple[-1]) # 70
# print(mark_tuple[:: -1])

# #greater find ----------------Traversing-----------------
# def greate_number(num):
#     new_value = []
#     for i in num:
#         if i >= 50:
#             new_value.append(i)
#     return new_value
# num = (50,60,30,50,60,80,90)
# print(greate_number(num))

# num = (50,60,30,50,60,80,90)
# reate_number = []
# for i in num:
#     if i > 55:
#         greate_number = i
# print(i)

# # sum of indices of tuple
# num = (50,60,30,50,60,80,90)
# res = 0
# for i in num:
#     res += i
# print(res)
