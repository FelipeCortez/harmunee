import cairo, math, random
from math import pi

# reference: https://github.com/pygobject/pycairo/blob/master/examples/pygame-demo.py

size = width, height = 658, 250


def draw(debug_text=""):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(surface)
    cr.select_font_face("Iosevka", cairo.FONT_SLANT_NORMAL,
                        cairo.FONT_WEIGHT_NORMAL)
    cr.set_line_width(1)

    offset = 24
    gap = 5
    key_size = 60
    padding = 5

    for row_idx, keys in enumerate(["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM,."]):
        for key_idx, key in enumerate(keys):
            draw_key(cr, key,
                     (key_size, key_size),
                     (padding + key_idx * (key_size + gap) + offset * row_idx,
                      padding + row_idx * (key_size + gap)))

    draw_debug(cr, debug_text)

    return surface


def draw_key(cr, text, size, pos):
    width, height = size
    x, y = pos

    cr.set_font_size(24)
    cr.move_to(x, y + 24)
    cr.show_text(text)

    area = (x, x + width, y, y + height)

    draw_rounded(cr, area, 3)


def draw_debug(cr, text):
    cr.set_font_size(16)
    cr.move_to(5, height - 6)
    cr.show_text(text)


def draw_rounded(cr, area, radius):
    x1, x2, y1, y2 = area
    cr.new_path()
    cr.arc(x1 + radius, y1 + radius, radius, 2 * (pi / 2), 3 * (pi / 2))
    cr.arc(x2 - radius, y1 + radius, radius, 3 * (pi / 2), 4 * (pi / 2))
    cr.arc(x2 - radius, y2 - radius, radius, 0 * (pi / 2), 1 * (pi / 2))
    cr.arc(x1 + radius, y2 - radius, radius, 1 * (pi / 2), 2 * (pi / 2))
    cr.close_path()
    cr.stroke()
