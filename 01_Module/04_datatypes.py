""" 
Data Types	  Classes
Numeric	     int, float
String	      str	
Sequence	    list, tuple, range	
Mapping	     dict
Boolean	     bool
Set          set, frozeenset
"""

# --- Numeric Data type ---

# --- Int ---
# num1 = 5
# print(num1, 'is of type', type(num1)) 
# NOTE: Type() is a method to get the type of the object

# --- float ---
# num2 = 2.0
# print(num2, 'is of type', type(num2))

# --- complex ---
# num3 = 1+2j
# print(num3, 'is of type', type(num3))

# --- String Data type ---
# String is a sequence of characters represented by either single
# or double quotes.
# name = "Roberto"
# print(name, 'is of type', type(name))
# print(name[0]) # NOTE: You can access a position in iterable variable by placing the index of the letter enclosing it in bracket

# --- Sequence Data Type ---

# --- List ---
# List is an ordered collection of similar or different types of items
# separated by commas and enclosed within brackets [ ].
# object_oriented_languages = ["Dart", "Java", "Python"]

# access element at index 0
# print(object_oriented_languages[0])

# access element at index 2
# print(object_oriented_languages[2])

# --- Tuple ---
# Tuple is an ordered sequence of items same as a list. 

# -- Diference between list a tuple --
# Immutability: Lists are mutable, meaning you can add, remove, and modify items in a list.
#  Tuples are immutable, meaning once you create a tuple, you cannot change its contents.

# Syntax: Lists are declared using square brackets [],
# while tuples are declared using parentheses ().

# Performance: Since tuples are immutable, they are faster than lists in some cases,
# such as when iterating through the items or checking if an item is in the collection.

# Use cases: Tuples are often used for collections of related items where the order is important
# and the items should not be changed, such as a point in a 3D space with x, y, and z coordinates. 
# Lists are more commonly used for collections of items that need to be changed, such as a list of tasks to do.
# create a tuple 
#product = ('Microsoft', 'Xbox', 499.99)

# access element at index 0
#print(product[0])   # Microsoft

# access element at index 1
#print(product[1])   # Xbox

# --- Set Data Type ---
# A set in Python is an unordered collection of unique elements. 
# It is defined using curly braces {} or the set() function.

# Sets are commonly used when you need to store multiple items in a collection, 
# but don't care about the order, and don't want duplicates.

# Example:

# create a set named student_id
# student_id = {112, 114, 116, 118, 115, 0}

# display student_id elements
# print(student_id)

# display type of student_id
# print(type(student_id))

# --- Dictionary Data Type ---
# Python dictionary is an ordered collection of items. 
# It stores elements in key/value pairs.

# create a dictionary named python_course
# python_course = {'profesor': 'Black Python', 'students': {'men': ["sterben", "rolando"], 'women': ["Mayra", "Silvina"]}}

# print(python_course["students"]["men"][0])
# print(type(python_course))