# The eval() function takes a string and evaluates the result of the string by taking it as a Python expression.
a, b = 5, 10 
result = eval("a+b-4") 
print(result) 
  
# using eval() along with input() function 
x = eval(input("Enter an expression: ")) 
print("Result= %d " % x)

# A Python program to accept a list and display it
lst = eval(input("Enter a list: ")) 
print("List= ", lst) 

# A Python program to accept a tuple and display it.  
tpl = eval(input("Enter a tuple: ")) 
print("Tuple= ", tpl) 