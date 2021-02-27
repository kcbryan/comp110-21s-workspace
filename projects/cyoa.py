"""Interactive game incorporating some aspects from the movie and novel versions of Jane Austen's "Pride and Prejudice." """

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

def main() -> None:
    """Opening point for this program."""
    global points
    points = 1000
    greet()
    play_game: str = input(f"\nDo you wish to continue engaging with this literary adventure, {player}? yes/no - ")
    while play_game == "yes":
        print(f"\nLet us commence our plot, {player}! {e_flowers}")
        print("To whence shall we first embark? Please enter a, b, or c")
        choice: str = input("a- Ball at Netherfield Park\tb- Dinner at Longbourn\tc- Shopping in Meryton ? ")
        print(f"\nAs a reminder, your current annuity is £{points}. Good luck!")
        if choice == "a":
            points = netherfield(points)
            choice = "Netherfield"
        if choice == "b":
            longbourn()
            choice = "Longbourn"
        if choice == "c":
            points = meryton(points)
            choice = "Meryton"
        play_game = input(f"Thank you for visiting {choice}. Do you wish to continue playing? yes/no - ")
    print(f"We are sorry to see you disembark, {player}.")
    if points < 1000:
        print(f"Unfortunately, {player}, your actions have diminished your annuity to £{points}.")
    if points == 1000:
        print(f"You shall leave this game with an annuity of £{points}.")
    else:
        print(f"You have acted most prudently, {player}, and increased your annuity to £{points}!")
    print(f"We hope our game has bewitched you, body and soul. {e_wink} Farewell, {player}, and have a nice day!")
    return
   

def greet() -> None:
    """Introduction to game, collects player name and starts point count."""
    welcome_message()
    global player
    player = input("\nWhat is your name, dear player? ")
    return 


def welcome_message() -> None:
    """Contains series of printed statements for game intro to conserve space in greet function."""
    print("\"It is a truth universally acknowledged...\" that anything is more fun when you add some Jane Austen! \n")
    print("Welcome to \"Pride and Prejudice\": COMP 110 Edition! In this game you will encounter marriage proposals and ")
    print("dance with the elegant ton, while trying to avoid the sinister influences of wealth-seeking suitors and overbearing mamas!")
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
    print(f"\nWelcome to Netherfield Park, {player}! Music swells around the happy assemblage, with a number of your friends already engaged in the revel.")
    points_n += 100
    print(f"Mr. Bennet was so pleased that you have decided to go to the ball! He has increased your annuity as a result.")
    dance_or_talk: str = input("Should you like to dance, or take a moment to converse with dear Miss Lucas? dance/talk - ")
    if dance_or_talk == "talk":
        points_n -= 50
        print("\nYou enjoy such humorous and engaging conversation with Miss Charlotte Lucas, that you completely forget the time!")
        print("But alas, Mrs. Bennet is displeased you did not take time to dance with eligible suitors, and has deducted some of your annuity.")
        print(f"However, do not let her get your spirits down, {player}. Sincere friendship is of infinite value, beyond any annuity. {e_gratitude}")
        return points_n 
    else:
        print("\nThe string quartet crescendos, and the opening notes of your favorite song flit through the air as you reach the center of the crowd.")
        i: int = 0 # thinking maybe have a total of three chances to find a dance partner
        assent: str = dancing_partner()
        while assent == "n" and i < 3:
            points_n -= 50
            print(f"Mrs. Bennet is displeased to see you being so discourteous, and has deducted from your annuity! {e_pensive}")
            assent = dancing_partner()
            i += 1 
        print("You happily offer your hand, and are swept onto the dance floor!")
        print(f"\n\t {e_sparkle} \t {e_music} \t {e_dance_man} \t {e_sparkle} \t {e_dance_woman} \t {e_music} \t {e_sparkle}")
        points_n += 150
        print("\nAfter a wonderful night of dancing, you contentedly return home.")
        print("As an added bonus, Mrs. Bennet was so thrilled to see you on the dance floor that she has increased your annuity!")
        return points_n 

            
def dancing_partner() -> str:
    """Randomly generates a dance partner for the player to accept or reject."""
    poss_partners: list[str] = ["Mr. Darcy", "Mr. Bingley", "Mr. Wickham", "Miss Bingley", "Mr. Collins", "Miss King"] 
    from random import randint
    your_partner: str = poss_partners[randint(0,5)]
    assent: str = input(f"\n{your_partner} approaches you and asks you to dance. Do you offer them your hand? y/n - ")
    return assent 


def longbourn() -> None:
    """Gain/lose points while interacting with dinner plans and a marriage proposal from Mr. Collins."""
    global points #allows for global reassignment of points value to comply with rubric
    print(f"\nWelcome to Longbourn, {player}!")
    print(f"Mrs. Bennet informs you that your dreaded cousin, Mr. Collins, will be coming tonight! {e_fearful}")
    print("What do you ask Mrs. Hill to fix for dinner- a or b?")
    meal: str = input("a- chicken and potatoes\tb- steak and green beans - ")
    print("\nMr. Collins has arrived! Your scheming mama forces you sit next to him at dinner, much to your chagrin.")
    # small if/then interaction about boiled potatoes, changing point values accordingly
    if meal == "a":
        points += 200
        print("Once the meal is served, Mr. Collins hastily begins eating. \"What EXCELLENT boiled potatoes!\" he exclaims.")
        print(f"Your mama is so pleased that you chose such an exemplary vegetable, and increases your annuity! {e_sparkle}")
    if meal == "b":
        points -= 200
        print("The meal is served, and Mr. Collins reluctantly begins eating. \"I wish we had some potatoes!\" he mourns.")
        print("\"My esteemed patroness, Lady Catherine de Bourgh, would NEVER serve a meal without boiled potatoes.\"")
        print(f"Your mama sees you roll your eyes at Mr. Collins' inane remarks, and deducts from your annuity! {e_pensive}")
    print(f"\nThe next morning at breakfast, Mr. Collins requests a private audience with you! {3*e_fearful}")
    print("Before you have time to react, your mama shoos everyone out of the kitchen, and Mr. Collins gets down on one knee.")
    proposal: str = input("Mr. Collins hands you a half-wilted flower, and asks you to marry him! What do you say? y/n - ")
    if proposal == "y":
        points += 3000
        print("\nAfter hearing your assent, your mama bursts in filled with joy, and increases your annuity!")
        points -= 2500
        print("However, your father is disappointed that his favorite child would marry someone so obsequious.")
        print(f"Accordingly, he deducts some money from your annuity. {e_pensive}")
    if proposal == "n":
        points -= 2000
        print("\nAfter hearing your refusal, your mama angrily bursts in and scolds you, and then deducts from your annuity!")
        points += 4000
        print("However, your father is proud that his child objected to tying themselves to such a vapid individual.")
        print(f"Accordingly, he graciously adds money to your annuity! {3*e_sparkle}")
    print(f"After weathering this turbulent dinner party and breakfast, you have survived with an annuity of £{points}.")
    return


def meryton(points_m: int) -> int:
    """Gain/lose points while shopping in Meryton and coming across Mr. Wickham or Mr. Bingley."""
    print(f"After a short walk with your sisters, you arrive at the shops in town. Welcome to Meryton, {player}!")
    print(f"You walk into the ribbon shop {e_ribbon}. You notice a familiar man in militia uniform by the counter.")
    approach: str = input(f"Do you want to converse with the man, {player}? yes/no - ")
    if approach == "yes":
        print("\nAs you walk over, the man turns around and you realize it is Mr. Wickham!")
        print("After chatting convivially for a few minutes, Mr. Wickham becomes a bit sheepish.")
        print(f"\n\"Please forgive me, {player}, but I was wondering if I could borrow your AustenExpress card?\" he asks you.")
        print("\"I've been dying to buy some new ribbons for my sister.\"")
        lending: str = input("Do you lend him your card? ")
        if lending == "yes":
            points_m = 0
            print("As soon as you hand him your card, Mr. Wickham runs away chuckling evilly! He's stolen all of your annuity!")
            print(f"You'll never look at ribbons the same way again. {5*e_pensive} You return home, penniless.")
        else: # essentially, if lending is no
            print("\nMr. Wickham dejectedly departs. Feeling remorseful, you tell the story to your family that night.")
            points_m += 300
            print("Hearing your tale, your father says not to feel down, and tells you Mr. Wickham is a known con-man!")
            print(f"As a reward for your discernment, your father increases your annuity to £{points_m}! {e_sparkle}")
    if approach == "no":
        print("You go about your business, buying ribbons. Leaving with your purchases, you and your sisters walk home.")
        print("\nAt dinner that night, you hear that there was a con artist disguised as a milita man sighted in town!")
        print(f"You realize that the man at the shop was the con artist, and are glad you did not approach him. {e_gratitude}")
    return points_m


if __name__ == "__main__":
    main()