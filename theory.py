from itertools import cycle, islice

ionian         = [2, 2, 1, 2, 2, 2, 1]
natural_minor  = [2, 1, 2, 2, 1, 2, 2]
harmonic_minor = [2, 1, 2, 2, 1, 3, 1]
melodic_minor =  [2, 1, 2, 2, 2, 1, 2]

def triad(base, root, deg):
    structure = list(islice(accumulator(base), deg, deg + 6, 2))
    return [root + n for n in structure]

def tetrad(base, root, deg):
    structure = list(islice(accumulator(base), deg, deg + 8, 2))
    return [root + n for n in structure]

def deg(base, roman, key, fn):
    idx = ["i", "ii", "iii", "iv", "v", "vi", "vii"].index(roman)
    return fn(base, key, idx)

def accumulator(base):
    accum = 0
    for x in cycle(base):
        yield accum
        accum = accum + x

def bass(chord, note):
    return [note - 12] + chord

def bass_fifth(chord, note):
    return [note - 24] + [note - 17] + chord

def invert_up(chord):
    return chord[1:] + [chord[0] + 12]

def invert_down(chord):
    return [chord[-1] - 12] + chord[:-1]

def midi_to_note(value):
    return "C C# D D# E F F# G G# A A# B".split()[value % 12]
