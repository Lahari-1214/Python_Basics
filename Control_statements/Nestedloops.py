# we can write a for loop inside a while loop or a for loop inside another for loop. Such loops are called ‘nested loops’
# mostly used for pattern printings and matrix printing
#  to display stars in right angled triangular form 
for i in range(1, 11):  # to display 10 rows 
    for j in range(1, i+1):  # no. of stars = row number 
        print('* ', end='') 
    print() 