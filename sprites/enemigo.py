import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, pocicion_inicial : tuple[int,int], size_ventana : tuple[int,int]) -> None:
        super().__init__()
        self.pocicion_inicial = pocicion_inicial
        self.size_ventana = size_ventana
        self.velocidad = 10
        self.vida = 3
        self.espera = 3000
        self.inicio_tiempo = pygame.time.get_ticks()
        self.desplasamiento_inicial = 64

    def update(self) -> None:
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.inicio_tiempo < self.espera:
            if self.rect.x >  self.pocicion_inicial[0] - self.desplasamiento_inicial :
                self.rect.x -= self.velocidad // 2

    
    def restar_vida(self) -> int:
        if self.vida > 1:
            self.vida -= 1
            return 0
        else:
            self.kill()
            return 1