import pygame

from src.game import abstract_game


class MockGame(abstract_game.AbstractGame):
    def update(self, events: list[pygame.event.Event] = None):
        self._events = events if events is not None else []
        self._active_scene.update()
