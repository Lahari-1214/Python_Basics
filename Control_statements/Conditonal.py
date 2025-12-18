# if statement
# This statement is used to execute one or more statement depending on whether a condition is True or not. 

# A Python program to display a group of messages when the condition is true. 
# understanding if statement 
str = 'Yes' 
if str == 'Yes': 
    print("Yes")  
    print("This is what you said") 
    print("Your response is good") 

# if else statement:The if … else statement executes a group of statements when a condition is True; otherwise, it will execute another group of statements
#  A Python program to test whether a number is even or odd. 
# to know if a given number is even or odd 
x=10 
if x % 2 == 0: 
    print(x, " is even number") 
else: 
    print(x, " is odd number")

# if … elif … else Statement: this is useful when the programmer used to test multiple conditions
#  A Python program to know if a given number is zero, positive or negative. 
# to know if a given number is zero or +ve or -ve 
num=-5 
if num==0: 
    print(num, "is zero") 
elif num>0: 
    print(num, "is positive") 
else: 
    print(num, "is negative") 



#  A program to accept a numeric digit from keyboard and display in words. 
# to display a numeric digit in words 
x = int(input('Enter a digit: ')) 
if x==0: print("ZERO") 
elif x==1: print("ONE") 
elif x==2: print("TWO") 
elif x==3: print("THREE") 
elif x==4: print("FOUR") 
elif x==5: print("FIVE") 
elif x==6: print("SIX") 
elif x==7: print("SEVEN") 
elif x==8: print("EIGHT") 
elif x==9: print("NINE")  # else part not compulsory

