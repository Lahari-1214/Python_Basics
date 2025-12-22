# Attributes of an Array
# ndim: return how many dimensions of an array
from numpy import *
a = array([[2,3,4,5],[1,2,3,5]])
print(a.ndim)

# shape:The ‘shape’ attribute gives the shape of an array
arr1 = array([1,2,3,4,5]) 
print(arr1.shape) 

# size:  ‘size’ attribute gives the total number of elements in the array
arr1 = array([[1,2,3,4,5],[3,4,5,6,5]]) 
print(arr1.size) 

# itemsize: The ‘itemsize’ attribute  gives the memory size of the array element in bytes.
arr1 = array([1,2,3,4,5,6]) 
print(arr1.itemsize) 


# reshape() Method:The ‘reshape()’ method is useful to change the shape of an array. The new array should have the same number of elements as in the original array.
arr1 = arr1.reshape(2,3)
print(arr1)

# flatten(): collapsed into single dimensional array
print(a.flatten())
