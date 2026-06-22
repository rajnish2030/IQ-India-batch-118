# def is_even(num):
#     if num % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
# print(is_even(5))


# #-=======Multiply Many Number through *args ====
# def multi(*args):
#     product = 1

#     for i in args:
#         product = product * i
#     return product
    
# print(multi(1,2,4,4,4,5,6,7,78,4))

# # ----- ADD WITH  *ARGS ------
# def add_num(*args):
#     add = 1
#     for i in args:
#         add = add + i
#     return add
# print(add_num(1,2,3,4,45,5,6,67))

# # ----- SUBSTRACT WITH *ARGS ------
# def sub_num(*args):
#     sub = 1
#     for i in args:
#         sub = sub -1
#     return sub

# print(sub_num(8,4,5,7,8,9,5,4,1))


# ----- divided WITH *ARGS ------
def divided(*args):
    divi = 1
    for i in args:
        divi = divi % i
    return divi
print(divided(19,8,2))

