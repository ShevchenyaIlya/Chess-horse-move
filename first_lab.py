import pygame
from laboratory.base import Grid
import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "400, 100"

surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Chess knight move")
pygame.init()

grid = Grid()
running = True

while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.fill((0, 0, 0))
    grid.draw(surface)
    pygame.display.flip()

pygame.quit()
