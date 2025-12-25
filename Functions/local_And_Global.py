# local variable is a variable whose scope is limited within the function where it is created
def myfun():
    a = 1
    a+=1
    print(a)
myfun()
# print(a) #error raised because a is created inside the function


# Global variable: when we declare the variable above the function it becomes a global variable
var = "Global varible"
def myfun2():
    print(var)
myfun2()


# Global keyword:the global keyword is used inside a function to indicate that a variable refers to the global scope (outside the function), rather than creating a new local variable.
a = 1
def myfunction(): 
    global a  
 # this is global var 
    print('global a= ', a)   # display global var 
    a=2  # modify global var value 
    print('modifed a= ', a)  # display new value 
myfunction() 
print('global a= ', a)  # display modified value

# passing group of elements into a funtion let say lists,tuples,strings,etc
def Group(lst):
    print(lst)
    sum = 0
    for i in lst:
        sum+=i
    print("Sum:",sum)
    print("Avg",sum/len(lst))
lst = [int(x) for x in input().split()]
Group(lst)