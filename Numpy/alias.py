# ‘Aliasing’ is not ‘copying’. Aliasing means giving another name to the existing object. 
from numpy import *
# aliasing an array. 
from numpy import * 
a = arange(1, 6)  # create a with elements 1 to 5. 
b = a  # give another name b to a 
print('Original array: ', a) 
print('Alias array: ', b) 
b[0]=99  # modify 0th element of b 
print('After modification: ') 
print('Original array: ', a) 
print('Alias array: ', b) 

# Viewing and Copying Arrays 
# creating view for an array 
# shallow copy
from numpy import * 
a = arange(1, 6)  # create a with elements 1 to 5. 
b = a.view()  # create a view of a and call it b (shallow copy)
print('Original array: ', a) 
print('New array: ', b) 
b[0]=99  # modify 0th element of b 
print('After modification: ') 
print('Original array: ', a) 
print('New array: ', b) 

# deep copy
# A Python program to copy an array as another array. 
# copying an array. (deep copy)
from numpy import * 
a = arange(1, 6)  # create a with elements 1 to 5. 
b = a.copy()  # create a copy of a and call it b 
print('Original array: ', a) 
print('New array: ', b) 
b[0]=99  # modify 0th element of b 
print('After modification: ') 
print('Original array: ', a) 
print('New array: ', b) 

