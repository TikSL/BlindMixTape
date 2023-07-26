import random

from pytube import Search
from pydub import AudioSegment


def validation(title):
    return title.split("(")[0]

class Song:

    def __init__(self, title, artist, startTimer, difficulty, id):
        self.title = validation(title)
        self.artist = artist
        self.startTimer = startTimer
        self.difficulty = difficulty
        self.id = id

        self.found = False
        self.foundTimer= -1
        self.founder = None
        self.foundPosition = -1

    def dspInfo(self):
        print(f"---\n"
              f"Titre : {self.title}\n"
              f"Artiste : {self.artist}\n"
              f"Difficulté : {self.difficulty}")

    def dspCompleteInfo(self):
        self.dspInfo()
        print(f"Commence à : {self.startTimer} s\n"
              f"Trouvé : {self.found}\n"
              f"Trouvé par {self.founder}\n"
              f"Trouvé en {self.foundTimer} s\n"
              f"Trouvé en postion {self.foundPosition}")

    def dl(self):
        audio_stream = Search(f"{self.artist} {self.title}").results[0].streams.filter(only_audio=True).first()
        audio_stream.download(filename=f"partie/{self.id}.mp4")
        print(f"Son {self.id} téléchargé")

    def setAudioLevel(self):
        audio = AudioSegment.from_file(f"partie/{self.id}.mp4", format="mp4")
        normalizedAudio = audio.apply_gain(-audio.dBFS)
        normalizedAudio.export(f"partie/{self.id}.mp4", format="mp4")

    def cut(self, duration):
        audio = AudioSegment.from_file("../partie/0.mp4", format="mp4")
        extracted_audio = audio[:duration * 1000]  # en ms
        extracted_audio.export(f"partie/{self.id}.mp4", format="mp4")

