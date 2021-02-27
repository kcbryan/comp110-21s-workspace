"""To be filled in greater detail here. A coded adventure"""

__author__ = "730394055"

player: str = "Miss Bennet"
points: int 
e_wink: str = "\U0001F609"
e_flowers: str = "\U0001F490" # this is a flower bouquet
e_gratitude: str = "\U0001F60A"
e_music: str = "\U0001F3B6"
e_sparkle: str = "\U00002728"
e_pensive: str = "\U0001F614"

def main() -> None:
    """Opening point for this program."""
    global points
    points = 1000
    greet()
    play_game: str = input(f" \n Do you wish to continue engaging with this literary adventure, {player}? yes/no - ")
    while play_game == "yes":
        print(f"Let us commence our plot, {player}! {e_flowers}")
        print("\n To whence shall we first embark? Please enter a, b, or c")
        choice: str = input("a- Ball at Netherfield Park \t b- Dinner at Longbourn \t c- Shopping in Meryton ? ")
        print(f"As a reminder, your current annuity is £{points}. Good luck!")
        if choice == "a":
            points = netherfield(points)
            choice = "Netherfield"
        if choice == "b":
            longbourn()
            choice = "Longbourn"
        if choice == "c":
            meryton()
            choice = "Meryton"
        play_game = input(f"We hope you enjoyed your time at {choice}. Do you wish to continue playing? yes/no - ")
    print(f"We are sorry to see you disembark, {player}.")
    if points < 1000:
        print(f"Unfortunately, {player}, your actions have diminished your annuity to £{points}.")
    if points == 1000:
        print(f"You shall leave this game with an annuity of £{points}.")
    else:
        print(f"You have acted most valiantly, {player}, and increased your annuity to £{points}!")
    print(f"We hope our game has bewitched you, body and soul. {e_wink} Farewell, {player}, and have a nice day!")
    return
   

def greet() -> None:
    """Introduction to game, collects player name and starts point count."""
    welcome_message()
    global player
    player = input("What is your name, dear player? ")
    return 


def welcome_message() -> None:
    """Contains series of printed statements for game intro to conserve space in greet function."""
    print("\"It is a truth universally acknowledged...\" that anything is more fun when you add some Jane Austen! \n")
    print("Welcome to \"Pride and Prejudice\": COMP 110 Edition! In this game you will have the opportunity to engage in sisterly affection and ")
    print("dance with the elegant ton, while making sure to avoid the sinister influences of wealth-seeking suitors and overbearing mamas!")
    print(f"You have been given a starting annuity of £{points}. Engaging with friends will increase your annuity, where as falling for less genial")
    print("counterparts will result in the theft of your precious inheritance!")
    return

    
def netherfield(points_n: int) -> int:
    """Engage with friends and dance, earning or losing points based on dance partner."""
    e_dance_woman: str = "\U0001F483" #dancing woman emoji
    e_dance_man: str = "\U0001F57A" # dancing man emoji
    global e_gratitude
    global e_music
    global e_sparkle
    print(f"Welcome to Netherfield Park, {player}! Music swells around the happy assemblage, with a number of your friends already engaged in the revel.")
    points_n += 100
    print(f"Mr. Bennet was so pleased that you have decided to go to the ball! He has increased your annuity as a result.")
    dance_or_talk: str = input("Should you like to dance, or take a moment to converse with dear Miss Lucas? dance/talk - ")
    if dance_or_talk == "talk":
        points_n -= 50
        print("You enjoy such humorous and engaging conversation with Miss Charlotte Lucas, that you completely forget the time!")
        print("Alas, Mrs. Bennet is displeased you did not take time to dance with eligible suitors, and has deducted some of your annuity.")
        print(f"However, do not let her get your spirits down, {player}. Sincere friendship is of infinite value, beyond any annuity. {e_gratitude}")
        return points_n 
    else:
        print("The string quartet crescendos, and the opening notes of your favorite song flit through the air as you reach the center of the crowd.")
        i: int = 0 # thinking maybe have a total of three chances to find a dance partner
        assent: str = dancing_partner()
        while assent == "n" and i < 3:
            points_n -= 50
            print(f"Mrs. Bennet is displeased to see you being so discourteous, and has deducted from your annuity! {e_pensive}")
            assent = dancing_partner()
            i += 1 
        print("You happily offer your hand, and are swept onto the dance floor!")
        print(f"\t {e_sparkle} \t {e_music} \t {e_dance_man} \t {e_sparkle} \t {e_dance_woman} \t {e_music} \t {e_sparkle}")
        points_n += 150
        print("After a wonderful night of dancing, you happily return home.")
        print("As an added bonus, Mrs. Bennet was so thrilled to see you on the dance floor that she has increased your annuity!")
        return points_n 

            
def dancing_partner() -> str:
    """Randomly generates a dance partner for the player to accept or reject."""
    poss_partners: list[str] = ["Mr. Darcy", "Mr. Bingley", "Mr. Wickham", "Miss Bingley", "Mr. Collins", "Miss King"] 
    from random import randint
    your_partner: str = poss_partners[randint(0,5)]
    assent: str = input(f"{your_partner} approaches you and asks you to dance. Do you offer them your hand? y/n - ")
    return assent 


def longbourn() -> None:
    """Gain/lose points while interacting with marriage proposal from Mr. Collins."""
    global points #allows for global reassignment of points value to comply with rubric
    # welcome_message to Longbourn estate
    # annouce arrival for mr collins
    # choice about what to have for dinner
    # small if/then interaction about boiled potatoes, changing point values accordingly
    # print statement about mr collins requests private audience, family leaves before you can object
    # proposal line


if __name__ == "__main__":
    main()
