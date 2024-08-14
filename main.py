import pygame
from sprites.jugador import Jugador
from sprites.disparo import Disparo
from sprites.enemigo_1 import Enemigo1
from sprites.enemigo_2 import Enemigo2
from sprites.enemigo_3 import Enemigo3
from sprites.explosion import Exlosion
from sprites.vidas import Vidas
from sprites.boton import Boton
import random




class Juego():
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.FPS = pygame.time.Clock()

        self.estado_juego = "Menu" # va a tener estado Menu,Jugar,GameOver
        self.ANCHO_VENTANA, self.ALTO_VENTANA = 800, 600
        self.velocidad_fondo = .5
        self.ventana = pygame.display.set_mode((self.ANCHO_VENTANA, self.ALTO_VENTANA))
        self.salir = False
        self.creacion_enemigo_1 = pygame.time.get_ticks()
        self.creacion_enemigo_2 = self.creacion_enemigo_1
        self.creacion_enemigo_3 = self.creacion_enemigo_1

        self.tiempo_crear_enemigo_1 = 3000
        self.tiempo_crear_enemigo_2 = 8000
        self.tiempo_crear_enemigo_3 = 15000

        self.reseteo_tiempo = 0

        self.sprites_lista = pygame.sprite.Group()
        self.disparos_lista = pygame.sprite.Group()
        self.disparo_enemigo_lista = pygame.sprite.Group()
        self.enemigos_lista = pygame.sprite.Group()
        self.menu_lista = pygame.sprite.Group()
        self.game_over_list = pygame.sprite.Group()
        
        self.boton_menu = Boton("Menu",(self.ANCHO_VENTANA//2-100,self.ALTO_VENTANA//4*2))
        self.game_over_list.add(self.boton_menu)
        
        self.img_vida = pygame.image.load("./assets/sprites/nave-1.png").convert_alpha()
        self.img_vida = pygame.transform.scale(self.img_vida,(16,16))
        self.rect_vida = self.img_vida.get_rect()
        self.jugador = Jugador((self.ANCHO_VENTANA,self.ALTO_VENTANA), self.sprites_lista)
        self.jugador.vidas = 0
        self.sprites_lista.add(self.jugador)

        self.fondo = pygame.image.load("./assets/fondos/fondo.jpg").convert()
        self.posicion_fondo = [-5,-5]
        self.invertir_fondo_x = False
        self.invertir_fondo_y = False

        self.fuente = pygame.font.Font("./assets/fonts/Gamer.ttf",64)

        sonido_fondo = pygame.mixer.music.load("./assets/sonidos/sonido_fondo.wav")
        pygame.mixer.music.play(-1, start=7)

        #pygame.mouse.set_visible(False)

        self.menu()

    def menu(self):
        self.boton_jugar = Boton("JUGAR",(self.ANCHO_VENTANA//2-100,self.ALTO_VENTANA//4))
        self.menu_lista.add(self.boton_jugar)
        self.boton_salir = Boton("SALIR",(self.ANCHO_VENTANA//2-100,self.ALTO_VENTANA//4*3))
        self.menu_lista.add(self.boton_salir)

    def colisiones(self):
        colision_disparo_jugador = pygame.sprite.groupcollide(self.disparos_lista, self.enemigos_lista, True, False)
        if colision_disparo_jugador:
            for disparos, enemigos in colision_disparo_jugador.items():
                for enemigo in enemigos:
                    x = enemigo.rect.x
                    y = enemigo.rect.y
                    if enemigo.restar_vida():
                        self.sprites_lista.add(Exlosion((x,y)))
        
        colision_disparo_enemigo = pygame.sprite.spritecollide(self.jugador, self.disparo_enemigo_lista, False)
        colision_enemigos = pygame.sprite.spritecollide(self.jugador, self.enemigos_lista, False)
        
        if colision_enemigos or colision_disparo_enemigo:
            if not self.jugador.herido:
                self.lista_vidas.pop(-1).kill()
                if self.jugador.sacar_vida():
                    self.sprites_lista.add(Exlosion((self.jugador.rect.x,self.jugador.rect.y)))
                if colision_enemigos:
                    for enemigo in colision_enemigos:
                        x = enemigo.rect.x
                        y = enemigo.rect.y
                        self.sprites_lista.add(Exlosion((x,y)))
                        enemigo.kill()
                if colision_disparo_enemigo:
                    for disparo in colision_disparo_enemigo:
                        disparo.kill()

    def dificultad(self):
        if self.tiempo_actual > 60000:
            self.tiempo_crear_enemigo_1 = 1500
            self.tiempo_crear_enemigo_2 = 3000
            self.tiempo_crear_enemigo_3 = 5000
        if self.tiempo_actual > 90000:
            self.tiempo_crear_enemigo_1 = 1000
            self.tiempo_crear_enemigo_2 = 1500
            self.tiempo_crear_enemigo_3 = 3000
    
    def creacion_enemigos(self):
        if self.tiempo_actual - self.creacion_enemigo_1 > self.tiempo_crear_enemigo_1:
            self.creacion_enemigo_1 = self.tiempo_actual
            enemigo = Enemigo1(
                                (self.ANCHO_VENTANA,random.randrange(64,self.ALTO_VENTANA - 64)),
                                (self.ANCHO_VENTANA, self.ALTO_VENTANA)
                                )
            self.sprites_lista.add(enemigo)
            self.enemigos_lista.add(enemigo)
        if self.tiempo_actual - self.creacion_enemigo_2 > self.tiempo_crear_enemigo_2:
            self.creacion_enemigo_2 = self.tiempo_actual
            enemigo = Enemigo2(
                                (self.ANCHO_VENTANA, random.randrange(64,self.ALTO_VENTANA - 64)),
                                (self.ANCHO_VENTANA, self.ALTO_VENTANA), self.disparo_enemigo_lista, self.sprites_lista
                                )
            self.sprites_lista.add(enemigo)
            self.enemigos_lista.add(enemigo)
        if self.tiempo_actual - self.creacion_enemigo_3 > self.tiempo_crear_enemigo_3:
            self.creacion_enemigo_3 = self.tiempo_actual
            enemigo = Enemigo3(
                                (self.ANCHO_VENTANA, random.randrange(64,self.ALTO_VENTANA - 64)),
                                (self.ANCHO_VENTANA, self.ALTO_VENTANA), self.disparo_enemigo_lista, self.sprites_lista
                                )
            self.sprites_lista.add(enemigo)
            self.enemigos_lista.add(enemigo)

    def animacion_fondo(self):
        self.ventana.blit(self.fondo, self.posicion_fondo)

        if self.posicion_fondo[0] == 0 or self.posicion_fondo[0] == -(self.fondo.get_size()[0] - self.ANCHO_VENTANA) :
            self.invertir_fondo_x = not self.invertir_fondo_x
        if self.posicion_fondo[1] == 0 or self.posicion_fondo[1] == -(self.fondo.get_size()[1] - self.ALTO_VENTANA):
            self.invertir_fondo_y = not self.invertir_fondo_y
        self.posicion_fondo[0] += self.velocidad_fondo if self.invertir_fondo_x else -self.velocidad_fondo
        self.posicion_fondo[1] += self.velocidad_fondo if self.invertir_fondo_y else -self.velocidad_fondo
    
    def mostrar_vidas(self):
        self.lista_vidas = []
        for num in range(1,4):
            temp = 32 * num
            self.lista_vidas.append(Vidas((temp,16)))
        for vida in self.lista_vidas:
            self.sprites_lista.add(vida)

    def run(self):
        while not self.salir:
            self.tiempo_actual = pygame.time.get_ticks() - self.reseteo_tiempo
            for evento in pygame.event.get():
                if evento.type  == pygame.QUIT:
                    self.salir = True
                if evento.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    if self.estado_juego == "Menu":
                        if self.boton_salir.click():
                            self.salir = True
                        if self.boton_jugar.click():
                            self.jugador.vidas = 3
                            self.reseteo_tiempo = pygame.time.get_ticks()
                            for sprite in self.sprites_lista:
                                sprite.kill()
                            self.mostrar_vidas()
                            self.sprites_lista.add(self.jugador)
                    if self.estado_juego == "GameOver":
                        if self.boton_menu.click():
                            self.jugador.muerto = False
                    if self.estado_juego == "Jugar":
                        disparo = Disparo("./assets/sprites/disparo.png",15,
                                            (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                                        )
                        self.sprites_lista.add(disparo)
                        self.disparos_lista.add(disparo)
            if self.jugador.vidas == 0 and not self.jugador.muerto:
                self.estado_juego = "Menu"
                self.animacion_fondo()
                self.menu_lista.update()
                self.menu_lista.draw(self.ventana)
            elif self.jugador.vidas > 0:
                self.estado_juego = "Jugar"
                self.colisiones()
                self.dificultad()
                self.creacion_enemigos()
                self.animacion_fondo()
                
                self.sprites_lista.update()
                self.sprites_lista.draw(self.ventana)
            else:
                self.estado_juego = "GameOver"
                self.game_over =  self.fuente.render("GAME OVER", False,(255,255,255))
                self.ventana.fill((0,0,0))
                self.game_over_list.update()
                self.game_over_list.draw(self.ventana)
                self.ventana.blit(self.game_over,(
                                                    self.ANCHO_VENTANA//2 - self.game_over.get_size()[0]//2,
                                                    self.ALTO_VENTANA//4
                                                ))
                
            
            pygame.display.flip()
            self.FPS.tick(60)

        pygame.quit()

if __name__ == "__main__":
    juego = Juego()
    juego.run()
    