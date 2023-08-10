import pygame
import ressources

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)


class TexteModifiable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.font = ressources.get_font(ressources.nunitoRegular, 30)
        self.text_input = "???"
        self.is_editing = False
        self.update_text_surface()

    def update_text_surface(self):
        if self.is_editing:
            self.text_surface = self.font.render(self.text_input, True, GRAY)
        else:
            self.text_surface = self.font.render(self.text_input, True, BLACK)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.text_surface.get_rect(topleft=(self.x, self.y)).collidepoint(event.pos):
                self.is_editing = True
                if self.text_input == "???":
                    self.text_input = ""
            else:
                self.is_editing = False
            self.update_text_surface()

        if self.is_editing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.text_input.count(" ") == len(self.text_input) or len(self.text_input) == 0:
                        self.text_input = "???"
                    self.is_editing = False
                    self.update_text_surface()
                elif event.key == pygame.K_BACKSPACE:
                    self.text_input = self.text_input[:-1]
                else:
                    if len(self.text_input) < 10 or event.unicode == pygame.K_DELETE:
                        self.text_input += event.unicode
                self.update_text_surface()

    def afficher(self, screen):
        screen.blit(self.text_surface, (self.x, self.y))

    def setPos(self, pos):
        self.x = pos[0]
        self.y = pos[1]
