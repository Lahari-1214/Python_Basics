student = {
    "name": "Leela",
    "age": 22,
    "course": "Python"
}


# Accessing Values
print(student['name'])
print(student["age"])

# get() is safer (no error if key is missing)
print(student.get('course'))
print(student.get('bloodgroup'))

# Adding New Elements
student["city"] = "Hyderabad"
print("New element is added:",student)

# Updating Values
student["age"] = 23

# Deleting Elements

del student["course"]      # delete specific key
student.pop("age")         # delete & return value
# student.popitem()          # delete last inserted item
# student.clear()            # delete all items

# membership

if "name" in student:
    print("Key exists")

# iteration

# through keys
for key in student:
    print(key)

# through values
for value in student.values():
    print(value)

# throgh key-value pairs
for k, v in student.items():
    print(k, ":", v)


