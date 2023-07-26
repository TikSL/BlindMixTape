import pygame, sys
from pygame import mixer

from button import Button

pygame.init()

# Définir la taille de la fenêtre
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("BlindMixTape")

# Charger l'image de fond
BG = pygame.image.load("assets/Background.png")

NunitoRegular = "assets/Nunito/static/Nunito-Regular.ttf"
def get_font(size):  # Fonction pour obtenir la police Press-Start-2P à la taille désirée
    return pygame.font.Font(NunitoRegular, size)

def play():
    num_players = 1  # Variable pour le nombre de joueurs, initialisée à 1
    difficulty = 1  # Variable pour le niveau de difficulté, initialisée à 1

    while True:
        # Obtenir la position de la souris
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # Remplir l'écran en noir
        SCREEN.fill("#C4BBAF")

        # Afficher le texte "This is the PLAY screen." centré
        PLAY_TEXT = get_font(45).render("Nouvelle partie", True, "#5C4742")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(200, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # Créer un bouton "BACK" avec un effet de changement de couleur au survol
        PLAY_BACK = Button(image=pygame.image.load("assets/home.png"), pos=(180, 660),
                           text_input="", font=get_font(10), base_color="White", hovering_color="Green")

        # Changer la couleur du bouton "BACK" en fonction du survol de la souris
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        # Afficher et mettre à jour le bouton "BACK"
        PLAY_BACK.update(SCREEN)

        # Décalage horizontal pour les options
        options_offset = 0

        # Créer des boutons pour ajouter un joueur, augmenter/diminuer le nombre et changer la difficulté
        ADD_PLAYER_BUTTON = Button(None, pos=(200 + options_offset, 200), text_input="Ajouter joueur", font=get_font(30),
                                   base_color="#d7fcd4", hovering_color="White")
        NUM_PLAYERS_BUTTON = Button(None, pos=(200 + options_offset, 300), text_input="Nombre de joueurs : 1", font=get_font(30),
                                    base_color="#d7fcd4", hovering_color="White")
        INCREASE_BUTTON = Button(None, pos=(200 + options_offset, 400), text_input="Augmenter", font=get_font(30),
                                 base_color="#d7fcd4", hovering_color="White")
        DECREASE_BUTTON = Button(None, pos=(400 + options_offset, 400), text_input="Diminuer", font=get_font(30),
                                 base_color="#d7fcd4", hovering_color="White")
        DIFFICULTY_BUTTON = Button(None, pos=(200 + options_offset, 500), text_input="Difficulté : 1", font=get_font(30),
                                   base_color="#d7fcd4", hovering_color="White")

        # Mettre à jour le texte des boutons en fonction des valeurs actuelles des variables
        NUM_PLAYERS_BUTTON.text_input = f"Nombre de joueurs : {num_players}"
        DIFFICULTY_BUTTON.text_input = f"Difficulté : {difficulty}"

        # Afficher et mettre à jour les boutons
        for button in [ADD_PLAYER_BUTTON, NUM_PLAYERS_BUTTON, INCREASE_BUTTON, DECREASE_BUTTON, DIFFICULTY_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si le bouton "BACK" est cliqué, retourner au menu principal
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                # Si le bouton "Ajouter joueur" est cliqué, augmenter le nombre de joueurs
                if ADD_PLAYER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    num_players += 1
                # Si le bouton "Augmenter" est cliqué, augmenter le nombre de joueurs
                if INCREASE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    num_players += 1
                # Si le bouton "Diminuer" est cliqué, diminuer le nombre de joueurs (minimum 1)
                if DECREASE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    num_players = max(1, num_players - 1)
                # Si le bouton "Difficulté" est cliqué, changer le niveau de difficulté (ici, nous utilisons une boucle entre 1 et 3)
                if DIFFICULTY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    difficulty = (difficulty % 3) + 1

        pygame.display.update()


def options():
    while True:
        # Obtenir la position de la souris
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        # Remplir l'écran en blanc
        SCREEN.fill("white")

        # Afficher le texte "This is the OPTIONS screen." centré
        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Créer un bouton "BACK" avec un effet de changement de couleur au survol
        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        # Changer la couleur du bouton "BACK" en fonction du survol de la souris
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        # Afficher et mettre à jour le bouton "BACK"
        OPTIONS_BACK.update(SCREEN)

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si le bouton "BACK" est cliqué, retourner au menu principal
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    mixer.music.play()
    while True:

        # Afficher l'image de fond
        SCREEN.blit(BG, (0, 0))

        # Obtenir la position de la souris
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Afficher le texte "MAIN MENU" centré
        BMT_TEXT = get_font(100).render("BlindMixTape", True, "#b68f40")
        BMT_RECT = BMT_TEXT.get_rect(center=(400, 100))

        # Afficher le texte "MAIN MENU" centré
        MENU_TEXT = get_font(100).render("Menu principal", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 230))

        # Créer les boutons "PLAY", "OPTIONS" et "QUIT" avec un effet de changement de couleur au survol
        PLAY_BUTTON = Button(image=None, pos=(280, 380),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        # OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
        #                         text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(None, pos=(280, 490),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        # Afficher le texte "MAIN MENU" et les boutons
        SCREEN.blit(BMT_TEXT, BMT_RECT)
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        # for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si le bouton "PLAY" est cliqué, aller au menu de jeu
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                # Si le bouton "OPTIONS" est cliqué, aller au menu des options
                # if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                #     options()
                # Si le bouton "QUIT" est cliqué, quitter le jeu
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


mixer.music.unload()
mixer.music.load("assets/AC theme.mp3")
mixer.music.set_volume(0.5)

main_menu()
