import pygame
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class Board:
    def __init__(self, x=800, y=600):
        self.x = x
        self.y = y

    def draw(self):
        square = pygame.draw.rect(screen, (255,0,0), (150,200,150,150))
        return square
