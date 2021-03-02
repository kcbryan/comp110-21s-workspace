"""A bunch of random things while I try to use loops."""

__author__ = "baokaijie"

def main() -> None:
    "Entry point to program"
    name: str = input("What is your name? ")
    wibbly(name)
    return


def wibbly(name: str) -> None:
    """Application of Doctor Who to loops."""
    silence_count: int = 0
    while silence_count < 10:
        question: str = input("Do you see them? yes/no - ")
        if question == "yes":
            silence_count += 1
            print("Go, while you still have time. Silence will fall when the question is answered.")
            chances_remaining: int = 10 - silence_count
            print(f"You have {chances_remaining} chances left. Be careful.")
        else:
            print("Look behind you. Don't forget.")
            leave: str = input("Do you want to forget? yes/no - ")
            if leave == "yes":
                print("Ye who are weak of heart, be careful. Silence will fall.")
                return
            else:
                print("Thank you, faithful companion.")
    print("It is too late now, the time has come. The question is, \"Doctor Who?\"")
    return

if __name__ == "__main__":
    main()

