from typing import Callable
from pryttier import lerp, map_range
import pygame as pg
from pygame.math import clamp
from select import select

from .manager import *


class Panel(UIElement):
    def __init__(self,
                 pos: Vector | tuple[int, int],
                 size: Vector | tuple[int, int],
                 rounded: bool = False,
                 bg_clear: bool = False,
                 fg_clear: bool = False):
        super().__init__(pos)
        self.size = size
        self.rounded = rounded

        self.theme = get_config("theme")

        self.bg_clear = bg_clear
        self.fg_clear = fg_clear

        self.rect = pg.rect.Rect(*self.pos, *self.size)

        self.tint = 0

        self._sep_x = []
        self._sep_y = []

    def add_seperator_y(self, y):
        if 0 < y < self.size[1]:
            self._sep_y.append(y)

    def add_seperator_x(self, x):
        if 0 < x < self.size[0]:
            self._sep_x.append(x)

    def draw(self, surface: pg.Surface):

        bg = self.theme.bg
        if self.tint > 0 and not self.bg_clear:
            r = lerp(self.theme.bg[0], self.theme.fg[0], self.tint)
            g = lerp(self.theme.bg[1], self.theme.fg[1], self.tint)
            b = lerp(self.theme.bg[2], self.theme.fg[2], self.tint)
            bg = (r, g, b)

        if not self.bg_clear:
            pg.draw.rect(surface, bg, self.rect)
        if not self.fg_clear:
            pg.draw.rect(surface, self.theme.fg, self.rect, 1)

        for i in self._sep_x:
            pg.draw.aaline(surface, self.theme.fg, (self.pos[0] + i, self.pos[1]),
                           (self.pos[0] + i, self.pos[1] + self.size[1] - 1))
        for i in self._sep_y:
            pg.draw.aaline(surface, self.theme.fg, (self.pos[0], self.pos[1] + i),
                           (self.pos[0] + self.size[0] - 1, self.pos[1] + i))


class Text(UIElement):
    def __init__(self,
                 text: str,
                 pos: Vector | tuple[int, int],
                 font_size: int = 50,
                 center=False,
                 panel=None,
                 **kwargs):
        super().__init__(pos)
        self.text = text
        font_name = get_config("font")

        self.panel = panel

        self.center = center

        self.font = pg.font.SysFont(font_name, font_size, **kwargs)

    def draw(self, surface: pg.Surface):
        text = self.font.render(self.text, True, self.theme.fg)
        off = Vector(text.get_width() // 2, text.get_height() // 2)
        if self.center:
            if self.panel:
                surface.blit(text, (Vector(*self.panel.pos) + Vector(*self.pos) - off).xy)
            else:
                surface.blit(text, (Vector(*self.pos) - off).xy)
        else:
            if self.panel:
                surface.blit(text, (Vector(*self.panel.pos) + Vector(*self.pos)).xy)
            else:
                surface.blit(text, (Vector(*self.pos)).xy)


class Button(UIElement):
    def __init__(self,
                 pos: Vector | tuple[int, int],
                 size: Vector | tuple[int, int] = (100, 50),
                 text: str = "Button",
                 font_size: int = 30,
                 panel_kwargs: dict = {},
                 panel=None,
                 **kwargs):
        super().__init__(pos)
        self.size = size
        self.text_str = text
        self.font_size = font_size
        font_name = get_config("font")

        if panel:
            self.panel = Panel(Vector(*panel.pos) + Vector(*pos), size, **kwargs)
        else:
            self.panel = Panel(pos, size, **kwargs)

        self.text = Text(self.text_str, Vector(self.size[0] // 2, self.size[1] // 2), font_size, center=True,
                         panel=self.panel)

        self.on_click = lambda: None
        self.click = False

        self.hovering = False

    def check_hover(self):
        if self.panel.rect.collidepoint(*pg.mouse.get_pos()):
            self.hovering = True
        else:
            self.hovering = False

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.MOUSEBUTTONDOWN and self.hovering:
            if event.button == pg.BUTTON_LEFT:
                self.on_click()
                self.click = True

    def update(self):
        self.click = False
        self.check_hover()

        if self.hovering:
            self.panel.tint = lerp(self.panel.tint, 0.3, 0.1)
        else:
            if self.panel.tint > 0.01:
                self.panel.tint = lerp(self.panel.tint, 0., 0.1)
            else:
                self.panel.tint = 0

    def draw(self, surface: pg.Surface):

        self.update()

        self.panel.draw(surface)
        self.text.draw(surface)


class Checkbox(UIElement):
    def __init__(self,
                 pos: Vector | tuple[int, int],
                 size: int):
        super().__init__(pos)
        self.size = size

        self.checked = False

        self.hovering = False

        self.panel = Panel(pos, Vector(size, size), bg_clear=True)
        self.check = Panel(Vector(*pos) + Vector(size // 6, size // 6), Vector(size - size // 3, size - size // 3)).rect

    def check_hover(self):
        if self.panel.rect.collidepoint(*pg.mouse.get_pos()):
            self.hovering = True
        else:
            self.hovering = False

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.MOUSEBUTTONDOWN and self.hovering:
            if event.button == pg.BUTTON_LEFT:
                self.checked = not self.checked

    def update(self):
        self.check_hover()

    def draw(self, surface: pg.Surface):
        self.update()
        self.panel.draw(surface)
        if self.checked:
            pg.draw.rect(surface, self.theme.fg, self.check)


class Slider(UIElement):
    def __init__(self,
                 pos: Vector | tuple[int, int],
                 length: int,
                 start_value: int,
                 end_value: int,
                 step: float,
                 initial: int = 0,
                 thickness: int = 20):
        super().__init__(pos)
        self.length = length
        self.thickness = thickness

        self.start = start_value
        self.end = end_value
        self.initial = initial
        self.curr_val = initial
        self.step = step

        self.panel = Panel(self.pos, Vector(self.length, self.thickness))

        self.bob_x = map_range(self.curr_val, self.start, self.end, 0, self.length - self.thickness)

        self.hovering = False
        self.dragging = False

        self.animate = False

    def set_value(self, val: float | int):
        val = clamp(val, self.start, self.end)
        stepped = round((val - self.start) / self.step) * self.step + self.start
        val = clamp(stepped, self.start, self.end)
        if self.animate:
            self.curr_val = lerp(self.curr_val, val, 0.1)
        else:
            self.curr_val = val

    def update(self):
        self.check_hover()
        if self.dragging:
            mouse_x = clamp(pg.mouse.get_pos()[0], self.pos.x, self.pos.x + self.length - self.thickness) - self.pos.x
            raw_val = map_range(mouse_x, 0, self.length - self.thickness, self.start, self.end)
            self.set_value(raw_val)

        self.bob_x = map_range(self.curr_val, self.start, self.end, 0, self.length - self.thickness)

    def check_hover(self):
        if self.panel.rect.collidepoint(*pg.mouse.get_pos()):
            self.hovering = True
        else:
            self.hovering = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.hovering and not self.dragging:
            self.dragging = True
        if event.type == pg.MOUSEBUTTONUP and self.dragging:
            self.dragging = False

    def draw(self, surface: pg.Surface):
        self.update()
        self.panel.draw(surface)
        pg.draw.rect(surface, self.theme.fg, [self.pos.x + self.bob_x, self.pos.y, self.thickness, self.thickness])


class RangeButton(UIElement):
    def __init__(self,
                 pos: Vector | tuple[int, int],
                 size: Vector | tuple[int, int] = (100, 50),
                 start: float | int = 0,
                 end: float | int = 1,
                 step: float | int = 0.1,
                 font_size: int = 30,
                 cmap: Callable = lambda v: [int(v*255), int(v*255), int(v*255)],
                 panel=None,
                 **kwargs):
        super().__init__(pos)
        self.size = size

        self.start = start
        self.end = end
        self.step = step

        self.init = (self.start+self.end)/2
        self.curr = self.init

        self.cmap = cmap

        if panel:
            self.panel = Panel(Vector(*panel.pos) + Vector(*pos), size, **kwargs)
        else:
            self.panel = Panel(pos, size, **kwargs)



        font_name = get_config("font")
        self.font = pg.font.SysFont(font_name, font_size)

        self.click = False

        self.hovering = False

    def reset(self):
        self.curr = self.init

    def check_hover(self):
        if self.panel.rect.collidepoint(*pg.mouse.get_pos()):
            self.hovering = True
        else:
            self.hovering = False

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.MOUSEWHEEL and self.hovering:
            if pg.key.get_pressed()[pg.K_LSHIFT]:
                self.curr += event.y*self.step*10
            else:
                self.curr += event.y*self.step

            self.curr = clamp(self.curr, self.start, self.end)
        if event.type == pg.MOUSEBUTTONDOWN and self.hovering:
            if event.button == pg.BUTTON_MIDDLE:
                self.reset()

    def update(self):
        self.check_hover()

    def draw(self, surface: pg.Surface):
        self.update()
        self.panel.draw(surface)
        t = map_range(self.curr, self.start, self.end, 0, 1)
        c = self.cmap(t)
        pg.draw.rect(surface, c, self.panel.rect)

        t = self.font.render(f"{self.curr:.2f}", False, (255 - c[0], 255 - c[1], 255 - c[2]))
        sx, sy = t.get_size()
        surface.blit(t, (Vector(*self.pos) - Vector(sx//2, sy//2) + Vector(self.size[0]//2, self.size[1]//2)).xy)

