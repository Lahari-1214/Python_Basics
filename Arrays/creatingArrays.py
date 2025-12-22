'''
 An array is an object that stores a group of elements (or values) of 
same datatype.
''' 



# Importing the Array Module: we can import in 3 different ways 
# 1. import array 
# 2.import array as ar 
# 3.from array import * 

import array as ar
a = ar.array('i',[2,3,4,5,6])
print(a)
print("Array elements are:")
for element in a:  
    print(element,end=' ') 

# creating an array with characters 
from array import * 
b = ar.array('u', ['a','b','c','d','e']) 
 
print('The array elements are: ') 
for ch in b:  
    print(ch,end = ' ') 