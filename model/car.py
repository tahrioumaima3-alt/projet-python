import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)


class Car:
    """Représente la voiture du joueur"""
    def __init__(self, start_col: int, start_row: int):
        """Initialise la position, la vitesse et l'image de la voiture"""
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.sprite = self.build_sprite()
        #
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        #
    def accelerate(self) -> None:
        """Augmente la vitesse de la voiture"""
        self.speed += CAR_ACCELERATION
#freinage
    def brake(self) -> None:
        """Diminue la vitesse sans la rendre négative"""
        self.speed = max(0, self.speed - CAR_ACCELERATION)
#marche arriere
    def reverse(self) -> None:
        """Diminue la vitesse de la voiture"""
        self.speed -= CAR_ACCELERATION
#
    def update_position(self) -> None:
        """Met à jour la position de la voiture"""
        self.x += self.speed * math.sin(math.radians(self.angle))
        self.y -= self.speed * math.cos(math.radians(self.angle))
    def turn_left(self) -> None:
        """Tourne la voiture vers la gauche"""
        self.angle -= 5
    def turn_right(self) -> None:
        """Tourne la voiture vers la droite"""
        self.angle += 5
    def apply_friction(self) -> None:
        """Diminue progressivement la vitesse de la voiture"""
        if self.speed > 0:
            self.speed = max(0, self.speed - 0.01)
        elif self.speed < 0:
            self.speed = min(0, self.speed + 0.01)
#
    def build_sprite(self) -> pygame.Surface:
        """Crée l'image rectangulaire de la voiture"""
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_WIDTH,
                         CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        """Retourne l'image tournée et le rectangle de la voiture"""
        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect
