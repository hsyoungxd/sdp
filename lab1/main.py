from rps import RockPaperScissors
from observer import Viewer
from decorator import RPS_Decorator
if __name__ == "__main__":
    rps = RockPaperScissors()
    rps.add_viewer(Viewer("hsy"))
    game = RPS_Decorator(rps)
    game.play()