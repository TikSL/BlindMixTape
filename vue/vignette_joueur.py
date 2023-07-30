import random
import pygame

import ressources
from button import Button
from zone_texte import TexteModifiable

font = "assets/Nunito/static/Nunito-Bold.ttf"


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
        self.text = TexteModifiable(self.x, self.y + 150 + 5)
        self.bufferPerso = random.choice(ressources.persos)
        self.personnage_image = Button(
            images=[pygame.transform.scale(pygame.image.load(self.bufferPerso), (100, 100))], pos=(self.x+75, self.y + 80),
            text_input=" ", font=ressources.get_font(ressources.nunitoRegular, 70),
            base_color="White",
            hovering_color="#6DC300")

    def afficher(self, screen):
        screen.blit(self.image, self.rect)
        self.text.afficher(screen)
        self.icon_croix.update(screen)
        self.personnage_image.update(screen)

    def realigner(self, k):
        self.x = 900 + (k % 3) * 170
        self.y = 125 + (k // 3) * 200
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.icon_croix.setPos(pos=(self.x + 150 - 5, self.y + 5))
        self.personnage_image.setPos(pos=(self.x+75, self.y + 80))
        self.text.setPos(pos=(self.x, self.y + 150 + 5))

    def changer_personnageApres(self):
        self.bufferPerso = ressources.persos[(ressources.persos.index(self.bufferPerso) + 1)%20]
        self.personnage_image.setImages([pygame.transform.scale(pygame.image.load(self.bufferPerso), (100, 100))])
        self.personnage_image.setPos(pos=(self.x + 75, self.y + 80))

    def changer_personnageAvant(self):
        self.bufferPerso = ressources.persos[(ressources.persos.index(self.bufferPerso) - 1)%20]
        self.personnage_image.setImages([pygame.transform.scale(pygame.image.load(self.bufferPerso), (100, 100))])
        self.personnage_image.setPos(pos=(self.x + 75, self.y + 80))