from game_of_life import GameOfLife
import pygame
from ui.grid_renderer import GridRenderer

CELL_SIZE = 20

class GameOfLifeRenderer:
    def __init__(self, game: GameOfLife, display):
        self._game = game
        self._display = display
        self._grid_renderer = GridRenderer(display, game, CELL_SIZE)
    
    def render(self):
        # Draw cells
        width = self._game.get_width()
        for y in range(self._game.get_height()):
            for x in range(self._game.get_width()):
                alive = self._game.get_cell(x, y)
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                color = (0, 0, 0) if alive else (255, 255, 255)
                pygame.draw.rect(self._display, color, rect)
        
        # Draw grid
        self._grid_renderer.render()
    
    def get_cell_from_mouse_position(self, mouse_pos):
        return (mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE)

