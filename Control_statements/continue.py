'''
The continue statement is used in a loop to go back to the beginning of the loop. It 
means, when continue is executed, the next repetition will start. When continue is 
executed, the subsequent statements in the loop are not executed. 
'''
# Using continue to execute next iteration of while loop 
x = 0 
while x<10:   
    x+=1      
    if x>5:  # if x > 5 then continue next iteration
            continue 
    print ('x= ', x) 
print("Out of loop") 