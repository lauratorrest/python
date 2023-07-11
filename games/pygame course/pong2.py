import pygame, sys
pygame.init()

black = (  0,   0,   0)
white = (255, 255, 255)

size = (800,600)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

players_width = 15
players_height = 90

player1_x_cord = 50
player1_y_cord = 300 - 45
player1_y_speed = 0

player2_x_cord = 750 - players_width
player2_y_cord = 300 - 45
player2_y_speed = 0

ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3
##Se le dan valores predeterminados a lo que se moverá solo

score_p1 = 0
score_p2 = 0

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        if event.type == pygame.KEYDOWN:
            #JUGADOR 1
            if event.key == pygame.K_w:
                player1_y_speed = -3 #Para que suba
            if event.key == pygame.K_s:
                player1_y_speed = 3 #Para que baje
            
            #JUGADOR 2
            if event.key == pygame.K_UP:
                player2_y_speed = -3 #Para que suba
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3 #Para que baje

        if event.type == pygame.KEYUP:
            #JUGADOR 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            
            #JUGADOR 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0


    if ball_y > 590 or ball_y < 10:
        ball_speed_y *= -1
    if ball_x < 10:
        score_p2 += 1
        print("p1: ",score_p1," p2: ",score_p2)
        ball_x = 400
        ball_y = 300
    if ball_x > 790:
        score_p1 += 1
        print("p1: ",score_p1," - p2: ",score_p2)
        ball_x = 400
        ball_y = 300
    if (ball_x > player2_x_cord-10) and (ball_y > player2_y_cord and ball_y < player2_y_cord+players_height):
        ball_speed_x *= -1
    if (ball_x < player1_x_cord+20) and (ball_y > player1_y_cord and ball_y < player1_y_cord+players_height):
        ball_speed_x *= -1

    # MOVIMIENTO
    player1_y_cord += player1_y_speed
    player2_y_cord += player2_y_speed
    # MOVIMIENTO PELOTA
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    screen.fill(black)

    # --------- ZONA DE DIBUJO

    player1 = pygame.draw.rect(screen,white,(player1_x_cord, player1_y_cord, players_width, players_height))
    player2 = pygame.draw.rect(screen,white,(player2_x_cord, player2_y_cord, players_width, players_height))
    ball = pygame.draw.circle(screen, white, (ball_x,ball_y), 10)

    # --------- ZONA DE DIBUJO

    pygame.display.flip()
    clock.tick(60)