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


# sum(): returns the sum of all the elements in the list
naturalnum = list(range(11))
print(sum(naturalnum))

# index(): returns the first occurance of x
print(naturalnum.index(10))


# insert(): Inserts x in to the list in the position specified by i  syntax: list.insert(i, x) 
naturalnum.insert(4,400)
print(naturalnum)