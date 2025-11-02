import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        velocity_one = self.velocity.rotate(random_angle)
        velocity_two = self.velocity.rotate(-1*random_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        
        sub1 = Asteroid(self.position.x, self.position.y, radius) 
        sub1.velocity = velocity_one * 1.2
        
        sub2 = Asteroid(self.position.x, self.position.y, radius)
        sub2.velocity = velocity_two * 1.2

