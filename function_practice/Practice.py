
# # ---- Reverse String-----
# def reverse_list(str1):
#     return str1[:: -1]
# str1 = 'pyhton'  
# print(reverse_list(str1))

# # ---- Reverse number-----
# def reverse_list(num):
#     return num[:: -1]
# num = [10,20,30,40]
# print(reverse_list(num))

# # --- Palindrome --
# def Palindrome(names):
#     for name in names:
#         if name == name[::-1]:
#             print("Palindrome")
#         else:
#             print("Not a palindrome")
# names = ['madam','rajnish','hello']
# Palindrome(names)

# # count vowel
# def vowels_count(str1):
#     vowel = "aeiouAEIOU"
#     count = 0
#     for i in str1:
#         if i in vowel:
#             count += 1
#     return count

# str1 = "Rajinsh"
# print(vowels_count(str1))

# def vowel_count(str1):
#     vowel = "aeiouAEIOU"
#     count = []

#     for i in str1:
#         if i in vowel:
#             count.append(i)
#     return count
# str1 = ["Rajnish","Pyhton","king"]
# print(vowel_count(str1))
    
# #--------Count Characters--------------
# def count_chars(text):
#     count = 0
#     for ch in text:
#         count += 1
#     return count

# print(count_chars("Python"))

# #---------Count Vowels------------
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0

#     for ch in text:
#         if ch in vowels:
#             count += 1
#     return count
# print(count_vowels("Rajnish"))


##--- index vowels ----
# def count_vowels(text):
#     result = []
#     for i in text:
#         for ch in i:
#             if ch in "aeiouAEIOU":
#                 result.append(ch)
#     return result
# text  = ["Hello,this is india"]
# print(count_vowels(text))

# # second method
# def count_vowels(text):
#     vowel= "aeiouAEIOU"
#     result = []
#     for i in text:
#         for vowels in i:
#             if vowels in vowel:
#                 result.append(vowels)
#     return result
# text = ["rajkishshshhsuhiuhui"]
# print(count_vowels(text))

## -----------reverse_string-------------
# def reverse_string(text):
#     rev = ''
#     for ch in text:
#         rev = ch + rev
#     return rev
# print(reverse_string("Python"))

##--------------------------------
# def reverse_string(text):
#     rev = []
#     for i in text:
#         rev.append(i)
#     rev.reverse()
#     return rev
# text = "python"
# print(reverse_string(text))

# # ==================================
# def reverse_string(text):
#     return list(text[:: -1])
# text = "python"
# print(reverse_string(text))

#Count Each Character

