import pygame


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


class ChessHorse:
    def __init__(self):
        self.image = pygame.image.load(r'/home/shevchenya/Software/ChessHorse.png')
        self.start_pos = (3, 3)
        self.current_pos = (3, 3)
        self.possible_steps = []
        self.is_active = False

    def change_pos(self, x, y):
        self.current_pos = (x, y)
        self.is_active = False

    def draw(self, surface):
        surface.blit(self.image, (self.current_pos[0] * 75, self.current_pos[1] * 75))

    def draw_frame(self, surface):
        pygame.draw.rect(surface, (0, 125, 0), (self.current_pos[0] * 75, self.current_pos[1] * 75, 75, 75), 2)

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
        if self.is_active:
            for test in possible_horse_steps:
                if 0 <= self.current_pos[0] + test[0] < 8 and 0 <= self.current_pos[1] + test[1] < 8:
                    self.possible_steps.append((self.current_pos[0] + test[0], self.current_pos[1] + test[1]))


class Grid:
    def __init__(self):
        self.active_cells = []
        self.forbidden_cells = []
        for i in range(8):
            for j in range(8):
                self.active_cells.append((j, i))
        self.horse_pos = (3, 3)
        self.active_cells.remove(self.horse_pos)
        self.forbidden_cells.append(self.horse_pos)

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
