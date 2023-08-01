import pygame

import ressources
from button import Button


class MusicBar:
    def __init__(self, x, y, width, height, total_time):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.total_time = total_time
        self.current_time = 0
        self.is_playing = False

        # Créer le bouton Play/Mute
        self.play_button = Button(
            images=ressources.playButtonPlayMusic,
            pos=(x, y),
            text_input=" ", font=ressources.get_font(ressources.nunitoRegular, round(0.179*ressources.screen_height)), base_color="White", hovering_color="Green")

    def update(self, elapsed_time, screen):
        if self.is_playing:
            self.current_time += elapsed_time
            if self.current_time >= self.total_time:
                # La musique est terminée
                self.current_time = self.total_time
                self.is_playing = False

        # Mettre à jour la barre de musique en fonction du temps actuel
        bar_length = int(self.width * (self.current_time / self.total_time))
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, bar_length, self.height))

        # Mettre à jour le bouton Play/Mute
        self.play_button.update(screen)

    def handle_event(self, event,screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button.checkForInput(pygame.mouse.get_pos()):
                # Inverser l'état du bouton Play/Mute
                if self.is_playing:
                    self.play_button.setImages(ressources.playButtonMuteMusic)
                else:
                    self.play_button.setImages(ressources.playButtonPlayMusic)
                self.is_playing = not self.is_playing
                self.play_button.update(screen)

    def set_total_time(self, total_time):
        self.total_time = total_time
