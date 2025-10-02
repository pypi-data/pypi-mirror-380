from typing import Literal, Callable
from pryttier import Vector

from . import RangeButton
from .components import Button
from .manager import UIElement
import pygame as pg

class ButtonArray(UIElement):
    def __init__(self,
                 pos: Vector | tuple[int, int],
                 length: int,
                 size: Vector | tuple[int, int],
                 spacing: int = 0,
                 axis: Literal["hor", "vert"] = "hor",
                 texts: Callable = lambda l: f"Button{l}",
                 button_kwargs: dict = None):
        super().__init__(pos)
        self.pos = pos
        self.length = length
        self.size = size
        self.spacing = spacing

        if button_kwargs is None:
            button_kwargs = {}

        self.buttons = []

        for i in range(self.length):
            if axis == "hor":
                position = Vector(self.pos[0] + i*(self.size[0] + self.spacing), self.pos[1])
            elif axis == "vert":
                position = Vector(self.pos[0], self.pos[1] + i*(self.size[1] + self.spacing))
            else:
                raise ValueError("Invalid Axis. try: 'hor'(horizontal) or 'vert'(vertical)")
            btn = Button(position, self.size, texts(i), **button_kwargs)
            self.buttons.append(btn)

    def handle_event(self, event):
        for btn in self.buttons:
            btn.handle_event(event)

    def draw(self, surface: pg.Surface):
        for btn in self.buttons:
            btn.draw(surface)

class ButtonMatrix(UIElement):
    def __init__(self,
                 pos: Vector | tuple[int, int],
                 width: int,
                 height: int,
                 size: Vector | tuple[int, int],
                 spacing: int = 0,
                 texts: Callable = lambda x, y: f"Button{x}{y}",
                 button_kwargs: dict = None):
        super().__init__(pos)
        self.pos = pos
        self.width = width
        self.height = height
        self.size = size
        self.spacing = spacing

        if button_kwargs is None:
            button_kwargs = {}

        self.buttons = []

        for y in range(self.width):
            row = []
            for x in range(self.height):
                position = Vector(self.pos[0] + x*(self.size[0] + self.spacing),
                                  self.pos[1] + y*(self.size[1] + self.spacing))
                btn = Button(position, self.size, texts(x, y), **button_kwargs)
                row.append(btn)
            self.buttons.append(row)



    def handle_event(self, event):
        for y in range(self.width):
            for x in range(self.height):
                self.buttons[y][x].handle_event(event)

    def draw(self, surface: pg.Surface):
        for y in range(self.width):
            for x in range(self.height):
                self.buttons[y][x].draw(surface)

class RangeButtonArray(UIElement):
    def __init__(self,
                 pos: Vector | tuple[int, int],
                 length: int,
                 size: Vector | tuple[int, int],
                 spacing: int = 0,
                 start: float | int = 0,
                 end: float | int = 1,
                 step: float | int = 0.1,
                 axis: Literal["hor", "vert"] = "hor",
                 button_kwargs: dict = None):
        super().__init__(pos)
        self.pos = pos
        self.length = length
        self.size = size
        self.spacing = spacing

        if button_kwargs is None:
            button_kwargs = {}

        self.buttons = []

        for i in range(self.length):
            if axis == "hor":
                position = Vector(self.pos[0] + i*(self.size[0] + self.spacing), self.pos[1])
            elif axis == "vert":
                position = Vector(self.pos[0], self.pos[1] + i*(self.size[1] + self.spacing))
            else:
                raise ValueError("Invalid Axis. try: 'hor'(horizontal) or 'vert'(vertical)")
            btn = RangeButton(position, self.size, start, end, step, **button_kwargs)
            self.buttons.append(btn)

    def handle_event(self, event):
        for btn in self.buttons:
            btn.handle_event(event)

    def draw(self, surface: pg.Surface):
        for btn in self.buttons:
            btn.draw(surface)

class RangeButtonMatrix(UIElement):
    def __init__(self,
                 pos: Vector | tuple[int, int],
                 width: int,
                 height: int,
                 size: Vector | tuple[int, int],
                 spacing: int = 0,
                 start: float | int = 0,
                 end: float | int = 1,
                 step: float | int = 0.1,
                 button_kwargs: dict = None):
        super().__init__(pos)
        self.pos = pos
        self.width = width
        self.height = height
        self.size = size
        self.spacing = spacing

        if button_kwargs is None:
            button_kwargs = {}

        self.buttons = []

        for y in range(self.width):
            row = []
            for x in range(self.height):
                position = Vector(self.pos[0] + x*(self.size[0] + self.spacing),
                                  self.pos[1] + y*(self.size[1] + self.spacing))
                btn = RangeButton(position, self.size, start, end, step, **button_kwargs)
                row.append(btn)
            self.buttons.append(row)

    def reset(self):
        for y in range(self.width):
            for x in range(self.height):
                self.buttons[y][x].reset()


    def handle_event(self, event):
        for y in range(self.width):
            for x in range(self.height):
                self.buttons[y][x].handle_event(event)

    def draw(self, surface: pg.Surface):
        for y in range(self.width):
            for x in range(self.height):
                self.buttons[y][x].draw(surface)