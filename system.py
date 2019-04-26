import sys, pygame, midi
pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)

black = 0, 0, 0

player = midi.MidiPlayer()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    player.play(58)
    screen.fill(black)
    pygame.display.flip()
