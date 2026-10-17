from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile


class GameModel:
    """Contient les données et l'état du jeu"""
    def __init__(self):
        """Initialise l'état du jeu, le circuit et la voiture"""
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None

    def load_circuit(self) -> None:
        """Crée la grille du circuit et place la voiture"""
        grid = [[RoadTile(col=col_idx, row=row_idx)
                for row_idx in range(GRID_COLS)] for col_idx in range(GRID_ROWS)]
        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        """Crée une voiture à sa position de départ"""
        self.car = Car(7, 1)

    def update(self) -> None:
        """Met à jour la position de la voiture pendant la course"""
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()
