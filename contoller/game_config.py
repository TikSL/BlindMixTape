class gameConfig:

    def __init__(self):
        self.difficulty = None
        self.numPlayers = 2
        self.numRounds = 3
        self.currentRound = 0
        self.listPlayers = []
        self.listMusics = []

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_num_players(self, num_players):
        self.numPlayers = num_players

    def set_num_rounds(self, num_rounds):
        self.numRounds = num_rounds

    def dspInfos(self):
        print(f"GAME CONFIG INFORMATION :"
              f"Difficulty : {self.difficulty}"
              f"Num. players : {self.numPlayers}"
              f"Num. rounds : {self.numRounds}"
              f"Currend round : {self.currentRound}")
        for player in self.listPlayers:
            player.dspInfos()
        for music in self.listMusics:
            music.dspInfos()
