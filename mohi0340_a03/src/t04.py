"""
-------------------------------------------------------
[Assignment 3 Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import array_to_stack

source1 = Stack()

array_to_stack(source1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

source1.reverse()

while not source1.is_empty():
    list = source1.pop()
    print(list)
