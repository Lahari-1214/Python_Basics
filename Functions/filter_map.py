# The filter() function is useful to filter out the elements of a sequence depending on the result of a function. 
def is_even(x):
    if x%2 == 0:
        return 1
    else:
        return 2
lst = list(map(int,input("Enter number").split(" ")))
lst1=list(filter(is_even,lst))
print(lst1)

# using lambda function

lst2 = list(filter((lambda x: x%2 == 0),lst))
print(lst2)

# The map() function is similar to filter() function but it acts on each element of the sequence and perhaps changes the elements.

lst3 = list(map(is_even,lst))
print(lst3)