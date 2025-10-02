import pygame as pg
from pryttier import Vector

from .config import get_config


class UIElement:
    def __init__(self, pos: Vector | tuple[int, int]):

        self.pos = pos

        self.visible = True
        self.active = True

        self.theme = get_config("theme")

    def handle_event(self, event):
        pass  # To be overridden

    def draw(self, surface):
        pass

class UIManager:
    def __init__(self):
        self.elements = []

    def add(self, *elements):
        for e in elements:
            self.elements.append(e)

    def handle_event(self, event):
        for element in self.elements:
            if element.active:
                element.handle_event(event)

    def draw(self, surface):
        for element in self.elements:
            if element.visible:
                element.draw(surface)
