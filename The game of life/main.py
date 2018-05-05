import pygame,random
pygame.init()

res = (600, 600)
display = pygame.display.set_mode(res)
clock = pygame.time.Clock()

desiredFPS = 60
on = True

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (200, 200, 200)

size = 50

grid = [[random.randint(0,1) for x in range(res[0]/size)] for y in range(res[0]/size)]
newgrid = [[0 for x in range(res[0]/size)] for y in range(res[0]/size)]

def countNeighbours(grid, x, y):
    sum = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            col = (x + i + res[0]/size) % (res[0]/size)
            row = (y + j + res[1]/size) % (res[1]/size)
            sum += grid[col][row]
    sum -= grid[x][y]
    return sum

while on:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            on = False
    display.fill(white)

    for x in range(res[0]/size):
        for y in range(res[1]/size):
            pygame.draw.rect(display, (255*(1-grid[x][y]),255*(1-grid[x][y]),255*(1-grid[x][y])), (x*size,y*size,size-1,size-1))
            # pygame.draw.rect(display, grey, (x * size, y * size, size, size), 1)

            # Count live neighbours
            sum = countNeighbours(grid, x, y)

            state = grid[x][y]
            if (state == 0 and sum == 3):
                newgrid[x][y] = 1
            elif (state == 1 and (sum < 2 or sum > 3)):
                newgrid[x][y] = 0
            else:
                newgrid[x][y] = grid[x][y]





    grid = newgrid

    pygame.display.update()
    clock.tick(desiredFPS)

pygame.quit()