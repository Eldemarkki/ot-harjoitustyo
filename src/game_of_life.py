from utils import create_empty_2d_array, parse_pattern
from textwrap import dedent

class GameOfLife:
    def __init__(self, width=40, height=30):
        self._width = width
        self._height = height
        self._cells = create_empty_2d_array(height, width)
        self.insert_glider(width // 2 - 1, height // 2 - 1)

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_cell(self, x, y):
        return self._cells[y][x]

    def insert_glider(self, x, y):
        # x and y is the top left of the glider
        glider = parse_pattern(dedent("""\
            .#.
            ..#
            ###"""))

        for offset in glider:
            self._cells[y + offset[1]][x + offset[0]] = True

    def __str__(self):
        text = ""
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                text += "#" if self.get_cell(x, y) else "."
            
            if y != self.get_height() - 1:
                text += "\n"
        
        return text