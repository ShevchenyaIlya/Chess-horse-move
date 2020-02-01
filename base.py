import pygame
import random
from tkinter import messagebox
import tkinter


class ChessBoard:
    def __init__(self):
        self.grid_horizontal_lines = [((0, 75), (600, 75)),
                                      ((0, 150), (600, 150)),
                                      ((0, 225), (600, 225)),
                                      ((0, 300), (600, 300)),
                                      ((0, 375), (600, 375)),
                                      ((0, 450), (600, 450)),
                                      ((0, 525), (600, 525))]
        self.grid_vertical_lines = [((75, 0), (75, 600)),
                                    ((150, 0), (150, 600)),
                                    ((225, 0), (225, 600)),
                                    ((300, 0), (300, 600)),
                                    ((375, 0), (375, 600)),
                                    ((450, 0), (450, 600)),
                                    ((525, 0), (525, 600))]

    def draw_horizontal_line(self, surface):
        for line in self.grid_horizontal_lines:
            pygame.draw.line(surface, (200, 200, 200), line[0], line[1], 2)

    def draw_vertical_line(self, surface):
        for line in self.grid_vertical_lines:
            pygame.draw.line(surface, (200, 200, 200), line[0], line[1], 2)

    def fill_cells(self, surface):
        x, y = 75, 0
        width = 75
        height = 75
        for lines in range(8):
            if lines % 2 == 1:
                x = 0
            else:
                x = 75
            for rect_ in range(4):
                pygame.draw.rect(surface, (175, 0, 245), (x, y, width, height))
                x += 150
            y += 75

    def draw(self, surface):
        self.draw_horizontal_line(surface)
        self.draw_vertical_line(surface)
        self.fill_cells(surface)


def restart(message):
    root = tkinter.Tk()
    root.wm_withdraw()
    message = messagebox.askyesno(message, "Do you want to restart?")
    if message:
        return "restart"
    else:
        return "quit"


class ChessHorse:
    def __init__(self):
        self.image = pygame.image.load(r'/home/shevchenya/Software/ChessHorse.png')
        self.is_start = False
        self.start_pos = (3, 3)
        self.current_pos = (3, 3)
        self.possible_steps = []
        self.is_active = False
        self.player = "user"

    def change_pos(self, x, y, cell):
        if self.player == "user":
            if (x, y) in self.possible_steps and (x, y) in cell.active_cells:
                cell.new_horse_pos(self.current_pos[0], self.current_pos[1])
                cell.count_of_steps += 1
                self.current_pos = (x, y)
                self.is_active = False
                self.player = "computer"

    def draw(self, surface):
        surface.blit(self.image, (self.current_pos[0] * 75, self.current_pos[1] * 75))

    def draw_frame(self, surface, cell):
        pygame.draw.rect(surface, (181, 0, 24), (self.current_pos[0] * 75, self.current_pos[1] * 75, 75, 75), 4)
        for step in self.possible_steps:
            if step in cell.active_cells:
                pygame.draw.rect(surface, (0, 100, 0), (step[0] * 75, step[1] * 75, 75, 75), 4)

    def click_horse_handler(self, surface):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True

    def get_possible_steps(self):
        possible_horse_steps = [(2, 1), (2, -1),
                                (-2, 1), (-2, -1),
                                (1, 2), (1, -2),
                                (-1, 2), (-1, -2)]
        self.possible_steps.clear()
        if self.is_active or self.player == "computer":
            for test in possible_horse_steps:
                if 0 <= self.current_pos[0] + test[0] < 8 and 0 <= self.current_pos[1] + test[1] < 8:
                    self.possible_steps.append((self.current_pos[0] + test[0], self.current_pos[1] + test[1]))

    def auto_step(self, cell, surface):
        if self.player == "computer":
            ready_steps = []

            self.get_possible_steps()

            for step in self.possible_steps:
                if step in cell.active_cells:
                    ready_steps.append(step)

            if len(ready_steps):
                random_choice = random.choice(ready_steps)
                cell.new_horse_pos(self.current_pos[0], self.current_pos[1])
                cell.count_of_steps += 1
                self.current_pos = (random_choice[0], random_choice[1])
                self.player = "user"

    def check_end(self, cell):
        mb_end = []
        for step in self.possible_steps:
            if step in cell.active_cells:
                mb_end.append(step)
        if self.is_active:
            if not len(mb_end):
                if self.player == "user":
                    return restart("Sorry, but you loser!!!")
                elif self.player == "computer":
                    return restart("Congratulations, now you winner!!!")


class Grid:
    def __init__(self):
        self.active_cells = []
        self.forbidden_cells = []

        for i in range(8):
            for j in range(8):
                self.active_cells.append((j, i))

        self.horse_pos = (3, 3)
        self.forbidden_cells.append(self.horse_pos)
        self.count_of_steps = 0

    def show(self):
        for cell in self.active_cells:
            print(cell[0], cell[1])

    def new_horse_pos(self, x_coord, y_coord):
        self.horse_pos = (x_coord, y_coord)
        self.active_cells.remove((x_coord, y_coord))
        self.forbidden_cells.append((x_coord, y_coord))

    def is_possible_step(self, x_coord, y_coord):
        step = (x_coord, y_coord)
        for cell in self.active_cells:
            if cell == step:
                return True
        else:
            return False

    def show_forbidden_cell(self, surface, color):
        for cell in self.forbidden_cells:
            pygame.draw.rect(surface, color, (cell[0] * 75, cell[1] * 75, 75, 75), 3)
            pygame.draw.line(surface, color, (cell[0] * 75, cell[1] * 75), (cell[0] * 75 + 75, cell[1] * 75 + 75), 3)
            pygame.draw.line(surface, color, (cell[0] * 75 + 75, cell[1] * 75), (cell[0] * 75, cell[1] * 75 + 75), 3)

