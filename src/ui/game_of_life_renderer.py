from game_of_life import GameOfLife
import pygame

CELL_SIZE = 20

class GameOfLifeRenderer:
    def render(self, game: GameOfLife, display):
        width = game.get_width()
        for y in range(game.get_height()):
            for x in range(game.get_width()):
                alive = game.get_cell(x, y)
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                color = (0, 0, 0) if alive else (255, 255, 255)
                pygame.draw.rect(display, color, rect)

