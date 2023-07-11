import turtle

wn = turtle.Screen()
wn.title("Ping-Pong by @Me")
wn.bgcolor("black")
wn.setup(width=800, height=600)
canvas = wn.getcanvas()

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Speed of animation seted to maximum
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)#50 pixeles de alto y 10 de ancho
paddle_a.penup()
paddle_a.goto(-350,0)

#Padde B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #Speed of animation seted to maximum
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)#50 pixeles de alto y 10 de ancho
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #Speed of animation seted to maximum
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 5 #Everytime moves 5 pixels
ball.dy = -5 #Everytime moves 5 pixels

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 - Player B: 0", align="center", font=("Courier",16,"normal"))

#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w") #When pressed "w" paddle_a_up occurres
wn.onkeypress(paddle_a_down, "s") #When pressed "s" paddle_a_down occurres
wn.onkeypress(paddle_b_up, "Up") #When pressed "Up" paddle_b_up occurres
wn.onkeypress(paddle_b_down, "Down") #When pressed "Down" paddle_b_down occurres

#Main game loop
while True:
    wn.update()

    #Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Vertical border checking
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1
    
    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
    
    #Horizontal border checking
    if ball.xcor() > 385:
        ball.goto(0,0) #If touches left or right of the sreen, goes to initial positionw
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} - Player B: {}".format(score_a,score_b), align="center", font=("Courier",16,"normal"))

    if ball.xcor() < -385:
        ball.goto(0,0) #If touches left or right of the sreen, goes to initial positionw
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} - Player B: {}".format(score_a,score_b), align="center", font=("Courier",16,"normal"))
    
    #Paddle collisions checking
    if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1

    if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1