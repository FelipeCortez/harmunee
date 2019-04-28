import sys, pygame, midi, cairo
from theory import *
from draw import *

size = width, height = 512, 512

pygame.init()
pygame.display.set_mode(size)

#clock = pygame.time.Clock()
#clock.tick(30)

screen = pygame.display.get_surface()

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

def pressed(keycode):
    return pygame.key.get_pressed()[keycode]

screen.fill((0, 0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
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
                chord = deg(base, key_to_chord[event.key], music_key, chordfn)
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
                image = pygame.image.frombuffer(buf, (width, height), "ARGB")

                screen.fill((0, 0, 0))
                screen.blit(image, (0, 0))
                pygame.display.flip()

        if event.type == pygame.KEYUP:
            if event.key in key_to_chord.keys():
                for note in active_keys.pop(event.key):
                    player.noteoff(note)

        if event.type == pygame.QUIT:
            sys.exit()

