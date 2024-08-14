import pygame

class Boton(pygame.sprite.Sprite):
    def __init__(self, texto, pocicion : tuple[int,int]) -> None:
        super().__init__()
        self.image = pygame.image.load("./assets/sprites/boton.png").convert_alpha()
        self.rect = self.image.get_rect()
        fuente = pygame.font.Font("./assets/fonts/Gamer.ttf",40)
        texto = fuente.render(texto,False,(191,67,58))
        texto_rect = texto.get_rect(center=self.rect.center)
        self.image.blit(texto,(self.rect.width // 2 - texto_rect.width // 2,
                                self.rect.height // 2 - texto_rect.height // 2))
        self.rect.x = pocicion[0]
        self.rect.y = pocicion[1]

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)