# A list within another list is called nested list

a = [80,90,100]
b=[10,20,30,40,50,60,70,a]
print(b)

b[7][0] = 200
print(b)

# b[7] = 500
# print(b)


for x in b[7]:
    print(x)



# nested list as matrices
#  A Python program to retrieve elements from a matrix and display them.  
# displaying nested list as a matrix 
# take a nested list 
mat = [[1,2,3], [4,5,6], [7,8,9]] 
 
print('Display the list as it is: ') 
print(mat) 
 
print('Display row by row: ') 
for r in mat: 
    print(r)   
 
print('Display each column in row 0: ') 
for c in mat[0]: 
    print('%d ' %c, end='')   
print() 
 
print('Display each column in row 1: ') 
for c in mat[1]: 
    print('%d ' %c, end='')   
print() 
 
print('Display each column in row 2: ') 
for c in mat[2]: 
    print('%d ' %c, end='')   
print() 
 
print('Display all elements using for: ') 
for r in mat:   
    for c in r:   # display columns in each row 
        print(c, end=' ')   
    print() 
 
print('Display all elements using for: ') 
for i in range(len(mat)): 
    for j in range(len(mat[i])): 
        print('%d ' %mat[i][j], end='') 
    print()
