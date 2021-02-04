"""daodi still trying to get those if/else statements down"""

print("Welcome to the Comparinator-3000! (Doofenshmirtz Patent Pending)")

name: str = input("What is your name? ")

def comparinator_3000():
    a_txt: str = input("Please enter a number (variable a): ")
    b_txt: str = input("Please enter a second number (variable b): ")

    a: int = int(a_txt)
    b: int = int(b_txt)

    if b > a:
        print("Doofenshmirtz says... b is greater than a!")
    elif b == a:
        print("Doofenshmirtz says... b and a are of equal value!")
    else:
        print("Doofenshmirtz says... b is less than a!")

def try_again():
    zai_yi_ci: str = input("Would you like to compare another set of numbers (y/n)? ")

    if zai_yi_ci == "y":
        complete()
    elif zai_yi_ci == "n":
        print("Thank you for choosing Comparinator-3000 for your number needs, " + name + "! Have a great day!")
    else:
        print("I'm sorry, " + name + ", your command is not recognized. Please try again!")
        try_again()

def complete():
    comparinator_3000()
    try_again()

complete()