# While Loop : The while loop execute a group of statements serveral times repeatedly depending on the condition is true or false

#  A Python program to display numbers from 1 to 10 using while loop. 
x = 1
while(x<=10):
    print(x)
    x+=1
print("End")

#  A Python program to display even numbers between m and n. 
x,y = [int(i) for i in input("Enter the min and max values").split(',')]
while(x<=y):
    if (x%2 == 0):
        print(x)
    x+=1

''' for loop: The for loop is useful to iterate over the elements of a sequence. It means, the for loop 
can be used to execute a group of statements repeatedly depending upon the number of 
elements in the sequence. The for loop can work with sequence like string, list, tuple, 
range etc.'''

#  A Python program to display characters of a string using for loop. 
# to display each character from a string 
str='Hello' 
for ch in str: 
    print(ch)     

# A Python program to display odd numbers from 1 to 10 using range() object.  
# to display odd numbers between 1 and 10 
for i in range(1, 10, 2): 
    print(i) 

# A program to display numbers from 10 to 1 in descending order. 
# to display numbers in descending order 
for x in range (10, 0, -1): 
    print(x)

# A program to display the elements of a list using for loop. 
# take a list of elements 
list = [10,20.5,'A','America'] 
 
# display each element from the list 
for element in list: 
    print(element) 
