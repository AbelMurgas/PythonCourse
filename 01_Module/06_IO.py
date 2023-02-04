# In Python, we can simply use the print() function to print output. For example,
# print("I \u2764  Python ")

# Print (only with one parameter) finish with '\n'
# Example:
# print("Hello World")
# print("Goodbye Wolrd")

# to change this, need to define "end" parameter
# print("Hello World", end=",")
# print("Goodbye World")

# to separate strings need to define the "sep" parameter
# print("Hello World", "Goodbye World", sep=",")

# to concatenate Strings need to put "+"
# print("Hello World" + "Goodbye world")

# --- Output formatting ---
# x = 12
# y = 1
# print("The value of x is {} and y is {} sum: {}".format(x,y,x+y))
# print(f"The value of x is {x} and y is {y} sum: {x+y}")

# --- Input in Python
# using input() to take user input
# num = input('Enter a number: ')

# print('You Entered:', num)

# print('Data type of num:', type(num))

# In the above example, we have used the input() function 
# to take input from the user and stored the user input in the num variable.
# It is important to note that the entered value is a string, not a number. So, type(num) returns <class 'str'>.
# To convert user input into a number we can use int() or float() functions as:

# num = int(input("Enter a number: "))

# print('You Entered:', num)

# print('Data type of num:', type(num))

