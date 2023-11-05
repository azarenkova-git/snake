from __future__ import annotations

import pygame

from src.components import text_component
from src.scenes import abstract_scene, main_scene
from src.game import game
from src.utils import coordinates


class StartScene(abstract_scene.AbstractScene):
    _text: text_component.TextComponent

    def __init__(self, game: game.Game):
        super().__init__(game, coordinates.Coordinates(600, 600), "Стартовый экран")
        self._text = text_component.TextComponent(
            self._game, "Нажмите любую клавишу, чтобы начать игру"
        )

    def update(self) -> None:
        """Обновляет сцену"""

        super().update()
        for event in self._game.get_events():
            if event.type == pygame.KEYDOWN:
                self._game.set_scene(main_scene.MainScene(self._game))

    def render(self) -> None:
        """Отрисовывает сцену"""

        super().render()
        self._text.render()
