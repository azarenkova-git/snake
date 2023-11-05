from __future__ import annotations

from src.tiles import abstract_bonus
from src.scenes import main_scene
from src.utils import colors


class Food(abstract_bonus.AbstractBonus):
    def __init__(self, main_scene: main_scene.MainScene):
        super().__init__(main_scene, colors.Colors.RED)

    def on_take(self) -> None:
        """Обработчик события, когда змея съела еду"""

        self._main_scene.get_snake().add_new_segment()
        self._main_scene.increment_score_by_one()
        self._main_scene.add_bonus(Food(self._main_scene))
        self._main_scene.increase_speed_of_snake()
