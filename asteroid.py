from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
import pygame
import random
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20, 50)
            vect1 = self.velocity.rotate(split_angle)
            vect2 = self.velocity.rotate(0-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = vect1 * 1.2
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2.velocity = vect2 * 1.2
