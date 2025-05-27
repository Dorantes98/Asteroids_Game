import pygame # type: ignore
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, "grey", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()  # Remove the current asteroid
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    random_angle = random.uniform(0, 360)

    # Create two smaller asteroids
    asteroid1 = Asteroid(self.position.x, self.position.y, self.radius * 0.7)
    asteroid2 = Asteroid(self.position.x, self.position.y, self.radius * 0.7)
    asteroid1.velocity = self.velocity.rotate(random_angle)
    asteroid2.velocity = self.velocity.rotate(-random_angle)

    asteroid1.velocity *= 1.2  # Increase speed slightly
    asteroid2.velocity *= 1.2  # Increase speed slightly
      