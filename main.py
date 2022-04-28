
# imports turtle module (basic graphics)
import turtle

# screen object
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# ------left Paddle-------
p_left = turtle.Turtle()
p_left.speed(0)
p_left.shape("square")
p_left.color("white")

# A turtle, when it moves, draws a line. In order to not have it
# draw a line, use penup
p_left.penup()

# x and y coordinates for where the left paddle should be. Coordinate
# system has (0, 0) in the middle.
p_left.goto(-350, 0)

# By default, the square has a size of 20x20 pixels. Change it to be paddle.
p_left.shapesize(stretch_wid=5, stretch_len=1)


# ------Right Paddle-------
p_right = turtle.Turtle()
p_right.speed(0)
p_right.shape("square")
p_right.color("white")
p_right.penup()
p_right.goto(350, 0)
p_right.shapesize(stretch_wid=5, stretch_len=1)


# -----ball------
ball = turtle.Turtle()

# animation speed
ball.speed(0)

ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# movement of ball in the x and y direction
ball.dx = 2
ball.dy = -2


# -----Score variables-----
score_a = 0
score_b = 0


# ----Pen----
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# ------move left paddle up------
def left_up():
    # ycor from turtle module and we're assigning that to a variable (just calling it y)
    y = p_left.ycor()

    # When paddle moves up, its y coordinate will increase by 20
    y += 40

    # the y position of y will now have been increased by 20
    p_left.sety(y)


# ------move left paddle down------
def left_down():
    # ycor from turtle module and we're assigning that to a variable (just calling it y)
    y = p_left.ycor()

    # When paddle moves up, its y coordinate will increase by 20
    y -= 40

    # the y position of y will now have been increased by 20
    p_left.sety(y)


# ------move right paddle up------
def right_up():
    # ycor from turtle module and we're assigning that to a variable (just calling it y)
    y = p_right.ycor()

    # When paddle moves up, its y coordinate will increase by 20
    y += 40

    # the y position of y will now have been increased by 20
    p_right.sety(y)


# ------move right paddle down------
def right_down():
    # ycor from turtle module and we're assigning that to a variable (just calling it y)
    y = p_right.ycor()

    # When paddle moves up, its y coordinate will increase by 20
    y -= 40

    # the y position of y will now have been increased by 20
    p_right.sety(y)


# -----keyboard binding--------
# tells the program to "listen" for keyboard input
wn.listen()
wn.onkeypress(left_up, "w")
wn.onkeypress(left_down, "s")
wn.onkeypress(right_up, "i")
wn.onkeypress(right_down, "k")


# main game loop
while True:
    wn.update()

    # Moves the ball. The screen is constantly updating because of "while True". This will
    # always be true. Since it's constantly updating, the 2 (from ball.dx) is constantly being
    # added to the x and y coordinates of the ball, giving the illusion of movement. Like a
    # flip book.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for when ball hits top. If y coordinate is greater than 290, then
    # reverse direction
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Border checking for when ball hits bottom. If y coordinate is less than -280, then
    # reverse direction
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    # Border checking for when ball hits right side. If x coordinate is greater than 290, then
    # the ball returns to the center
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Border checking for when ball hits left. If x coordinate is less than -390, then
    # the ball returns to the center
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # collision for right paddle
    if ball.xcor() == p_right.xcor() - 20 and ((ball.ycor() < p_right.ycor() + 50) and (ball.ycor() > p_right.ycor() - 50)):
        ball.dx *= -1

    # collision for left paddle
    if ball.xcor() == p_left.xcor() + 20 and ((ball.ycor() < p_left.ycor() + 50) and (ball.ycor() > p_left.ycor() - 50)):
        ball.dx *= -1