import pygame
class Paddle (pygame.Rect):

    def __init__(self,position=[0,0], size=[20,60], color = (255, 255, 255) ):
        self.speedX = 0.5
        self.speedY = 8
        super().__init__(position[0], position[1], size[0], size[1])
        self.initial_position = position
        self.score = 0
        self.color = color
        
    def setSpeed(self, speedX, speedY):
        self.speedX = speedX
        self.speedY = speedY

    def draw(self,screen):
        pygame.draw.rect(screen.display, self.color, self)
    
    def move_towards_ball(self, ball):
        
        if self.bottom < ball.y:
            self.bottom += self.speedY
        
        elif self.top > ball.y:
            self.top -= self.speedY