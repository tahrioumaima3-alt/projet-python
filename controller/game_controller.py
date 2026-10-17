import pygame
import sys
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    GameState
)
from model.game_model import GameModel
from view.game_view import GameView
from controller.input_handler import InputHandler


class GameController:
    """Gère le déroulement général du jeu."""

    def __init__(self):
        """Initialise la fenêtre, le modèle, la vue et les contrôles"""
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.input_handler = InputHandler()
        self.running = True

    def run(self) -> None: #Cette boucle se répète environ 60 fois par seconde.
                          # Chaque répétition s'appelle une frame
        """Lance la boucle principale du jeu"""
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self) -> None:
        """Récupère et traite les événements de Pygame"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key: int) -> None:
        """Traite une touche pressée selon l'état du jeu"""
        state = self.model.state

        if state == GameState.MENU:
            self.handle_menu_key(key)

    def handle_menu_key(self, key: int) -> None:
        """Traite les touches utilisées dans le menu"""
        if key == pygame.K_RETURN:
            self.model.load_circuit()
            self.model.state = GameState.RACING
        elif key == pygame.K_ESCAPE:
            self.quit()

    def update(self) -> None:
        """Met à jour le jeu pendant la course"""
        if self.model.state != GameState.RACING:
            return

        p1_input = self.input_handler.get_inputs()
        car = self.model.car
        self.apply_input(car, p1_input)
        self.model.update()

    def apply_input(self, car, player_input) -> None:
        """Applique les actions du joueur à la voiture"""
        if player_input['accelerate']:
            car.accelerate()
#freinage et marche à arriere
        if player_input['brake']:
            car.brake()
        if player_input['reverse']:
            car.reverse()

    def render(self) -> None:
        """Demande à la vue de dessiner le jeu"""
        self.view.draw(self.model)

    def quit(self) -> None:
        """Arrête le jeu et ferme Pygame"""
        self.running = False
        pygame.quit()
        sys.exit()
