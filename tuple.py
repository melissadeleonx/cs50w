# A tuple is an ordered collection of items, just like lists.
# The main difference is that tuples are immutable, meaning once they are created, their elements cannot be changed, added, or removed.


# 1. Creating Tuples:

# Tuples are created by enclosing comma-separated values within parentheses ().
# Even if you have a single value, you still need to include a comma to create a tuple: (value,).

# my_tuple = (1, 2, 3, 4, 5)     
# empty_tuple = ()
# single_value_tuple = (42,)  # note the comma
# print(my_tuple)
# print(single_value_tuple)

# Tuples can indeed contain any number of elements, making them quite flexible for storing ordered collections of data.

# my_tuple = (1, 2, 3)
# print(my_tuple)  # Output: (1, 2, 3)

# nested_tuple = (1, (2, 3), 4)
# print(nested_tuple)  # Output: (1, (2, 3), 4)

# mixed_tuple = (1, "hello", 3.14, True)
# print(mixed_tuple)  # Output: (1, 'hello', 3.14, True)

# Simplified example of a book cataloging application using Python tuple
# Each book represented as a tuple: (title, author, publication_year, isbn)
# book1 = ("To Kill a Mockingbird", "Harper Lee", 1960, "978-0061120084")
# book2 = ("1984", "George Orwell", 1949, "978-0451524935")
# book3 = ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-0743273565")

# List of books
# book_catalog = [book1, book2, book3]

# Function to display book information
# def display_book_info(book):
#     title, author, publication_year, isbn = book
#     print(f"Title: {title}")
#     print(f"Author: {author}")
#     print(f"Publication Year: {publication_year}")
#     print(f"ISBN: {isbn}")
#     print() 

# Display information for each book in the catalog
# for book in book_catalog:
#     display_book_info(book)

# The print() statement without any arguments is used to print a blank line, effectively creating a space between the information displayed for each book.

# Tuples in Python are often used to represent collections of related data where each element in the tuple corresponds to a specific piece of information. The order of elements in a tuple is typically meaningful, as it defines the structure of the data.

# While tuples themselves are immutable, meaning you cannot change their elements after creation, there are still some operations you can perform on tuples and with tuples to achieve certain manipulations or transformations. Here are some techniques commonly used with tuples:

# Concatenation: You can concatenate two or more tuples together to create a new tuple.
# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')
# concatenated_tuple = tuple1 + tuple2
# print(concatenated_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

# Repetition: You can repeat a tuple by multiplying it with an integer.
# tuple1 = (1, 2)
# repeated_tuple = tuple1 * 3
# print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

# Slicing: You can slice tuples to create new tuples containing subsets of the original elements.
# my_tuple = (1, 2, 3, 4, 5)
# sliced_tuple = my_tuple[1:4]
# print(sliced_tuple)  # Output: (2, 3, 4)

# book1 = ("To Kill a Mockingbird", "Harper Lee", 1960, "978-0061120084")
# basic_book_info = book1[0:2]
# print(basic_book_info)

# Here's another example of slicing a tuple to access non-consecutive elements:
# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Using a Positive Step:
# selected_elements = my_tuple[1:8:2]

# Using a Negative Step:
# selected_elements = my_tuple[8:1:-2]

# Omitting Start and Stop:
# selected_elements = my_tuple[::3]

# Unpacking: You can unpack a tuple into individual variables, which can be useful for assigning values or passing arguments to functions.
# my_tuple = (1, 2, 3)
# a, b, c = my_tuple
# print(a, b, c)  # Output: 1 2 3

# Conversion: You can convert a tuple into a list, perform operations on the list, and then convert it back to a tuple if needed.
# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)
# my_list.append(4)
# modified_tuple = tuple(my_list)
# print(modified_tuple)  # Output: (1, 2, 3, 4)

# book1 = ("To Kill a Mockingbird", "Harper Lee", 1960, "978-0061120084")
# book1_list = list(book1)
# book1_list.append('Scottsboro Boys')
# book1_modified = tuple(book1_list)
# print(book1_modified)
#  You can reuse the old tuple name, and it will be replaced with the new tuple after the reassignment.





# In Python, tuples can indeed be of arbitrary length, including sizes of 100 or more elements. Tuples are commonly used to represent fixed collections of data where the number of elements is known and consistent.

# While it's true that handling very large tuples can become cumbersome in terms of readability and manageability, there are situations where using large tuples might be appropriate:

# Data Structures: Tuples are sometimes used to represent fixed-size data structures where each element has a specific meaning or role. For example, a tuple might represent a point in 3D space (x, y, z), where each element corresponds to a coordinate.

# Return Values: Functions may return tuples with many elements to convey multiple pieces of information. For instance, a function might return various statistics or results bundled together in a tuple.

# Configuration Parameters: Tuples can be used to store configuration parameters or settings for a program, where each element represents a different aspect of the configuration.

# While tuples are certainly flexible in terms of size, it's essential to consider readability and maintainability when working with large tuples. In some cases, it might be more appropriate to use other data structures like lists or dictionaries, especially if the size of the data structure could change or if you need to perform operations like appending or removing elements.

# TEST ABOUT TUPLE
# What is a tuple in Python, and how does it differ from a list?
# Tuples are immutable data structures in Python.
# They are often used to store related pieces of data together.
# Tuples are created using parentheses () or the tuple() constructor.
# Unlike lists, tuples cannot be modified after creation, but you can create a new tuple with modified elements.
# The order of elements in a tuple is significant and often carries meaning.

# Can you provide an example of how you would create a tuple in Python?
# Ofcourse, tuples are created using ( ). 
# Here are examples of tuples, 
# simple_tuple = (1, 2, 3, 4, 5) 
# mixed_tuple = (1, 'give equation', 3.14, 'pi') 
# nested_tuple = ((1, 2, 3), (4, 5, 6)) 
# single_tuple = (1, )
# empty_tuple = tuple()
# Using tuple constructor
# tuple1 = (1, 2, 3)
# tuple2 = (7, ) + tuple(tuple1)
# print(tuple2)
# Accessing index
# tuple1 = (1, 2, 3)
# tuple2 = (7, tuple1[1]) + tuple1[2:] 
# print(tuple2)

# What are some advantages of using tuples over lists in Python?
# For small data, tuples are efficient and faster esp. with memory allocation. Tuples are also more significant for elements that are related
# to each other. Although for larger data, an SQL database is more advisable for scalability.
# Here are a few more advantages of using tuples over lists:
# Immutable Nature: Tuples are immutable, meaning their elements cannot be changed after creation. This immutability guarantees data integrity and prevents accidental modifications, making tuples suitable for storing constant values or configurations.
# Hashability: Tuples are hashable, which means they can be used as keys in dictionaries and elements in sets. This property makes tuples useful for data structures that require hashable objects.
# Performance: Due to their immutability, tuples are generally faster to iterate over compared to lists. Additionally, accessing elements in tuples is slightly faster than accessing elements in lists.
# Safety in Data Integrity: Because tuples are immutable, they are safer to pass around in programs where data integrity is crucial. Since their contents cannot be changed accidentally, there's less risk of unintended side effects.
# Unpacking: Tuples support unpacking, allowing multiple values to be assigned or returned from functions simultaneously. This feature can lead to cleaner and more concise code in certain situations.

# How do you access elements in a tuple?
# I already answered 1 and 2, we can access tuple by indexing or slicing. Example below
# tuple1 = (1, 2, 3, 4, 5)
# print(tuple1[3])
# Output: 4
# print(tuple1[2:4])
# Output: (3, 4)

# What does it mean for tuples to be immutable? Why is immutability important?
# Tuples are immutable, meaning once created, it cannot be changed or modified easily which adds integrity to the data. It is important for
# safety of the data where accidental removal or changes can be avoided. Tuple also has hashability which is great for keys used in dictionaries.
# It makes the data storage more reliable and secure.
# Data Integrity: Immutable objects like tuples guarantee that their contents remain unchanged throughout the program execution. This property is essential for maintaining data integrity, especially in scenarios where data consistency is critical.
# Hashability: Tuples are hashable because of their immutability. This property makes tuples suitable for use as keys in dictionaries and elements in sets. Immutable objects can be hashed once and used as identifiers in various data structures without the risk of unexpected behavior.
# Thread Safety: In multi-threaded applications, immutable objects like tuples are inherently thread-safe. Since their contents cannot be modified, there's no risk of data corruption due to concurrent access from multiple threads.
# Performance: Immutable objects often provide better performance characteristics in certain scenarios. For example, the immutability of tuples allows Python to optimize memory allocation and reduce overhead associated with memory management.
# Concurrency and Parallelism: Immutability simplifies concurrent and parallel programming by eliminating the need for synchronization mechanisms to protect shared mutable state. Immutable data structures can be safely accessed and manipulated by multiple threads or processes without the risk of race conditions.

# Explain the concept of tuple unpacking and provide an example.
# Unpacking in tuple is used for functions returning multiple values. Here is an example.
# tuple1 = (1, 2, 3)
# x, y, z = tuple1
# print(x, y, z)
# Output: 1, 2, 3
# Tuple unpacking is a feature in Python that allows you to assign the elements of a tuple to multiple variables in a single statement. This can be particularly useful when working with functions that return multiple values or when iterating over tuples containing multiple elements.
# In your example, you've unpacked the tuple tuple1 into three variables x, y, and z, respectively. Each variable is assigned the value of the corresponding element in the tuple. This concise syntax simplifies the assignment of multiple variables in one line of code.
# Tuple unpacking provides a clean and intuitive way to handle multiple values returned from functions or to destructure tuples into individual components, enhancing readability and reducing code verbosity.

# How can you concatenate or combine two tuples?
# You can concatenate tuples using the + operator: Here is an example.
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# combined_tuple = tuple1 + tuple2
# Output: (1, 2, 3, 4, 5, 6)
# Additional notes: Concatenating tuples involves combining the elements of two or more tuples to create a new tuple. In Python, you can use the + operator to concatenate tuples. When you use the + operator between two tuples, Python creates a new tuple containing all the elements from the operands.
# You can also use the repetition operator *
# tuple1 = (1, 2, 3)
# repeated_tuple = tuple1 * 3
# print(repeated_tuple)
# # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
# You can create a shallow copy of a tuple
# tuple1 = (1, 2, 3)
# tuple_copy = tuple1[:]
# # Or using tuple constructor
# tuple_copy = tuple(tuple1)


# What is the difference between a tuple and a named tuple in Python?
# Tuple: A tuple is an immutable sequence of elements in Python. It's a simple data structure where elements are accessed by their index. Tuples are typically used to group together related pieces of data.
# simple_tuple = (1, 2, 3)
# A named tuple is a subclass of tuple provided by the collections module in Python. It allows you to create tuple-like objects with named fields, making your code more readable and self-documenting. Named tuples are useful when you want to represent simple classes without the overhead of defining a full class.# For example

# from collections import namedtuple

# Define a named tuple called 'Book' with fields 'title' and 'author'
# Book = namedtuple('Book', ['title', 'author'])

# Create instances of the named tuple 'Book'
# book1 = Book(title='Python', author='Anonymous')
# book2 = Book(title='Love', author='Cupid')

# print(book1)  # Output: Book(title='Python', author='Anonymous')
# print(book2)  # Output: Book(title='Love', author='Cupid')

# Another example
# from collections import namedtuple

# Car = namedtuple('Car', ['model', 'brand'])

# car1 = Car(model='XJR', brand='yamaha')
# car2 = Car(model='GX', brand='toyota')

# print(car1)
# print(car2)

# How can you convert a tuple into a list, and vice versa?
# You can convert a tuple to a list using list constructor and from list to tuple using tuple constructor.
tuple1 = (1, 2, 3, 4, 5)
tuple_list = list(tuple1)
new_tuple = tuple(tuple_list)
print(tuple_list)
print(new_tuple)


# Can you explain when it might be appropriate to use a tuple instead of a list in a Python program?
# For data or elements related to each other and have specific meanings in their order are more suitable as tuples. When the data needs
# to be more secure and immutable, a tuple is more appropriate.








