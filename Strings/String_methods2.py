# Checking Starting and Ending of a String 
# The startswith() method is useful to know whether a string is starting with a sub string or not.
str = 'This is Python' 
print(str.startswith('This'))

# to check the ending of a string, we can use endswith() method. It returns True if the string ends with the specified sub string, otherwise it returns False.
str = 'This is Python' 
print(str.endswith('Python')) 

# String testing methods: 1)isalpha() 2)isalnum()  3)isdigit() 4)islower() 5)isupper() 6)istitle() 7)isspace()  


# Sorting Strings
# take an empty array 
str = [] 
 
# accept how many strings 
n = int(input('How many strings? ')) 
 
# append strings to str array 
for i in range(n): 
    print('Enter string: ', end='') 
    str.append(input()) 
 
# sort the array 
# str.sort() 
str1 = sorted(str) 
 
# display the sorted array 
print('Sorted list: ') 
for i in str1: 
    print(i) 

# Searching in the string(linear search)
#  A Python program to search for the position of a string in a given group of strings.  
# searching for a string in a group of strings 
# take an empty array 
str = [] 
 
# accept how many strings 
n = int(input('How many strings? ')) 
 
# append strings to str array 
for i in range(n): 
    print('Enter string: ', end='') 
    str.append(input()) 
 
# ask for the string to search 
s = input('Enter string to search: ') 
 
# linear search or sequential search 
flag = False   
 
for i in range(len(str)): 
    if s==str[i]: 
        print('Found at: ', i+1) 
        flag=True 
 
if flag==False: 
    print('Not found') 