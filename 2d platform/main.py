import pygame, Color
pygame.init()

res = (1280, 720)
name = "2D platformer playground"
base_fps = 30

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode(res)
pygame.display.set_caption(name)

gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    gameDisplay.fill(Color.dark_grey)



    pygame.display.update()
    clock.tick(base_fps)
pygame.quit()