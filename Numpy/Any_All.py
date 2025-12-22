'''
The any() function can be used to determine if any one element of the array is True. 
The all() function can be used to determine whether all the elements in the array are True. 
The any() and all() functions return either True or False. 
'''

# A Python program to know the effects of any() and all() functions. 
# using any() and all() functions 
from numpy import * 
a = array([1,2,3,0]) 
b = array([0,2,3,1]) 
 
c = a > b 
print('Result of a>b: ', c) 
 
print('Check if any one element is true: ', any(c)) 
print('Check if all elements are true: ', all(c)) 
 
if(any(a>b)): 
    print('a contains atleast one element greater than those of b')