# A decorator is a function that accepts a function as parameter and returns a function.
# A decorator takes the result of a function, modifies the result and returns it.

# Example:1 incrementing the returned value by 2 using decorator
# a decorator that increments the value of a function by 2 
def decor(fun):   
# this is decorator function 
    def inner():  
 # this is the inner function that modifies 
       value = fun() 
       return value+2 
    return inner  
 # return inner function 
# take a function to which decorator should be applied 
@decor # ‘@’ symbol is useful to call the associated decorator internally, whenever the function is called. 
def num(): 
    return 10 
# call decorator function and pass num 
result_fun = decor(num)   
# result_fun represents 'inner' function  
print(result_fun())   
# call result_fun and display the result  


# using '@' symbol
print(num())

# Example:2 A Python program to apply two decorators to the same function using @ symbol. 
 
# a decorator that doubles the value of a function  
def decor1(fun):    
    def inner():    
        value = fun() 
        return value*2 
    return inner

# take a function to which decorator should be applied 
@decor 
@decor1 
def num(): 
    return 10 
 
# call num() function and apply decor1 and then decor  
print(num()) 



# Decorator with arguments
def dect(fun):
    def inner(name):
        print("Hey! How are you")
        fun(name)
        print("So good to see you")
    return inner

@dect
def greet(name):
    print(name)

greet("Leela")

