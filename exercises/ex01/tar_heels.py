"""An exercise in remainders and boolean logic."""

__author__ = "730394055"


# Begin your solution here...
chapel: int = int(input("Enter an int: "))
tar_test: bool = chapel % 2 == 0
heels_test: bool = chapel % 7 == 0
if tar_test and heels_test is True:
    print("TAR HEELS")
else:
    if tar_test is True:
        print("TAR")
    else:
        if heels_test is True:
            print("HEELS")
        else:
            if (tar_test is False) and (heels_test is False):
                print("CAROLINA")