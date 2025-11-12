from game_of_life import GameOfLife
import pygame
from ui.grid_renderer import GridRenderer
from ui.button import Button

CELL_SIZE = 20

class GameOfLifeRenderer:
    def __init__(self, game: GameOfLife, display, on_pause):
        self._game = game
        self._display = display
        self._grid_renderer = GridRenderer(display, game, CELL_SIZE)
        self._font = pygame.font.SysFont('Arial', 20)
        self._on_pause = on_pause

        info = pygame.display.Info()
        width = info.current_w
        height = info.current_h

        button_height = 50
        button_width = 100

        button_bottom_margin = 15

        self._pause_button = Button(pygame.Rect(width / 2 - button_width / 2, height - button_height - button_bottom_margin, button_width, button_height), display, on_pause, self._font)
    
    def render(self, paused):
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

        self._pause_button.render("Resume" if paused else "Pause")

    def on_click(self, pos):
        if self._pause_button.get_rect().collidepoint(pos):
            self._pause_button.click()
            return

        cell_coordinates = self._get_cell_from_mouse_position(pos)
        self._game.toggle_cell(cell_coordinates[0], cell_coordinates[1])

        # Toggling a cell should pause the simulation
        self._on_pause(True)

    def _get_cell_from_mouse_position(self, mouse_pos):
        return (mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE)

