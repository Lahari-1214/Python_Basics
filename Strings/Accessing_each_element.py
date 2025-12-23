# A Python program to access each element of a string in forward and reverse orders using while loop. 

# using while loop

str = input("Enter the string")
s = len(str)
i = 0
print("Accessing each element using while loop:")
while(i<s):
    print(str[i],end=" ")
    i+=1
print("\nAccessing each element in reverse order using while loop")
i = len(str)-1
while(i>=0):
    print(str[i],end=" ")
    i-=1


# using for loop

str2 = input("\nEnter the string")
print("\nAccessing each element using for loop")
for i in str2:
    print(i,end=' ')

print("\nAccessing each element in reverse order using for loop")
for i in str2[: :-1]:
    print(i,end = ' ')


