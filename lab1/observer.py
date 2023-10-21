class Observer():
    def update(self, message):
        pass

class Viewer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name}, {message}")