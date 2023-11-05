from __future__ import annotations

from src.tiles import abstract_tile
from src.snake import snake
from src.utils import coordinates, direction


class SnakeSegment(abstract_tile.AbstractTile):
    def __init__(
        self, snake: snake.Snake, coordinates: coordinates.Coordinates
    ) -> None:
        super().__init__(
            snake.get_main_scene(),
            snake.get_main_scene().get_snake_color(),
            coordinates,
        )

    def move_in_direction(self, direction_l: direction.Direction) -> None:
        """Перемещает сегмент змеи в заданном направлении"""

        tile_size = self._main_scene.get_tile_size()

        match direction_l:
            case direction.Direction.RIGHT:
                self._coordinates.x += tile_size

            case direction.Direction.LEFT:
                self._coordinates.x -= tile_size

            case direction.Direction.UP:
                self._coordinates.y -= tile_size

            case direction.Direction.DOWN:
                self._coordinates.y += tile_size

    def move_to_segment(self, segment: "SnakeSegment") -> None:
        """Перемещает сегмент змеи на заданный другой сегмент"""

        self._coordinates = segment.get_coordinates()
