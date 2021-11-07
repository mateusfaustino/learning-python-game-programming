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
    
    def getMidHeight(self):
        return self.height/2
    
    
    def getMidWidth(self):
        return self.width/2
    
    def getMidWidthCentralized(self,object_width):
        return self.width/2 - object_width/2
    
    def getMidHeightCentralized(self, object_height):
        return self.height/2 - object_height/2