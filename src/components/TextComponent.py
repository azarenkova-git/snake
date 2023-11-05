import pygame

import src


class TextComponent(src.components.AbstractComponent):
    _text: str
    _font: pygame.font.Font

    def __init__(self, game: src.game.Game, text: str):
        super().__init__(game)
        self._text = text
        self._font = pygame.font.SysFont("monospace", 75)

    def render(self) -> None:
        super().render()
        label = self._font.render(
            "Нажмите любую клавишу, чтобы начать игру", 1, src.utils.Colors.WHITE
        )
        self._game.get_display().blit(label, (0, 0))

    def set_text(self, text: str) -> None:
        """Устанавливает текст компонента"""

        self._text = text
