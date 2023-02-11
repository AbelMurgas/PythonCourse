"""
--- 
Data Format Problem
A company has a system that obtains all the information from its customers, it has a method to collect the data obtaining this format:
"Abel Murgas 25" Name last name Age, and the company want to change the format supported by the Database.
...

Important things:
1. Some customers have a middle name and maternal last name: "Abel Jazir Murgas Tapia 25"
2. Some customers write their first or last name in lower case: "abel jazir Murgas tapia 25"
3. Some clients do not put their age: "Abel Jazir Murgas Tapia"

The expected result:
The method must be able to change this format:
"
abel murgas tapia 25
Carmen Ortega 30
july ruiz
roberto lopez
Marta Campos" (str)
to:
[
    [1,Abel,Murgas,Tapia,25],
    [2, Carmen, Ortega, 30],
    [3, Julio, Ruiz, None],
    [4, Roberto, Lopez, None],
    [5,Marta, Campos, None]
] (list)

Validation:
1- Names and lastname must begin with a capital letter
2- If the client has no age, you must put None in the last position of the list
3- Each client must have a unique code
4- The client renders a vector inside the main list

¡Good luck!
Data example (use to test):
"""
clients = """Abel Murgas Tapia 25
Raul ortega martinez 10
paul Walker
martin Ruiz 100
carlos juan martinez castillo"""

result_expected = [
    ["Abel","Murgas","Tapia",25],
    ["Raul","Ortega","Martinez",10],
    ["Paul","Walker",None],
    ["Martin","Ruiz",100],
    ["Carlos","Juan","Martinez","Castillo", None]
]




