import pygame
from random import randint

ANCHO = 640
ALTO = 480
C_BLANCO = (255, 255, 255)
FPS = 60

ANCHO_PALETA = 5
ALTO_PALETA = 50
MARGEN_LATERAL = 40
TAM_PELOTA = 10
MARGEN = 25
VEL_MAX = 5


class Jugador(pygame.Rect):
    SUBIR = True
    BAJAR = False
    VELOCIDAD = 10

    def __init__(self, pos_x, pos_y, speed):
        super(Jugador, self).__init__(pos_x, pos_y, ANCHO_PALETA, ALTO_PALETA)
        # super(Jugador,self).__init__.rect(self.pantalla, C_BLANCO, self)
        # self.rectangulo = pygame.Rect(pos_x,pos_y,ANCHO_PALETA,ALTO_PALETA)

    def pintame(self, pantalla):
        # def pintame(self):
        pygame.draw.rect(pantalla, C_BLANCO, self)

    def muevete(self, direccion):
        # if(self.y>=0 and self.y<=ALTO-ALTO_PALETA):
        if direccion == self.SUBIR:
            # print("Muevete arriba")
            # self.y = self.y - self.speed
            self.y = self.y - self.VELOCIDAD
            if self.y < 0:
                self.y = 0
        else:
            # print("Muevete hacia abajo")
            self.y = self.y + self.VELOCIDAD
            if self.y > ALTO-ALTO_PALETA:
                self.y = ALTO-ALTO_PALETA
        """
            else:
            if(direccion == self.SUBIR):
                self.y = 0
            else:
                self.y = ALTO-ALTO_PALETA
        """


class Pelota(pygame.Rect):

    # velocidad_x = 5
    # velocidad_y = 5
    # velocidad_x = randint(-5, 5)
    # velocidad_y = randint(-5, 5)
    # flag_inicio = False

    def __init__(self, x, y):
        super(Pelota, self).__init__(x, y, TAM_PELOTA, TAM_PELOTA)
        self.flag_inicio = False
        self.velocidad_y = randint(-VEL_MAX, VEL_MAX)
        self.velocidad_x = 0
        while self.velocidad_x == 0:
            self.velocidad_x = randint(-VEL_MAX, VEL_MAX)

    # self.rectangulo = pygame.Rect(x, y, TAM_PELOTA, TAM_PELOTA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, C_BLANCO, self)

    def mover(self):
        if (self.flag_inicio):
            self.x = ANCHO/2
            self.y = ALTO/2
        else:
            self.x = self.x + self.velocidad_x
            self.y = self.y + self.velocidad_y
            if (self.y <= 0):
                self.y = 0
                self.velocidad_y = -self.velocidad_y
            if (self.y >= ALTO - TAM_PELOTA):
                self.y = ALTO - TAM_PELOTA
                self.velocidad_y = -self.velocidad_y
            # if (self.colliderect(self)):
            #    self.velocidad_x = -self.velocidad_x

    def comprobar_punto(self):
        resultado = 0
        if self.x < 0:
            # print("Punto para el jugador 2")
            self.x = (ANCHO - TAM_PELOTA)/2
            self.y = (ALTO - TAM_PELOTA)/2
            self.velocidad_y = randint(-VEL_MAX, VEL_MAX)
            self.velocidad_X = randint(-VEL_MAX, -1)
            resultado = 2
        elif self.x > ANCHO:
            # print("Punto para el jugador 1")
            self.x = (ANCHO - TAM_PELOTA)/2
            self.y = (ALTO - TAM_PELOTA)/2
            self.velocidad_y = randint(-VEL_MAX, VEL_MAX)
            self.velocidad_X = randint(1, VEL_MAX)
            resultado = 1
        return resultado

    # r = pelota1.comprobar_punto()
    # if r>0:
    #    marcador.puntuacion[r-1] += 1

    def colisionar(self, Jugador):
        if self.colliderect(Jugador):
            self.velocidad_x = -self.velocidad_x


class Marcador:
    def __init__(self):
        self.puntuacion = [0, 0]
        self.mostrar()

    def reset(self):
        self.puntuacion = [0, 0]

    def sumar_punto(self, jugador):
        self.puntuacion[jugador-1] += 1
        self.mostrar()

    def mostrar(self):
        print(
            f"El marcador ahora es: ({self.puntuacion[0]},{self.puntuacion[1]})")


class Pong():

    # reiniciar = False

    def __init__(self):
        # print("Construyendo un objeto de la calse Pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.reloj = pygame.time.Clock()
        pos_y = (ALTO - ALTO_PALETA)/2
        pos_x_2 = ANCHO - MARGEN_LATERAL-ANCHO_PALETA
        self.jugador1 = Jugador(MARGEN_LATERAL, pos_y, 10)
        self.jugador2 = Jugador(pos_x_2, pos_y, 20)
        self.pelota1 = Pelota(ANCHO/2-TAM_PELOTA/2, ALTO/2-TAM_PELOTA/2)
        self.pelota1.flag_inicio = False
        self.marcador = Marcador()

    def bucle_princiapal(self):
        # TRAMO_PINTADO=15
        # TRAMO_VACIO=5
        # ANCHO_LINEA=4
        # print("Estoy en el bucle principal")

        salir = False
        iniciar = False
        pausar = False
        jugador_que_puntua = 0

        while not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_ESCAPE:
                        salir = True
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_SPACE:
                        iniciar = True
                        self.pelota1.flag_inicio = False
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_p:
                        if pausar == False:
                            pausar = True
                        else:
                            pausar = False
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_r:
                        # reiniciar = True
                        iniciar = False
                        self.pelota1.flag_inicio = True

                estado_teclado = pygame.key.get_pressed()
                if estado_teclado[pygame.K_a]:
                    self.jugador1.muevete(Jugador.SUBIR)
                if estado_teclado[pygame.K_z]:
                    self.jugador1.muevete(Jugador.BAJAR)
                if estado_teclado[pygame.K_j]:
                    self.jugador2.muevete(Jugador.SUBIR)
                if estado_teclado[pygame.K_m]:
                    self.jugador2.muevete(Jugador.BAJAR)
                """
                    elif evento.key == pygame.K_a:
                        self.jugador1.muevete(Jugador.SUBIR)
                    elif evento.key == pygame.K_z:
                        self.jugador1.muevete(Jugador.BAJAR)
                    elif evento.key == pygame.K_UP:
                        self.jugador2.muevete(Jugador.SUBIR)
                    elif evento.key == pygame.K_DOWN:
                        self.jugador2.muevete(Jugador.BAJAR)
                """
            self.pantalla.fill((0, 100, 0))
            # pygame.draw.lines(self.pantalla,C_BLANCO,
            # True,[(ANCHO/2-1,0),(ANCHO/2-1,ALTO/8),(ANCHO/2-1,ALTO*1/4),(ANCHO/2-1,ALTO/4),
            # (ANCHO/2-1,),(ANCHO/2-1,)],2)

            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)
            # self.pelota1.pintame(self.pantalla)
            # self.pelota1.mover()
            # self.pelota1.colisionar(self.jugador1)
            # self.pelota1.colisionar(self.jugador2)
            if iniciar == True:
                self.pelota1.pintame(self.pantalla)
                if pausar == False:
                    self.pelota1.mover()
                self.pelota1.colisionar(self.jugador1)
                self.pelota1.colisionar(self.jugador2)
                # self.pinta_pelota()
            # self.pelota1.comprobar_punto()
            jugador_que_puntua = self.pelota1.comprobar_punto()

            if jugador_que_puntua > 0:
                # self.marcador.puntuacion[jugador_que_puntua-1] += 1
                # print(f"El marcador ahora es: {self.marcador.puntuacion}")
                self.marcador.sumar_punto(jugador_que_puntua)

            self.pinta_red()
            # if reiniciar:
            #    reiniciar = False
            # for red_y in range(MARGEN,ALTO-MARGEN,TRAMO_PINTADO+TRAMO_VACIO):
            #    pygame.draw.line(self.pantalla,C_BLANCO,((ANCHO-ANCHO_LINEA)/2,red_y),
            #    ((ANCHO-ANCHO_LINEA)/2,red_y+TRAMO_PINTADO),ANCHO_LINEA)

            """
            pygame.draw.rect(
                .

                self.pantalla, C_BLANCO, 
                pygame.Rect(
                    MARGEN_LATERAL,
                    ALTO/2 - ALTO_PALETA/2,
                    ANCHO_PALETA,
                    ALTO_PALETA)
            )
            #pygame.display.flip()
            pygame.draw.rect(
                self.pantalla, C_BLANCO, 
                pygame.Rect(
                    ANCHO-MARGEN_LATERAL-ANCHO_PALETA,
                    ALTO/2 - ALTO_PALETA/2,
                    ANCHO_PALETA,
                    ALTO_PALETA)
            )
            """
            pygame.display.flip()
            self.reloj.tick(60)

    def pinta_pelota(self):
        # if pausar == False:
        self.pelota1.mover()
        if self.pelota1.colliderect(self.jugador1) or self.pelota1.colliderect(self.jugador2):
            self.pelota1.velocidad_x = - \
                self.pelota1.velocidad_x + randint(-2, 2)
            self.pelota1.velocidad_y = randint(-VEL_MAX, VEL_MAX)
        self.pelota1.pintame(self.pantalla)

    def pinta_red(self):
        TRAMO_PINTADO = 15
        TRAMO_VACIO = 5
        ANCHO_LINEA = 4
        for red_y in range(MARGEN, ALTO-MARGEN, TRAMO_PINTADO+TRAMO_VACIO):
            pygame.draw.line(self.pantalla, C_BLANCO, ((ANCHO-ANCHO_LINEA)/2, red_y),
                             ((ANCHO-ANCHO_LINEA)/2, red_y+TRAMO_PINTADO), ANCHO_LINEA)


if __name__ == "__main__":
    reiniciar = False
    juego = Pong()
    juego.bucle_princiapal()
