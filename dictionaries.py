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

# student = {
#     'name': 'Alice',
#     'age': 20,
#     'major': 'Computer Science'
# }
# print(student)

# The variable student represents a dictionary. In this dictionary, each key-value pair represents an attribute of a student. Here, the keys are 'name', 'age', and 'major', while the corresponding values are 'Alice', 20, and 'Computer Science', respectively. So, the dictionary student is representing the information about a student named Alice, who is 20 years old and majoring in Computer Science.

# Accessing Elements in a Dictionary: Accessing elements in a dictionary is done by using square brackets [] and specifying the key associated with the value you want to retrieve.
# print(student['name'])  # Output: Alice
# print(student['age'])   # Output: 20

# Modifying Elements in a Dictionary: You can modify the value associated with a key in a dictionary by assigning a new value to that key.
# student['age'] = 21
# print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}
# student['age'] = 35
# print(student)
# print(student['age'])

# Adding Elements to a Dictionary: New key-value pairs can be added to a dictionary by assigning a value to a new key.
# student['year'] = 'Senior'
# print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'year': 'Senior'}

# student['student number'] = 200512345
# print(student)

# Removing Elements from a Dictionary: Elements can be removed from a dictionary using the del keyword or the pop() method.
# del student['student number']
# print(student)

# del student['major']
# print(student)  # Output: {'name': 'Alice', 'age': 21, 'year': 'Senior'}

# major = student.pop('year')
# print(student)  # Output: {'name': 'Alice', 'age': 21}
# print(major)    # Output: Senior

# Dictionary Operations:

# Checking if a Key Exists: You can check if a key exists in a dictionary using the in keyword.
# print('love' in student)
# print('name' in student)  # Output: True
# print('grade' in student) # Output: False

# Iterating Over a Dictionary:
# You can iterate over the keys, values, or key-value pairs of a dictionary using loops and dictionary methods.

# for key in student:
#     print(key, ':', student[key])

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

#  When you want to associate more than one value with a key in a dictionary, 
#  you typically use a data structure that can hold multiple values, such as a list, tuple, set, or even another dictionary. 
#  In Python, to define a list, tuple, or set, you use square brackets [], parentheses (), or curly braces {}, respectively.

# For example, if you want to associate multiple courses with a student's name in a dictionary, 
# you can use a list as the value, enclosed in square brackets [], like this:
    
student_courses = {
    'Alice': ['Math', 'Physics', 'Chemistry'],
    'Bob': ['History', 'Literature'],
    'Charlie': ['Computer Science', 'Math', 'Physics']
}

# print(student_courses['Alice'])

# print(student_courses['Bob'])

# print(student_courses['Charlie'][0])

# for student, subjects in student_courses.items():
#     print(f"{student}'s subjects: {', '.join(subjects)}")

# shorter version to print all subjects
# all_subjects = [subject for subjects in student_courses.values() for subject in subjects]
# print(all_subjects)

# Longer and verbose version
# all_subjects = []
# for subjects_list in student_courses.values():
#     for subject in subjects_list:
#         all_subjects.append(subject)
# print(all_subjects)

# More ways to manipulate dictionaries
# for student, subjects in student_courses.items():
#     print(f"{subjects}")

# first_student = next(iter(student_courses.keys()))
# print(first_student)

# In Python dictionaries, elements are not ordered in the same way as in sequences like lists or tuples. 
# Therefore, you cannot access elements using numeric indices like [0], [1], etc. as you would with sequences.
# Dictionaries are implemented using hash tables, which allow for fast lookup of values based on their keys, 
# but they do not preserve the order of insertion of key-value pairs.

# To get the information for the second student in the student_courses dictionary, you can use a combination of slicing and iteration. Here's how you can do it:
# students = list(student_courses.keys())  # Get a list of all student names
# if len(students) > 1:
#     second_student = students[1]  
#     print(second_student)
# else:
#     print("There is no second student.")

# This code snippet first converts the keys of the student_courses dictionary (i.e., the student names) into a list using list(student_courses.keys()). Then, it checks if there are at least two students in the dictionary. If there are, it retrieves the name of the second student from the list of student names using indexing (students[1]). Finally, it prints the name of the second student.

# Keep in mind that dictionaries in Python do not maintain the order of keys by default, so the "second student" may not be deterministic unless you're using Python 3.7 or later where dictionaries maintain the order of insertion. If the order is important, you may want to consider using collections.OrderedDict or sorting the keys before retrieving the second student.

#  More advanced topics and methods related to dictionaries in Python:
# Dictionary Methods:

# **keys(): Returns a view object that displays a list of all the keys in the dictionary.    
# print(student_courses.keys())

# Iterate over keys and print each key
# for key in student_courses.keys():
#     print(key)

# Check if a specific key exists in the dictionary
# print('Alice' in student_courses.keys())

# OR
# if 'Alice' in student_courses.keys():
#     print("Alice exists in the dictionary.")
# else:
#     print("Alice does not exist in the dictionary.")

# Convert keys to a list
# student_courses_list = list(student_courses.keys())
# print(student_courses_list)
# OR
# keys_list = list(student_courses.keys())
# print(keys_list)

# Create a list of uppercase keys (Using Keys in List Comprehension)
# uppercase_keys = [key.upper() for key in student_courses.keys()]
# print(uppercase_keys)
# OR
# for key in uppercase_keys:
#     print(key)

# Count the number of keys in the dictionary
# num_keys = len(student_courses.keys())
# print(num_keys)
# print("Number of keys:", num_keys)


# Sort keys alphabetically and print them
# alpha_keys = sorted(student_courses.keys())
# print(alpha_keys)
# OR
# sorted_keys = sorted(student_courses.keys())
# print("Sorted keys:", sorted_keys)

# Create a new dictionary with default values from keys
# The dict.fromkeys() method is used to create a new dictionary with keys taken from an iterable (such as a list, tuple, or view object) and with each key associated with the same default value.
# default_dict = dict.fromkeys(student_courses.keys(), 'Not enrolled')
# print(default_dict)
# The dict.fromkeys() method is used to create a new dictionary with keys taken from an iterable (such as a list, tuple, or view object) 
# and with each key associated with the same default value.
# Example for format - dict.fromkeys(iterable, value=None)
# iterable: This is the iterable (e.g., list, tuple, or view object) from which the keys will be taken to create the new dictionary.
# value: This is the value that will be associated with each key in the new dictionary. If not provided, the default value is None.
# This method is particularly useful when you want to quickly create a dictionary with default values for each key. In the example you provided:
# the dict.fromkeys() method can actually work with any iterable, not just the keys() 
# my_list = ['a', 'b', 'c']
# new_dict = dict.fromkeys(my_list, 0)
# print(new_dict)
# Output: {'a': 0, 'b': 0, 'c': 0}

# my_tuple = (1, 2, 3)
# new_dict = dict.fromkeys(my_tuple, 'default')
# print(new_dict)
# Output: {1: 'default', 2: 'default', 3: 'default'}

# my_range = range(5)
# new_dict = dict.fromkeys(my_range, 'value')
# print(new_dict)
# Output: {0: 'value', 1: 'value', 2: 'value', 3: 'value', 4: 'value'}

# Example: Using an empty list as the initial value
# keys = ['apple', 'banana', 'cherry']
# result_dict = dict.fromkeys(keys, [])  # Associate an empty list with each key
# print(result_dict)  # Output: {'apple': [], 'banana': [], 'cherry': []}

# # Append elements to the lists
# result_dict['apple'].append(1)
# result_dict['banana'].append(2)
# result_dict['cherry'].append(3)

# print(result_dict)  Output: {'apple': [1, 2, 3], 'banana': [1, 2, 3], 'cherry': [1, 2, 3]}

# While dict.fromkeys() can be useful in certain scenarios, such as when you want to initialize all keys with the same default value, 
# it's not suitable when the default value is mutable and you want each key to have its own separate mutable object.
# In cases where you want each key to have its own separate mutable object (such as an empty list), 
# it's better to use a dictionary comprehension or a loop to explicitly create the dictionary with the desired structure. 
# This ensures that each key gets its own separate mutable object, preventing unintended side effects when modifying the objects later.

# keys = ['apple', 'banana', 'cherry']
# result_dict = {key: [] for key in keys}  # Associate an empty list with each key

# Append elements to the lists
# result_dict['apple'].append(1)
# result_dict['banana'].append(2)
# result_dict['cherry'].append(3)

# print(result_dict) #Output: {'apple': [1], 'banana': [2], 'cherry': [3]}

# There are a few additional aspects worth noting about the keys() method:
# View Object: When you call the keys() method on a dictionary, it returns a view object. 
# This view object provides a dynamic view of the keys in the dictionary, allowing you to observe and interact with them.

# View Object and Iteration:
student_courses = {
    'Alice': ['Math', 'Physics', 'Chemistry'],
    'Bob': ['History', 'Literature'],
    'Charlie': ['Computer Science', 'Math', 'Physics']
}

# Get the view object of keys
keys_view = student_courses.keys()

# Print the view object
print(keys_view)  # Output: dict_keys(['Alice', 'Bob', 'Charlie'])

# Iterate over the keys directly
for key in keys_view:
    print(key)

# Output:
# Alice
# Bob
# Charlie

# Add a new student to the dictionary
student_courses['David'] = ['Biology']

# The change is reflected in the view object
print(keys_view)  # Output: dict_keys(['Alice', 'Bob', 'Charlie', 'David'])
print(student_courses.values())
print(student_courses)

# This code iterates over each key-value pair in the student_courses dictionary using the .items() method.
for key, values in student_courses.items():
    print (f"{key}: {values}")

# Immutable:
# Attempting to add a new key directly through the view object
keys_view.add('Eve')  # This will raise an AttributeError because the view object is immutable












# **values(): Returns a view object that displays a list of all the values in the dictionary.
# physics_present = any('Physics' in subjects for subjects in student_courses.values())
# print(physics_present)


# items(): Returns a view object that displays a list of tuples, where each tuple consists of a key-value pair.
# get(key[, default]): Returns the value associated with the specified key. If the key is not found, it returns the default value (or None if not provided) instead of raising a KeyError.
# pop(key[, default]): Removes the item with the specified key from the dictionary and returns its value. If the key is not found, it returns the default value (or raises a KeyError if not provided).
# popitem(): Removes and returns an arbitrary (key, value) pair from the dictionary. Useful for removing items in LIFO (Last In, First Out) order.
# clear(): Removes all items from the dictionary.
# update(iterable): Updates the dictionary with the key-value pairs from another dictionary or iterable (such as another dictionary, list of tuples, or keyword arguments).
# Dictionary Comprehensions:

# Like list comprehensions, dictionary comprehensions allow you to create dictionaries in a concise and readable way.
# Syntax: {key_expression: value_expression for item in iterable if condition}
# Example:
# python
# Copy code
# squares = {x: x*x for x in range(1, 6)}
# # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Nested Dictionaries:

# Dictionaries can contain other dictionaries as values, allowing for hierarchical or nested data structures.
# Example:
# python
# Copy code
# student_info = {
#     'Alice': {'age': 20, 'major': 'Computer Science'},
#     'Bob': {'age': 22, 'major': 'Mathematics'}
# }
# Dictionary Views:

# Dictionary views provide dynamic and live views of the keys, values, or key-value pairs in a dictionary, allowing you to observe changes made to the dictionary.
# Three types of views: dict.keys(), dict.values(), and dict.items().
# Example:
# python
# Copy code
# student_info = {'Alice': 20, 'Bob': 22, 'Charlie': 21}
# keys_view = student_info.keys()
# values_view = student_info.values()
# items_view = student_info.items()
# OrderedDict:

# collections.OrderedDict is a subclass of dictionary that maintains the order of insertion of keys.
# Useful when you need to preserve the order of keys as they were added.
# Example:
# python
# Copy code
# from collections import OrderedDict
# student_info = OrderedDict([('Alice', 20), ('Bob', 22), ('Charlie', 21)]) 
