# Generator is a functions that returns sequence of values
# It was similar to ordinary function but it uses 'yield' statement

# Example 1: Generator function to return  values from x to y
def mygen(x,y):
    while x<=y:
        yield x
        x+=1
g = mygen(5,10)


# converting g into list
lst = list(g)
print(lst)
g=mygen(10,15)
# using for loop
for i in g:
    print(i)

# using next()
g=mygen(15,20)
print(next(g))





# 🦜note: Generators can be iterated only once.
