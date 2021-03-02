"""Lecture examples of list concepts."""

rolls: list[int] # Declare a variable of type "list of integers"

rolls = [2, 3, 2, 6] # Initialize with list literal syntax

print(f"Length of rolls is {len(rolls)}")
print(f"The last value in the list is {rolls[len(rolls) - 1]}")

from random import randint
rolls.append(randint(1, 6)) # List's append method adds to the end of a list
print(rolls)

rolls.pop() # List's pop method, with no arg, removes the last item of a list
rolls.pop(0) # Pop method with one argument removes the item with that index value
print(rolls)

words: list[str] = list() # Construct an empty list using the list constructor
words.append("Hello")
print(words)