# Recursive functions: A function calls itself is called recursive functions
# recursive function to calculate factorial 
def factorial(n):   
    """ to find factorial of n """   
    if n==0: 
        result=1 
    else: 
        result=n*factorial(n-1) 
    return result 
 
# find factorial values for first 10 numbers 
for i in range(1, 11): 
    print('Factorial of {} is {}'.format(i, factorial(i)))
        



# Tower of hanoi
# A Python program to solve Towers of Hanoi problem. 
# recursive function to solve Towers of Hanoi 
def towers(n, a, c, b): 
    if n==1: 
        # if only 1 disk, then move it from A to C 
        print('Move disk %i from pole %s to pole %s' %(n, a, c)) 
    else:   # if more than 1 disk 
        # move first n-1 disks from A to B using C as intermediate pole 
        towers(n-1, a, b, c) 
 
        # move remaining 1 disk from A to C  
        print('Move disk %i from pole %s to pole %s'%(n, a, c)) 
 
        # move n-1 disks from B to C using A as intermediate pole 
        towers(n-1, b, c, a) 
 
# call the function  
n = int(input('Enter number of disks: ')) 
 
# we should change n disk
            
        