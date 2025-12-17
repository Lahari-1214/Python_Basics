'''A set is an unordered collection of elements much like a set in Mathematics. The order of 
elements is not maintained in the sets. It means the elements may not appear in the 
same order as they are entered into the set. Moreover, a set does not accept duplicate 
elements. There are two sub types in sets: 
 set datatype 
 frozenset datatype '''

# Set datatype: To create a set, we should enter the elements separated by commas inside curly  braces { }. -->mutable
s = {10, 20, 30, 20, 50} 
print(s) # may display {50, 10, 20, 30} 
ch = set("Hello") 
print(ch) # may display {'H', 'e', 'l', 'o'} 
lst = [1,2,5,4,3]   
s = set(lst) 
print(s) # may display {1, 2, 3, 4, 5} 

# Frozenset datatype:same as set but we can't modify the data inside the function called frozenset() --> immutable
fs = frozenset("LeelaKanthi")
print(fs)