'''Pass by value represents that a copy of the variable value is passed to the function and 
any modifications to that value will not reflect outside the function. Pass by reference 
represents sending the reference or memory address of the variable to the function. The 
variable value is modified by the function through memory address and hence the 
modified value will reflect outside the function also. '''

# pass by value

def fun(x):
    x += 1
    print("Inside",x)
x = 10
print(x)
fun(x)
print("Outside",x)
# pass by reference

# a = 10
# b = 10
# print(id(a))
# print(id(b))
# lst1 = [10,20,30]
# lst2 = [10,20,30]
# print(id(lst1))
# print(id(lst2))

# pass by reference

def fun2(list):
    list.append(40)
    print(list)
lst = [10,20,30]
print(lst)
fun2(lst)
print(lst)


