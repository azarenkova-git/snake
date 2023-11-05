import src


class Food(src.tiles.AbstractBonus):
    def __init__(self, main_scene: src.scenes.MainScene):
        super().__init__(main_scene, src.utils.Colors.RED)

    def on_take(self) -> None:
        """Обработчик события, когда змея съела еду"""

        self._main_scene.get_snake().add_new_segment()
        self._main_scene.increment_score_by_one()
        self._main_scene.add_bonus(Food(self._main_scene))
