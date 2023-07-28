import pygame
import sys


class VolumeBar:
    def __init__(self, x, y, width, height, min_volume=0.0, max_volume=1.0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_volume = min_volume
        self.max_volume = max_volume
        self.current_volume = 0.5  # Volume initial (0.5 = 50%)
        self.is_dragging = False

        # Charger les images de la barre de volume (vous pouvez les remplacer par vos images)
        self.volume_fill = pygame.transform.scale(pygame.image.load("assets/windows/Window_66.png"), (self.width, self.height))
        self.volume_bar = pygame.transform.scale(pygame.image.load("assets/windows/Window_65.png"), (self.width, self.height))
        self.volume_icon = pygame.transform.scale(pygame.image.load("assets/buttons/Button2_25.png"), (self.height*2, self.height*2))

    def draw(self, surface):
        # Afficher les éléments de la barre de volume sur l'écran
        surface.blit(self.volume_fill, (self.x, self.y))  # Afficher la barre de volume remplie

        # Redimensionner la barre de volume en fonction du volume actuel
        volume_bar_width = int(self.current_volume * self.width)
        volume_bar_current = pygame.transform.scale(self.volume_bar.subsurface((0, 0, volume_bar_width, self.height)),
                                                    (volume_bar_width, self.height))
        surface.blit(volume_bar_current, (self.x, self.y))  # Afficher la barre de volume actuelle

        # Afficher l'icône du volume
        # Afficher l'icône du volume à côté de la barre
        surface.blit(self.volume_icon,
                     (self.x - 70, self.y + self.height // 2 - self.volume_icon.get_height() // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                mouse_x, mouse_y = event.pos
                if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                    self.is_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Clic gauche
                self.is_dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.is_dragging:
                mouse_x, _ = event.pos
                # Limiter la position de la souris à l'intérieur de la barre de volume
                mouse_x = min(max(mouse_x, self.x), self.x + self.width)
                # Calculer le volume en fonction de la position de la souris sur la barre
                relative_x = mouse_x - self.x
                volume_ratio = relative_x / self.width
                self.current_volume = self.min_volume + volume_ratio * (self.max_volume - self.min_volume)
                # Ajuster le volume de la musique
                pygame.mixer.music.set_volume(self.current_volume)



