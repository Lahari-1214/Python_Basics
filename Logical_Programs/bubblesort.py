x = []

n = int(input("How many elements? "))

for i in range(n):
    x.append(int(input("Enter element: ")))

print("Original list:", x)

for i in range(n - 1):
    flag = False
    for j in range(n - 1 - i):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]
            flag = True
    if flag == False:
        break

print("Sorted list:", x)


# note: range(n - 1 - i): Compare only the unsorted portion of the list
