import pygame
import sys
from pygame import mixer, time, USEREVENT

import ressources
from button import Button
from vignette_joueur import VignetteJoueur
from volume_bar import VolumeBar

pygame.init()

screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Définir la taille de la fenêtre en utilisant les dimensions de l'écran
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("BlindMixTape")

# Charger l'image de fond en utilisant les dimensions de l'écran
background = pygame.transform.scale(pygame.image.load(ressources.background), (screen_width, screen_height))
volume_bar = VolumeBar(screen_width - 300, screen_height - 100, 200, 30)


def play():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background, (0, 0))
        pygame.display.update()


def lobby():
    liste_vignettes = [VignetteJoueur(900, 150), VignetteJoueur(900 + 170, 150 + (1 // 3) * 200)]

    difficulty = ["FACILE", "MOYEN", "DIFFICILE"]
    difficulty_lvl = 0

    while True:
        num_players = len(liste_vignettes)

        # Obtenir la position de la souris
        lobbyMousePosition = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        volume_bar.draw(screen)
        for i, vignette in enumerate(liste_vignettes):
            vignette.afficher(screen)

        # Fenetre des options
        screen.blit(ressources.lobbyWindowOption1, (140, 50))

        # Titre
        lobbyTitreOption = ressources.get_font(ressources.nunitoRegular, 45).render("OPTIONS", True, "white")
        lobbyTitreOption_Rect = lobbyTitreOption.get_rect(center=(415, 100))
        screen.blit(lobbyTitreOption, lobbyTitreOption_Rect)

        # Options du nombre de joueurs
        screen.blit(ressources.lobbyWindowOption2, (180, 200))
        screen.blit(ressources.lobbyIconPlayers, (190, 215))
        lobbyTitreOptionNbrJoueurs = ressources.get_font(ressources.nunitoRegular, 25).render(f"Nombre de joueurs",
                                                                                              True,
                                                                                              "#CC191C")
        lobbyTitreOptionNbrJoueurs_Rect = lobbyTitreOptionNbrJoueurs.get_rect(center=(440, 230))
        screen.blit(lobbyTitreOptionNbrJoueurs, lobbyTitreOptionNbrJoueurs_Rect)

        lobbyDataNombreJoueurs = ressources.get_font(ressources.nunitoRegular, 25).render(f"{num_players}", True,
                                                                                          "#CC191C")
        lobbyDataNombreJoueurs_Rect = lobbyDataNombreJoueurs.get_rect(center=(450, 280))
        screen.blit(lobbyDataNombreJoueurs, lobbyDataNombreJoueurs_Rect)

        lobbyOptionButtonNbrJoueursPlus = Button(
            images=ressources.lobbyButtonPlus,
            pos=(550, 280),
            text_input="", font=ressources.get_font(ressources.nunitoRegular, 10), base_color="White",
            hovering_color="Green")

        lobbyOptionButtonNbrJoueursPlus.update(screen)

        lobbyOptionButtonNbrJoueursMoins = Button(
            images=ressources.lobbyButtonMoins,
            pos=(350, 280),
            text_input="",
            font=ressources.get_font(ressources.nunitoRegular, 10), base_color="White", hovering_color="Green")
        lobbyOptionButtonNbrJoueursMoins.update(screen)

        # Option difficulté
        screen.blit(ressources.lobbyWindowOption2, (180, 370))
        screen.blit(ressources.lobbyIconDifficulty, (190, 385))

        lobbyTitreOptionDifficulte = ressources.get_font(ressources.nunitoRegular, 25).render(f"Difficulté", True,
                                                                                              "#CC191C")
        lobbyTitreOptionDifficulte_Rect = lobbyTitreOptionDifficulte.get_rect(center=(440, 400))
        screen.blit(lobbyTitreOptionDifficulte, lobbyTitreOptionDifficulte_Rect)

        lobbyDataLvlDifficulte = ressources.get_font(ressources.nunitoRegular, 25).render(
            f"{difficulty[difficulty_lvl]}", True,
            "#CC191C")
        lobbyDataLvlDifficulte_Rect = lobbyDataLvlDifficulte.get_rect(center=(450, 450))
        screen.blit(lobbyDataLvlDifficulte, lobbyDataLvlDifficulte_Rect)

        lobbyOptionButtonDiffPlus = Button(
            images=ressources.lobbyButtonPlus,
            pos=(550, 450),
            text_input="", font=ressources.get_font(ressources.nunitoRegular, 10), base_color="White",
            hovering_color="Green")
        lobbyOptionButtonDiffPlus.update(screen)
        lobbyOptionButtonDiffMoins = Button(
            images=ressources.lobbyButtonMoins,
            pos=(350, 450),
            text_input="", font=ressources.get_font(ressources.nunitoRegular, 10), base_color="White",
            hovering_color="Green")
        lobbyOptionButtonDiffMoins.update(screen)

        # TODO Rajouter une option
        screen.blit(ressources.lobbyWindowOption2, (180, 540))

        # Retour menu principal
        lobbyButtonBack = Button(
            images=ressources.lobbyButtonBack,
            pos=(80, 795),
            text_input="", font=ressources.get_font(ressources.nunitoRegular, 10), base_color="White",
            hovering_color="Green")
        lobbyButtonBack.update(screen)

        lobbyButtonPlay = Button(images=ressources.lobbyButtonPlay, pos=(915, 790),
                                 text_input="PLAY", font=ressources.get_font(ressources.nunitoRegular, 70),
                                 base_color="White",
                                 hovering_color="#6DC300")

        for button in [lobbyButtonPlay]:
            button.changeColor(lobbyMousePosition)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for vignette in liste_vignettes:

                    if vignette.icon_croix.checkForInput(lobbyMousePosition) and len(liste_vignettes) > 2:
                        index_suppr = liste_vignettes.index(vignette)
                        liste_vignettes.remove(vignette)
                        for k in range(0, len(liste_vignettes)):
                            if k >= index_suppr:
                                liste_vignettes[k].realigner_vignette(k)

                    if vignette.personnage_image.checkForInput(lobbyMousePosition):
                        vignette.changer_personnage()

                if lobbyButtonBack.checkForInput(lobbyMousePosition):
                    main_menu()

                if lobbyButtonPlay.checkForInput(lobbyMousePosition):
                    play()

                if lobbyOptionButtonNbrJoueursPlus.checkForInput(lobbyMousePosition):
                    if len(liste_vignettes) < 9:
                        lobbyOptionButtonNbrJoueursPlus.press(screen)
                        nouvelle_vignette = VignetteJoueur(900 + (len(liste_vignettes) % 3) * 170,
                                                           150 + (len(liste_vignettes) // 3) * 200)
                        liste_vignettes.append(nouvelle_vignette)

                if lobbyOptionButtonNbrJoueursMoins.checkForInput(lobbyMousePosition):
                    if len(liste_vignettes) > 2:
                        lobbyOptionButtonNbrJoueursMoins.press(screen)
                        liste_vignettes.pop()

                if lobbyOptionButtonDiffPlus.checkForInput(lobbyMousePosition):
                    if difficulty_lvl < 2:
                        lobbyOptionButtonDiffPlus.press(screen)
                        difficulty_lvl += 1
                if lobbyOptionButtonDiffMoins.checkForInput(lobbyMousePosition):
                    if difficulty_lvl > 0:
                        lobbyOptionButtonDiffMoins.press(screen)
                        difficulty_lvl -= 1

            volume_bar.handle_event(event, lobbyMousePosition)
        pygame.display.update()


def main_menu():
    if not mixer.music.get_busy():
        mixer.music.play()

    current_image_index_floss = 0
    liste_image_floss = ressources.menuGIF

    time.set_timer(USEREVENT, 80)
    elapsed_time1 = 0

    while True:

        # Afficher l'image de fond
        screen.blit(background, (0, 0))
        volume_bar.draw(screen)

        # Obtenir la position de la souris
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Afficher le texte "MAIN MENU" centré
        screen.blit(pygame.image.load("assets/logo.png"), (350, 100))
        # Créer les boutons "PLAY", "OPTIONS" et "QUIT" avec un effet de changement de couleur au survol
        menuButtonPlay = Button(images=ressources.menuPlayButton, pos=(screen_width / 4, screen_height * 0.5),
                                text_input="PLAY", font=ressources.get_font(ressources.nunitoRegular, 70),
                                base_color="White",
                                hovering_color="#6DC300")
        # OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
        #                         text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        menuButtonQuit = Button(images=ressources.menuQuitButton, pos=(screen_width / 4, screen_height * 0.7),
                                text_input="QUIT", font=ressources.get_font(ressources.nunitoRegular, 70),
                                base_color="White",
                                hovering_color="#CC191C")

        # Afficher le texte "MAIN MENU" et les boutons

        for button in [menuButtonPlay, menuButtonQuit]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuButtonPlay.checkForInput(MENU_MOUSE_POS):
                    menuButtonPlay.press(screen)
                    lobby()
                if menuButtonQuit.checkForInput(MENU_MOUSE_POS):
                    menuButtonQuit.press(screen)
                    pygame.quit()
                    sys.exit()

            if event.type == USEREVENT:
                elapsed_time1 += 0.08
                if elapsed_time1 >= 15:
                    screen.blit(liste_image_floss[current_image_index_floss],
                                (screen_width * 4 / 7, screen_height * 0.4))
                    current_image_index_floss = (current_image_index_floss + 1) % 18

                pygame.display.update()

            volume_bar.handle_event(event, MENU_MOUSE_POS,screen)


mixer.music.unload()
mixer.music.load("assets/AC theme.mp3")
mixer.music.set_volume(0.5)

main_menu()
