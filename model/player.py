class Player:

    def __init__(self, name, vignette):
        self.name = name
        self.vignette = vignette
        self.score = 0

    def dspInfos(self):
        print(f"PLAYERS INFOS\n"
              f"Nom : {self.name}\n"
              f"Score : {self.score}")
