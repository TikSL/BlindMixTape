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
        self.icon_croix = Button(images=ressources.vignetteButtonCroix,
                                 pos=(self.x + (0.094 * ressources.screen_width), self.y +
                                      (0.003 * ressources.screen_height)),
                                 text_input=" ", font=ressources.get_font(ressources.nunitoRegular,
                                                                          round(0.081 * ressources.screen_height)),
                                 base_color="White",
                                 hovering_color="#6DC300")
        self.text = TexteModifiable(self.x, self.y + (0.179*ressources.screen_height))
        self.bufferPerso = random.choice(ressources.persos)
        self.personnage_image = Button(
            images=[pygame.transform.scale(pygame.image.load(self.bufferPerso),
                                           (0.065 * ressources.screen_width, 0.116 * ressources.screen_height))],
            pos=(self.x + (0.049*ressources.screen_width), self.y + (0.093*ressources.screen_height)),
            text_input=" ", font=ressources.get_font(ressources.nunitoRegular, round(0.179*ressources.screen_height)),
            base_color="White",
            hovering_color="#6DC300")

    def afficher(self, screen):
        screen.blit(self.image, self.rect)
        self.text.afficher(screen)
        self.icon_croix.update(screen)
        self.personnage_image.update(screen)

    def realigner(self, k):
        self.x = 0.586 * ressources.screen_width + (k % 3) * 0.197 * ressources.screen_height
        self.y = 0.081 * ressources.screen_width + (k // 3) * 0.231 * ressources.screen_height
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.icon_croix.setPos(pos=(self.x + (0.094 * ressources.screen_width), self.y +
                                    (0.003 * ressources.screen_height)))
        self.personnage_image.setPos(pos=(self.x + (0.049 * ressources.screen_width), self.y +
                                          (0.093 * ressources.screen_height)))
        self.text.setPos(pos=(self.x, self.y + (0.179 * ressources.screen_height)))

    def changer_personnageApres(self):
        self.bufferPerso = ressources.persos[(ressources.persos.index(self.bufferPerso) + 1) % 20]
        self.personnage_image.setImages([pygame.transform.scale(pygame.image.load(self.bufferPerso),
                                                                (0.065 * ressources.screen_width, 0.116 *
                                                                 ressources.screen_height))])
        self.personnage_image.setPos(pos=(self.x + (0.049 * ressources.screen_width),
                                          self.y + (0.093 * ressources.screen_height)))

    def changer_personnageAvant(self):
        self.bufferPerso = ressources.persos[(ressources.persos.index(self.bufferPerso) - 1) % 20]
        self.personnage_image.setImages([pygame.transform.scale(pygame.image.load(self.bufferPerso),
                                                                (0.065 * ressources.screen_width, 0.116 *
                                                                 ressources.screen_height))])
        self.personnage_image.setPos(pos=(self.x + (0.049 * ressources.screen_width),
                                          self.y + (0.093 * ressources.screen_height)))