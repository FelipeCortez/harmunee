import ctypes, os, sys, pygame, midi, cairo
from theory import *
from draw import *


def prevent_stretching():
    if os.name != "nt" or sys.getwindowsversion()[0] < 6:
        raise NotImplementedError(
            'this script requires Windows Vista or newer')

    if os.path.basename(sys.executable) == 'pythonw.exe':
        selection = 'y'
    else:
        from pygame.compat import raw_input_
        selection = None
        while selection not in ('y', 'n'):
            selection = raw_input_(
                'Prevent stretching? (y/n): ').strip().lower()

    if selection == 'y':
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()


def pressed(keycode):
    return pygame.key.get_pressed()[keycode]


def main():
    prevent_stretching()

    size = width, height = 512, 512

    player = midi.MidiPlayer()

    bases = cycle([ionian, natural_minor, harmonic_minor, melodic_minor])
    base = next(bases)

    music_key = 60

    key_to_chord = {
        pygame.K_a: "i",
        pygame.K_s: "iv",
        pygame.K_d: "v",
        pygame.K_z: "ii",
        pygame.K_x: "iii",
        pygame.K_c: "vi",
        pygame.K_v: "vii",
    }

    active_keys = {}

    pygame.init()
    pygame.display.set_mode(size)
    screen = pygame.display.get_surface()

    screen.fill((255, 255, 255))

    clock = pygame.time.Clock()

    done = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    for i in range(130):
                        player.noteoff(i)

                if event.key == pygame.K_UP:
                    music_key += 1

                if event.key == pygame.K_DOWN:
                    music_key -= 1

                if event.key == pygame.K_RIGHT:
                    base = next(bases)

                if event.key in key_to_chord.keys():
                    chordfn = triad if not pressed(pygame.K_j) else tetrad
                    chord = deg(base, key_to_chord[event.key], music_key,
                                chordfn)
                    root = chord[0]

                    inv_keys = [pygame.K_p, pygame.K_o, pygame.K_i]
                    for _ in [k for k in inv_keys if pressed(k)]:
                        chord = invert_down(chord)

                    if pressed(pygame.K_SPACE):
                        chord = bass(chord, root)

                    if pressed(pygame.K_n):
                        chord = bass_fifth(chord, root)

                    print(chord)

                    active_keys[event.key] = chord

                    for note in chord:
                        player.noteon(note)

                if event.key == pygame.K_t:
                    surface = draw()
                    buf = surface.get_data()
                    image = pygame.image.frombuffer(buf, (width, height),
                                                    "ARGB")

                    screen.fill((255, 255, 255))
                    screen.blit(image, (0, 0))
                    pygame.display.flip()

            if event.type == pygame.KEYUP:
                if event.key in key_to_chord.keys():
                    for note in active_keys.pop(event.key):
                        player.noteoff(note)

        clock.tick(50)


if __name__ == '__main__':
    main()
