
from state import DeterminingResultState, WaitingForChoiceState
from singleton import *
from observer import *
class RockPaperScissors(metaclass = SingletonMeta):
    def __init__(self):
        self.viewers = []

    def add_viewer(self, viewer):
        self.viewers.append(viewer)
    
    def remove_viewer(self, viewer):
        self.viewers.remove(viewer)

    def send_message(self, message):
        for viewer in self.viewers:
            viewer.update(message)

    def start(self):
        ur_score = 0
        comp_score = 0
        while True:
            game_state = WaitingForChoiceState()
            user_choice, comp_choice = game_state.play()
            game_state = DeterminingResultState(user_choice, comp_choice)
            result = game_state.play()
            if result == None:
                continue
            result_message = result.result(user_choice, comp_choice)
            self.send_message(result_message)
            if "Player wins." in result_message:
                ur_score += 1
            elif "Computer wins." in result_message:
                comp_score += 1
            self.send_message(f"Результат: {ur_score} - {comp_score}")
            if(comp_score == 3):
                self.send_message("Computer won the game")
                break
            elif(ur_score == 3):
                self.send_message("You won the game")
                break 