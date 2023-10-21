import time

class RPS_Decorator:
    def __init__(self, game):
        self.game = game

    def play(self):
        start_time = time.time()
        self.game.start()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Время игры: {elapsed_time:.0f} секунд")
