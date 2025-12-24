# fact = int(input("Enter number"))
def factorial(fact):
    num = 1
    for i in range(1,fact+1):
        num *= i
    print(num)


