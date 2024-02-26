# Creating a list - List consists of mutable sequences
# my_list = [1, 2, 3, 'a', 'b', 'c', 'banana', 'banana']

# Indexing: Accessing elements by index
# print("Element at index 0:", my_list[0]) # Output 1
# print("Element at index 3:", my_list[3]) # Output 2

# print(my_list.index('b'))

# Slicing: Getting a sublist
# print("Sublist from index 2 to 4:", my_list[2:5]) 

# Appending: Adding elements to the end of the list
# my_list.append('d')
# print("After appending 'd':", my_list)

# my_list.append('e')
# print("Testing the new list:", my_list)

# Inserting: The insert() method takes two arguments: the index at which to insert the element and the element itself. 
# my_list.insert(3, 4)
# print(my_list)

# my_list.insert(4, 'z')
# print("The new list:", my_list)

# Removing: removing element by value
# my_list.remove(3)
# print(my_list)

# Deleting by index, we can use the method del or pop()
# del my_list[3]
# print(my_list)

# my_list.pop(4)
# print(my_list)

# Length: Getting the length of the list using len
# print("Length of the list:", len(my_list))

# Iterating: Looping through elements of the list
# print("Elements of the list:")
# for item in my_list:
#     print(item)

# Checking membership or existence in the list
# print("Is 'b' in the list?", 'b' in my_list)
# print('z' in my_list)

# Count(): The count() method returns the number of occurrences of a specified value in the list.
# print(my_list.count('banana'))

# Sort(): The sort() method sorts the elements of the list in ascending order by default. It modifies the original list in place.
# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# my_list.sort()
# print(my_list.sort())

# Reverse(): The reverse() method reverses the elements of the list in place.
# my_list.reverse()
# print(my_list)

# Sort() + reverse=True: To arrange the elements of the list in descending order
# my_list.sort(reverse=True)
# print(my_list)

# List Comprehensions: List comprehensions provide a concise way to create lists. They allow you to generate a new list by applying an expression to each item in an existing iterable. Here's an example:
# squares = [x**2 for x in range(5)]  # Generates a list of squares of numbers from 0 to 4
# print(squares)

# More examples of List Comprehensions, generating lists using existing logical expressions
# even_numbers = [x for x in range(10) if x % 2 == 0]
# print(even_numbers)

# squares_of_even_numbers = [x**2 for x in range(10) if x % 2 == 0]
# print(squares_of_even_numbers)  # Output: [0, 4, 16, 36, 64]

# string = 'hello'
# uppercase_letters = [letter.upper() for letter in string]
# print(uppercase_letters)

# To avoid the commas when transforming the uppercase, you can use this expression
# string = 'hello'
# uppercase_letters = [letter.upper() for letter in string]
# print("".join(uppercase_letters))

# Trying out examples for sentences or multiple words
# string = 'All I want for Christmas is you!'
# uppercase_words = [word.upper() for word in string.split()]
# print(' '.join(uppercase_words))

# phrase = 'Love is all that Matters'
# lowercase_words = [word.lower() for word in phrase.split()]
# print(' '.join(lowercase_words))

# Generating words with specific length, for example words with greater than 5
# sentence = 'My love for you is eternal and powerful for you are my everything'
# words_with_greater_than_6= [word for word in sentence.split() if len(word) > 6]
# print(words_with_greater_than_6)

# List of Tuples - pair of numbers and their square
# numbers = [1, 2, 3, 4, 5]
# numbers_square_tuples = [(x, x**2) for x in numbers]
# print(numbers_square_tuples)

# List of lists: Generating list of lists, for example below
# multipliers = [2, 3, 4]
# multiplied_list = [[multiplier * x for x in range(1, 4)] for multiplier in multipliers]  # range(stop) -> range object range(start, stop[, step]) -> range object
# print(multiplied_list)

# Another example of list of lists. Write a Python program to create a new list containing the lengths of each word in the original list.
# words = ["apple", "banana", "orange", "kiwi", "pear"]
# words_length = [len(word) for word in words]
# print(words_length)

# More problem to solve. Write a Python program to create a new list containing the sums of each inner list in the original list.
# lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# sum_lists = [sum(list) for list in lists]
# print(sum_lists)

# Copying Lists: When working with lists, it's important to understand how to create a copy of a list. You can use slicing (my_list[:]), the list() constructor (list(my_list)), or the copy() method (my_list.copy()) to create a shallow copy of a list.
# words = ["apple", "banana", "orange", "kiwi", "pear"]
# words_copy = words.copy()
# print(words_copy)

# Nested Lists: Lists can contain other lists as elements, allowing you to create nested data structures. This can be useful for representing multi-dimensional data or hierarchical structures.

# List Methods: Lists have several built-in methods beyond the ones mentioned earlier, such as count(), index(), sort(), reverse(), etc. These methods provide additional functionality for manipulating and working with lists.

# List Concatenation and Repetition: You can concatenate two lists using the + operator and repeat a list using the * operator.
# With this example, we combine the numbers as 1 list, not summing them up
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# concatenated_list = list1 + list2
# print(concatenated_list)

# Repetition involves creating a new list by repeating the elements of an existing list a certain number of times. Self-explanatory, one list of multiplied list.
# original_list = [1, 2, 3]
# repeated_list = original_list * 3
# print(repeated_list)

# Mutability: 
# Lists are mutable, meaning that you can modify their elements after creation. 
# This is in contrast to immutable sequence types like tuples and strings, where elements cannot be changed after creation.
# The ability to modify list elements makes them versatile for dynamic data storage and manipulation.

# List Iteration: Experiment with different methods of iterating over lists, including using traditional for loops, list comprehensions, and built-in functions like enumerate() and zip().
# Example using enumerate()
# fruits = ['apple', 'banana', 'coconut', 'durian', 'fig', 'guava']
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}: {fruit}")

# Another variation of the same example, to separate the element from the index, we will not include the index in the print statement
# for index, fruit in enumerate(fruits):
#     print(fruit)

# Advanced List Manipulation:
# Learn about advanced techniques for list manipulation, such as using the zip() function to combine multiple lists, or using list unpacking to assign multiple variables from a single list.
    
# The zip() function in Python is used to combine multiple iterables (such as lists, tuples, or other sequences) into a single iterable of tuples. Each tuple contains the corresponding elements from the input iterables. Here's how zip() works and how you can use it:
    
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# Use zip to combine the lists into tuples
# zipped = zip(list1, list2)

# for item in zipped:
#     print(item)

# Unpack the tuples to separate variables
# for num, letter in zip(list1, list2):
#     print(f"Number: {num}, Letter: {letter}")

# zip() can accept more than two iterables.
# You can also use zip() with other types of iterables, such as tuples or strings.
# zip() is a versatile function that is useful for many scenarios, including combining data from multiple sources, iterating over multiple sequences simultaneously, and more.

# TEST FOR LIST
# Question 1: What are the different ways to create a copy of a list in Python? Explain briefly.
# Question 2: Given a list original_list = [1, 2, 3, 4, 5], demonstrate how you would create a shallow copy of this list using each of the methods you mentioned.

# To make a copy of the list, we can use the copy method, copy()
# original_list = [1, 2, 3, 4, 5]
# copy_list = original_list.copy()
# print(copy_list)

# Question: What is list slicing, and how can it be used to create a copy of a list in Python? Provide an example.
# Slicing is used to access certain elements of the list and creating a sublist. List slicing can also be used to create a copy of the list
# original_list = [1, 2, 3, 4, 5]
# slice_list = original_list[:]
# print(slice_list)

# Copying Lists:
# Explain three different methods to create a copy of a list in Python.
# Using the copy() method:
# my_list = [1, 2, 3, 4, 5]
# copy_list = my_list.copy()
# print(copy_list)

# Using list slicing:
# slice_list = my_list[:]
# print(slice_list)

# Using the list constructor:
# list_copy = list(my_list)
# print(list_copy)

# List Slicing:
# What is list slicing, and how does it work? Provide an example of using list slicing to extract specific elements from a list.
# Slicing is a method to access certain elements inside the list or creating a sublist. We can use this method like this - my_list(2:5)
# my_list = [1, 2, 3, 4, 5, a, b, c]
# slice_list = my_list[3:7]
# print(slice_list)
# The output would be. 4, 5, a, b

# List Concatenation:
# Describe how list concatenation works in Python. Provide an example of concatenating two lists.
# List concatenation in Python works using the + operator, joining two or more lists together. Below is an example.
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c', 'd']
# combined_list = list1 + list2
# print(combined_list)


# List Repetition:
# How can you repeat a list in Python? Provide an example.
# We can use the * operator to make repetitions in Python list. Example below.
# my_list = [1, 2, 3]
# repeat_list = my_list * 4
# print(repeat_list)

# List Methods:
# Name three built-in methods that can be used to manipulate lists in Python. Provide a brief description of each method.
# There are several Python built-in methods and functionalities to manipulate list, there is index() to access elements of the list by index, sorted() to arrange the elements in ascending order, reverse() to arrange the elements in reverse order and more. See the examples below.
# index()
# my_list = ['car', 'truck', 'bike', 'van']
# print(my_list[1]) 

# sorted() or sort() - both method works
# sorted_list = sorted(my_list)
# print(sorted_list)
# my_list.sort()
# print(my_list)

# reverse
# my_list.reverse()
# print(my_list)


# Enumerate Function:
# What does the enumerate() function do in Python? Provide an example of using enumerate() with a list.
# The enumerate() functions enable enumerating the elements of the list and their index numbers. Example below.
# my_list = ['car', 'truck', 'bike', 'van']
# for index, element in enumerate(my_list):
#     print(f"Index {index}: {element}")

# Zip Function:
# Explain the purpose of the zip() function in Python. Provide an example of using zip() with two lists.
# zip() is used to combine multiple lists into list of tuples. The lists are separated by commas inside the ()
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# zipped_list = zip(list1, list2)
# for item in zipped_list:
#     print(item) 

# List Comprehensions:
# Describe what list comprehensions are and how they can be used to create lists in Python. Provide an example of a simple list comprehension.
# List comprehensions are list with common logical expressions and are often use in coding. For example are odd numbers list, even numbers, squared, uppercase letters and more. One example below:
# squared_list = [(x**2) for x in range(10)]
# print(squared_list)


# Nested Lists:
# What are nested lists, and how can they be used in Python? Provide an example of a nested list.
# Nested lists are lists inside of a list. List in Python is flexible and dynamic and it can also holds lists within its list. Example below.
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # Accessing elements within the nested list:
# print(matrix[0][0])  # Output: 1 (accessing the first element of the first inner list)
# print(matrix[1][2])  # Output: 6 (accessing the third element of the second inner list)

# # Modifying elements within the nested list:
# matrix[2][1] = 10
# print(matrix) 

# Mutability of Lists:
# Mutability refers to the ability of a list to be modified after it has been created.
# Example of modifying elements of a list in place:
# my_list = [1, 2, 3, 4, 5]

# # Modifying an element at a specific index:
# my_list[2] = 10
# print(my_list)  # Output: [1, 2, 10, 4, 5]

# # Appending elements to the end of the list:
# my_list.append(6)
# print(my_list)  # Output: [1, 2, 10, 4, 5, 6]

# # Removing an element from the list:
# my_list.remove(4)
# print(my_list)  # Output: [1, 2, 10, 5, 6]

# # Inserting an element at a specific index:
# my_list.insert(2, 7)
# print(my_list)  # Output: [1, 2, 7, 10, 5, 6]

# CS50w NOTES
names = ["Harry", "Ron", "Hermione"]
print(names)

names[1] = "Melissa"
print(names)

names.insert(2, "Mimmo")
print(names)

names.remove("Melissa")
print(names)

names.append("Marco")
print(names)

print(len(names))


