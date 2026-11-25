"""Circuit : grille 2D de tuiles et accès par coordonnées."""

from model.road_tile import RoadTile
from constants import TILE_SIZE


class Circuit:
    """Grille rectangulaire de tuiles formant le circuit.

    Les tuiles sont indexées ``grid[row][col]`` (ligne puis colonne), comme
    le veut la convention des tableaux 2D en Python. Les coordonnées
    ``(col, row)`` sont donc **inversées** par rapport à un accès direct.

    Attributes:
        grid: Grille de tuiles, ``grid[row][col]``.
        rows: Nombre de lignes de la grille.
        cols: Nombre de colonnes de la grille.
    """

    def __init__(self, grid: list[list[RoadTile]]):
        """Construit un circuit à partir d'une grille de tuiles.

        Args:
            grid: Grille non vide de tuiles, au format ``grid[row][col]``.
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0

    def get_tile(self, col: int, row: int) -> RoadTile | None:
        """Retourne la tuile à la case ``(col, row)``, ou ``None`` si hors grille.

        Args:
            col: Indice de colonne (0 = gauche).
            row: Indice de ligne (0 = haut).

        Returns:
            La tuile demandée, ou ``None`` si ``(col, row)`` est en dehors.
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def get_tile_at_pixel(self, px: float, py: float) -> RoadTile | None:
        """Convertit une position pixel en case et retourne la tuile associée.

        Args:
            px: Coordonnée horizontale en pixels.
            py: Coordonnée verticale en pixels.

        Returns:
            La tuile sous le pixel donné, ou ``None`` si hors circuit.
        """
        col = int(px // TILE_SIZE)
        row = int(py // TILE_SIZE)
        return self.get_tile(col, row)

    def pixel_width(self) -> int:
        """Retourne la largeur du circuit en pixels."""
        return self.cols * TILE_SIZE

    def pixel_height(self) -> int:
        """Retourne la hauteur du circuit en pixels."""
        return self.rows * TILE_SIZE
