import pygame # type: ignore
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
  def __init__(self, x, y, rotation):
    super().__init__(x, y, SHOT_RADIUS)
    self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED


  def draw(self, screen):
    pygame.draw.circle(screen, "red", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt