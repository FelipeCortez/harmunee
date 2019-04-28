import cairo, math, random

# reference: https://github.com/pygobject/pycairo/blob/master/examples/pygame-demo.py

size = width, height = 512, 512

def draw():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

    x, y, radius = (random.randint(230, 270), random.randint(230, 270), 200)
    ctx = cairo.Context(surface)
    ctx.set_line_width(15)
    ctx.arc(x, y, radius, 0, 2.0 * math.pi)
    ctx.set_source_rgb(0.8, 0.8, 0.8)
    ctx.fill_preserve()
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()

    return surface
