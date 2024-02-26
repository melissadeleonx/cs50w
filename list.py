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
