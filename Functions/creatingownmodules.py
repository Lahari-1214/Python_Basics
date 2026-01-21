# A module represents a group of classes , methods, functions and variables

# step:1 save the file as ‘employee.py’. 
# save this code as employee.py 
# to calculate dearness allowance 
def da(basic): 
    """ da is 80% of basic salary """ 
    da = basic*80/100 
    return da 
 
# to calculate house rent allowance 
def hra(basic): 
    """ hra is 15% of basic salary """ 
    hra = basic*15/100 
    return hra 
 
# to calculate provident fund amount 
def pf(basic): 
    """ pf is 12% of basic salary """ 
    pf = basic*12/100 
    return pf 
 
# to calculate income tax payable by employee 
def itax(gross): 
    """ tax is calculated at 10% on gross """ 
    tax = gross*0.1 
    return tax 


# step 2: employee.py module contains 4 functions which can be used in any program by importing this module.
# To import the module, we can write:  
    # import employee    
# In this case, we have to refer to the functions by adding the module name as: 
# employee.da(), employee.hra(), employee.pf(), employee.itax().
    # from employee import *
# we can refer to them without using the module name, simply as: 
# da(), hra(), pf() and itax(). 