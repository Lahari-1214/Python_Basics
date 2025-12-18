# A Python program to accept 3 integers in the same line and display their sum. 
# accepting 3 numbers separated by space 
var1, var2, var3 = [int(x) for x in input("Enter three numbers: ").split()] 
print('Sum = ', var1+var2+var3) 