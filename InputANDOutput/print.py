# To display output or results, Python provides the print() function.

#  print() Statement 
print() # it will throw the cursor to the next line

#The print(“string”) Statement 
print("Hello")
print("City name="+"Hyderabad") 

#The print(variables list) Statement 
a, b = 2, 4 
print(a) 
print(b)
print(a,b)

# sep : represents separator. The format is sep="characters" which are used to separate the values in the output.  
print(a, b, sep=",") 

print(a, b, sep=':') 
 
print(a, b, sep='----') 

# end="characters" which indicates the ending characters for the line
print("Hello", end='') 
print("Dear", end='') 
print('How are U?', end='') 

print("Hello", end='\t') 
print("Dear", end='\t') 
print('How are U?', end='\t')

# The print(object) Statement: We can pass objects like lists, tuples or dictionaries to the print() function to display the elements of those objects.

lst = [10, 'A', 'Hai'] 
print(lst) 
d = {'Idly':30.00, 'Roti':45.00, 'Chappati':55.50} 
print(d) 

# The print(formatted string) Statement
x=10 
print('value= %i' %  x) 

# .format()
name, salary = 'Ravi', 12500.75 
print('Hello {0}, your salary is {1}'.format(name, salary)) 
print('Hello {n}, your salary is {s}'.format(n=name, s=salary)) 
print('Hello {:s}, your salary is {:.2f}'.format(name, salary)) 
print('Hello %s, your salary is %.2f' % (name, salary)) 
