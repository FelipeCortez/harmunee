import sys, pygame, midi
from theory import *
pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)

black = 0, 0, 0

player = midi.MidiPlayer()

base = ionian

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

            if event.key in key_to_chord.keys():
                chord = deg(base, key_to_chord[event.key], music_key)

                for note in bass(chord):
                    player.noteon(note)

        if event.type == pygame.KEYUP:
            if event.key in key_to_chord.keys():
                chord = deg(base, key_to_chord[event.key], music_key)

                for note in bass(chord):
                    player.noteoff(note)

        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    pygame.display.flip()
