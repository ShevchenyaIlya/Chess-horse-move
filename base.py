import pygame


class Grid:
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

