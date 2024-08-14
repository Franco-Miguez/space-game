import pygame

class Vidas(pygame.sprite.Sprite):
    def __init__(self, posicion :tuple[int,int]) -> None:
        super().__init__()
        self.image = pygame.image.load("./assets/sprites/nave-1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(32,32))
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        
