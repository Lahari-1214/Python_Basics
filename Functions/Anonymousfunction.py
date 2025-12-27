# A function without name is called anonymous function
x = lambda f :f%2 == 0 
y = x(10)
print(y)

# caluculate two numbers using lambda functions
f = lambda x,y: x+y #writing lamda function 
result = f(7,7) # calling lamda function
print("Sum:",result) #displaying the result

# Lamda function to find bigger number among 2 numbers
g = lambda x,y:x if x>y else y
print(g(9,4))
