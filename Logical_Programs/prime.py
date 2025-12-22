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

num = int(input("Enter the number"))
result = 'false'
for n in range(2,num+1):
    for m in range(2,n):
        if n%m == 0:
            result = 'false'
            break
    else:
        result = 'true'
if result == 'true':
    print("Your number is prime number")
else:
    print("Your number is not a prime number")