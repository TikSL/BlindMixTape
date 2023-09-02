import ressources


class GameConfig:

    def __init__(self):
        self.difficulty = 0
        self.numPlayers = 2
        self.numRounds = 2
        self.currentRound = 0
        self.listVignettes = []
        self.listPlayers = []
        self.listMixtapes = []
        self.joueurSelectionne = None
        self.sonSelectionne = None
        self.premierPassagePlay = True
        self.style = "Actuel"

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_num_players(self, num_players):
        self.numPlayers = num_players

    def set_num_rounds(self, num_rounds):
        self.numRounds = num_rounds

    def dspInfos(self):
        print(f"GAME CONFIG INFOS\n"
              f"Difficulty : {self.difficulty}\n"
              f"Num. players : {self.numPlayers}\n"
              f"Num. rounds : {self.numRounds}\n"
              f"Currend round : {self.currentRound}")
        for player in self.listPlayers:
            player.dspInfos()
        for mixtape in self.listMixtapes:
            mixtape.dspInfos()

    def updateStyle(self, param):
        listeStyle = list(ressources.playlistsDeezer.keys()) + ["playlist\nperso"]
        index = listeStyle.index(self.style)
        if param == 1:
            if index == len(listeStyle)-1:
                self.style = listeStyle[0]
            else:
                self.style = listeStyle[index + 1]
        elif param == -1:
            if index == 0:
                self.style = listeStyle[len(listeStyle)-1]
            else:
                self.style = listeStyle[index - 1]
