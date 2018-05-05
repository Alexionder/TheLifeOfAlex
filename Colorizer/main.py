import pygame
pygame.init()

res = (730, 280)

display = pygame.display.set_mode(res)
clock = pygame.time.Clock()

img = pygame.image.load("jace.jpg")
# img = pygame.transform.scale(img, (2560, 1600))
image = pygame.image.load("jace.jpg")
# image = pygame.transform.scale(pygame.image.load("jace.jpg"), (2560, 1600))
on = True

RGBchange = [1, 0, 1]

def redraw(change):
    for x in range(res[0]):
        for y in range(res[1]):
            color = img.get_at((x, y))
            color2 = (color[0]*change[2], color[1]*change[1], color[2]*change[0])
            image.set_at((x, y), color2)

redraw(RGBchange)

while on:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            on = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                r = float(raw_input("Amount of Red: "))
                RGBchange[0] = r
                redraw(RGBchange)
            elif e.key == pygame.K_g:
                g = float(raw_input("Amount of Green: "))
                RGBchange[1] = g
                redraw(RGBchange)
            elif e.key == pygame.K_b:
                b = float(raw_input("Amount of Blue: "))
                RGBchange[2] = b
                redraw(RGBchange)
            elif e.key == pygame.K_s:
                pygame.image.save(image, "Wallpaper2.jpg")
    display.blit(image, (0,0))

    pygame.display.update()