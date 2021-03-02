"""test to see if i messed something up by confirming pylance"""

def yeet():
    print("Hello mein freund")

yeet()


def yeehaw() -> str: 
    """A random test"""

def dancing_partner() -> str:
    poss_partners: list[str] = ["Mr. Darcy", "Mr. Bingley", "Mr. Wickham"]
    from random import randint
    your_partner: str = poss_partners[randint(0,2)]
    print(your_partner)

dancing_partner()
