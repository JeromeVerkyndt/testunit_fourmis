class Basic_ant:
    def __init__(self, isalive, birth, phase):
        self.isAlive = isalive
        self.birth = birth
        self.phase = phase

    def __str__(self):
        return "Fourmis basique"

    def isGonnaDie(self, day):
        if day - self.birth >= 10:
            self.isAlive = False

class Queen_ant(Basic_ant):

    def __init__(self, isalive, birth, phase):
        super().__init__(isalive, birth, phase)

    def __str__(self):
        return f"Reine"