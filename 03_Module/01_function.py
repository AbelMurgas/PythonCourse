# A function is a block of code that performs a specific task.
# The syntax to declare a function is:

# def function_name(arguments):
#     # function body 
#     return

# def - keyword used to declare a function
# function_name - any name given to the function
# arguments - any value passed to function
# return (optional) - returns value from a function
#Let's see an example:

# def print_hello_world():
#     print("Hello World")
# print_hello_world() # Calling the function
# method named always in snake case (Not use capital letter )

# --- Function Arguments ---
# def sum(number1, number2):  # the arguments order is important 
#     return number1 + number2 # return the sum of the two numbers

# print(sum(3,5))

# --- Good Practice ---
# def sum(number1:int, number2:int): # the data type of the parameters has been specified
#     return number1 + number2

# print(sum(3,3)) 

# --- void function ---
# Void function is a method that no return data

# def sum(number1:int, number2:int):
#     print(number1, number2)

# sum(2,3) # not need to use print method, because inside of the function we use it

# --- Good Practice ---
# def sum(number1:int, number2:int) -> None: # the data type of the returns has been specified
#     print(number1 + number2)

# --- DocString ---
# def sum(number1:int, number2:int) -> None: 
#     """ 
#     ## This is a docstring, here we talk abut the function (or classes)

#     Args:
#         number1 (int): first number
#         number2 (int): second number
#     """
#     print(number1 + number2)

# sum(100,2)