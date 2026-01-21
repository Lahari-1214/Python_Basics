# a general way to create lists  
# create a list with integer numbers 
num = [10, 20, 30, 40, 50]  
print('Total list= ', num)  # display total list 
print('First= %d, Last= %d' % (num[0], num[4]))  # display first and   last elements 
 
# create a list with strings 
names = ["Raju", "Vani", "Gopal", "Laxmi"] 
print('Total list= ', names)  # display entire list 
print('First= %s, Last= %s' % (names[0], names[3]))  # display first   and last elements 
 
# create a list with different elements 
x = [10, 20, 10.5, 2.55, "Ganesh", 'Vishnu'] 
print('Total list= ', x)  # display entire list 
print('First= %d, Last= %s' % (x[0], x[5]))  # display first and last   elements 


# 5-basic operation
''' 
1)Finding length
2)Concatenation
3)repetition
4)membership
5)iteration
'''
print(len(x)) #finding length

print(num+names) #concatenation

print(names*2) #repetition

y= 'Raju' in names #membership
print("membership",y)

for i in x:  #iteration
    print(i)



# range(): range() function to generate a sequence of integers which can be stored in a list.
b=list(range(10,20,1))
print(b)