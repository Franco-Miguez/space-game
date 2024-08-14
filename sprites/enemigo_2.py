from .enemigo import Enemigo
from .disparo import Disparo
import pygame
import random

class Enemigo2(Enemigo):
    def __init__(
                    self, pocicion_inicial: tuple[int, int], size_ventana : tuple [int,int],
                    lista_disparo, lista_sprite
                ) -> None:
        super().__init__(pocicion_inicial, size_ventana)
        self.image = pygame.image.load("./assets/sprites/nave-4.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pocicion_inicial[0] 
        self.rect.y = pocicion_inicial[1]
        self.desplasamiento_inicial = self.image.get_size()[0]*2
        self.espera = 2000
        self.direccion = random.choice([-1,1])
        self.velocidad = 3
        self.tiempo_disparo = 500
        self.tiempo_guardado = pygame.time.get_ticks()
        self.lista_disparo = lista_disparo
        self.lista_sprite = lista_sprite
        
    def update(self) -> None:
        tiempo_actual = pygame.time.get_ticks()
        super().update()
        if self.rect.x < -64:
            self.kill()
        if tiempo_actual - self.inicio_tiempo > self.espera:
            self.rect.y += self.direccion * self.velocidad
            if self.rect.y > self.size_ventana[1] - self.image.get_size()[1] or self.rect.y < self.image.get_size()[1]:
                self.direccion *= -1
            if tiempo_actual - self.tiempo_guardado > self.tiempo_disparo:
                self.tiempo_guardado = tiempo_actual
                disparo = Disparo("./assets/sprites/disparo-2.png",-7,(self.rect.x,self.rect.y))
                self.lista_disparo.add(disparo)
                self.lista_sprite.add(disparo)
            