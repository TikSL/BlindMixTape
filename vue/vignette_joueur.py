import random

import pygame

font = "assets/Nunito/static/Nunito-Bold.ttf"


class VignetteJoueur:

    positionNouveau = 2

    def __init__(self, x, y):
        self.nom_joueur = "???"
        self.image = pygame.transform.scale(pygame.image.load("assets/windows/Window_13.png"), (150, 150))
        self.icon_croix = pygame.transform.scale(pygame.image.load("assets/buttons/Button_23.png"), (30, 30))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.icon_croix_rect = self.icon_croix.get_rect(topright=(self.rect.right - 5, self.rect.y + 5))
        self.text = pygame.font.Font(font, 25).render(self.nom_joueur, True, "white")
        self.text_rect = self.text.get_rect(center=(x + 150 // 2, y + 150 + 12))
        self.position = self.positionNouveau
        self.personnage_image = pygame.transform.scale(pygame.image.load(f"assets/perso/perso_{random.randint(1, 9)}.png"),(100, 100))
        self.personnage_image_rect = self.personnage_image.get_rect(center=(self.x + 75, self.y + 75 + 5))

    def afficher(self, screen):

        screen.blit(self.image, self.rect)
        screen.blit(self.icon_croix, self.icon_croix_rect)
        screen.blit(self.text, self.text_rect)
        screen.blit(self.personnage_image, self.personnage_image_rect)


    def check_clic(self, position):
        if self.icon_croix_rect.collidepoint(position):
            return 1
        elif self.rect.collidepoint(position):
            print("clic image")
            return 2
        return 3

    def realigner_vignette(self):
        print(self.position, self.x, self.y, self.nom_joueur)
        self.position -= 1
        self.x = 900 + (self.position % 3) * 170
        self.y = 150 + (self.position // 3) * 200
        print(self.position, self.x, self.y, self.nom_joueur)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.icon_croix_rect = self.icon_croix.get_rect(topright=(self.rect.right - 5, self.rect.y + 5))
        self.text = pygame.font.Font(font, 25).render(self.nom_joueur, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x + 150 // 2, self.y + 150 + 12))
        self.personnage_image = pygame.transform.scale(
            pygame.image.load(f"assets/perso/perso_{random.randint(1, 9)}.png"), (100, 100))
        self.personnage_image_rect = self.personnage_image.get_rect(center=(self.x + 75, self.y + 75 + 5))

    def changer_personnage(self):
        perso_file = f"assets/perso/perso_{random.randint(1, 9)}.png"
        self.personnage_image = pygame.transform.scale(pygame.image.load(perso_file),(100, 100))
        self.personnage_image_rect = self.personnage_image.get_rect(center=(self.x + 75, self.y + 75 + 5))
