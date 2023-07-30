import random
import pygame

import ressources
from button import Button
from zone_texte import TexteModifiable

font = "assets/Nunito/static/Nunito-Bold.ttf"


def piocherPerso():
    return pygame.transform.scale(pygame.image.load(f"assets/perso/perso_{random.randint(1, 16)}.png"), (100, 100))


class VignetteJoueur:

    def __init__(self, x, y):
        self.nom_joueur = "???"
        self.image = ressources.vignetteFond
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.icon_croix = Button(images=ressources.vignetteButtonCroix, pos=(self.x + 145, self.y + 5),
                                 text_input=" ", font=ressources.get_font(ressources.nunitoRegular, 70),
                                 base_color="White",
                                 hovering_color="#6DC300")

        # self.icon_croix_rect = self.icon_croix.get_rect(topright=(self.rect.right - 5, self.rect.y + 5))
        # self.text = pygame.font.Font(font, 25).render(self.nom_joueur, True, "white")
        # self.text_rect = self.text.get_rect(center=(x + 150 // 2, y + 150 + 12))
        self.text = TexteModifiable(self.x, self.y + 150 + 5)
        self.personnage_image = Button(
            images=[piocherPerso()], pos=(self.x+75, self.y + 80),
            text_input=" ", font=ressources.get_font(ressources.nunitoRegular, 70),
            base_color="White",
            hovering_color="#6DC300")
        # self.personnage_image = piocherPerso()
        # self.personnage_image_rect = self.personnage_image.get_rect(center=(self.x + 75, self.y + 75 + 5))

    def afficher(self, screen):
        screen.blit(self.image, self.rect)
        # screen.blit(self.text, self.text_rect)
        self.text.afficher(screen)
        self.icon_croix.update(screen)
        self.personnage_image.update(screen)
        # screen.blit(self.text, self.text_rect)
        # screen.blit(self.personnage_image, self.personnage_image_rect)

    # def check_clic(self, position):
    #     # if self.icon_croix_rect.collidepoint(position):
    #     #     return 1
    #     elif self.rect.collidepoint(position):
    #         return 2
    #     return 3

    def realigner_vignette(self, k):
        self.x = 900 + (k % 3) * 170
        self.y = 125 + (k // 3) * 200
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        # self.icon_croix_rect = self.icon_croix.get_rect(topright=(self.rect.right - 5, self.rect.y + 5))
        # self.text = pygame.font.Font(font, 25).render(self.nom_joueur, True, "white")
        # self.text_rect = self.text.get_rect(center=(self.x + 150 // 2, self.y + 150 + 12))
        # self.personnage_image_rect = self.personnage_image.get_rect(center=(self.x + 75, self.y + 75 + 5))
        self.icon_croix.setPos(pos=(self.x + 150 - 5, self.y + 5))
        self.personnage_image.setPos(pos=(self.x+75, self.y + 80))
        self.text.setPos(pos=(self.x, self.y + 150 + 5))

    def changer_personnage(self):
        self.personnage_image.setImages([piocherPerso()])
        self.personnage_image.setPos(pos=(self.x + 75, self.y + 80))
