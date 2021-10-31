import pygame
class Screen :
    def __init__(self, caption,height, width, fill):
        self.caption = caption
        self.height = height
        self.width = width
        self.fill_color = fill

        self.limit_top = 0
        self.limit_right = self.width
        self.limit_left = 0
        self.limit_bottom = self.height

        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

    def fill(self):
         self.display.fill(self.fill_color)