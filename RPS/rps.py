import random

def get_choices():
    player_choice = input("enter player choice for RPS :")
    
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"you selected {player} computer choosed {computer}")
    if player==computer:
        return "Tie"
    elif player =="rock":
        if computer =="scissor":
            return "player win"
        else :
            return "player lose"
    elif player =="paper":
        if computer=="scissor":
            return "computer win"
        else:
            return "player win"
    elif player =="scissor":
        if computer =="rock":
            return "computer win"
        else:
            return "player win"

choices = get_choices()

result = (check_win(choices["player"],choices["computer"]))

print(result)