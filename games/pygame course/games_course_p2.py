import pygame, sys, random
pygame.init()

#Animaciones Parte 1

white = ( 255, 255, 255)
red   = ( 255,   0,   0)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

cord_list = []
for i in range(60): #Quiero 60 circulos
    x = random.randint(0 , 800) #Cualquier entero de 0 a 800
    y = random.randint(0, 500) #Cualquier entero de 0 a 500
    cord_list.append([x,y]) #Guarda coordenadas


while True:
    for event in pygame.event.get():
        #Si le damos a cerrar, el programa se cierra
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(white)
    
    for cord in cord_list:
        pygame.draw.circle(screen, red, cord, 2)
        cord[1] += 1
        # Dejan de aparecer desde arriba, así que cuando llenen la pantalla se vuelve 0 e inicia otra vez
        if cord[1] > 500:
            cord[1] = 0

    pygame.display.flip()
    clock.tick(60)