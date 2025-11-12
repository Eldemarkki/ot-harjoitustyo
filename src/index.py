from game_of_life import GameOfLife
import pygame
from ui.game_of_life_renderer import CELL_SIZE
from ui.game_loop import GameLoop

def main():
    game = GameOfLife()

    window_width = game.get_width() * CELL_SIZE
    window_height = game.get_height() * CELL_SIZE

    display = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Game of Life")

    pygame.init()

    game_loop = GameLoop(game, display)
    game_loop.run()

    pygame.quit()

if __name__ == "__main__":
    main()