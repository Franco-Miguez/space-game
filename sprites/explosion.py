import pygame
import os

class Exlosion(pygame.sprite.Sprite):
    def __init__(self, pocion_inicial : tuple[int,int] ) -> None:
        super().__init__()
        ruta_imagenes = os.path.join("assets", "explocion")
        self.animacion = [(os.path.join(ruta_imagenes,f"{x}.png")) for x in range(1,7)]
        self.animacion = [pygame.image.load(self.animacion[x]).convert_alpha() for x in range(6)]
        self.image = self.animacion[0]
        self.rect = self.image.get_rect()
        self.rect.x = pocion_inicial[0]
        self.rect.y = pocion_inicial[1]
        self.index_animacion = 0
        self.ultimo_cambio = pygame.time.get_ticks()
        self.TIEMPO_CAMBIO = 100
        self.sonido_explosion = pygame.mixer.Sound("./assets/sonidos/explosion.wav")
        self.sonido_explosion.play()
    
    def update(self):
        tiempo_actual = pygame.time.get_ticks()
        if self.index_animacion == 6:
            self.index_animacion = 0
            self.kill()
        self.image = self.animacion[self.index_animacion]
        if tiempo_actual - self.ultimo_cambio >= self.TIEMPO_CAMBIO:
            self.index_animacion += 1
            self.ultimo_cambio = tiempo_actual
        