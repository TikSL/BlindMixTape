import pygame

import button
import ressources


class VolumeBar:
    def __init__(self, x, y, width, height, min_volume=0.0, max_volume=1.0):
        self.bufferVolume = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_volume = min_volume
        self.max_volume = max_volume
        self.current_volume = 0.5  # Volume initial (0.5 = 50%)
        self.is_dragging = False

        # Charger les images de la barre de volume (vous pouvez les remplacer par vos images)
        self.volume_fill = pygame.transform.scale(pygame.image.load("view/assets/windows/Window_66.png"), (self.width, self.height))
        self.volume_bar = pygame.transform.scale(pygame.image.load("view/assets/windows/Window_65.png"), (self.width, self.height))
        #self.volume_icon = pygame.transform.scale(pygame.image.load("assets/buttons/Button2_25.png"), (self.height*2, self.height*2))
        self.volumeButton = button.Button(
            images=ressources.lobbySoundOn, pos=(self.x - 32, self.y + 15),
            text_input=" ", font=ressources.get_font(ressources.nunitoRegular, 70),
            base_color="White",
            hovering_color="#6DC300"
        )

    def draw(self, surface):
        surface.blit(self.volume_fill, (self.x, self.y))  # Afficher la barre de volume remplie

        volume_bar_width = int(self.current_volume * self.width)
        volume_bar_current = pygame.transform.scale(self.volume_bar.subsurface((0, 0, volume_bar_width, self.height)),
                                                    (volume_bar_width, self.height))
        surface.blit(volume_bar_current, (self.x, self.y))  # Afficher la barre de volume actuelle
        self.volumeButton.update(surface)

    def handle_event(self, event, mousePosition, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.volumeButton.checkForInput(mousePosition):
                self.volumeButton.press(screen)
                if self.current_volume != 0:
                    self.volumeButton.setImages(ressources.lobbyMute)
                    self.bufferVolume = self.current_volume
                    self.current_volume = 0
                    pygame.mixer.music.set_volume(self.current_volume)
                else:
                    if self.bufferVolume in [0, None]:
                        self.current_volume = 0.5
                        pygame.mixer.music.set_volume(self.current_volume)
                    else:
                        self.current_volume = self.bufferVolume
                        pygame.mixer.music.set_volume(self.current_volume)
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

        if self.current_volume == 0:
            self.volumeButton.setImages(ressources.lobbyMute)
            pygame.mixer.music.set_volume(self.current_volume)

        else:
            self.volumeButton.setImages(ressources.lobbySoundOn)



