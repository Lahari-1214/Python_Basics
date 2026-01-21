# append()
# Appending an element means adding an element at the end of the list
lst = list(range(10))
print(lst)
lst.append(100)
print(lst)

# updating 1st and 2nd element in a list

lst[1:3] = 10,11
print("Updated list",lst)

# The del statement takes the position number of the element to be deleted. 
del lst[1]
print(lst)

# remove()
lst.remove(9)
print("Removing 9 from the list",lst)

lst.reverse()
print(lst,"Reversed")