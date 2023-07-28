import pygame
import sys
from pygame import mixer, time, USEREVENT

from button import Button
from volume_bar import VolumeBar

pygame.init()

screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Définir la taille de la fenêtre en utilisant les dimensions de l'écran
SCREEN = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("BlindMixTape")

# Charger l'image de fond en utilisant les dimensions de l'écran
BG = pygame.transform.scale(pygame.image.load("assets/windows/Window_10.png"), (screen_width, screen_height))
BUTTON_PLAY = [pygame.transform.scale(pygame.image.load("assets/buttons/Button_14.png"), (427 / 1.5, 190 / 1.5))]
BUTTON_QUIT = [pygame.transform.scale(pygame.image.load("assets/buttons/Button_15.png"), (427 / 1.5, 190 / 1.5))]

NunitoRegular = "assets/Nunito/static/Nunito-Bold.ttf"
BubbleFont = "assets/bubble3D.ttf"

volume_bar = VolumeBar(screen_width - 300, screen_height - 100, 200, 30)


def get_font(font, size):  # Fonction pour obtenir la police Press-Start-2P à la taille désirée
    return pygame.font.Font(font, size)


def play():
    num_players = 2
    difficulty = ["FACILE", "MOYEN", "DIFFICILE"]
    difficulty_lvl = 0

    while True:

        # Obtenir la position de la souris
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))
        volume_bar.draw(SCREEN)

        # Fenetre des options
        SCREEN.blit(pygame.transform.scale(pygame.image.load("assets/windows/Window_24.png"), (550, 750)), (140, 50))

        # Titre
        OPTIONS_TEXT = get_font(NunitoRegular, 45).render("OPTIONS", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(415, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Options du nombre de joueurs
        SCREEN.blit(pygame.image.load("assets/windows/Window_35.png"), (180, 200))
        SCREEN.blit(pygame.transform.scale(pygame.image.load("assets/buttons/Button_98.png"), (111, 106)), (190, 215))

        JOUEURS_TEXT = get_font(NunitoRegular, 25).render(f"Nombre de joueurs", True, "#CC191C")
        JOUEURS_RECT = JOUEURS_TEXT.get_rect(center=(440, 230))
        SCREEN.blit(JOUEURS_TEXT, JOUEURS_RECT)

        NBR_JOUEURS_TEXT = get_font(NunitoRegular, 25).render(f"{num_players}", True, "#CC191C")
        NBR_JOUEURS_RECT = NBR_JOUEURS_TEXT.get_rect(center=(450, 280))
        SCREEN.blit(NBR_JOUEURS_TEXT, NBR_JOUEURS_RECT)
        #
        # PLAY_PLAYER_PLUS = Button(
        #     images=[pygame.transform.scale(pygame.image.load("assets/buttons/Button2_53.png"), (60, 60))],
        #     pos=(550, 280),
        #     text_input="", font=get_font(NunitoRegular, 10), base_color="White", hovering_color="Green")

        PLAY_PLAYER_PLUS = Button(
            images=[pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Button2_50.png"), (60, 60)),
        pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Frame2.png"), (60, 60)),
        pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Frame3.png"), (60, 60)),
        pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Frame4.png"), (60, 60))],
            pos=(550, 280),
            text_input="", font=get_font(NunitoRegular, 10), base_color="White", hovering_color="Green")


        PLAY_PLAYER_PLUS.update(SCREEN)
        PLAY_PLAYER_LESS = Button(
            images=[pygame.transform.scale(pygame.image.load("assets/buttons/Button2_69.png"), (60, 60))],
            pos=(350, 280),
            text_input="", font=get_font(NunitoRegular, 10), base_color="White", hovering_color="Green")
        PLAY_PLAYER_LESS.update(SCREEN)

        # Option difficulté
        SCREEN.blit(pygame.image.load("assets/windows/Window_35.png"), (180, 370))
        SCREEN.blit(pygame.transform.scale(pygame.image.load("assets/buttons/Button_29.png"), (111, 106)), (190, 385))

        DIFF_TEXT = get_font(NunitoRegular, 25).render(f"Difficulté", True, "#CC191C")
        DIFF_RECT = DIFF_TEXT.get_rect(center=(440, 400))
        SCREEN.blit(DIFF_TEXT, DIFF_RECT)

        DIFF_LVL_TEXT = get_font(NunitoRegular, 25).render(f"{difficulty[difficulty_lvl]}", True, "#CC191C")
        DIFF_LVL_RECT = DIFF_LVL_TEXT.get_rect(center=(450, 450))
        SCREEN.blit(DIFF_LVL_TEXT, DIFF_LVL_RECT)

        DIFF_PLUS = Button(
            images=[pygame.transform.scale(pygame.image.load("assets/buttons/Button2_53.png"), (60, 60))],
            pos=(550, 450),
            text_input="", font=get_font(NunitoRegular, 10), base_color="White", hovering_color="Green")
        DIFF_PLUS.update(SCREEN)
        DIFF_LESS = Button(
            images=[pygame.transform.scale(pygame.image.load("assets/buttons/Button2_69.png"), (60, 60))],
            pos=(350, 450),
            text_input="", font=get_font(NunitoRegular, 10), base_color="White", hovering_color="Green")
        DIFF_LESS.update(SCREEN)

        # TODO Rajouter une option
        SCREEN.blit(pygame.image.load("assets/windows/Window_35.png"), (180, 540))

        # Retour menu principal
        PLAY_BACK = Button(
            images=[pygame.transform.scale(pygame.image.load("assets/buttons/Button_50.png"), (100, 100))],
            pos=(80, 795),
            text_input="", font=get_font(NunitoRegular, 10), base_color="White", hovering_color="Green")
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_PLAYER_PLUS.checkForInput(PLAY_MOUSE_POS):
                    if num_players < 9:
                        PLAY_PLAYER_PLUS.press(SCREEN)
                        num_players += 1
                if PLAY_PLAYER_LESS.checkForInput(PLAY_MOUSE_POS):
                    if num_players > 2:
                        num_players -= 1
                if DIFF_PLUS.checkForInput(PLAY_MOUSE_POS):
                    if difficulty_lvl < 2:
                        difficulty_lvl += 1
                if DIFF_LESS.checkForInput(PLAY_MOUSE_POS):
                    if difficulty_lvl > 0:
                        difficulty_lvl -= 1

            volume_bar.handle_event(event)
        pygame.display.update()


# def options():
#     while True:
#         # Obtenir la position de la souris
#         OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
#
#         # Remplir l'écran en blanc
#         SCREEN.fill("white")
#
#         # Afficher le texte "This is the OPTIONS screen." centré
#         OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
#         OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
#         SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
#
#         # Créer un bouton "BACK" avec un effet de changement de couleur au survol
#         OPTIONS_BACK = Button(images=None, pos=(640, 460),
#                               text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
#
#         # Changer la couleur du bouton "BACK" en fonction du survol de la souris
#         OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
#         # Afficher et mettre à jour le bouton "BACK"
#         OPTIONS_BACK.update(SCREEN)
#
#         # Gérer les événements
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 # Si le bouton "BACK" est cliqué, retourner au menu principal
#                 if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
#                     main_menu()
#
#         pygame.display.update()

def main_menu():
    if not mixer.music.get_busy():
        mixer.music.play()

    current_image_index_floss = 0
    # current_image_index_alien = 0
    liste_image_floss = [
        pygame.transform.scale(pygame.image.load(f"assets/GIF_dance/frame_{i}_delay-0.08s.gif"), (300, 300)) for i in
        range(18)]
    # liste_image_alien_dance = [pygame.transform.scale(pygame.image.load(f"assets/GIF_alien/frame_{
    # i}_delay-0.04s.gif"), (100, 100)) for i in range(75)]
    time.set_timer(USEREVENT, 80)
    # time.set_timer(USEREVENT + 1, 40)
    elapsed_time1 = 0
    # elapsed_time2 = 0

    while True:

        # Afficher l'image de fond
        SCREEN.blit(BG, (0, 0))
        volume_bar.draw(SCREEN)

        # Obtenir la position de la souris
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Afficher le texte "MAIN MENU" centré
        SCREEN.blit(pygame.image.load("assets/logo.png"), (350, 100))
        # Créer les boutons "PLAY", "OPTIONS" et "QUIT" avec un effet de changement de couleur au survol
        PLAY_BUTTON = Button(images=BUTTON_PLAY, pos=(screen_width / 4, screen_height * 0.5),
                             text_input="PLAY", font=get_font(NunitoRegular, 70), base_color="White",
                             hovering_color="#6DC300")
        # OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
        #                         text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(images=BUTTON_QUIT, pos=(screen_width / 4, screen_height * 0.7),
                             text_input="QUIT", font=get_font(NunitoRegular, 70), base_color="White",
                             hovering_color="#CC191C")

        # Afficher le texte "MAIN MENU" et les boutons

        # for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        #
        # SCREEN.blit(volume_fill, (1080, 775))
        # SCREEN.blit(volume_bar, (1092, 780))
        # SCREEN.blit(volume_icon, (990, 760))

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

            if event.type == USEREVENT:
                elapsed_time1 += 0.08
                if elapsed_time1 >= 15:
                    SCREEN.blit(liste_image_floss[current_image_index_floss],
                                (screen_width * 4 / 7, screen_height * 0.4))
                    current_image_index_floss = (current_image_index_floss + 1) % 18

                pygame.display.update()

            volume_bar.handle_event(event)


mixer.music.unload()
mixer.music.load("assets/AC theme.mp3")
mixer.music.set_volume(0.5)

main_menu()
