# Identity operators
# operators compare the memory locations of two objects 1)is 2)is not
a = 25 
b = 25 
print(id(a) == id(b))

# is operator: The ‘is’ operator is useful to compare whether two objects are same or not. 
a = 25 
b = 25 
if(a is b): 
    print("a and b have same identity") 
else: 
    print("a and b do not have same identity") 

# is not:this is not operator returns True, if the identity numbers of two objects being compared are not same. If they are same, then it will return False.  
one = [1,2,3,4] 
two = [1,2,3,4] 
if(one is two): 
    print("one and two are same") 
else: 
    print("one and two are not same") #Since both the lists are created at different memory locations, we have their identity numbers different

