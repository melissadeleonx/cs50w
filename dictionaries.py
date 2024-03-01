# Dictionaries in Python are powerful data structures that allow for the storage and retrieval of data using key-value pairs. 
# Unlike sequences such as lists or tuples, dictionaries are unordered collections, meaning that the elements are not indexed by position but by keys. 
# This makes dictionaries highly efficient for retrieving and manipulating data, especially when the data is accessed by a unique identifier or key. 
# Dictionaries are mutable, meaning that they can be modified after creation, allowing for dynamic updates and changes to the stored data.

# Dictionaries in Python:
# Data stored as key-value pairs.
# Accessed and manipulated using Python code.
# Typically used for in-memory data storage.

# SQL Databases:
# Data stored in tables with rows and columns.
# Accessed and manipulated using SQL queries.
# Designed for persistent data storage.
# Regarding CSV files:

# CSV files can be converted to dictionaries in Python.
# Each row in the CSV file can be represented as a dictionary.
# Keys are the column headers, and values are the corresponding row values.

# Creating a Dictionary: Dictionaries in Python are created using curly braces {} and comma-separated key-value pairs in the format key: value.

student = {
    'name': 'Alice',
    'age': 20,
    'major': 'Computer Science'
}
print(student)

# The variable student represents a dictionary. In this dictionary, each key-value pair represents an attribute of a student. Here, the keys are 'name', 'age', and 'major', while the corresponding values are 'Alice', 20, and 'Computer Science', respectively. So, the dictionary student is representing the information about a student named Alice, who is 20 years old and majoring in Computer Science.

# Accessing Elements in a Dictionary: Accessing elements in a dictionary is done by using square brackets [] and specifying the key associated with the value you want to retrieve.
print(student['name'])  # Output: Alice
print(student['age'])   # Output: 20

# Modifying Elements in a Dictionary: You can modify the value associated with a key in a dictionary by assigning a new value to that key.
student['age'] = 21
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}
student['age'] = 35
print(student)
print(student['age'])

# Adding Elements to a Dictionary: New key-value pairs can be added to a dictionary by assigning a value to a new key.
student['year'] = 'Senior'
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'year': 'Senior'}

student['student number'] = 200512345
print(student)

# Removing Elements from a Dictionary: Elements can be removed from a dictionary using the del keyword or the pop() method.
del student['student number']
print(student)

del student['major']
print(student)  # Output: {'name': 'Alice', 'age': 21, 'year': 'Senior'}

major = student.pop('year')
print(student)  # Output: {'name': 'Alice', 'age': 21}
print(major)    # Output: Senior

# Dictionary Operations:

# Checking if a Key Exists: You can check if a key exists in a dictionary using the in keyword.
print('love' in student)
print('name' in student)  # Output: True
print('grade' in student) # Output: False

# Iterating Over a Dictionary:
# You can iterate over the keys, values, or key-value pairs of a dictionary using loops and dictionary methods.

for key in student:
    print(key, ':', student[key])

# Output:
# name : Alice
# age : 21

# The iteration variable key iterates over the keys of the dictionary student. 
# In each iteration, key represents one of the keys in the dictionary.
# Inside the loop, student[key] is used to access the value associated with the current key (key). 
# So, student[key] retrieves the value corresponding to the current key in each iteration.
# The loop iterates over the keys of the dictionary, but within the loop body, 
# you're using these keys to access their corresponding values in the dictionary. 
# This is a common pattern when iterating over dictionaries in Python, allowing you to access both keys and values within the loop.






