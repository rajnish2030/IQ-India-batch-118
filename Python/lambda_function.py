                              
age_limit= lambda x : "Able" if x >= 18 else "Not Able"
x = int(input("Enter your Age : "))
res = age_limit(x)
print(res)
#-------------------------------------------------------
master = lambda x,y:[x+y,x-y,x*y,x/y]
res = master(20,30)
print(res)

#----------------------------------------------
name = lambda s : len(s)
print(name)