import deezer
import random
import requests
import time

from pytube import Search

import song

songPasses = []

def download_image(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, "wb") as file:
            file.write(response.content)
    else:
        print(f"Échec du téléchargement de l'image. URL {url}")


def _evalDiff(diffSon):
    if diffSon > 400000000:
        return 0
    elif diffSon > 100000000:
        return 1
    else:
        return 2


def generationMixtape(id_playlist, difficulty):

    client = deezer.Client()
    playlist = client.get_playlist(id_playlist)
    liste_sons = playlist.get_tracks()
    listeMixtape = []
    listeATrouver = []
    t_init = time.time()
    while len(listeMixtape) < 6 and time.time() - t_init < 60:
        essai = random.choice(liste_sons)
        if essai not in listeMixtape and essai not in songPasses:

            try:
                search_query = f"{essai.artist.name} {essai.title}"
                search_results = Search(search_query).results
                if search_results:
                    first_result = search_results[0]
                    views = first_result.views
                else:
                    views = 0
                print(essai.rank, views, essai.title_short, essai.artist.name, essai.rank * 10 + views)
                diffSon = essai.rank * 10 + views
                diffSon = _evalDiff(diffSon)
                if diffSon in difficulty:
                    difficulty.remove(diffSon)
                    songPasses.append(essai)
                    listeMixtape.append(essai)
                    start = random.randint(30000, 60000)
                    listeATrouver.append(song.Song(essai.title_short, essai.artist.name, start, diffSon,
                                                   index=len(listeMixtape)-1))
                    print(f"Son de diff {diffSon} trouvé. Restants : {difficulty}")
                    download_image(essai.album.cover_medium, f"game/cover_{str(len(listeMixtape)-1)}.jpg")

            except Exception:
                pass

    if len(listeMixtape) < 6:
        while len(listeMixtape) < 6:
            essai = random.choice(liste_sons)
            if essai not in listeMixtape and essai not in songPasses:
                songPasses.append(essai)
                listeMixtape.append(essai)
                start = random.randint(30000, 60000)
                listeATrouver.append(song.Song(essai.title_short, essai.artist.name, start, None,
                                               index=len(listeMixtape)-1))
                print(f"Son de difficulté aléatoire trouvé car la recherche a duré plus d'une minute.")
                download_image(essai.album.cover_medium, f"game/cover_{str(len(listeMixtape)-1)}.jpg")

    return listeMixtape, listeATrouver


class Mixtape:

    def __init__(self, difficulty, playlist="Rock", ):

        self.nomFichierMix = None
        self.mixtape, self.listeATrouver = generationMixtape(playlist, difficulty)
        self.dl()
        self.normaliserAudio()

    def dspInfos(self):
        print(f"---------\n"
              f"MIXTAPE INFOS\n")
        print(f"Liste a Trouver : ")
        for element in self.listeATrouver:
            element.dspInfo()

    def dl(self):
        for element in self.listeATrouver:
            element.dl()

    def normaliserAudio(self):
        for element in self.listeATrouver:
            element.setAudioLevel()
