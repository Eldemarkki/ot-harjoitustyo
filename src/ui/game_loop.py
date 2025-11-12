import pygame
from ui.game_of_life_renderer import GameOfLifeRenderer

class GameLoop():

    def __init__(self, game, display):
        self._clock = pygame.time.Clock()
        self._game = game
        self._display = display
        self._paused = False

        def toggle_pause(new_state: bool | None = None):
            if new_state is None:
                self._paused = not self._paused
            else:
                self._paused = new_state

        self._renderer = GameOfLifeRenderer(self._game, self._display, on_pause=toggle_pause)

    def _toggle_pause(self):
        self._paused = not self._paused

    def run(self):
        time_since_simulation = 0

        while True:
            # Run game at 60 FPS
            ms_since_last_tick = self._clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._toggle_pause()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self._renderer.on_click(pos)
                elif event.type == pygame.QUIT:
                    return
            
            self._renderer.render(self._paused)
            pygame.display.update()

            time_since_simulation += ms_since_last_tick

            # Simulate at 2 FPS
            if not self._paused and time_since_simulation > 500:
                self._game.simulate()
                time_since_simulation = 0
