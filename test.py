import pygame

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

running = True
while running:
    clock.tick(30)
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), player)
    # look at mouse buttons
    pos_mouse = pygame.mouse.get_pos()
    if player.collidepoint(pos_mouse):
        print("Mouse is inside the player rectangle!")

    if pygame.mouse.get_pressed()[0]:
        print("Left mouse clicked")
    if pygame.mouse.get_pressed()[2]:
        print("Right mouse clicked")

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)

    
    

    pygame.display.update()


pygame.quit()