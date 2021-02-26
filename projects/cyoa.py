"""To be filled in greater detail here. A coded adventure"""

__author__ = "730394055"

player: str 
points: int 

def main() -> None:
    """Opening point for this program."""
    global points
    points = 0
    greet()
    # other things/function calls here
    print("Fare thee well, my dearest companion!")
    return
   

def greet() -> None:
    """Introduction to game, collects player name and starts point count."""
    emoji_1: str = "\U00000000" # enter desired unicode here
    print("Welcome Message Here!")
    global player
    player = input("What is your name? ")
    print(f"Get your engines ready, {player}, cause it's go time! {emoji_1}")
    return 


def netherfield(points_n: int) -> int:
    """Engage with friends and dance, earning or losing points based on dance partner."""
    e_dance_woman: str = "\U0001F483"
    e_dance_man: str = "\U0001F57A"
    #Some sort of welcome statement about the splendor
    #Ask to go find your friend Charlotte, or go to the dance floor to try to find a partner
    dance_or_talk: str = input("Should you like to dance, or take a moment to converse with dear Miss Lucas? dance/talk - ")
    if dance_or_talk == "talk":
        # some print statement about talking to Charlotte, then going home. edit point count on the positive side
        return 0 # add in the actual variable for points here
    else:
        # print statement welcoming to dance floor
        ready: str = input(f"Are you ready to dance, {player}? {e_dance_woman}{e_dance_man}") # maybe use this?
        i: int = 0 # thinking maybe have a total of three chances to find a dance partner
        assent: str = dancing_partner()
        if assent == "n":
            while i < 3:
                dancing_partner()
                i += 1 # have new dancing partner be selected each time- maybe a new function which takes 
                        #final partner determines point, or number of chances, or each partner choice affects it if you are feeling edgy
            #put something here about calling points from global and reassigning the value, deducting points cause you displeased dad for wasting time
            #print message about how ball is over and dad is mad, dowry deducted
            # call to longbourn function
        else: # assuming that it is y, don't know if there is a more "formal" way to code this
            # print statement about taking your partner's hand and having a good time
            # reassign point value for positive engagement with peeps
            #

            


        


def dancing_partner() -> str:
    """Randomly generates a dance partner for the player to accept or reject."""
    poss_partners: list[str] = ["Mr. Darcy", "Mr. Bingley", "Mr. Wickham", "Miss Bingley", "Mr. Collins", "Miss King"] # add in some unicode emojis for each option
    from random import randint
    your_partner: str = poss_partners[randint(0,5)]
    assent: str = input(f"{your_partner} approaches you and asks you to dance. Do you offer them your hand? y/n - ")
    return assent 



if __name__ == "__main__":
    main()
