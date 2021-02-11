"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730394055"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Generates an integer and pairs it with a fortune."""
    fortune_type: int = randint(1, 4)

    if fortune_type == 1:
        return("Somebody once told me the world is NOT gonna roll you.")
    else:
        if fortune_type == 2:
            return("You ARE the sharpest tool in the shed!")
        else:
            if fortune_type == 3:
                return("Your true love is never gonna give you up, never gonna let you down.")
            else:
                if fortune_type == 4:
                    return("Rick Astley is never gonna run around or hurt you.")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()