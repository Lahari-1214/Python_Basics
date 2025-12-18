# input(): function takes a value from the keyboard and returns it as a string value from the keyboard and returns it as a string. For example,  
str = input()   # this will wait till we enter a string 
print(str) 

# It is a better idea to display a message to the user so that the user understands what to enter.
str = input("Enter the name")
print(str)

# We can convert string into int,float etc
str = input('Enter a number: ') 
x =  int(str)  # str is converted into int 
print(x) 
#  A Python program to accept two integer numbers from keyboard.
x = int(input('Enter first number: ')) 
y = int(input('Enter second number: ')) 
print('U entered: ', x, y) #display both the numbers separating with a space 
