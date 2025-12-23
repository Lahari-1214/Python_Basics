# A Python program to know whether a sub string exists in main string or not
str = input("Enter the main string")
sub = input("Enter the sub string that you want to find")
if sub in str:
    print("Found")
else:
    print("Not Found")


# Comparing strings
s1 = "Boy"
s2 = "Buy"
if s1 == s2:
    print("Both are same")
elif s1<s2:
    print("s1 is greater")
elif s1>s2:
    print("s2 is greater")
else:
    print("Both are not same")


# Removing spaces from the string
# 1.The rstrip() method removes the spaces which are at the right side of the string. 
# 2.The lstrip() method removes spaces which are at the left side of the string. 
# 3.strip() method removes spaces from both the sides of the strings.
name = "                  Leela Kanthi      "
print(name.rstrip())
print(name.lstrip())
print(name.strip())


# Finding sub strings
# The find() and index() methods search for the sub string from the beginning of the main string. 
# The rfind() and rindex() methods search for the sub string from right to left, i.e. in backward order. 
# to find first occurrence of sub string in a main string 
str = input('Enter main string: ') 
sub = input('Enter sub string: ') 
# find position of sub in str 
# search from 0th to last characters in str 
n = str.find(sub, 0, len(str)) 
# find() returns -1 if sub string is not found 
if n == -1: 
    print('Sub string not found') 
else: 
    print('Sub string found at position: ', n+1) 

# Replace method: The replace() method is useful to replace a sub string in a string with another sub string.:stringname.replace(old, new)
v1 = "I am a Java developer"
v2 = v1.replace("Java","Python")
print(v2)

# split(): is used to brake a string into pieces
x1 = "one,two,three" 
x2 = x1.split(',')
print(x2)



