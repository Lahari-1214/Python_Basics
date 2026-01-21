# Aliasing list:Giving a new name to an existing list is called ‘aliasing’. The new name is called ‘alias name’.
x = [10,20,30,40,50] 
y = x  
 # x is aliased as y 
print("Alias of X:",x)  #will display [10,20,30,40,50] 
print("Alias of Y",y) #will display [10,20,30,40,50]
x[1] = 99   # modify 1st element in x 
print("Effect of Alias on X",x)  #will display [10,99,30,40,50] 
print("Effect of Alias on Y",y) #will display [10,99,30,40,50]

# note:if we modify x, y will also be changed because both x and y refer to the same list.

# Cloning: Obtaining exact copy of an existing object (or list) is called ‘cloning’. 
x = [10,20,30,40,50] 
y = x[:]   
# x is cloned as y 
print("Cloning results")
print("Cloning of X",x)  #will display [10,20,30,40,50] 
print("Cloning of Y",y) #will display [10,20,30,40,50] 
x[1] = 99   # modify 1st element in x 
print("Effect of cloning on X",x)  #will display [10,99,30,40,50] 
print("Effect of cloning on Y",y) #will display [10,20,30,40,50] 

# the above same thing can be done using copy()
y = x.copy()   # x is copied as y 
# x and y are independent
