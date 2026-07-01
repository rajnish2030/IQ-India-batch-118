#numpy integer
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.dtype)

# integer to string
import numpy as np
arr = np.array([10,20, "Rajnish"])
print(arr)
print(arr.dtype)

#integer to float
import numpy as np
num1 = np.array([10,20,30.1,40])
print(num1)
print(num1.dtype)

# addition 2d
import numpy as np
num1 = np.array([10,20,30])
num2 = np.array([30,40,50])
print(num1+num2)

# multiply 1d
import numpy as np
var1 = np.array([2,3,4])
print(var1*2)

#string array(integer)
import numpy as np
str1 = np.array([10,20,30])
print(str1[1])
print(str1[2])

# slicing string
import numpy as np
ste = "RAJNISh"
print(ste[0:4])

import numpy as np
name ="IQ-INDIA"
print(name[1:5])

# Mathmatical numpy
import numpy as np
num1 = np.array([20,30,40])
num2 = np.array([50,60,70])
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)


# matrix 
import numpy as np
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(A @ B) 