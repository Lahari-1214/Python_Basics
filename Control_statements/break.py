'''The break statement can be used inside a for loop or while loop to come out of the loop. 
When 'break' is executed, the Python interpreter jumps out of the loop to process the 
next statement in the program.''' 
# Example:1
# searching for an element in a list 
group1 = [1,2,3,4,5]   #take a list of elements 
search = int(input('Enter element to search: ')) 
for element in group1: 
    if search == element: 
        print('Element found in group1') 
        break  # come out of for loop 
else: 
    print('Element not found in group1')   # this is else suite 


# Example:2
# Using break to come out of while loop 
x = 10 
while x>=1: 
    print ('x= ', x) 
    x-=1 
    if x==5:  # if x is 5 then come out from while loop 
        break 
print("Out of loop")  