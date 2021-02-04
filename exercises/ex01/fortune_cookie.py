"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730394055"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune_type: int = randint(1,4)

if fortune_type == 1:
    print("Somebody once told me the world is NOT gonna roll you.")
else:
    if fortune_type == 2:
        print("You ARE the sharpest tool in the shed!")
    else:
        if fortune_type == 3:
            print("Your true love is never gonna give you up, never gonna let you down.")
        else:
            if fortune_type == 4:
                print("Rick Astley is never gonna run around or hurt you.")

print("Now, go spread positive vibes!")