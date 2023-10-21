class RPS_Strategy:
    def answer(self, ans1, ans2):
        pass

class Rock_Strategy(RPS_Strategy):
    def answer(self, ans1, ans2):
        if ans1 == ans2:
            return f"It's a tie."
        elif ans1 == "rock":
            if ans2 == "scissors":
                return f"Player wins. {ans1} > {ans2}"
            else:
                return f"Computer wins. {ans1} < {ans2}"
            
class Paper_Strategy(RPS_Strategy):
     def answer(self, ans1, ans2):
        if ans1 == ans2:
            return f"It's a tie."
        elif ans1 == "paper":
            if ans2 == "rock":
                return f"Player wins. {ans1} > {ans2}"
            else:
                return f"Computer wins. {ans1} < {ans2}"
            
class Scissors_Strategy(RPS_Strategy):
    def answer(self, ans1, ans2):
        if ans1 == ans2:
            return f"It's a tie."
        elif ans1 == "scissors":
            if ans2 == "paper":
                return f"Player wins. {ans1} > {ans2}"
            else:
                return f"Computer wins. {ans1} < {ans2}"

class RPS:
    def __init__(self, strategy):
        self.strategy = strategy

    def result(self, ans1, ans2):
        return self.strategy.answer(ans1, ans2)