import pygame # type: ignore
from constants import *
from player import Player

def main ():
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))        # Clear screen
        player.draw_player(screen)         # Draw player
        pygame.display.flip()       # Update the screen
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()