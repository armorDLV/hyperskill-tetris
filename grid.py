import copy

import numpy as np

from pieces import Piece


class Grid:

    def __init__(self, size_x: int, size_y: int):
        self.size_x, self.size_y = size_x, size_y
        self.cells = np.full((size_x, size_y), '-').T
        self.piece = None
        self.piece_starting_location = (3, 0)
        self.piece_x, self.piece_y = self.piece_starting_location

    def add_piece(self, name: str):
        self.piece = Piece(name)
        self.piece_x, self.piece_y = self.piece_starting_location

    def print(self):
        cells = copy.copy(self.cells)

        if self.piece:
            for (x, y) in self.get_piece_block_coordinates():
                cells[y][x] = '0'

        for row in cells:
            print(*row)
        print()

    def command(self, action: str):
        if self.piece:
            getattr(self, action)()

            if action != 'down':
                self.down()

    def rotate(self):
        self.piece.rotate()

    def down(self):
        if self.piece:
            if self.bottom_reached() or self.piece_contact():
                self.fix_piece()
            else:
                self.piece_y += 1

    def right(self):
        if self.piece_x + self.piece.right_boundary() < self.size_x - 1:
            self.piece_x += 1

    def left(self):
        if self.piece_x + self.piece.left_boundary() > 0:
            self.piece_x -= 1

    def break_rows(self):
        for y in range(len(self.cells)):
            if self.is_full_array(self.cells[y]):
                self.break_row(y)

    def break_row(self, y: int):
        self.cells[1:y + 1] = self.cells[:y]
        self.cells[0] = '-'

    def get_piece_block_coordinates(self):
        result = []
        for n in self.piece.state:
            x = self.piece_x + n % 4
            y = self.piece_y + (n // 4)
            result.append((x, y))
        return result

    def bottom_reached(self):
        return self.piece_y + self.piece.low_boundary() == self.size_y - 1

    def piece_contact(self):
        for (x, y) in self.get_piece_block_coordinates():
            if self.cells[y + 1][x] == '0':
                return True

    def fix_piece(self):
        for (x, y) in self.get_piece_block_coordinates():
            self.cells[y][x] = '0'

        self.piece = None

    def is_game_over(self):
        for column in self.cells.T:
            if self.is_full_array(column):
                return True

    @staticmethod
    def is_full_array(array):
        if set(array) == {'0'}:
            return True
