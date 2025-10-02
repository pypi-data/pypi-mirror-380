
class Theme:
    def __init__(self, bg, fg):
        self.bg = bg
        self.fg = fg


def dark_theme():
    return Theme((30, 30, 30), (205, 205, 205))

def dark_high_contrast_theme():
    return Theme((0, 0, 0), (255, 255, 255))


def dark_red_theme():
    return Theme((15, 15, 15), (200, 0, 10))


def light_theme():
    return Theme((210, 210, 210), (30, 30, 30))

def light_high_contrast_theme():
    return Theme((255, 255, 255), (0, 0, 0))


def light_red_theme():
    return Theme((255, 255, 255), (200, 0, 10))


def cyberpunk_theme():
    return Theme((10, 10, 25), (0, 255, 200))


def solarized_theme():
    return Theme((0, 43, 54), (131, 148, 150))


def forest_theme():
    return Theme((34, 40, 34), (220, 230, 220))


def ocean_theme():
    return Theme((0, 48, 73), (173, 216, 230))
