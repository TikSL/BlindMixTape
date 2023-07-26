import mixtape

if __name__ == "__main__":
    # Chemin vers le fichier audio (musique)

    new_mix = mixtape.Mixtape()
    new_mix.infos()
    while len(new_mix.listeATrouver) > 2:
        new_mix.play_music()
