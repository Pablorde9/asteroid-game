from logger import log_event
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ang = random.uniform(20, 50)
        a = Asteroid(self.position.x, self.position.y, new_radius)
        a.velocity = self.velocity.rotate(ang * 1.2)
        b = Asteroid(self.position.x, self.position.y, new_radius)
        b.velocity = self.velocity.rotate(-ang * 1.2)
