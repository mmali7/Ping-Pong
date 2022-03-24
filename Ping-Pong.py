import turtle

# Screen
wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(height=600, width=800)
wind.tracer(0)  # no update and you can control update

# madrab1
madr1 = turtle.Turtle()
madr1.shape("square")
madr1.speed(0)
madr1.color("blue")
madr1.penup()  # stops the object from drawing lines
madr1.goto(370, 0)  # the position
madr1.shapesize(stretch_wid=5, stretch_len=1)
# madrab2
madr2 = turtle.Turtle()
madr2.shape("square")
madr2.speed(0)
madr2.color("red")
madr2.penup()
madr2.goto(-370, 0)
madr2.shapesize(stretch_wid=5, stretch_len=1)
# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.50
ball.dy = 0.50


# functions
def madr1_up():
    y = madr1.ycor()  # get the y of the object
    y += 20
    madr1.sety(y)  # put the new y


def madr1_down():
    y = madr1.ycor()
    y -= 20
    madr1.sety(y)


def madr2_up():
    y = madr2.ycor()
    y += 20
    madr2.sety(y)


def madr2_down():
    y = madr2.ycor()
    y -= 20
    madr2.sety(y)


# keyboard bindings
wind.listen()  # tell the window to expect input
wind.onkeypress(madr1_up, "Up")  # add button
wind.onkeypress(madr1_down, "Down")
wind.onkeypress(madr2_up, "w")
wind.onkeypress(madr2_down, "s")
# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.color("white")
score.speed(0)
score.penup()
score.goto(0, 260)
score.hideturtle()
score.write("Player 1:0    ||   Player 2: 0", align="center", font=("Arial", 20, "normal"))

# up border
up_bordere = turtle.Turtle()
up_bordere.color("white")
up_bordere.shape("square")
up_bordere.shapesize(0.1, 40)
up_bordere.penup()
up_bordere.goto(0, -300)
# up border
down_bordere = turtle.Turtle()
down_bordere.color("white")
down_bordere.shape("square")
down_bordere.shapesize(0.1, 40)
down_bordere.penup()
down_bordere.goto(0, 300)

# main game loop
while True:
    wind.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)  # increase dx everytime the loop run
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:  # top
        ball.sety(290)
        ball.dy *= -1  # reverse
    if ball.ycor() < -290:  # bottom
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:  # right
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {}   ||   Player 2: {}".format(score1, score2), align="center",
                    font=("Arial", 20, "normal"))
    if ball.xcor() < -390:  # lift
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {}   ||   Player 2: {}".format(score1, score2), align="center",
                    font=("Arial", 20, "normal"))

    if (340 < ball.xcor() > 350) and (
            madr1.ycor() + 40 > ball.ycor() > madr1.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() < -350) and (
            madr2.ycor() + 40 > ball.ycor() > madr2.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    if madr1.ycor() > 240:
        madr1.sety(240)

    if madr1.ycor() < -240:
        madr1.sety(-240)
    if madr2.ycor() > 240:
        madr2.sety(240)

    if madr2.ycor() < -240:
        madr2.sety(-240)
