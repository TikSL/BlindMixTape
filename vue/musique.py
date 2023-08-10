import pygame

import ressources
from button import Button


font = ressources.get_font(ressources.nunitoRegular, round(ressources.screen_width * 0.055))


class Musique:
    def __init__(self, titre, artiste, points, refCover, pos, ):
        self.font = font
        self.x = pos[0]
        self.y = pos[1]
        self.titre = titre
        self.textTitre, self.textRectTitre = self.__generationTexte__(titre, pos=(self.x+10, self.y))
        self.artiste = artiste
        self.textArtiste, self.textRectArtiste = self.__generationTexte__(artiste, pos=(self.x+10, self.y + 30))
        self.points = points
        self.refCover = refCover
        self.cover = pygame.transform.scale(pygame.image.load(self.refCover), (
        ressources.screen_width * 0.100, ressources.screen_height * 0.178))
        self.coverAffiche = Button(images=[self.cover], pos=pos, text_input=None, font=None, base_color=None, hovering_color=None)

    def __generationTexte__(self, texte, pos):
        text = self.font.render(texte, True, "black")
        textRect = text.get_rect(center=(pos[0], pos[1]))
        return text, textRect

    def update(self, screen):
        self.coverAffiche.update(screen=screen)
        screen.blit(self.textTitre, self.textRectTitre)
        screen.blit(self.textArtiste, self.textRectArtiste)
