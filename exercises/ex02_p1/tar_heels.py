"""Tar Heels exercise redux as a structured program."""

__author__ = "730394055"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(response: int) -> str:
    """Returns a UNC-themed string based on the divisibility of an inputted integer."""
    chapel: int = response
    tar_test: bool = chapel % 2 == 0
    heels_test: bool = chapel % 7 == 0
    if tar_test and heels_test is True:
        return("TAR HEELS")
    else:
        if tar_test is True:
            return("TAR")
        else:
            if heels_test is True:
                return("HEELS")
            else:
                if (tar_test is False) and (heels_test is False):
                    return("CAROLINA")


if __name__ == "__main__":
    main()
