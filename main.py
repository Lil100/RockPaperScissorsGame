import random
def get_choices():
    player_choice = input(" Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice (options)
    choices = {"player": player_choice , "computer" : computer_choice}
    return choices

def check_win(player, computer):
    print (f"You chose {player} , Computer chose {computer}")
    if player == computer:
        return "Its a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes Scissors! You win!!"
        else:
            return " Paper covers Rock! You lose."
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper! You lose."
        else:
            return "Paper cover Rock! You win!"
    elif player == "scissors":
        if computer == "Rock":
            return "Rock smashes Scissors! You lose."
        else:
            return "Scissors cuts Paper! You win!"

choices = get_choices()
results = check_win(choices ["player"], choices["computer"])
print(results)


