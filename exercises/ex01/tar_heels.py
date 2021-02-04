"""An exercise in remainders and boolean logic."""

__author__ = "730394055"


# Begin your solution here...


def kevin_g():
    chapel: int = int(input("Enter an int: "))
    tar_test: bool = chapel % 2 == 0
    heels_test: bool = chapel % 7 == 0

    if tar_test and heels_test == True:
        print("TAR HEELS")
    else:
        if tar_test == True:
            print("TAR")
        else:
            if heels_test == True:
                print("HEELS")
            else:
                if (tar_test == False) and (heels_test == False):
                    print("CAROLINA")
    zai_yi_ci: str = input("again? ")
    if zai_yi_ci == "y":
        kevin_g()

kevin_g()
