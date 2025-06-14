import pygame
import random

pygame.init()

sfondo = pygame.image.load('immagini/sfondo.png')
uccello = pygame.image.load('immagini/uccello.png')
base = pygame.image.load('immagini/base.png')
gameover = pygame.image.load('immagini/gameover.png')
tubo_giu = pygame.image.load('immagini/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)

Schermo = pygame.display.set_mode((288, 512))
pygame.display.set_caption("Flappy Bird")
FPS = 50
vel_avanz = 3
Font = pygame.font.SysFont("Arial", 60, bold=True, italic=False)

class tubi_classe:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75,150)
    def avanza_e_disegna(self):
        self.x -= vel_avanz
        Schermo.blit(tubo_giu, (self.x,self.y+210))
        Schermo.blit(tubo_su, (self.x,self.y-210))
    def collisione(self, uccello, uccellox, uccelloy):
        tolleranza = 5
        uccello_lato_dx = uccellox+uccello.get_width()-tolleranza
        uccello_lato_sx = uccellox+tolleranza
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x
        uccello_lato_su = uccelloy+tolleranza
        uccello_lato_giu = uccelloy+uccello.get_height()-tolleranza
        tubi_lato_su = self.y+110
        tubi_lato_giu = self.y+210
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                hai_perso()
    def fra_i_tubi(self, uccello, uccellox):
        tolleranza = 5
        uccello_lato_dx = uccellox+uccello.get_width()-tolleranza
        uccello_lato_sx = uccellox+tolleranza
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            return True

def disegna_oggetti():
    Schermo.blit(sfondo, (0,0))
    for t in tubi:
        t.avanza_e_disegna()
    Schermo.blit(uccello, (uccellox,uccelloy))
    Schermo.blit(base, (basex,400))
    punti_render = Font.render(str(punti), 1, (255,255,255))
    Schermo.blit(punti_render, (144,0))

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)


def inizializza():
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi
    global punti
    global fra_i_tubi
    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    basex = 0
    tubi = []
    tubi.append(tubi_classe())
    punti = [] 
    fra_i_tubi = False

def hai_perso():
    Schermo.blit(gameover, (50,180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()

inizializza()

while True:
    basex -= vel_avanz
    if basex < -45: basex = 0
    uccello_vely += 1
    uccelloy += uccello_vely
    for event in pygame.event.get():
        if ( event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE):
            uccello_vely = -10
        if event.type == pygame.QUIT:
            pygame.quit()
    if tubi[-1].x < 150: tubi.append(tubi_classe())
    for t in tubi:
        t.collisione(uccello, uccellox, uccelloy)
    if not fra_i_tubi:
        for t in tubi:
            if t.fra_i_tubi(uccello, uccellox):
                fra_i_tubi = True
                break
    if fra_i_tubi:
        fra_i_tubi = False
        for t in tubi:
            if t.fra_i_tubi(uccello, uccellox):
                fra_i_tubi = True
                break
        if not fra_i_tubi:
            punti += 1
    if uccelloy > 385 :
        hai_perso()

    disegna_oggetti()
    aggiorna() 