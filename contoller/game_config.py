class gameConfig:

    def __init__(self):
        self.difficulty = 0
        self.numPlayers = 2
        self.numRounds = 3
        self.currentRound = 0
        self.listVignettes = []
        self.listPlayers = []
        self.listMixtapes = []
        self.joueurSelectionne = None

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_num_players(self, num_players):
        self.numPlayers = num_players

    def set_num_rounds(self, num_rounds):
        self.numRounds = num_rounds

    def dspInfos(self):
        print(f"GAME CONFIG INFORMATION :\n"
              f"Difficulty : {self.difficulty}\n"
              f"Num. players : {self.numPlayers}\n"
              f"Num. rounds : {self.numRounds}\n"
              f"Currend round : {self.currentRound}")
        for player in self.listPlayers:
            player.dspInfos()
        for mixtape in self.listMixtapes:
            mixtape.dspInfos()
