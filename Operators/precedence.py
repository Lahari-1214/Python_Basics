# The sequence of execution of the operators is called operator precedence.
# Precedence represents the priority level of the operator. The operators with higher precedence will be executed first than of lower precedence.
a = 3/2*4+3+(10/4)**3-2 
print("Value of a:", a)
'''Evaluation of an Expression  
Expression  
Explanation  
value = 3/2*4+3+(10/4)**3-2 
value = 3/2*4+3+2.5**3-2 
The expression in ( ) is evaluated first. 
value = 3/2*4+3+15.625-2 
Exponentiation ** is next.  
value = 1.5*4+3+15.625-2 
value = 6.0+3+15.625-2 
* and / have equal precedence. They are evaluated from left 
to right (associativity). So, first / and then *.  
value = 9.0+15.625-2 
value = 24.625-2 
value = 22.625 
+ and - have equal precedence. They are evaluated from left 
to right (associativity). So, first + and then -.  '''