from random import randint
# THIS two are the global variables and can be used anywhere in the function
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5


#function to check users guess against actual number
def check_answer(user_guess,actual_guess,turns):
    """checks answer against guess,returns the number of turns remaining """
    if user_guess>actual_guess:
        print("Too high!")
        return turns -1 
    elif user_guess<actual_guess:
        print("Too low!")
        return turns -1
        
    else:
        print(f"You Got it ! The answer was {actual_guess}")
# function to set difficulty
def set_difficulty():
    level=input("choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
# choosing a random number 1 and 100
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer=randint(1,100)
    

    turns= set_difficulty()


    guess=0
    while guess!= answer:
        print(f"You hsve {turns} attempts remaining to guess the number.")
    # let the user guess a  number
        guess=int(input("Make a guess:"))
        turns=check_answer(guess,answer,turns)
        if turns ==0:
            print("You've run out og guesses , you loose")
            return
        elif guess!= answer:
            print("Guess again.")
game()