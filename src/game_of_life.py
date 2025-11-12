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

    def get_live_neighbors(self, x, y):
        offsets = [-1, 0, 1]

        neighbors = []
        for y_offset in offsets:
            for x_offset in offsets:
                # The cell itself is not included in the neighbors
                if y_offset == 0 and x_offset == 0:
                    continue

                # If it's out of bounds, consider the neighbor dead
                nx = x + x_offset
                ny = y + y_offset
                if nx < 0 or nx > self.get_width() - 1 or ny < 0 or ny > self.get_height() - 1:
                    continue
                
                if self.get_cell(nx, ny):
                    neighbors.append([nx, ny])
        
        return neighbors

    def _simulate_cell(self, x, y):
        alive = self.get_cell(x, y)
        neighbors = self.get_live_neighbors(x, y)

        # "Any live cell with fewer than two live neighbours dies, as if by underpopulation."
        if alive and len(neighbors) < 2:
            return False

        # "Any live cell with two or three live neighbours lives on to the next generation."
        if alive and (len(neighbors) == 2 or len(neighbors) == 3):
            return True

        # "Any live cell with more than three live neighbours dies, as if by overpopulation."
        if alive and len(neighbors) > 3:
            return False

        # "Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction."
        if not alive and len(neighbors) == 3:
            return True

        # (dead cells remain dead)
        return False


    def simulate(self):
        new_cells = []

        for y in range(self.get_height()):
            row = []
            for x in range(self.get_width()):
                new_state = self._simulate_cell(x, y)
                row.append(new_state)
            new_cells.append(row)

        self._cells = new_cells

    def __str__(self):
        text = ""
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                text += "#" if self.get_cell(x, y) else "."
            
            if y != self.get_height() - 1:
                text += "\n"
        
        return text
    
    def toggle_cell(self, x, y):
        self._cells[y][x] = not self.get_cell(x, y)