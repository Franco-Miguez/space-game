import pygame

class Disparo(pygame.sprite.Sprite):
    def __init__(self, img, velocidad, pocicion_inicial : tuple[int,int]) -> None:
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pocicion_inicial[0]
        self.rect.y = pocicion_inicial[1]
        self.velocidad = velocidad
        sonido_disparo = pygame.mixer.Sound("./assets/sonidos/disparo.wav")
        sonido_disparo.play()
    
    def update(self) -> None:
        self.rect.x += self.velocidad
        if self.rect.bottom < 0:
            self.kill()
    
        
    