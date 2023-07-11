import pygame, sys
pygame.init()

#Animaciones Parte 2

white = ( 255, 255, 255)
red   = ( 255,   0,   0)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)#No ver le mouse. Si es 1, se ve

while True:
    for event in pygame.event.get():
        #Si le damos a cerrar, el programa se cierra
        if event.type == pygame.QUIT:
            sys.exit()
    
    #Primero se hace lógica y luego se hace el fill

    mouse_pos = pygame.mouse.get_pos() # Mouse position (x,y)
    x = mouse_pos[0]
    y = mouse_pos[1]
    screen.fill(white)
    
    pygame.draw.rect(screen, red, (x,y,100,100))

    pygame.display.flip()
    clock.tick(60)