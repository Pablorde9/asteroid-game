import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from score import ScoreBoard
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

    ponto = ScoreBoard(20, 20)
    pygame.display.set_caption("Asteroids")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for ast in asteroids:
            for shot in shots:
                if shot.collides_with(ast):
                    log_event("asteroid_shot")
                    ponto.add_score(1)
                    shot.kill()
                    ast.split()
            if ast.collides_with(p) and p.vuln != 1:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for d in drawable:
            d.draw(screen)
        log_state()
        ponto.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
