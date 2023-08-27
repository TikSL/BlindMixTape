import random
import difflib

import requests
from pydub import AudioSegment
from pygame import mixer
from pytube import Search

import song
import deezer


class Mixtape:

    def download_image(self, url, destination):
        response = requests.get(url)
        if response.status_code == 200:
            with open(destination, "wb") as file:
                file.write(response.content)
            # print("Image téléchargée avec succès.")
        else:
            print("Échec du téléchargement de l'image.")

    def __init__(self, difficulte):

        self.nomFichierMix = None
        client = deezer.Client()
        # playlist = client.get_playlist(10295099302)
        # playlist = client.get_playlist(11682866204)
        # playlist = client.get_playlist(11682866204)
        # playlist = client.get_playlist(10797319022)
        playlist = client.get_playlist(741188545) #top france 2022
        # playlist = client.get_playlist(4380024462) #rock
        # playlist = client.get_playlist(11672649764) #blindmixtape bmt
        # playlist = client.get_playlist(10896810924) #top monde 2022
        liste_sons = playlist.get_tracks()

        self.mixtape = self.piocher(liste_sons, difficulte)

        self.listeATrouver = []
        for id, s in enumerate(self.mixtape):
            self.listeATrouver.append(song.Song(s.title_short, s.artist.name, 30, s.rank, id=id))
            self.download_image(s.album.cover_medium, f"game/cover_{str(id)}.jpg")

        self.dl()
        print("CREATION MIXTAPE Téléchargement OK")
        # self.cut()
        self.normaliserAudio()
        # self.mixer()
        print("CREATION MIXTAPE Mixage OK")

    def dspInfos(self):
        print(f"---------\n"
              f"MIXTAPE INFOS\n")
        print(f"Liste a Trouver : ")
        for song in self.listeATrouver:
            song.dspInfo()

    def dl(self):
        for song in self.listeATrouver:
            song.dl()

    def normaliserAudio(self):
        for song in self.listeATrouver:
            song.setAudioLevel()

    def cut(self, duration):
        for song in self.listeATrouver:
            song.cut(duration)

    def mixer(self):
        # self.nomFichierMix = f"partie/mix_{len(self.listeATrouver)}.mp3"
        # sound0 = AudioSegment.from_file(f"partie/{self.listeATrouver[0].id}.mp4", format="mp4")
        # sound1 = AudioSegment.from_file(f"partie/{self.listeATrouver[1].id}.mp4", format="mp4")
        # overlay = sound0.overlay(sound1, position=0)
        # print(f"Mixage {self.listeATrouver[0].id} OK")
        # print(f"Mixage {self.listeATrouver[1].id} OK")
        # for song in self.listeATrouver[2:]:
        #     soundn = AudioSegment.from_file(f"partie/{song.id}.mp4", format="mp4")
        #     overlay = overlay.overlay(soundn, position=0)
        #     print(f"Mixage {song.id} OK")
        # overlay.export(self.nomFichierMix, format="mp3")

        self.nomFichierMix = f"game/mix_{len(self.listeATrouver)}.mp3"

        # Créer une liste pour stocker les segments audio trouvés
        found_segments = []

        for song in self.listeATrouver:
            if song.found:
                sound = AudioSegment.from_file(f"game/{song.id}.mp4", format="mp4")
                found_segments.append(sound)
                print(f"Mixage {song.id} OK")

        # Vérifier s'il y a des segments à mélanger
        if found_segments:
            self.nomFichierMix = f"game/mix_{len(found_segments)}.mp3"
            # Mélanger les segments trouvés
            overlay = found_segments[0]
            for sound_segment in found_segments[1:]:
                overlay = overlay.overlay(sound_segment, position=0)

            # Exporter le fichier mixé
            overlay.export(self.nomFichierMix, format="mp3")
            print("Mixage final OK")
        else:
            print("Aucun segment audio trouvé à mixer.")

    def play_music(self):
        start_time = 45
        mixer.init()
        mixer.music.load(self.nomFichierMix)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        mixer.music.set_pos(start_time)

        while True:
            print("Press 'p' to pause, 'r' to resume")
            print("Press 'e' to exit the program")
            query = input(" ")
            if query == 'p':
                mixer.music.pause()
                sonTrouve = self.deviner()
                if sonTrouve > 0:
                    self.listeATrouver = self.listeATrouver[:sonTrouve] + self.listeATrouver[sonTrouve + 1:]
                    self.mixer()
                    mixer.music.unload()
                    mixer.music.load(self.nomFichierMix)
                    mixer.music.set_volume(0.7)
                    mixer.music.play()
                    mixer.music.set_pos(start_time)
                mixer.music.unpause()
            elif query == 'r':
                mixer.music.unpause()
            elif query == 'e':
                mixer.music.unload()
                break

    def is_one_typo(self, proposition, target):
        similarity_ratio = difflib.SequenceMatcher(None, proposition.lower(), target.lower()).ratio()
        return similarity_ratio >= 0.9

    def deviner(self):
        print("Taper le nom de l'artiste ou le titre de la musique")
        proposition = input(" ").lower()

        for song in self.listeATrouver:
            titre = song.title.lower()
            artiste = song.artist.lower()
            if self.is_one_typo(proposition, artiste):
                print("Ptn c'est le bon artiste bien joué ! Est ce que tu as le titre ?")
                proposition = input(" ").lower()
                if self.is_one_typo(proposition, titre):
                    print("MEC T'ES TROP CHAUD ARTISTE + TITRE  WAOUH")
                else:
                    print("C'est OK t'avais que le nom de l'artiste")
                return song.id
            elif self.is_one_typo(proposition, titre):
                print("Ptn c'est le bon titre bien joué ! Est ce que tu as l'artiste ?")
                proposition = input(" ").lower()
                if self.is_one_typo(proposition, artiste):
                    print("MEC T'ES TROP CHAUD TITRE + ARTISTE  SHEEEEESH")
                else:
                    print("C'est OK t'avais que le titre")
                return song.id

        print("T'avais rien nt ... (nulos)")
        return -1

    def piocher(self, liste_sons, difficulte):
        print("Pioche Mixtape début")
        listeMixtape = []
        while len(listeMixtape) < 6:
            essai = random.choice(liste_sons)
            if essai not in listeMixtape:
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
                    diffSon = self._evalDiff(diffSon)
                    if diffSon in difficulte:
                        difficulte.remove(diffSon)
                        listeMixtape.append(essai)
                        print(f"Son de diff {diffSon} trouvé. Restants : {difficulte}")

                except Exception as e:
                    pass

        return listeMixtape

    def _evalDiff(self, diffSon):
        if diffSon > 400000000:
            return 0
        elif diffSon > 100000000:
            return 1
        else:
            return 2



