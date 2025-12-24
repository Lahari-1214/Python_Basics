# program to print prime numbers upto a given number 
# accept upto what number the user wants 
max = int(input("Upto what number? ")) 

for num in range(2, max+1):    # generate from 2 onwards till max 
    for i in range(2,num):  # i represents numbers from 2 to num-1 
        if (num % i) == 0:  # if num is divisible by i 
            break  # then it is not prime, hence go back and check next 
             # number 
    else: 
        print(num)  # otherwise it is prime and hence display 

    # Checking wheather your number is prime or not

# num = int(input("Enter the number"))
# result = 'false'
# for n in range(2,num+1):
#     for m in range(2,n):
#         if n%m == 0:
#             result = 'false'
#             break
#     else:
#         result = 'true'
# if result == 'true':
#     print("Your number is prime number")
# else:
#     print("Your number is not a prime number")

n = int(input("Enter the number"))
for i in range(2,n//2+1):
    if n%2 == 0:
        print('It is not a pm')
        break
else:
    print("It is a prime")


# using function
# A Python function to check if a given number is prime or not. 
# a function to test whether a number is prime or not 
def prime(n): 
    """ to check if n is prime or not """ 
    x=1   # this will be 0 if not prime 
    for i in range(2, n):   # divide n from 2 to n-1 
        if n%i == 0:   # if divisible by any number 
            x=0   # take x as 0 
            break 
        else: 
            x=1   # else take x as 1 
    return x 
 
# test if a number is prime or not 
num = int(input('Enter a number: ')) 
 
# check if num is prime or not 
result = prime(num) 
if result == 1: 
    print(num, ' is prime') 
else: 
    print(num, ' is not prime') 