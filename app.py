import turtle

# Game Window
wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)


# Game Objects

# paddle1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

# paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))


# functions
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


# keyboard bindings
wind.listen()
wind.onkeypress(paddle1_up, "s")
wind.onkeypress(paddle1_down, "w")
wind.onkeypress(paddle2_up, "Up")
wind.onkeypress(paddle2_down, "Down")

# main game loop
while True:
    wind.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # collision between ball and paddles
    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
