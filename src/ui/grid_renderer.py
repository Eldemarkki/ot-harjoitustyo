from game_of_life import GameOfLife
import pygame

class GridRenderer:
    def __init__(self, display, game: GameOfLife, spacing, color = (230, 230, 230)):
        self._display = display
        self._game = game
        self._spacing = spacing
        self._color = color

    def _draw_line(self, start_pos, end_pos):
        pygame.draw.line(self._display, self._color, start_pos, end_pos)

    def render(self):
        # Draw horizontal lines
        horizontal_line_length = self._game.get_width() * self._spacing
        for y in range(self._game.get_height()):            
            line_y = y * self._spacing
            self._draw_line((0, line_y), (horizontal_line_length, line_y))

        # Draw vertical lines
        vertical_line_length = self._game.get_height() * self._spacing
        for x in range(self._game.get_width()):
            line_x = x * self._spacing
            self._draw_line((line_x, 0), (line_x, horizontal_line_length))
