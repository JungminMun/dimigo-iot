import pygame 

pygame.init()

pygame.mixer.music.load('sample.mp3')

while True:
    cmd = input('Play:p, Pause:pp, Unpause:up, Stop:s, Quit:q ')

    if cmd == 'p':
        pygame.mixer.music.play()
    elif cmd == 'pp':
        pygame.mixer.music.pause()
    elif cmd == 'up':
        pygame.mixer.music.unpause()
    elif cmd == 's':
        pygame.mixer.music.stop()
    elif cmd == 'q':
        break
    else :
        print('incorrect command')

