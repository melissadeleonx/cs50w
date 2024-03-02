# Let's test your knowledge on dictionaries, focusing on concepts up to the keys() method. Here are some questions:

# Dictionary Creation: How do you create a dictionary in Python?
# We can create a dictionary in python using curly brackets {} and making unorder list inside them. Each elements include a unique key and their value or set of values, which can be a single element or a sequence of elements like list, tuples,
# For example:
weekly_schedule = {
    'Monday': ['cleaning', 'studying', 'relaxing'],
    'Tuesday': ['a', 'b', 'c'],
    'Wednesday': ['d', 'e', 'f'],
    'Thursday': ['studying', 'relaxing']
}
# We can also use the function dict.fromkeys() to create a new dictionary from a dictionary or list, tuple, etc.

# Accessing Values: How do you access the value associated with a specific key in a dictionary?
# Accessing elements in a dictionary is done by using square brackets [] and specifying the key associated with the value you want to retrieve.
print(weekly_schedule['Monday'])

# Modifying Elements: How can you modify the value associated with a key in a dictionary?
# We can modify the value associated with a key by accessing the key and defining the new values that we want to indicate on that key. This will overwrite the old value of the key with the new one.
weekly_schedule['Tuesday'] = ['relaxing']
print(weekly_schedule['Tuesday'])
print(weekly_schedule)

# Adding Elements: How do you add a new key-value pair to an existing dictionary?
# We can add new elements to the dictionary by introducing a new key and assign its value. You can see example below.
weekly_schedule['Friday'] = ['running', 'sleeping']
print(weekly_schedule)

# Removing Elements: What are two ways to remove a key-value pair from a dictionary?
# We can remove the key value pair or delete one of them by using the methods del or pop()
del (weekly_schedule['Tuesday'])
print(weekly_schedule)

excluded_day = weekly_schedule.pop('Friday')
print(weekly_schedule)
print(excluded_day)

# Checking Key Existence: How do you check if a specific key exists in a dictionary?
# We can check if a key exist by using the 'in' operation
if 'Tuesday' in weekly_schedule:
    print("tuesday exists")
else:
    print("It does not exist!")    
print('Tuesday' in weekly_schedule)


# Iterating Over a Dictionary: What method do you use to iterate over the keys of a dictionary?
# We can use the for loop to iterate the keys of the dictionary.
for key in weekly_schedule:
    print(key)