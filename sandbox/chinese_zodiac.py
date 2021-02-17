"""A program for approximating your Chinese zodiac animal."""

__author__ = "baokaijie"

def main() -> None:
    """Entry point for the module."""
    print("欢迎你来到我的电脑程序/Welcome to my computer program!")
    lang: str = input("Would you like to interact with this module in Chinese or English/用这个程序的时候，您想用普通话还是英语？")
    if lang == "English":
        animal: str = zodiac_matcher(en_yearfinder())
        print("Congrats, your zodiac animal is the " + animal + "!")
    else:
        animal : str = zh_zodiac_converter(zodiac_matcher(zh_yearfinder()))
        print("恭喜你，你的生肖是" + animal + "!")

        
    #birth_year: int = int(input("你几年出生了?/What is your birth year? "))
    #zodiac_animal: str = zodiac_matcher(birth_year)
    #if zodiac_animal == "对不起，这个程序还没写完/I'm sorry, this program is not complete yet":
    #    print(zodiac_animal)
    #else:
    #    print("恭喜你，你的生肖是" + zodiac_animal + " eht si caidoz esenihC ruoy ,stargnoC")

def zh_yearfinder() -> int:
    """Using Chinese interface, returns the birth year of user."""
    birth_year: int = int(input("你几年出生了? "))
    return birth_year


def en_yearfinder() -> int:
    """Using English interface, returns the birth year of user."""
    birth_year: int = int(input("What is your birth year? "))
    return birth_year


def zodiac_matcher(birth_year: int) -> str:
    """Matches input birth year to a specific english-language zodiac animal."""
    year: int = birth_year
    if year == 2020 or year == 2008:
        return("rat")
#yo make sure you fix the or lists cause they don't work, until tuple knowledge is acquired 
#please use the model of the if statement for the rat block
    else:
        if year == (2021 or 2009 or 1997 or 1985 or 1973 or 1961 or 1949):
            return("ox")
        else:
            if year == (2022 or 2010 or 1998 or 1986 or 1974 or 1962 or 1950):
                return("tiger")
            else:
                if year == (2023 or 2011 or 1999 or 1987 or 1975 or 1963 or 1951):
                    return("rabbit")
                else:
                    return("对不起，这个程序还没写完/I'm sorry, this program is not complete yet")


def zh_zodiac_converter(shengxiao: str) -> str:
    """Translates English name of zodiac animal into Chinese for user."""
    if shengxiao == "rat":
        return("鼠")
    if shengxiao == "ox":
        return("牛")
    if shengxiao == "tiger":
        return("虎")
    if shengxiao == "rabbit":
        return("兔")
    if shengxiao == "dragon":
        return("龙")
    if shengxiao == "snake":
        return("蛇")
    if shengxiao == "horse":
        return("马")
    if shengxiao == "goat":
        return("羊")
    if shengxiao == "monkey":
        return("猴")
    if shengxiao == "rooster":
        return("鸡")
    if shengxiao == "dog":
        return("狗")
    if shengxiao == "pig":
        return("猪")


if __name__ == "__main__":
    main()