# function is a specific task to perform specific task
# a function to add two numbers 

# Defining the function
def sum(a, b): 
    c = a+b 
    print("Sum:",c)
# Calling a function
sum(10,5)


# Return statement: It is used inside a function to send a value back to the caller and terminate the function’s execution.
# a function to add two numbers 
def sum(a, b): 
    c = a+b 
    return c  # return result 
# call the function 
x = sum(10, 15) 
print('The sum is: ', x)  
y = sum(1.5, 10.75)   
print('The sum is: ', y) 
