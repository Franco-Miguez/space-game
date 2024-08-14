import pygame
from .explosion import Exlosion

class Jugador(pygame.sprite.Sprite):
    def __init__(self, ventana_size : tuple[int,int], lista_sprite) -> None:
        super().__init__()
        self.ventana_size = ventana_size
        self.image = pygame.image.load("./assets/sprites/nave-1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vidas = 3
        self.herido = False # verifico si se le quito 1 vida
        self.muerto = False
        self.tiepo_inicial = pygame.time.get_ticks()
        self.espera = 100
        self.contador_herido = 0 # guarda las veces que cambio la opacidad cuando esta herido
        self.lista_sprite = lista_sprite
    
    
    def update(self):
        tiempo_actual = pygame.time.get_ticks()
        #Movimiento y limites de la pantalla
        if self.vidas >= 1:
            mouse = pygame.mouse.get_pos()
            self.rect.x = mouse[0] - self.image.get_size()[0] // 2
            
            if self.rect.x <= 0:
                self.rect.x =  0
            elif self.rect.x >= self.ventana_size[0] - self.image.get_size()[0]:
                self.rect.x = self.ventana_size[0] - self.image.get_size()[0]

            self.rect.y = mouse[1] - self.image.get_size()[1] // 2
            if self.rect.y <= -(self.image.get_size()[1] // 2):
                self.rect.y =  -(self.image.get_size()[1] // 2)
            elif self.rect.y >= self.ventana_size[1] - self.image.get_size()[1] // 2:
                self.rect.y = self.ventana_size[1] - self.image.get_size()[1] // 2
            
        # herido
        if self.herido:
            if tiempo_actual - self.tiepo_inicial > self.espera:
                self.tiepo_inicial = tiempo_actual
                self.image.set_alpha(150) if self.image.get_alpha() == 255 else self.image.set_alpha(255)
                self.contador_herido += 1
            if self.contador_herido == 10:
                self.herido = False
                self.contador_herido = 0


    def sacar_vida(self)-> int:
        if self.vidas > 0:
            explocion = Exlosion((self.rect.x, self.rect.y))
            self.lista_sprite.add(explocion)
            self.herido = True
            self.vidas -= 1
            if self.vidas > 0:
                return 0
            else:
                self.muerto = True
                return 1