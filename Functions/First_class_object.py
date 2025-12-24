# It is possible to assign a function to a variable. 
# It is possible to define one function inside another function.
# It is possible to pass a function as parameter to another function. 
# It is possible that a function can return another function.  


#  1.A Python program to see how to assign a function to a variable. 
# assign a function to a variable 
def display(str): 
    return 'Hai '+str 
# assign function to variable x 
x = display("Krishna") 
print(x)

# 2.A Python program to know how to define a function inside another function. 
# define a function inside another function 
def display(str): 
    def message(): 
        return 'How are U?' 
    result = message()+str 
    return result 
# call display() function  
print(display("Krishna")) 


# functions can be passed as parameters to other functions 
def display(fun): 
    return 'Hai '+ fun 
def message(): 
    return 'How are U? ' 
# call display() function and pass message() function 
print(display(message()))

#  A Python program to know how a function can return another function.  
# functions can return other functions 
def display(): 
    def message(): 
        return 'How are U?' 
    return message 
# call display() function and it returns message() function 
# in the following code, fun refers to the name: message.  
fun = display() 
print(fun()) 


