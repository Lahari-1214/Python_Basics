# since tuples are immutable we can't insert elements into a tuple
# but we can convert the tuple into a list, insert the element into the list and convert
# Method 1: Convert Tuple → List → Tuple

t = (1, 2, 3)

lst = list(t)
lst.append(4)

t = tuple(lst)
print(t)


# Method 2: Using Tuple Concatenation
t = (1, 2, 3)
t = t + (4,)
print(t)

# insert at Specific Position
t = (1, 2, 3, 4)

t = t[:2] + (99,) + t[2:]
print(t)

t = t[:3]+(23,)+t[3:]
print(t)
