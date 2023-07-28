import mixtape


class Partie:

    def __init__(self):
        self.playersList = []
        self.mixtape = mixtape.Mixtape()

    def addPlayer(self, player):
        self.playersList.append(player)

    def rmvPlayer(self, player):
        self.playersList.remove(player)

