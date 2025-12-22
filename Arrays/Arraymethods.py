import array as arr
arr = arr.array('i',[2,3,4,5,6,7,8,9,10])
print(arr)

# a.append(x): Adds an element x at the end of the existing array a. 
print("After appending the element")
arr.append(99)
print(arr)

 
# a.insert(i, x): Inserts x in the position i in the array. 
arr.insert(1, 99) 
print('After inserting 99 in 1st position: ', arr)   
 
# a.remove(x): Removes the first occurrence of x in the array a. Raises ‘ValueError’ if not found.  
arr.remove(2) 
print('After removing 2: ', arr)   
 
# a.pop():Remove last item from the array a. 
n = arr.pop() 
print('Array after using pop(): ', arr) 
print('Popped element: ', n) 
 
# finding position of element using index() method 
n = arr.index(3) 
print('First occurrence of element 3 is at: ', n) 
 
# a.tolist(): Converts the array ‘a’ into a list.  
lst = arr.tolist() 
print('List: ', lst) 
print('Array: ', arr)


