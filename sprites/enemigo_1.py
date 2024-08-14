from .enemigo import Enemigo
import pygame

class Enemigo1(Enemigo):
    def __init__(self, pocicion_inicial: tuple[int, int], size_ventana) -> None:
        super().__init__(pocicion_inicial, size_ventana)
        self.image = pygame.image.load("./assets/sprites/nave-3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pocicion_inicial[0] 
        self.rect.y = pocicion_inicial[1]

    def update(self) -> None:
        tiempo_actual = pygame.time.get_ticks()
        super().update()
        if tiempo_actual - self.inicio_tiempo > self.espera:
            self.rect.x -= self.velocidad
    