#  A Python program to display and find the sum of a list of numbers using for loop.  
# to find sum of list of numbers using for. 
# take a list of numbers 
list = [10,20,30,40,50] 
sum=0  #initially sum is zero 
for i in list: 
    print(i)  #display the element from list 
    sum+=i    #add each element to sum 
print('Sum= ', sum) 

# using while loop
while (i < len(list)):
    print(list[i])
    sum+=list[i]
    i+=1
print("Sum=",sum)