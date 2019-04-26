import sys, pygame, midi, theory
pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)

black = 0, 0, 0

player = midi.MidiPlayer()

key_to_chord = {
    pygame.K_a: theory.major(60),
    pygame.K_s: theory.major(65),
    pygame.K_d: theory.major(67),

    pygame.K_z: theory.minor(62),
    pygame.K_x: theory.minor(64),

    pygame.K_c: theory.dim(71),
}

print(key_to_chord)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in key_to_chord.keys():
                for note in key_to_chord[event.key]:
                    player.noteon(note)

        if event.type == pygame.KEYUP:
            if event.key in key_to_chord.keys():
                for note in key_to_chord[event.key]:
                    player.noteoff(note)

        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    pygame.display.flip()
