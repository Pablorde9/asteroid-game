import pygame


class ScoreBoard:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.score = 0

        self.font = pygame.font.Font(None, 36)

        self.text_surface = None

        self.update_text()

    def add_score(self, points: int):
        self.score += points
        self.update_text()

    def update_text(self):
        texto_formatado = f"Score: {self.score}"
        self.text_surface = self.font.render(texto_formatado, True, "white")

    def draw(self, screen: pygame.Surface):
        screen.blit(self.text_surface, (self.x, self.y))
