import unittest

import pygame
import pytest

from src.game import mock_game
from src.scenes import main_scene
from src.snake import snake_game_settings
from src.tiles import food_bonus
from src.utils import coordinates
from src.utils.coordinates import Coordinates


class SnakeGameTests(unittest.TestCase):
    _mock_game: mock_game.MockGame

    _main_scene: main_scene.MainScene

    @pytest.fixture(autouse=True)
    def prepare(self):
        self._mock_game = mock_game.MockGame()

        game_settings = snake_game_settings.SnakeGameSettings()

        self._main_scene = main_scene.MainScene(
            self._mock_game,
            game_settings,
        )

        self._mock_game.set_scene(self._main_scene)

    def test_segments_count(self):
        self.assertEqual(self._main_scene.get_snake().get_segments_count(), 1)

    def test_movement(self):
        current_coordinates = (
            self._main_scene.get_snake().get_head_segment().get_coordinates()
        )

        self._mock_game.update(
            [
                pygame.event.Event(
                    pygame.KEYDOWN,
                    {
                        "key": pygame.K_UP,
                    },
                )
            ]
        )

        new_coordinates = (
            self._main_scene.get_snake().get_head_segment().get_coordinates()
        )

        self.assertEqual(
            new_coordinates,
            Coordinates(
                current_coordinates.x,
                current_coordinates.y - self._main_scene.get_tile_size(),
            ),
        )

    def test_food(self):
        self._main_scene.remove_all_bonuses()

        current_coordinates = (
            self._main_scene.get_snake().get_head_segment().get_coordinates()
        )

        food_potential_coordinates = coordinates.Coordinates(
            current_coordinates.x,
            current_coordinates.y - self._main_scene.get_tile_size(),
        )

        food_bonus_l = food_bonus.FoodBonus(self._main_scene)

        food_bonus_l.set_coordinates(food_potential_coordinates)

        self._main_scene.add_bonus(food_bonus_l)

        self._mock_game.update(
            [
                pygame.event.Event(
                    pygame.KEYDOWN,
                    {
                        "key": pygame.K_UP,
                    },
                )
            ]
        )

        self.assertEqual(self._main_scene.get_snake().get_segments_count(), 2)


if __name__ == "__main__":
    unittest.main()
