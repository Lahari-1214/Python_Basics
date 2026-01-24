# The 5 basic operations: finding length, concatenation, repetition, membership and iteration

# len()
tup = (10, 20, 30, 40, 50)
print("Length of tuple:", len(tup))

#repetition
tup1 = (1, 2, 3)
tup2 = tup1 * 3 
print("Repetition of tuple:", tup2)

# concatenation
tup3 = (4, 5, 6)
tup4 = tup1 + tup3      
print("Concatenation of tuples:", tup4)

# membership
print("Is 20 in tuple?", 20 in tup) 

# iteration
print("Iterating through tuple:")
for item in tup:
    print(item)