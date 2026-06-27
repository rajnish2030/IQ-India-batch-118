string1 = set("Hello-this is my set code")
vowel = set("aeiouAEIOU")
res=(list(string1-vowel))
print(res)

#_---ADD()-----------
str1 ={"Rajnish","Rahul","Rohan","Rohit"}
str1.add("Rocky")
print(list(str1))

# 2.
num = {10,20,30,40,50}
num.add(60)
print(num)

# Update--------------------------------------------------
string = {"Rajnish","Gandhi","Fizza","AMAN"}
string.update(["Rajnish","Banti","Deepak","Sanjeev"])
print(string)

# Remove -----------------------
name = {"Kausal","Aman","Aman","Sanjeev"}
name.remove("Sanjeev")
print(name)

#-----discard()-----------
name = {"Kausal","Aman","deepak","Sanjeev"}
name.discard("Kausal")
print(name)

# pop() ============================ (take Random name from name)
name = {"Kausal","Aman","deepak","Sanjeev"}
winner = name.pop()
print("Winner -",winner)
#--------------------------------------------
fruits = {"Apple", "Mango", "Banana"}
item = fruits.pop()
print(item)
print(fruits)

# clear() =============================
fruits = {"Apple", "Mango", "Banana"}
fruits.clear()
print(fruits)

#copy() =============================
fruits = {"Apple", "Mango", "Banana","Apple"}
fruits_copy=fruits.copy()
print(fruits_copy)
print(fruits)
#-------------------------
students = {"Rajnish", "Amit", "Rahul"}
backup = students.copy()
students.remove("Rahul")
print("Current:", students)
print("Backup:", backup)

# ----union()---
students_1 = {"Rajnish", "Amit", "Rahul"}
students_2 = {"Rajnish", "priya", "Rohan"}
res = students_1.union(students_2)
print(res)

# intersection()----------------------------------
# comman value print only-
students_1 = {"Rajnish", "Amit", "Rahul"}
students_2 = {"Rajnish", "priya", "Rohan"}
res = students_1.intersection(students_2)
print(res)

#--difference()---------------------
students_1 = {"Rajnish", "Amit", "Rahul"}
students_2 = {"Rajnish", "priya", "Rohan"}
res = students_1.difference(students_2)
res1 = students_2.difference(students_1)
print(res)
print(res1)

#-------symmetric_difference()--------------
students_1 = {"Rajnish", "Amit", "Rahul"}
students_2 = {"Rajnish", "priya", "Rohan"}
res = students_1.symmetric_difference(students_2)
print(res)

#issubset()----------------------
team_a = {"Rajnish", "Amit"}
team_b = {"Rajnish", "Amit", "Rahul"}

print(team_a.issubset(team_b))

#issuperset()--------------------
team_b = {"Rajnish", "Amit", "Rahul"}
team_a = {"Rajnish", "Amit"}

print(team_b.issuperset(team_a))

#isdisjoint()=======================
team_a = {"Rajnish", "Amit"}
team_b = {"Priya", "Rahul"}

print(team_a.isdisjoint(team_b))
