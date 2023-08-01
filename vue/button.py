import pygame


class Button:
    def __init__(self, images, pos, text_input, font, base_color, hovering_color):
        self.images = images
        self.num_images = len(images)
        self.x_pos = pos[0]
        self.y_pos = pos[1]

        if text_input:
            self.text_input = text_input
            self.font = font
            self.base_color = base_color
            self.hovering_color = hovering_color
            self.text = self.font.render(self.text_input, True, self.base_color)
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        else:
            self.text = None

        self.image_index = 0
        self.is_hovering = False
        self.is_pressed = False
        self.rect = self.images[self.image_index].get_rect(center=(self.x_pos, self.y_pos))

    def setPos(self, pos):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.images[self.image_index].get_rect(center=(self.x_pos, self.y_pos))

    def setImages(self, nouvelleListe):
        self.images = nouvelleListe

    def update(self, screen):
        screen.blit(self.images[self.image_index], self.rect)
        if self.text:
            screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if self.rect.collidepoint(position):
            self.is_hovering = True
            return True
        else:
            self.is_hovering = False
            return False

    def changeColor(self, position):
        if self.text :
            if self.rect.collidepoint(position):
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            else:
                self.text = self.font.render(self.text_input, True, self.base_color)

    def press(self, screen):
        if self.is_pressed:
            return

        self.is_pressed = True

        for k in range(len(self.images)):
            self.image_index = k
            self.update(screen)
            pygame.display.flip()
            pygame.time.delay(50)
        for k in range(len(self.images)):
            self.image_index = len(self.images)-1-k
            self.update(screen)
            pygame.display.flip()
            pygame.time.delay(50)

        self.is_pressed = False
