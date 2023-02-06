import pygame

ANCHO = 640
ALTO = 480
C_BLANCO = (255,255,255)

ANCHO_PALETA = 5
ALTO_PALETA  = 50
MARGEN_LATERAL = 40
TAM_PELOTA = 10
MARGEN=25

class Jugador():
    def __init__(self, pos_x, pos_y):
        self.rectangulo = pygame.Rect(pos_x,pos_y,ANCHO_PALETA,ALTO_PALETA)
    def pintame(self,pantalla):
        pygame.draw.rect(pantalla, C_BLANCO, self.rectangulo)

class Pelota():
    def __init__(self,x,y):
        self.rectangulo = pygame.Rect(x,y,TAM_PELOTA,TAM_PELOTA)
    def pintame(self,pantalla):
        pygame.draw.rect(pantalla, C_BLANCO, self.rectangulo)






class Pong():
    def __init__(self):
        #print("Construyendo un objeto de la calse Pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO,ALTO))
        pos_y = (ALTO -ALTO_PALETA)/2
        pos_x_2 = ANCHO - MARGEN_LATERAL-ANCHO_PALETA
        self.jugador1 = Jugador( MARGEN_LATERAL, pos_y)
        self.jugador2 = Jugador( pos_x_2, pos_y)
        self.pelota1 = Pelota(ANCHO/2-TAM_PELOTA/2,ALTO/2-TAM_PELOTA/2)

    
    def bucle_princiapal(self):
        #TRAMO_PINTADO=15
        #TRAMO_VACIO=5
        #ANCHO_LINEA=4
        #print("Estoy en el bucle principal")
        salir = False
        while not salir:
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
                if evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE:
                    salir = True
            
            self.pantalla.fill((0,100,0))
            #pygame.draw.lines(self.pantalla,C_BLANCO,
            #True,[(ANCHO/2-1,0),(ANCHO/2-1,ALTO/8),(ANCHO/2-1,ALTO*1/4),(ANCHO/2-1,ALTO/4),
            #(ANCHO/2-1,),(ANCHO/2-1,)],2)
                    
            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)
            self.pelota1.pintame(self.pantalla)
            self.pinta_red()

            #for red_y in range(MARGEN,ALTO-MARGEN,TRAMO_PINTADO+TRAMO_VACIO):
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
    def pinta_red(self):
        TRAMO_PINTADO=15
        TRAMO_VACIO=5
        ANCHO_LINEA=4
        for red_y in range(MARGEN,ALTO-MARGEN,TRAMO_PINTADO+TRAMO_VACIO):
                pygame.draw.line(self.pantalla,C_BLANCO,((ANCHO-ANCHO_LINEA)/2,red_y),
                ((ANCHO-ANCHO_LINEA)/2,red_y+TRAMO_PINTADO),ANCHO_LINEA)
                
if __name__ == "__main__":
    juego = Pong()
    juego.bucle_princiapal()

