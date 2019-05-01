import cairo, math, random
from math import pi

# reference: https://github.com/pygobject/pycairo/blob/master/examples/pygame-demo.py

size = width, height = 512, 512

def draw():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

    x, y, radius = (random.randint(230, 270), random.randint(230, 270), 200)
    cr = cairo.Context(surface)
    cr.set_line_width(15)
    cr.arc(x, y, radius, 0, 2.0 * math.pi)
    cr.set_source_rgba(random.random(), 1, 0, 0.3)
    cr.fill_preserve()
    cr.set_source_rgb(0, 0, 0)
    cr.stroke()

    cr.set_line_width(1)
    draw_rounded(cr, (30, 60, 30, 60), 5)

    return surface

def draw_rounded(cr, area, radius):
    a, b, c, d = area
    cr.arc(a + radius, c + radius, radius, 2*(pi/2), 3*(pi/2))
    cr.arc(b - radius, c + radius, radius, 3*(pi/2), 4*(pi/2))
    cr.arc(b - radius, d - radius, radius, 0*(pi/2), 1*(pi/2))
    cr.arc(a + radius, d - radius, radius, 1*(pi/2), 2*(pi/2))
    cr.close_path()
    cr.stroke()
