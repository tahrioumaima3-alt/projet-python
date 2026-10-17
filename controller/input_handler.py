import pygame


MAPPING = {
    pygame.K_UP:     "accelerate",
    pygame.K_s: "brake",
    pygame.K_DOWN: "reverse", 
}


class InputHandler:
    """Arrête le jeu et ferme Pygame"""
    def __init__(self):
        """Initialise la correspondance entre les touches et les actions"""
        self.mapping = MAPPING

    def get_inputs(self) -> dict:
        """Indique quelles actions le joueur effectue actuellement"""
        keys = pygame.key.get_pressed()
        p = {action: False for action in self.mapping.values()}

        for key, action in self.mapping.items():
            if keys[key]:
                p[action] = True

        return p
