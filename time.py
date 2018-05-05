import pygame, time
from math import *
pygame.init()

width = 600
height = 600

display = pygame.display.set_mode((width, height))

on = True

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (51,51,51)

accuracy = 100
two_pi = 2.0 * pi
half_pi = pi / 2.0
smoothTime = 50

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump


angleh = 0
anglem = 0
angles = 0

while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    display.fill(grey)
    currentTime = time.localtime()


    # Hours
    newangleh = 2*pi*(currentTime.tm_hour/24.0)
    angleh += (newangleh - angleh) / smoothTime
    r = 250
    drawList = []

    if angleh > half_pi:
        pygame.draw.arc(display, red, ((width-r*2)/2, (height-r*2)/2, r*2, r*2), 0, half_pi, 10)
        pygame.draw.arc(display, red, ((width - r * 2)/2, (height - r * 2)/2, r * 2, r * 2), two_pi-angleh+half_pi, two_pi, 10)
    else:
        pygame.draw.arc(display, red, ((width - r * 2)/2, (height - r * 2)/2, r * 2, r * 2), half_pi-angleh, half_pi, 10)

    '''for a in frange(pi-angleh,pi,two_pi/accuracy):
        x = sin(a) * r
        y = cos(a) * r
        drawList.append([width/2+x,height/2+y])
    if len(drawList) > 1:
        pygame.draw.lines(display, red, False, drawList, 10)'''

    # Minutes
    newanglem = 2 * pi * (currentTime.tm_min / 60.0)
    anglem += (newanglem - anglem) / smoothTime
    r = 220
    drawList = []

    if anglem > half_pi:
        pygame.draw.arc(display, green, ((width-r*2)/2, (height-r*2)/2, r*2, r*2), 0, half_pi, 10)
        pygame.draw.arc(display, green, ((width - r * 2)/2, (height - r * 2)/2, r * 2, r * 2), two_pi-anglem+half_pi, two_pi, 10)
    else:
        pygame.draw.arc(display, green, ((width - r * 2)/2, (height - r * 2)/2, r * 2, r * 2), half_pi-anglem, half_pi, 10)

    '''for a in frange(pi - anglem, pi, two_pi / accuracy):
        x = sin(a) * r
        y = cos(a) * r
        drawList.append([width / 2 + x, height / 2 + y])
    if len(drawList) > 1:
        pygame.draw.lines(display, green, False, drawList, 10)'''

    # Seconds
    newangles = 2 * pi * (currentTime.tm_sec / 60.0)
    angles += (newangles - angles) / smoothTime
    r = 190
    drawList = []

    if angles > half_pi:
        pygame.draw.arc(display, blue, ((width-r*2)/2, (height-r*2)/2, r*2, r*2), 0, half_pi, 10)
        pygame.draw.arc(display, blue, ((width - r * 2)/2, (height - r * 2)/2, r * 2, r * 2), two_pi-angles+half_pi, two_pi, 10)
    else:
        pygame.draw.arc(display, blue, ((width - r * 2)/2, (height - r * 2)/2, r * 2, r * 2), half_pi-angles, half_pi, 10)

    '''for a in frange(pi - angles, pi, two_pi / accuracy):
        x = sin(a) * r
        y = cos(a) * r
        drawList.append([width / 2 + x, height / 2 + y])
    if len(drawList) > 1:
        pygame.draw.lines(display, blue, False, drawList, 10)'''

    # Text
    text = "{:02d}:{:02d}:{:02d}".format(currentTime.tm_hour, currentTime.tm_min, currentTime.tm_sec)
    font = pygame.font.Font("Squares _Bold_Free.otf", 47)
    label = font.render(text, 0, white)

    x = width / 2 - label.get_rect().width / 2
    y = height / 2 - label.get_rect().height / 2

    display.blit(label, (x, y))


    pygame.display.update()
pygame.quit()