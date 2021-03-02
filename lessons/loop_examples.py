"""Lecture examples for learning loops."""

count: int = 0
while input("Do you need more love? yes/no - ") == "yes":
    #Body block of the while  loops is evaluated
    #when the test expression is true
    print("I love you!")
    count += 1
    print(f"Count is {count}.")
    if count > 3:
        print("Wow, I realllly, trulllyyyy love you.")

# Iterating a specific number of times
i: int = 0 # i is typically short for index
iterations: int = 1000000
while i < iterations: # keeep in mind that once i == 10 it would acutall y be the 11th iteration
    if i % 1000 == 0:
        print(f"I love you! i: {i}")
    i += 1 # Important that this increment is NOT in the if statement

print("Have a lovely day.")