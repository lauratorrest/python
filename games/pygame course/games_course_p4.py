import pygame, sys
pygame.init()

#Animaciones de Teclado

white = ( 255, 255, 255)
red   = ( 255,   0,   0)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)#No ver le mouse. Si es 1, se ve

cord_x = 10
cord_y = 10
x_speed = 0
y_speed = 0

while True:
    for event in pygame.event.get():
        #Si le damos a cerrar, el programa se cierra
        if event.type == pygame.QUIT:
            sys.exit()
    
        #Eventos teclado (debe ir en el for)
        if event.type == pygame.KEYDOWN: #Cuando se unde la tecla
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3

        if event.type == pygame.KEYUP: #Cuando se deja de undir
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0

    screen.fill(white)

    cord_x += x_speed
    cord_y += y_speed
    
    pygame.draw.rect(screen, red, (cord_x,cord_y,100,100))

    pygame.display.flip()
    clock.tick(60)