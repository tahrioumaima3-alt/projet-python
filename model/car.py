import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)
GRIP_SCALE = 0.87
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
        self.velocity_x = 0.0 #vitesse horiz
        self.velocity_y = 0.0 #vitesse vertic
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
        """Met à jour la position de la voiture avec le drift"""
        # Direction vers laquelle la voiture regarde
        angle_rad = math.radians(self.angle)
        forward_x = math.sin(angle_rad)
        forward_y = -math.cos(angle_rad)
        # Direction perpendiculaire (glissement latéral)
        side_x = math.cos(angle_rad)
        side_y = math.sin(angle_rad)
        # Séparation de la vitesse en deux composantes
        forward_speed = (
            self.velocity_x * forward_x
            + self.velocity_y * forward_y)
        lateral_speed = (
            self.velocity_x * side_x
            + self.velocity_y * side_y)
        # La vitesse vers l'avant s'adapte à l'accélération
        forward_speed += (self.speed - forward_speed) * 0.25
        # Le glissement latéral diminue progressivement
        lateral_speed *= GRIP_SCALE * LATERAL_FRICTION
        # Reconstruction de la vitesse sur les deux axes
        self.velocity_x = (
            forward_speed * forward_x + lateral_speed * side_x
        )
        self.velocity_y = (
            forward_speed * forward_y + lateral_speed * side_y
        )
        # Déplacement
        self.x += self.velocity_x
        self.y += self.velocity_y

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
