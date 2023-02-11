# --- Default Values ---
# Function Argument with Default Values
# In Python, we can provide default values to function arguments.
# We use the "=" operator to provide default values.
# For example:

# def print_prof_name(name:str="Abel Murgas") -> None:
#     """Method to print the name of the profesor

#     Args:
#         name (str, optional): prof's name. Defaults to "Abel Murgas".
#     """
#     print(name)

# --- Keyword Argument ---
# In keyword arguments, arguments are assigned based on the name of arguments.
# For example:

# def get_complete_name(first_name, last_name):
#     return first_name + " " + last_name
# name = "Abel"
# last_name = "Murgas"
# print(get_complete_name(last_name, name)) # order is important
# print(get_complete_name(last_name=last_name, first_name=name)) # With Keywor fix this

# --- args ---
# Sometimes, we do not know in advance the number of arguments that will be passed into a function.
# o handle this kind of situation, we can use arbitrary arguments in Python.

# def get_my_friends(*friend: str) -> str:
#     friends = ""
#     for i in friend:
#         friends += i + " "
#     return friends


# print(get_my_friends("Mayra", "Dayron", "Isabel"))
