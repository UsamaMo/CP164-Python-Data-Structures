"""
-------------------------------------------------------
[Assignment 9 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-26"
-------------------------------------------------------
"""

from Hash_Set_BST import Hash_Set
from functions import insert_words, comparison_total

hsh = Hash_Set(10)

file = open('otoos610.txt', 'rt')

insert_words(file, hsh)


total, max_value = comparison_total(hsh)

print("Using linked BST Hash_Set")
print()
print(f"Comparisons Total Count: {total:,}")
print(
    f"Word with Most Comparisons '{max_value.word}': {max_value.comparisons:,}")

file.close()
