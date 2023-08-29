from pytube import Search
from pydub import AudioSegment


def validation(title):
    return title.split("(")[0]


def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)


class Song:

    def __init__(self, title, artist, startTimer, difficulty, index):
        self.title = validation(title)
        self.artist = artist
        self.startTimer = startTimer
        self.difficulty = difficulty
        self.id = index

        self.found = False
        self.foundTimer = -1
        self.founder = None
        self.foundPosition = -1
        self.cover = f"game/cover_{str(self.id)}.jpg"

    def dspInfo(self):
        print(f"ID : {self.id} - Titre : {self.title}, Artiste : {self.artist}, Difficulté : {self.difficulty}")

    def dspCompleteInfo(self):
        self.dspInfo()
        print(f"Commence à : {self.startTimer} s\n"
              f"Trouvé : {self.found}\n"
              f"Trouvé par {self.founder}\n"
              f"Trouvé en {self.foundTimer} s\n"
              f"Trouvé en position {self.foundPosition}")

    def dl(self):
        audio_stream = Search(f"{self.artist} {self.title}").results[0].streams.filter(only_audio=True).first()
        audio_stream.download(filename=f"game/{self.id}.mp4")
        song = AudioSegment.from_file(f"game/{self.id}.mp4", format="mp4")
        song[self.startTimer:self.startTimer + 30000].export(f"game/{self.id}.mp3", format="mp3")
        print(f"Son {self.id} téléchargé")

    def setAudioLevel(self):
        sound = AudioSegment.from_file(f"game/{self.id}.mp3", "mp3")
        normalized_sound = match_target_amplitude(sound, -20.0)
        normalized_sound.export(f"game/{self.id}.mp3", format="mp3")
