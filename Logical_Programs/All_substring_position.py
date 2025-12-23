# A Python program to display all positions of a sub string in a given main string.
# to find all occurrences of sub string in a main string 
str = input('Enter main string: ') 
sub = input('Enter sub string: ') 
 
i=0   
flag=False  # becomes True if sub string is found 
n = len(str) 
while i<n:  # repeat from 0th to nth characters 
    pos = str.find(sub, i, n) 
    if pos != -1:  # if found display its position 
        print('Found at position: ', pos+1)                 
        i=pos+1  # search from pos+1 position onwards 
        flag=True   
    else: 
        print('Sub string not found') 
        break
        # i=i+1  # search from next character onwards
# if flag == False:  
  
