# List comphrensions represent creation of new lists from an iterable object(like a list,set,tuple,dictionary or range)
# that satisfies a given condition 
# List comprehensions contain very compact code usually a single statement that performs the task


# ex:1  create a list with squares of integers from 1 to 10
squares = []  
 # create empty list 
for x in range(1, 11):  
 # repeat x values from 1 to 10 
    squares.append(x**2)   # add squares of x to the list 
    
print(squares)

# The previous code can be rewritten in a compact way as: squares = [x**2 for x in range(1, 11)] 

''' Syntax:[ expression for item1 in iterable1 if statement1 
for item2 in iterable2 if statement2 
for item3 in iterable3 if statement3 ... ] '''

squares = [x**2 for x in range(1,11)]
print(squares)

#  If we have two lists ‘x’ and ‘y’ and we want to add each element of ‘x’ with each element of ‘y’, we can write for loops as

x=[10,20,30]
y=[1,2,3]

result = [i+j for i in x for j in y]
print(result)