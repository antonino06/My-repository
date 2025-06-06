
import pygame
import random

# Inizializzazione pygame
pygame.init()

# Colori
bianco = (255, 255, 255)
azzurro = (52, 143, 235)

# Creazione finestra di gioco
larghezza_finestra = 800
altezza_finestra = 600

finestra = pygame.display.set_mode((larghezza_finestra, altezza_finestra))
pygame.display.set_caption("Pong")

# Controllo degli FPS
clock = pygame.time.Clock()
fps = 60

# Creazione delle racchette
larghezza_racchetta = 15
altezza_racchetta = 100
velocita_racchetta = 5

racchetta_sinistra = pygame.Rect(50, altezza_finestra // 2 - altezza_racchetta // 2,
                                 larghezza_racchetta, altezza_racchetta)

racchetta_destra = pygame.Rect(larghezza_finestra - 50 - larghezza_racchetta,
                               altezza_finestra // 2 - altezza_racchetta // 2,
                               larghezza_racchetta, altezza_racchetta)

# Creazione della palla
dimensione_palla = 20
velocita_palla_x = 5
velocita_palla_y = 5

palla = pygame.Rect(larghezza_finestra // 2 - dimensione_palla // 2,
                    altezza_finestra // 2 - dimensione_palla // 2,
                    dimensione_palla,
                    dimensione_palla)

# Punteggio
punteggio = 0
font = pygame.font.SysFont("Arial", 60, bold=True, italic=False)

# Funzione per disegnare gli oggetti sullo schermo
def disegna_oggetti():
    finestra.fill(azzurro)
    pygame.draw.rect(finestra, bianco, racchetta_sinistra)
    pygame.draw.rect(finestra, bianco, racchetta_destra)
    pygame.draw.ellipse(finestra, bianco, palla)

    testo = font.render(str(punteggio), True, bianco)
    finestra.blit(testo, (larghezza_finestra // 2 - testo.get_width() // 2, 60))

# Ciclo infinito
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Movimento delle racchette
    tasti = pygame.key.get_pressed()
    if tasti[pygame.K_w]:
        racchetta_sinistra.y -= velocita_racchetta
    if tasti[pygame.K_s]:
        racchetta_sinistra.y += velocita_racchetta
    if tasti[pygame.K_UP]:
        racchetta_destra.y -= velocita_racchetta
    if tasti[pygame.K_DOWN]:
        racchetta_destra.y += velocita_racchetta

    # Movimento della palla
    palla.x += velocita_palla_x
    palla.y += velocita_palla_y

    # La palla collide con i bordi verticali
    if palla.top <= 0 or palla.bottom >= altezza_finestra:
        velocita_palla_y = -velocita_palla_y

    # La palla collide con i bordi orizzontali
    if palla.left <= 0 or palla.right >= larghezza_finestra:
        # Il giocatore perde
        palla.x = larghezza_finestra // 2 - dimensione_palla // 2
        palla.y = altezza_finestra // 2 - dimensione_palla // 2
        
        velocita_palla_x = random.choice([-5, 5])
        velocita_palla_y = random.choice([-5, 5])

        punteggio = 0

    # La palla collide con le racchette
    if palla.colliderect(racchetta_sinistra) or palla.colliderect(racchetta_destra):
        velocita_palla_x = -velocita_palla_x
        punteggio += 1

    disegna_oggetti()

    pygame.display.update()
    clock.tick(fps)
