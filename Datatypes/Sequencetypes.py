"""
A sequence represents a group of elements or items. For example, a group of 
integer numbers will form a sequence. There are six types of sequences in Python
 str 
 bytes 
 bytearray 
 list 
 tuple 
 range 
"""

#1.str Datatype: str represents string datatype. A string is represented by a group of characters. Strings are enclosed in single quotes or double quotes. Both are valid. 
s = 'Welcome to Core Python'  # this is the original string 
print(s) 

print(s[3:7])  # display from 3rd to 6th characters 
print(s[11:])  # display from 11th characters onwards till end 
print(s[-1])  # display first character from the end 
print(s*2) 

#2. bytes Datatype:The bytes datatype represents a group of byte numbers just like an array does (we cannot modify the data in this data type once we created)

# program to understand bytes type array 
# create a list of byte numbers 
elements = [10, 20, 0, 40, 15]  
# convert the list into bytes type array  
x = bytes(elements)
# retrieve elements from x using for loop and display 
for i in x: print(i) 

# 3.bytearray Datatype: similar to bytes but we can modify the data
# program to understand bytearray type array 
# create a list of byte numbers 
elements = [10, 20, 0, 40, 15]  
 
# convert the list into bytearray type array  
x = bytearray(elements)  
 
# modify the first two elements of x 
x[0] = 88 
x[1] = 99 
 
# retrieve elements from x using for loop and display 
for i in x: print(i) 
# 4.list datatype:list represents group of differnt types of elements inside the square brackets (mutable)
list = [10, -20, 15.5, 'Vijay', "Mary"]
print(list) # we will discuss this in upcoming programs

#5.Tuple Datatype: similar to list but the elements are arranged in parenthesis (immutable)
tpl = (10, -20, 15.5, 'Vijay', "Mary") 
print(tpl) #we will discuss this in upcoming programs

#6. range: it is a built in function which is used with for loop. It generates the sequence numbers between the given range
lst = list(range(10)) 
print(lst) # will display: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

