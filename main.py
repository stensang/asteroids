import sys

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import constants
from constants import *

from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game over!")
                sys.exit(0)
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_collision(shot):
                    shot.kill()
                    asteroid.split()

        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()
