import pygame, sys

#INICIO - Dibujar con ciclos

#Definir colores
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red   = ( 255,   0,   0)
blue  = (   0,   0, 255)

size = (800, 500)

screen = pygame.display.set_mode(size)

#Controlar Frames Per Second (FPS)
clock = pygame.time.Clock()

cord_x = 400
cord_y = 200

#velocidad de movimiento
speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #### -------- LÓGICA
    #Cuando llegue al borde se devuelve
    if (cord_x > 720 or cord_x < 0):
        speed_x *= -1
    if (cord_y > 420 or cord_y < 0):
        speed_y *= -1
    
    cord_x += speed_x
    cord_y += speed_y
    #### -------- LÓGICA

    #Color de fondo
    screen.fill(white)

    ### -------- ZONA DE DIBUJO
    pygame.draw.rect(screen, red, (cord_x,cord_y,80,80))
    

    #CICLOS CON DIBUJOS    
    #for x in range(100, 700, 100): #Inicia en 100 hasta 700 sando saltos de 100
    #    for y in range(100, 500, 100):
    #        pygame.draw.rect(screen , black, (x, y, 50, 50)) #Repartirlos en x a la altura 230 y con dimesiones 50*50
    #        pygame.draw.line(screen, green, (x,y), (x, y+100), 5)#Dibujar línea dónde, el color, donde inicia y finaliza, y grosor       

    #DIBUJAR
    #pygame.draw.line(screen, green, [0,100], [100,300], 5)#Dibujar línea dónde, el color, y donde inicia y finaliza, y grosor
    #pygame.draw.rect(screen, black, (100,100,80,80))#Cuadrado. Punto de inicio (x: 100,y: 100), y 80 de ancho y alto.
    #pygame.draw.circle(screen, red, (200,200), 30)
    
    ### -------- ZONA DE DIBUJO

    #Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)