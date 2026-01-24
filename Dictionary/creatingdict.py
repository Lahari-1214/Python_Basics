# A dictionary represents a group of elements arranged in the form of key-value pairs, enclosed inside the curly braces {}
dict = {'Name': 'Chandra', 'Id': 200, 'Salary': 9080.50} 
# access value by giving key 
print('Name of employee= ', dict['Name']) 
print('Id number= ', dict['Id']) 
print('Salary= ', dict['Salary']) #the first element is considered as ‘key’ and the immediate next 
#element is taken as its ‘value’. The key and its value are separated by a colon (:)



# rules to declare keys
# 1.Keys should be unique. It means, duplicate keys are not allowed. If we enter same 
#   key again, the old key will be overwritten and only the new key will be available.
# 2.Keys should be immutable type. For example, we can use a number, string or tuples 
    # as keys since they are immutable. We cannot use lists or dictionaries as keys. If they 
    # are used as keys, we will get ‘TypeError’.