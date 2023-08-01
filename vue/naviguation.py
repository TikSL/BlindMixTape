import pygame
import sys
from pygame import mixer, time, USEREVENT

import player
import ressources
from button import Button
from music_bar import MusicBar
from vignette_joueur import VignetteJoueur
from volume_bar import VolumeBar

pygame.init()

# screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen_width = 1280
screen_height = 720
print(screen_width, screen_height)

# Définir la taille de la fenêtre en utilisant les dimensions de l'écran
screen = pygame.display.set_mode((screen_width, screen_height))
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("BlindMixTape")

# Charger l'image de fond en utilisant les dimensions de l'écran
background = pygame.transform.scale(pygame.image.load(ressources.background), (screen_width, screen_height))
volume_bar = VolumeBar(screen_width * 0.805, screen_height * 0.884, screen_width * 0.130, screen_height * 0.035)

listeVignettes = []
listeJoueurs = []


def playAlignementJoueursBas(nbrVignettes):
    total_width = screen_width * 0.097 * nbrVignettes
    espace_horizontal = (screen_width - total_width) / (nbrVignettes + 1)

    for index_vignette, vignette in enumerate(listeVignettes):
        position_x = espace_horizontal * (index_vignette + 1) + 0.097 * screen_width * index_vignette
        vignette.icon_croix = None
        vignette.setPos((position_x, screen_height - 0.24 * screen_height))



def playListening():
    global listeVignettes
    global listeJoueurs

    playAlignementJoueursBas(len(listeVignettes))

    playButtonMusic = Button(
        images=ressources.playButtonPlayMusic,
        pos=(screen_width * 0.5, screen_height * 0.1),
        text_input=None, font=None, base_color=None, hovering_color = None)
    playSoundOn = True

    playButtonBack = Button(
        images=ressources.lobbyButtonBack,
        pos=(screen_width * 0.948, screen_height * 0.08),
        text_input=None, font=None, base_color=None, hovering_color=None)

    while True:
        screen.blit(background, (0, 0))
        playMousePosition = pygame.mouse.get_pos()
        for i, vignette in enumerate(listeVignettes):
            vignette.afficher(screen)

        for button in [playButtonBack, playButtonMusic]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButtonBack.checkForInput(playMousePosition):
                    listeVignettes = []
                    main_menu()
                if playButtonMusic.checkForInput(playMousePosition):
                    if playSoundOn:
                        playButtonMusic.setImages(ressources.playButtonMuteMusic)
                        pygame.mixer.music.pause()
                        playPause()

        pygame.display.update()

def playPause():

    playButtonMusic = Button(
        images=ressources.playButtonMuteMusic,
        pos=(screen_width * 0.5, screen_height * 0.1),
        text_input=None, font=None, base_color=None, hovering_color=None)
    playSoundOn = True

    playButtonTest = Button(
        images=ressources.playButtonMuteMusic,
        pos=(screen_width * 0.5, screen_height * 0.5),
        text_input=None, font=None, base_color=None, hovering_color=None)


    while True:
        screen.blit(background, (0, 0))
        playMousePosition = pygame.mouse.get_pos()

        for button in [playButtonMusic, playButtonTest]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButtonMusic.checkForInput(playMousePosition):
                    if playSoundOn:
                        playButtonMusic.setImages(ressources.playButtonMuteMusic)
                        pygame.mixer.music.unpause()
                        playListening()

                if playButtonTest.checkForInput(playMousePosition):
                    attribution_points()

        pygame.display.update()


def lobby():
    global listeVignettes
    global listeJoueurs

    listeVignettes.append(VignetteJoueur(ressources.screen_width * 0.586, ressources.screen_height * 0.145))
    listeVignettes.append(VignetteJoueur(ressources.screen_width * 0.697, ressources.screen_height * 0.145))

    difficulty = ["FACILE", "MOYEN", "DIFFICILE"]
    difficulty_lvl = 0
    nbrRounds = 1

    lobbyTitreOption = ressources.get_font(ressources.nunitoRegular,
                                           round(ressources.screen_height * 0.052)).render("OPTIONS", True, "white")
    lobbyTitreOption_Rect = lobbyTitreOption.get_rect(
        center=(ressources.screen_width * 0.270, ressources.screen_height * 0.116))

    lobbyOptionButtonNbrJoueursPlus = Button(
        images=ressources.lobbyButtonPlus,
        pos=(ressources.screen_width * 0.358, ressources.screen_height * 0.324),
        text_input=None, font=None, base_color=None, hovering_color=None)

    lobbyOptionButtonNbrJoueursMoins = Button(
        images=ressources.lobbyButtonMoins,
        pos=(ressources.screen_width * 0.228, ressources.screen_height * 0.324),
        text_input=None, font=None, base_color=None, hovering_color=None)

    lobbyOptionButtonDiffPlus = Button(
        images=ressources.lobbyButtonPlus,
        pos=(ressources.screen_width * 0.358, ressources.screen_height * 0.521),
        text_input=None, font=None, base_color=None, hovering_color=None)

    lobbyOptionButtonDiffMoins = Button(
        images=ressources.lobbyButtonMoins,
        pos=(ressources.screen_width * 0.228, ressources.screen_height * 0.521),
        text_input=None, font=None, base_color=None, hovering_color=None)

    lobbyOptionButtonRoundPlus = Button(
        images=ressources.lobbyButtonPlus,
        pos=(ressources.screen_width * 0.358, ressources.screen_height * 0.718),
        text_input=None, font=None, base_color=None, hovering_color=None)

    lobbyOptionButtonRoundMoins = Button(
        images=ressources.lobbyButtonMoins,
        pos=(ressources.screen_width * 0.228, ressources.screen_height * 0.718),
        text_input=None, font=None, base_color=None, hovering_color=None)

    lobbyButtonBack = Button(
        images=ressources.lobbyButtonBack,
        pos=(ressources.screen_width * 0.052, ressources.screen_height * 0.920),
        text_input=None, font=None, base_color=None, hovering_color=None)

    lobbyButtonPlay = Button(
        images=ressources.lobbyButtonPlay,
        pos=(ressources.screen_width * 0.596, ressources.screen_height * 0.914),
        text_input="PLAY",
        font=ressources.get_font(ressources.nunitoRegular, round(screen_width * 0.055)),
        base_color="White",
        hovering_color="#6DC300")

    while True:
        lobbyMousePosition = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        volume_bar.draw(screen)

        num_players = len(listeVignettes)
        for i, vignette in enumerate(listeVignettes):
            vignette.afficher(screen)

        # Fenetre des options
        screen.blit(ressources.lobbyWindowOption1, (ressources.screen_width * 0.091, ressources.screen_height * 0.058))

        # Titre

        screen.blit(lobbyTitreOption, lobbyTitreOption_Rect)

        # Options du nombre de joueurs
        screen.blit(ressources.lobbyWindowOption2, (ressources.screen_width * 0.117, ressources.screen_height * 0.231))
        screen.blit(ressources.lobbyIconPlayers, (ressources.screen_width * 0.124, ressources.screen_height * 0.249))
        lobbyTitreOptionNbrJoueurs = ressources.get_font(ressources.nunitoRegular,
                                                         round(ressources.screen_height * 0.029)).render(
            f"Nombre de joueurs",
            True,
            "#CC191C")
        lobbyTitreOptionNbrJoueurs_Rect = lobbyTitreOptionNbrJoueurs.get_rect(
            center=(ressources.screen_width * 0.286, ressources.screen_height * 0.266))
        screen.blit(lobbyTitreOptionNbrJoueurs, lobbyTitreOptionNbrJoueurs_Rect)

        lobbyDataNombreJoueurs = ressources.get_font(ressources.nunitoRegular,
                                                     round(ressources.screen_height * 0.029)).render(f"{num_players}",
                                                                                                     True,
                                                                                                     "#CC191C")
        lobbyDataNombreJoueurs_Rect = lobbyDataNombreJoueurs.get_rect(
            center=(ressources.screen_width * 0.293, ressources.screen_height * 0.324))
        screen.blit(lobbyDataNombreJoueurs, lobbyDataNombreJoueurs_Rect)


        # Option difficulté
        screen.blit(ressources.lobbyWindowOption2, (ressources.screen_width * 0.117, ressources.screen_height * 0.428))
        screen.blit(ressources.lobbyIconDifficulty, (ressources.screen_width * 0.124, ressources.screen_height * 0.446))

        lobbyTitreOptionDifficulte = ressources.get_font(ressources.nunitoRegular, round(screen_height * 0.029)).render(
            f"Difficulté", True,
            "#CC191C")
        lobbyTitreOptionDifficulte_Rect = lobbyTitreOptionDifficulte.get_rect(
            center=(ressources.screen_width * 0.286, ressources.screen_height * 0.463))
        screen.blit(lobbyTitreOptionDifficulte, lobbyTitreOptionDifficulte_Rect)

        lobbyDataLvlDifficulte = ressources.get_font(ressources.nunitoRegular, round(screen_height * 0.029)).render(
            f"{difficulty[difficulty_lvl]}", True,
            "#CC191C")
        lobbyDataLvlDifficulte_Rect = lobbyDataLvlDifficulte.get_rect(
            center=(ressources.screen_width * 0.293, ressources.screen_height * 0.521))
        screen.blit(lobbyDataLvlDifficulte, lobbyDataLvlDifficulte_Rect)

        # Option nombres de rounds
        screen.blit(ressources.lobbyWindowOption2, (ressources.screen_width * 0.117, ressources.screen_height * 0.625))
        screen.blit(ressources.lobbyIconRounds, (ressources.screen_width * 0.124, ressources.screen_height * 0.643))

        lobbyTitreOptionRounds = ressources.get_font(ressources.nunitoRegular, round(screen_height * 0.029)).render(
            f"Nombre de manches", True,
            "#CC191C")
        lobbyTitreOptionRounds_Rect = lobbyTitreOptionRounds.get_rect(
            center=(ressources.screen_width * 0.286, ressources.screen_height * 0.660))
        screen.blit(lobbyTitreOptionRounds, lobbyTitreOptionRounds_Rect)

        lobbyDataRounds = ressources.get_font(ressources.nunitoRegular, round(screen_height * 0.029)).render(
            f"{nbrRounds}", True,
            "#CC191C")
        lobbyDataRounds_Rect = lobbyDataRounds.get_rect(
            center=(ressources.screen_width * 0.293, ressources.screen_height * 0.718))
        screen.blit(lobbyDataRounds, lobbyDataRounds_Rect)

        for button in [lobbyButtonBack, lobbyButtonPlay,
                       lobbyOptionButtonRoundMoins, lobbyOptionButtonRoundPlus,
                       lobbyOptionButtonDiffMoins, lobbyOptionButtonDiffPlus,
                       lobbyOptionButtonNbrJoueursPlus, lobbyOptionButtonNbrJoueursMoins]:
            button.changeColor(lobbyMousePosition)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for vignette in listeVignettes:
                vignette.text.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for vignette in listeVignettes:

                    if vignette.icon_croix.checkForInput(lobbyMousePosition) and len(listeVignettes) > 2:
                        index_suppr = listeVignettes.index(vignette)
                        listeVignettes.remove(vignette)
                        for k in range(0, len(listeVignettes)):
                            if k >= index_suppr:
                                listeVignettes[k].realigner(k)

                    if vignette.personnage_image.checkForInput(lobbyMousePosition):
                        if event.button == 3:
                            vignette.changer_personnageAvant()
                        else:
                            vignette.changer_personnageApres()

                if lobbyButtonBack.checkForInput(lobbyMousePosition):
                    listeVignettes = []
                    main_menu()

                if lobbyButtonPlay.checkForInput(lobbyMousePosition):
                    for vignette in listeVignettes:
                        listeJoueurs.append(player.Player(vignette.text))
                    playListening()

                if lobbyOptionButtonNbrJoueursPlus.checkForInput(lobbyMousePosition):
                    if len(listeVignettes) < 9:
                        lobbyOptionButtonNbrJoueursPlus.press(screen)
                        nouvelle_vignette = VignetteJoueur(ressources.screen_width * 0.586 + (
                                    len(listeVignettes) % 3) * ressources.screen_width * 0.111,
                                                           ressources.screen_height * 0.145 + (
                                                                       len(listeVignettes) // 3) * ressources.screen_height * 0.231)
                        listeVignettes.append(nouvelle_vignette)

                if lobbyOptionButtonNbrJoueursMoins.checkForInput(lobbyMousePosition):
                    if len(listeVignettes) > 2:
                        lobbyOptionButtonNbrJoueursMoins.press(screen)
                        listeVignettes.pop()

                if lobbyOptionButtonDiffPlus.checkForInput(lobbyMousePosition):
                    if difficulty_lvl < 2:
                        lobbyOptionButtonDiffPlus.press(screen)
                        difficulty_lvl += 1
                if lobbyOptionButtonDiffMoins.checkForInput(lobbyMousePosition):
                    if difficulty_lvl > 0:
                        lobbyOptionButtonDiffMoins.press(screen)
                        difficulty_lvl -= 1

                if lobbyOptionButtonRoundPlus.checkForInput(lobbyMousePosition):
                    if nbrRounds < 5:
                        lobbyOptionButtonRoundPlus.press(screen)
                        nbrRounds += 1

                if lobbyOptionButtonRoundMoins.checkForInput(lobbyMousePosition):
                    if nbrRounds > 1:
                        lobbyOptionButtonRoundMoins.press(screen)
                        nbrRounds -= 1

            volume_bar.handle_event(event, mousePosition=lobbyMousePosition, screen=screen)

        pygame.display.update()


def main_menu():
    if not mixer.music.get_busy():
        mixer.music.play()

    current_image_index_floss = 0
    liste_image_floss = ressources.menuGIF

    elapsed_time1 = 0

    menuButtonPlay = Button(images=ressources.menuPlayButton, pos=(screen_width * 0.25, screen_height * 0.500),
                            text_input="PLAY",
                            font=ressources.get_font(ressources.nunitoRegular, round(screen_width * 0.055)),
                            base_color="White",
                            hovering_color="#6DC300")

    menuButtonQuit = Button(images=ressources.menuQuitButton, pos=(screen_width * 0.250, screen_height * 0.700),
                            text_input="QUIT",
                            font=ressources.get_font(ressources.nunitoRegular, round(screen_width * 0.055)),
                            base_color="White",
                            hovering_color="#CC191C")

    while True:

        menuMousePosition = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))
        screen.blit(ressources.menuLogo,
                    (ressources.screen_width * 0.228, ressources.screen_height * 0.046))
        volume_bar.draw(screen)

        for button in [menuButtonPlay, menuButtonQuit]:
            button.changeColor(menuMousePosition)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuButtonPlay.checkForInput(menuMousePosition):
                    menuButtonPlay.press(screen)
                    lobby()
                if menuButtonQuit.checkForInput(menuMousePosition):
                    menuButtonQuit.press(screen)
                    pygame.quit()
                    sys.exit()

            if event.type == USEREVENT:
                elapsed_time1 += 0.08
                if elapsed_time1 >= 15:
                    screen.blit(liste_image_floss[current_image_index_floss],
                                (screen_width * 0.571, screen_height * 0.400))
                    current_image_index_floss = (current_image_index_floss + 1) % 18

                pygame.display.update()

            volume_bar.handle_event(event, mousePosition=menuMousePosition, screen=screen)


mixer.music.unload()
mixer.music.load("assets/AC theme.mp3")
mixer.music.set_volume(0.5)
time.set_timer(USEREVENT, 80)

main_menu()
