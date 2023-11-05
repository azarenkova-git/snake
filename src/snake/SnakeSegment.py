import src


class SnakeSegment(src.tiles.AbstractTile):
    def __init__(
        self, snake: src.snake.Snake, coordinates: src.utils.Coordinates
    ) -> None:
        super().__init__(
            snake.get_main_scene(),
            snake.get_main_scene().get_snake_color(),
            coordinates,
        )

    def move_in_direction(self, direction: src.utils.Direction) -> None:
        """Перемещает сегмент змеи в заданном направлении"""

        tile_size = self._main_scene.get_tile_size()

        match direction:
            case src.utils.Direction.RIGHT:
                self._coordinates.y += tile_size

            case src.utils.Direction.LEFT:
                self._coordinates.y -= tile_size

            case src.utils.Direction.UP:
                self._coordinates.x -= tile_size

            case src.utils.Direction.DOWN:
                self._coordinates.x += tile_size

    def move_to_segment(self, segment: src.snake.SnakeSegment) -> None:
        """Перемещает сегмент змеи на заданный другой сегмент"""

        self._coordinates = segment.get_coordinates()
