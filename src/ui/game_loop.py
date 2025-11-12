import pygame
from ui.game_of_life_renderer import GameOfLifeRenderer

class GameLoop():
    def __init__(self, game, display):
        self._clock = pygame.time.Clock()
        self._renderer = GameOfLifeRenderer(game, display)
        self._game = game

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            
            self._renderer.render()
            pygame.display.update()

            self._game.simulate()

            self._clock.tick(2)