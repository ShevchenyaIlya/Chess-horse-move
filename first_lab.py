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
    if cells.count_of_steps:
        cells.show_forbidden_cell(surface, (0, 0, 0))
    if horse.is_active:
        horse.draw_frame(surface, cells)

    pygame.display.flip()


def restart_game():
    global grid, horse, cells
    del grid, horse, cells
    grid = ChessBoard()
    horse = ChessHorse()
    cells = Grid()


def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if (pos[0] // 75, pos[1] // 75) == horse.current_pos:
                        horse.click_horse_handler(surface)
                        horse.get_possible_steps()
                    else:
                        if horse.is_active:
                            horse.change_pos(pos[0] // 75, pos[1] // 75, cells)
                            horse.draw(surface)
                            horse.auto_step(cells, surface)

                case = horse.check_end(cells)
                if case == "restart":
                    restart_game()
                elif case == "quit":
                    running = False

        stand_color()
    pygame.quit()


main()
