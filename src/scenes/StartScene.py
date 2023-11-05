import pygame

import src


class StartScene(src.scenes.AbstractScene):
    _text: src.components.TextComponent

    def __init__(self, game: src.game.Game):
        super().__init__(game, src.utils.Coordinates(600, 600), "Стартовый экран")
        self._text = src.components.TextComponent(
            self._game, "Нажмите любую клавишу, чтобы начать игру"
        )

    def update(self) -> None:
        """Обновляет сцену"""

        super().update()
        for event in self._game.get_events():
            if event.type == pygame.KEYDOWN:
                self._game.set_scene(src.scenes.MainScene(self._game))

    def render(self) -> None:
        """Отрисовывает сцену"""

        super().render()
        self._text.render()
