import pygame
from laboratory.base import ChessBoard, ChessHorse, Grid
import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "400, 100"

surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Chess knight move")
pygame.init()

grid = ChessBoard()
horse = ChessHorse()
cells = Grid()


def stand_color():
    surface.fill((255, 255, 255))
    grid.draw(surface)
    horse.draw(surface)
    pygame.display.flip()


def main():
    running = True

    while running:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    horse.change_pos(pos[0] // 75, pos[1] // 75)
                    horse.draw(surface)

        stand_color()
    pygame.quit()


main()
# print(pos[0] // 75, pos[1] // 75)