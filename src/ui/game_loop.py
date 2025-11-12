import pygame
from ui.game_of_life_renderer import GameOfLifeRenderer

class GameLoop():
    def __init__(self, game, display):
        self._clock = pygame.time.Clock()
        self._renderer = GameOfLifeRenderer(game, display)
        self._game = game

    def run(self):
        paused = False
        time_since_simulation = 0
        while True:
            # Run game at 60 FPS
            ms_since_last_tick = self._clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    cell_coordinates = self._renderer.get_cell_from_mouse_position(pos)
                    self._game.toggle_cell(cell_coordinates[0], cell_coordinates[1])
                elif event.type == pygame.QUIT:
                    return
            
            self._renderer.render()
            pygame.display.update()

            time_since_simulation += ms_since_last_tick

            # Simulate at 2 FPS
            if not paused and time_since_simulation > 500:
                self._game.simulate()
                time_since_simulation = 0
