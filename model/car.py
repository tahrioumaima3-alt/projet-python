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

    def update_position(self) -> None:
        """Met à jour la position de la voiture"""
        self.y += self.speed

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
