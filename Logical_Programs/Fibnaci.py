n = int(input('How many Fibonaccis ? ')) 
f1=0  # this is first Fibonacci no 
f2=1  # this is the second one 
c=2   # counts the no of Fibonaccis 
if n==1: 
    print(f1) 
elif n==2: 
    print(f1, '\n', f2, sep='') 
else:  
    print(f1, '\n', f2, sep='') 
    while c<n: 
        f = f1+f2 # add two Fibonaccis to get the new one 
        print(f) 
        f1, f2 = f2, f   # this is same as f1=f2, f2=f 
        c+=1   # increment counter

