"""
-------------------------------------------------------
[Lab 6 Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-27"
-------------------------------------------------------
"""

from Food_utilities import read_foods
from List_linked import List


file_variable = open("foods.txt", "rt")

foods = read_foods(file_variable)


new_list = List()

for value in foods:
    new_list.append(value)

print("-----Find: ")
print(new_list.find(foods[2]))
print()
print("-----Index: ")
print(new_list.index(foods[2]))
print()
print("-----Find In:")
print(foods[2] in new_list)

file_variable.close()
