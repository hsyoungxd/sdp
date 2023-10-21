import random
from strategy import RPS, Rock_Strategy, Paper_Strategy, Scissors_Strategy
class GameState:
    def play(self):
        pass

class WaitingForChoiceState(GameState):
    def play(self):
        possible_actions = ["rock", "paper", "scissors"]
        choice = input("Enter a choice (rock, paper, scissors): ").lower()
        comp_choice = random.choice(possible_actions)
        print(f"Computer chose {comp_choice}")
        return choice, comp_choice
    
class DeterminingResultState(GameState):
    def __init__(self, user_choice, computer_choice):
        self.user_choice = user_choice
        self.computer_choice = computer_choice
    def play(self):
        if self.user_choice == "rock":
            rps = RPS(Rock_Strategy())
        elif self.user_choice == "paper":
            rps = RPS(Paper_Strategy())
        elif self.user_choice == "scissors":
            rps = RPS(Scissors_Strategy())
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            return None
        return rps