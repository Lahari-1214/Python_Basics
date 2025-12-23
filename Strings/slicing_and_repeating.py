# Slice represents a piece of string
str = 'Core Python'
print(len(str))
str[0:9:1]   # access string from 0th to 8th element in steps of 1 
str[0:9:2] #step to 2 elements
str[::]  # access string from 0th to last character
str[2:4:1]  # access from str[2] to str[3] in steps of 1 
str[::2]  # access entire string in steps of 2 
str[2::]  # access string from str[2] to ending
str[:4:]  # access string from str[0] to str[3] in steps of 1 
str[-4:-1]  # access from str[-4] to str[-2] from left to right in str.
str[-6::]  # access from str[-6] till the end of the string
str[-1:-4:-1]  # retrieve from str[-1] to str[-3] from right to left
str[-1::-1]  # retrieve from str[-1] till first element from right to left 

# Repeating the Strings:The repetition operator is denoted by ‘*’ symbol and is useful to repeat the string for several times.
print(str*3)
# similarly, it is possible to repeat a part of the string obtained by slicing as: 
s = str[5:7]*3   
# repeat 5th 6th characters for 3 times 
print(s)

# Concatenation of Strings:+’ on strings to attach a string at the end of another string. 
s1 = 'Core'
s2 = 'Python'
s3=s1+s2   # concatenate s1 and s2 
print(s3)  
 # display the total string s3 