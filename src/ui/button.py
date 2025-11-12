import pygame

class Button:
    def __init__(self, rect, display, on_click, font):
        self._rect = rect
        self._display = display
        self._on_click = on_click
        self._font = font

    def render(self, text):
        mouse_pos = pygame.mouse.get_pos()

        hovering = self._rect.collidepoint(mouse_pos)
        
        color = "#969696" if hovering else "#adadad"
        pygame.draw.rect(self._display, color, self._rect, border_radius=4)
        
        rendered = self._font.render(text, True, "#000000")

        text_x = self._rect.centerx - rendered.get_width() / 2
        text_y = self._rect.centery - rendered.get_height() / 2

        self._display.blit(rendered, (text_x, text_y))

    def get_rect(self):
        return self._rect

    def click(self):
        self._on_click()