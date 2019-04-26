import sys, pygame, midi
pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)

black = 0, 0, 0

player = midi.MidiPlayer()

key_to_chord = {
    pygame.K_a: 60,
    pygame.K_s: 65,
    pygame.K_d: 67
}

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in key_to_chord.keys():
                for note in midi.triad(key_to_chord[event.key]):
                    player.noteon(note)

        if event.type == pygame.KEYUP:
            if event.key in key_to_chord.keys():
                for note in midi.triad(key_to_chord[event.key]):
                    player.noteoff(note)

        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    pygame.display.flip()
