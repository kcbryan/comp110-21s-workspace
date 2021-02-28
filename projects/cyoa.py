"""An interactive game incorporating aspects from the movie and novel versions of Jane Austen's Pride and Prejudice.

For the first above and beyond criterion, I have created a while loop in the main function based on the variable 
'play_game' that allows the player to rechoose any location or leave the game. For the second above and beyond
criterion, I have included a fourth option called 'Meryton', in addition to the Netherfield option, Longbourn
option, and leave game option.
"""

__author__ = "730394055"

player: str 
points: int 
e_wink: str = "\U0001F609"
e_flowers: str = "\U0001F490" 
e_gratitude: str = "\U0001F60A"
e_music: str = "\U0001F3B6"
e_sparkle: str = "\U00002728"
e_pensive: str = "\U0001F614"
e_fearful: str = "\U0001F628"
e_ribbon: str = "\U0001F380"
e_dance_woman: str = "\U0001F483"
e_dance_man: str = "\U0001F57A"


def main() -> None:
    """Opening point for this program."""
    greet()
    global points
    points = 1000
    exposition()
    play_game: str = input(f"\nDo you wish to continue engaging with this literary adventure, {player}? yes/no - ")
    while play_game == "yes":
        print(f"\nLet us commence, {player}! {e_flowers}")
        print("To whence shall we embark? Please enter a, b, c, or d")
        choice: str = input("a-Ball at Netherfield\tb-Dinner at Longbourn\tc-Shopping in Meryton\td-Leave Game ? ")
        if choice == "a":
            points = netherfield(points)
            choice = "Netherfield"
        if choice == "b":
            longbourn()
            choice = "Longbourn"
        if choice == "c":
            points = meryton(points)
            choice = "Meryton"
        if choice == "d":
            exit_game()
            return
        print(f"\nThank you for visiting {choice}. As a reminder, your current annuity is £{points}.")    
        play_game = input("Do you wish to continue playing? yes/no - ")
    exit_game()
    return


def exit_game() -> None:
    """Prints closing messages for game."""
    print(f"\nWe are sorry to see you disembark, {player}.")
    if points < 1000:
        print(f"Unfortunately, {player}, your actions have diminished your annuity to £{points}.")
    if points == 1000:
        print(f"You shall leave this game with an annuity of £{points}.")
    if points > 1000:
        print(f"You have acted most prudently, {player}, and increased your annuity to £{points}!")
    print(f"We hope our game has bewitched you, body and soul. {e_wink} Farewell, {player}, and have a nice day!")
    return
   

def greet() -> None:
    """Introduction to game that collects player name."""
    global player
    player = input("\nWelcome to \"Pride and Prejudice\": COMP 110 Edition! What is your name, dear player? ")
    return 


def exposition() -> None:
    """More backgroud information about the game."""
    print("\n\"It is a truth universally acknowledged...\" that anything is more fun when you add some Jane Austen!")
    print("\nIn this game you will encounter marriage proposals")
    print("and dance with the elegant ton, while avoiding sinister influences of wealth-seeking suitors and")
    print(f"overbearing mamas! You have a starting annuity of £{points}. Engaging with friends will increase")
    print("your annuity, whereas interactions with less genial counterparts will result in the")
    print("theft of your precious inheritance!")
    return

    
def netherfield(points_n: int) -> int:
    """Engage with friends and dance, earning or losing points based on dance partner."""
    print(f"\nWelcome to Netherfield Park, {player}! Music swells around the happy assemblage, with a number of your")
    print("friends already engaged in the revelry.")
    points_n += 100
    print("Mr. Bennet was so pleased that you have decided to go to the ball!") 
    print(f"He has increased your annuity as a result! {e_sparkle}")
    dance_or_talk: str = input("Should you like to dance, or converse with dear Miss Lucas? dance/talk - ")
    if dance_or_talk == "talk":
        points_n -= 50
        print("\nYou enjoy such engaging conversation with Miss Lucas that you completely forget the time!")
        print("But alas, Mrs. Bennet is displeased you did not dance with any suitors,") 
        print(f"and has deducted some of your annuity. {e_pensive} ")
        print(f"However, do not let her get your spirits down, {player}.") 
        print(f"Sincere friendship is of infinite value, beyond any annuity. {e_gratitude}")
        return points_n 
    else:
        print("\nThe string quartet crescendos, and the opening notes of your favorite song flit through the air") 
        print("as you reach the center of the crowd.")
        i: int = 0
        assent: str = dancing_partner()
        while assent == "n" and i < 2:
            points_n -= 50
            print("Mrs. Bennet is displeased to see you being so discourteous,") 
            print(f"and has deducted from your annuity! {e_pensive}")
            assent = dancing_partner()
            i += 1 
        if assent == "n" and i >= 2:
            print("\nThe night is over, and Mrs. Bennet is furious that you danced with NO one!!")
            points_n -= 300
            print(f"As a result, she reduces your annuity to £{points_n}")
            return points_n
        else:
            print("You happily offer your hand, and are swept onto the dance floor!")
            print(f"\n\t{e_sparkle}\t{e_music}\t{e_dance_man}\t{e_sparkle}\t{e_dance_woman}\t{e_music}\t{e_sparkle}")
            points_n += 150
            print("\nAfter a wonderful night of dancing, you contentedly return home.")
            print("Mrs. Bennet was so thrilled to see you on the dance floor!")
            print(f"So as an added bonus, she has increased your annuity to £{points_n}! {e_sparkle}")
            return points_n 

            
def dancing_partner() -> str:
    """Randomly generates a dance partner for the player to accept or reject."""
    poss_partners: list[str]
    poss_partners = ["Mr. Darcy", "Mr. Bingley", "Mr. Wickham", "Miss Bingley", "Mr. Collins", "Miss King"] 
    from random import randint
    your_partner: str = poss_partners[randint(0, 5)]
    assent: str = input(f"\n{your_partner} approaches you and asks you to dance. Do you offer them your hand? y/n - ")
    return assent 


def longbourn() -> None:
    """Gain/lose points while interacting with dinner plans and a marriage proposal from Mr. Collins."""
    global points 
    print(f"\nWelcome to Longbourn, {player}!")
    print(f"Mrs. Bennet informs you that your dreaded cousin, Mr. Collins, will be coming tonight! {e_fearful}")
    print("What do you ask Mrs. Hill to fix for dinner- a or b?")
    meal: str = input("a- chicken and potatoes\tb- steak and green beans - ")
    print("\nMr. Collins has arrived! Your scheming mama forces you sit next to him at dinner, much to your chagrin.")
    if meal == "a":
        points += 200
        print("Mr. Collins hastily begins eating. \"What EXCELLENT boiled potatoes!\" he exclaims.")
        print(f"Your mama is pleased you chose such an exemplary vegetable, and increases your annuity! {e_sparkle}")
    if meal == "b":
        points -= 200
        print("Mr. Collins reluctantly begins eating. \"I wish we had some potatoes!\" he mourns.")
        print("\"My esteemed patroness, Lady Catherine de Bourgh, would NEVER serve meals without boiled potatoes.\"")
        print(f"Your mama sees you roll your eyes at Mr. Collins, and deducts from your annuity! {e_pensive}")
    print(f"\nThe next morning at breakfast, Mr. Collins requests a private audience with you! {3*e_fearful}")
    print("Before you have time to react, your mama shoos everyone out, and Mr. Collins gets down on one knee.")
    proposal: str = input("Mr. Collins hands you a wilted flower, and asks you to marry him! What do you say? y/n - ")
    if proposal == "y":
        points += 3000
        print("\nAfter hearing your assent, your mama bursts in filled with joy, and increases your annuity!")
        points -= 2500
        print("However, your father is disappointed that his favorite child would marry someone so obsequious.")
        print(f"Accordingly, he deducts some money from your annuity. {e_pensive}")
    if proposal == "n":
        points -= 2000
        print("\nAfter hearing your refusal, your mama angrily bursts in, scolds you, and deducts from your annuity!")
        points += 4000
        print("However, your father is proud that his child objected to tying themselves to such a vapid individual.")
        print(f"Accordingly, he graciously adds money to your annuity! {3*e_sparkle}")
    print(f"After weathering this turbulent dinner and breakfast, you have survived with an annuity of £{points}.")
    return


def meryton(points_m: int) -> int:
    """Gain/lose points while shopping in Meryton and coming across Mr. Wickham or Mr. Bingley."""
    print(f"\nAfter a short walk with your sisters, you arrive at the shops in town. Welcome to Meryton, {player}!")
    print(f"You walk into the ribbon shop {e_ribbon}. You notice a familiar man in militia uniform by the counter.")
    approach: str = input(f"Do you want to converse with the man, {player}? yes/no - ")
    if approach == "yes":
        print("\nAs you walk over, the man turns around and you realize it is Mr. Wickham!")
        print("\nAfter chatting convivially for a few minutes, Mr. Wickham becomes a bit sheepish.")
        print(f"\"Forgive me, {player}, but I was wondering if I could borrow your AustenExpress card?\" he asks.")
        print("\"I've been dying to buy some new ribbons for my sister.\"")
        lending: str = input("Do you lend him your card? ")
        if lending == "yes":
            points_m = 0
            print("\nAs soon as you hand him your card, Mr. Wickham runs away chuckling evilly!")
            print("He's stolen all of your annuity!")
            print(f"You'll never look at ribbons the same way again. {5*e_pensive} You return home, penniless.")
        else:
            print("\nMr. Wickham dejectedly departs. Feeling remorseful, you tell your family the story that night.")
            points_m += 300
            print("Hearing the tale, your father says not to feel down, and tells you Mr. Wickham is a con-man!")
            print(f"As a reward for your discernment, your father increases your annuity to £{points_m}! {e_sparkle}")
    if approach == "no":
        print("You go about your business, buying ribbons, then walk home with your sisters.")
        print("\nAt dinner that night, you hear there was a con artist disguised as a milita man sighted in town!")
        print("You realize that the man at the shop was the con artist,")
        print(f"and are glad you did not approach him. {e_gratitude}")
    return points_m


if __name__ == "__main__":
    main()