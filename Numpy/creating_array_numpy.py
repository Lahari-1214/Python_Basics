# numpy is a package that contains several classes, functions, variables etc. to deal with scientific calculations in Python. 
# creating single dimensional array using numpy 
import numpy as np
arr = np.array([10, 20, 30, 40, 50])  # create array 
print(arr) # display array 

# linespace: The linspace() function is used to create an array with evenly spaced points between a starting point and ending point.
# creating an array using linspace() 
from numpy import * 
# divide 0 to 10 into 5 parts and take those points in the array 
a = linspace(0, 10, 20) 
print('a = ', a) 
# arange():is like range function
b = arange(10)
print(b)

b1 = arange(1,10,2)
print(b1)
