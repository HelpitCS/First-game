import pygame
from board import screen
#from board import Board
def draw_row():
    start_x = 300
    y = 10
    width = 70
    height = 70

    for i in range(4):
        x = start_x
        y += height
        for i in range(4):
            # print white square
            pygame.draw.rect(screen, (235,236,208), (x, y, width, height))
            x += width
            # print black square next to it
            pygame.draw.rect(screen, (119, 149, 86), (x, y, width, height))
            x += width

        x = start_x
        y += height
        # print other row
        for i in range(4):
            pygame.draw.rect(screen, (119, 149, 86), (x, y, width, height))
            x += width
            pygame.draw.rect(screen, (235,236,208), (x, y, width, height))
            x += width
        

running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    screen.fill((255,0,255))
    draw_row()

    pygame.display.flip()

pygame.quit()
