# finding maximun and minimum elements in a list

lst = []
# taking the input from the user

n = int(input("Enter How many numbers you want in a list"))

for i in range(n):
    print("Enter the number")
    lst.append(int(input()))
print(lst)

b=lst[0]
s=lst[0]

for i in range(1,n):
    if lst[i]>b:
        b=lst[i]
    if lst[i]<s:
        s=lst[i]
print("Maximum element is:",b)
print("Minimum element is:",s)