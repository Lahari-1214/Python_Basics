# An index represents the position number of an element in an array
#  A Python program to retrieve the elements of an array using array index. 
# accessing elements of an array using index 
# Index always starts from 0 that means x[0] = 10,x[1]=20 etc

from array import * 
x = array('i', [10, 20, 30, 40, 50]) 
# find number of elements in the array 
n = len(x) 
# display array elements using indexing 
for i in range(n):  # repeat from 0 to n-1 
    print(x[i], end=' ') 

#  A Python program to retrieve elements of an array using while loop. 
x = array('i', [10, 20, 30, 40, 50])
i =0
while(i < len(x)):
    print(x[i],end = ' ')
    i+=1

