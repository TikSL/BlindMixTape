# Ressources générales
import pygame

background = "assets/windows/Window_10.png"

nunitoRegular = "assets/Nunito/static/Nunito-Bold.ttf"
BubbleFont = "assets/bubble3D.ttf"

# Menu Principal

menuGIF = [pygame.transform.scale(pygame.image.load(f"assets/GIF_dance/frame_{i}_delay-0.08s.gif"), (300, 300)) for i in range(18)]
menuPlayButton = [pygame.transform.scale(pygame.image.load("assets/buttons/Button_14.png"), (427 / 1.5, 190 / 1.5))]
menuQuitButton = [pygame.transform.scale(pygame.image.load("assets/buttons/Button_15.png"), (427 / 1.5, 190 / 1.5))]

# Lobby

lobbyWindowOption1 = pygame.transform.scale(pygame.image.load("assets/windows/Window_24.png"), (550, 750))
lobbyWindowOption2 = pygame.image.load("assets/windows/Window_35.png")
lobbyIconPlayers = pygame.transform.scale(pygame.image.load("assets/buttons/Button_98.png"), (111, 106))
lobbyIconDifficulty = pygame.transform.scale(pygame.image.load("assets/buttons/Button_29.png"), (111, 106))

lobbyButtonPlus = [pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Button2_50.png"), (60, 60)),
        pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Frame2.png"), (60, 60)),
        pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Frame3.png"), (60, 60)),
        pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Frame4.png"), (60, 60))]

lobbyButtonMoins = [pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Button2_50.png"), (60, 60)),
        pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Frame2.png"), (60, 60)),
        pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Frame3.png"), (60, 60)),
        pygame.transform.scale(pygame.image.load("assets/buttons/Bouton50/Frame4.png"), (60, 60))]

lobbyButtonBack = [pygame.transform.scale(pygame.image.load("assets/buttons/Button_50.png"), (100, 100))]

lobbyButtonPlay = [pygame.transform.scale(pygame.image.load("assets/buttons/Button_14.png"), (427 / 1.5, 190 / 1.5))]

# Play


