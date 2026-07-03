import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (drawable, updatable, shots)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    a = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0.0
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for ast in asteroids:
            if ast.collides_with(p):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for d in drawable:
            d.draw(screen)
        log_state()
        pygame.display.flip()


if __name__ == "__main__":
    main()
