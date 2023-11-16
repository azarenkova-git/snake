from __future__ import annotations

from src.tiles import abstract_bonus
from src.scenes import main_scene
from src.utils import colors


class TimeSlowBonus(abstract_bonus.AbstractBonus):
    def __init__(self, main_scene: main_scene.MainScene):
        super().__init__(main_scene, colors.Colors.BLUE)

    def on_take(self) -> None:
        """Обработчик события, когда змея съела еду"""

        self._main_scene.decrease_speed_of_snake()
