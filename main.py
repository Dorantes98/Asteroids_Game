import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main ():
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    pygame.init()

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)           # Update player rotation before drawing    
        screen.fill((0,0,0))        # Clear screen
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()       # Update the screen
        dt = clock.tick(60) / 1000  # 



if __name__ == "__main__":
    main()