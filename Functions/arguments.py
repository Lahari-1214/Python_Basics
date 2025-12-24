# Formal and Actual Arguments
# These parameters are useful to receive values from outside of the function. They are called ‘formal arguments’.
# When we call the function, we should pass data or values to the function. These values are called ‘actual arguments’.
#  Actual args are 4 types: 1)positional 2)Keyword 3)default 4)variable length

# Positional argument:  the arguments passed to a function in correct positional order (should match exactly the no.of position order )
def add(a,b):
    addition = a+b
    print(addition)

add(5,6)
add(9.3,4)

# keyword argument: identify the parameters by their names
def city(name = "babi",pincode = 45):
    print(f"My name:{name} and Pincode: {pincode}")

City_name = "Pithapuram"
code = 533450

city(code,City_name) # My name:533450 and Pincode: Pithapuram
city(pincode = code,name=City_name)

# Default argument:some default value for the function parameters in the definition

def grocery(item, price=40.000000): 
    print('Item = %s' % item) 
    print('Price = %.2f' % price) 
# call grocery() and pass arguments 
grocery(item='Sugar', price=50.7500)  
 # pass 2 arguments 
grocery(item='Sugar') 

# variable length arguments: A variable length argument is an argument that can accept any number of values.
def fun(*args):
    print(*args)
fun("leela","babi","ram",22,89,21) #it will store the *args in a tuple 

# **kargs is a dictionary object which is used to store key-value pairs
