"""Modèle principal du jeu : état global, circuit courant, voitures.

Cette classe est le point d'entrée du modèle.
Elle orchestre le chargement du circuit, la sélection de circuit, et
délègue la logique de course au RaceCoordinator.
"""

from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile


class GameModel:
    """État complet du jeu, indépendant de pygame.

    Attributes:
        state: État courant du jeu (voir ``GameState``).
        circuit: Circuit actuellement chargé, ou ``None`` avant chargement.
        car: Voiture du joueur (une seule pour l'instant).
        available_circuits: Liste des identifiants de circuits disponibles.
        selected_circuit_index: Index du circuit sélectionné dans le menu.
    """

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None
        self.available_circuits: list[str] = ["track1", "track2"]
        self.selected_circuit_index: int = 0

    # ---- Sélection de circuit ----------------------------------------

    def select_next_circuit(self) -> None:
        """Passe au circuit suivant dans la liste (bouclage en fin de liste)."""
        self.selected_circuit_index = (
            (self.selected_circuit_index + 1) % len(self.available_circuits)
        )

    def select_previous_circuit(self) -> None:
        """Passe au circuit précédent dans la liste (bouclage en début)."""
        self.selected_circuit_index = (
            (self.selected_circuit_index - 1) % len(self.available_circuits)
        )

    def get_selected_circuit_name(self) -> str:
        """Retourne l'identifiant du circuit actuellement sélectionné."""
        return self.available_circuits[self.selected_circuit_index]

    # ---- Chargement --------------------------------------------------

    def load_circuit(self) -> None:
        """Charge le circuit actuellement sélectionné.

        Pour l'instant, charge une grille uniforme de ``RoadTile`` (comme le
        code de départ). Sera remplacé par un chargement depuis JSON une fois
        les terrains et blocs implémentés.
        """
        grid = [[RoadTile(col=col_idx, row=row_idx)
                 for col_idx in range(GRID_COLS)]
                for row_idx in range(GRID_ROWS)]
        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        """Place la voiture du joueur à sa position de départ."""
        self.car = Car(7, 1)

    # ---- Mise à jour -------------------------------------------------

    def update(self) -> None:
        """Met à jour la logique du jeu pour une frame.

        Ne fait rien si on n'est pas en course.
        """
        if self.state != GameState.RACING or self.circuit is None:
            return
        if self.car is not None:
            self.car.apply_friction()
            self.car.update_position()