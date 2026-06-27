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


# # 21. Filter strings from the list language = ['python', 'php', 'java', 
# # 'c++', 'javascript', 'ruby'] that contain a specific letter provided by 
# # the user, using list comprehension. 
# language = ['python', 'php', 'java', 'c++', 'javascript', 'ruby']
# letter = input("Enter a letter: ")
# result = []
# for lang in language:
#     if letter.lower() in lang.lower():
#         result.append(lang)
# print(result)

# #22. Flatten a nested list like [[1,2], [3,4], [5,6]] into a single list. 
# nested_list = [[1, 2], [3, 4], [5, 6]]
# flat_list = [num for sublist in nested_list for num in sublist]
# print(flat_list)


# # 23. Find the frequency of each element in a list. 
# # List: 
# # [1, 2, 2, 3, 4, 1, 5, 2] 
# # Output: 
# # 1 → 2 times 
# # 2 → 3 times 
# # 3 → 1 time 
# # 4 → 1 time 
# # 5 → 1 time 
# numbers = [1, 2, 2, 3, 4, 1, 5, 2]
# frequency = {num: numbers.count(num) for num in set(numbers)}
# print(frequency)

# # #24. Check whether a given list is a palindrome. 
# # List: 
# # [1, 2, 3, 2, 1] 
# # Output: 
# # Palindrome
# #---------------------------
# numbers = [1, 2, 3, 2, 1]
# if numbers == list(reversed(numbers)):
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# #---------------------------
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# if numbers == numbers[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# # #25. Find the longest string in a list of strings.   
# # List:["cat", "elephant", "dog", "hippopotamus"] 
# # Output: "hippopotamus"
# words = ["cat", "elephant", "dog", "hippopotamus"]
# longest = words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print(longest)

# #--------------------------
# words = input("Enter words separated by spaces: ").split()
# longest = max(words, key=len)
# print("Longest word:", longest)

# # #26. Count how many strings in a list start with a vowel. 
# # List: 
# # ["apple", "banana", "orange", "umbrella", "grape", "ice"] 
# # Output: 
# # 4 strings start with a vowel 
# # (apple, orange, umbrella, ice)
# words = ["apple", "banana", "orange", "umbrella", "grape", "ice"]
# count = 0
# for word in words:
#     if word[0].lower() in "aeiou":
#         count += 1
# print(count)
#----------------------------------------------------------------------
# words = ["apple", "banana", "orange", "umbrella", "grape", "ice"]
# count = sum(word[0].lower() in "aeiou" for word in words)
# print(count)

# #27. Replace all negative numbers in a list with zero 
# List: 
# [5, -3, 7, -1, 0, -8, 4] 
# Output: 
# [5, 0, 7, 0, 0, 0, 4]

# numbers = [5, -3, 7, -1, 0, -8, 4]
# result = []
# for num in numbers:
#     if num < 0:
#         result.append(0)
#     else:
#         result.append(num)
# print(result)
#------------------------------------------------------------
# numbers = [5, -3, 7, -1, 0, -8, 4]
# result = [0 if num < 0 else num for num in numbers]
# print(result)

##28. Create a new list containing only prime numbers from a given list.
# numbers = [2, 4, 5, 6, 7, 8, 11, 13, 15, 17, 20]
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# prime_numbers = [num for num in numbers if is_prime(num)]
# print(prime_numbers)

# #29. Convert a list of integers into a single integer number (e.g., [1,2,3,4] → 1234). 
# numbers = [1, 2, 3, 4]
# result = 0
# for num in numbers:
#     result = result * 10 + num
# print(result)
          
# #30. Group elements of a list based on even and odd indices
# numbers = [10, 20, 30, 40, 50, 60, 70]
# even_index = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
# odd_index = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

# print("Even Index:", even_index)
# print("Odd Index :", odd_index)

# #31. Find the largest even number in a list.
# numbers = [12, 5, 8, 21, 18, 7, 30, 15]
# largest_even = max([num for num in numbers if num % 2 == 0])
# print("Largest Even Number:", largest_even)


# # #32. Find the majority element in a list (an element that appears more than n/2 times). 
# # List:[2, 2, 1, 2, 3, 2, 2] 
# # Output:2
# numbers = [2, 2, 1, 2, 3, 2, 2]
# n = len(numbers)
# for num in numbers:
#     if numbers.count(num) > n // 2:
#         print("Majority Element:", num)
#         break

# # 33. Find the difference between the maximum and minimum values in a list. 
# # List:[10, 4, 7, 2, 15, 6] 
# # Output:13
# numbers = [10, 4, 7, 2, 15, 6]
# difference = max(numbers) - min(numbers)
# print("Difference:", difference)

# # 34. Remove every third element from a list.   
# # List:[1, 2, 3, 4, 5, 6, 7, 8, 9] 
# # Output:[1, 2, 4, 5, 7, 8]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = [numbers[i] for i in range(len(numbers)) if (i + 1) % 3 != 0]
# print(result)


# # 35. Insert an element at every even index of a list. 
# # Original List:[1, 2, 3] 
# # Element to Insert: 0 
# # Output:[0, 1, 0, 2, 0, 3]
# numbers = [1, 2, 3]
# element = 0
# result = []
# for num in numbers:
#     result.append(element)
#     result.append(num)
# print(result)

# # #36. Rearrange a list so that positive and negative numbers alternate. 
# # List: [1, 2, -3, -4, 5, -6] 
# # Output:[1, -3, 2, -4, 5, -6]
# numbers = list(map(int, input("Enter numbers: ").split()))

# positive = [num for num in numbers if num >= 0]
# negative = [num for num in numbers if num < 0]

# result = []

# for i in range(min(len(positive), len(negative))):
#     result.append(positive[i])
#     result.append(negative[i])

# result.extend(positive[len(negative):])
# result.extend(negative[len(positive):])

# print(result)


# #37. Find all pairs of elements in a list whose sum equals a given target number. 
# # List = [2, 4, 3, 5, 7, 8, 9] 
# # Target = 7 
# # Valid pairs:(2, 5),(4, 3)
# numbers = [2, 4, 3, 5, 7, 8, 9]
# target = 7

# pairs = []

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             pairs.append((numbers[i], numbers[j]))

# print(pairs)


# #38. Find the Missing Number from a Sequence. 
# # List:[1, 2, 4, 5, 6] 
# # Expected Range: 1 to 6 
# # Output:3

# numbers = [1, 2, 4, 5, 6]
# n = 6
# expected_sum = n * (n + 1) // 2
# actual_sum = sum(numbers)

# missing = expected_sum - actual_sum

# print("Missing Number:", missing)

# # #39. Split a List into Chunks of Size 3. 
# # List:[1, 2, 3, 4, 5, 6, 7, 8, 9] 
# # Output:[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = []
# for i in range(0, len(numbers), 3):
#     result.append(numbers[i:i+3])
# print(result)

# 40. Reverse Each String in a List. 
# List:["python", "java", "script"] 
# Output: ["nohtyp", "avaj", "tpircs"]

# words = ["python", "java", "script"]
# result = []
# for word in words:
#     result.append(word[::-1])
# print(result)

# # #41. Extract All Digits from a List of Strings 
# # List:["abc123", "45def", "gh6"] 
# # Output:["123", "45", "6"] 
# words = ["abc123", "45def", "gh6"]
# result = ["".join(ch for ch in word if ch.isdigit()) for word in words]
# print(result)


# # 42. Find All Anagram Groups in a List of Words. 
# # List:["eat", "tea", "tan", "ate", "nat", "bat"] 
# # Output:[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# groups = {}
# for word in words:
#     key = "".join(sorted(word))
#     if key not in groups:
#         groups[key] = []

#     groups[key].append(word)

# print(list(groups.values()))