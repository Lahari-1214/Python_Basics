# slice represents piece in an array. where we can retrive range of elements from the array
# where indexing is useful to retrive an element from the array
#  A Python program that helps to know the effects of slicing operations on an array. 
# create array y with elements from 1st to 3rd from x 
import array as arr
x = arr.array('i',[10,20,30,40,50,60,70,80,90,100])
y = x[1:4] 
print(y) 
 
# create array y with elements from 0th till the last element in x 
y = x[0:] 
print(y) 
 
# create array y with elements from 0th to 3rd from x 
y = x[:4] 
print(y) 
 
# create array y with last 4 elements from x 
y = x[-4:] 
print(y) 
 
# create y with last 4th element and with 3 [-4-(-1)= -3]elements  
 # towards right.  



# A Python program to retrieve and display only a range of elements from an array using slicing.  
# using slicing to display elements of an array. 
from array import * 
x = array('i', [10, 20, 30, 40, 50, 60, 70]) 
 
# display elements from 2nd to 4th only 
for i in x[2:5]: 
    print(i) 