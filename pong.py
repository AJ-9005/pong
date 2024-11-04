import turtle
wn = turtle.Screen()
wn.title("Pong by @aj__9005")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.penup()
paddle_A.goto(-350, 0)
paddle_A.shapesize(stretch_wid=5, stretch_len=1)

paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.penup()
paddle_B.goto(350, 0)
paddle_B.shapesize(stretch_wid=5, stretch_len=1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.07
ball.dy = 0.07

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def  paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def  paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def  paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def  paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

wn.listen()
wn.onkeypress(paddle_A_up, "w")
wn.onkeypress(paddle_A_down, "s")
wn.onkeypress(paddle_B_up, "Up")
wn.onkeypress(paddle_B_down, "Down")
points_A = 0
points_B = 0
pen.write(f"Left: {points_A} Right: {points_B}",  align="center", font=("Courier", 24, "normal"))

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if paddle_A.ycor() > 250:
        paddle_A.sety(250)
    if paddle_A.ycor() < -250:
        paddle_A.sety(-250)
    if paddle_B.ycor() > 250:
        paddle_B.sety(250)
    if paddle_B.ycor() < -250:
        paddle_B.sety(-250)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        points_A += 1
        pen.clear()
        pen.write(f"Left: {points_A} Right: {points_B}",  align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        points_B += 1
        pen.clear()
        pen.write(f"Left: {points_A} Right: {points_B}",  align="center", font=("Courier", 24, "normal"))
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if (-350 <= ball.xcor() <= -340) and ((paddle_A.ycor() - 50) <= ball.ycor() <= (paddle_A.ycor() + 50)):
        ball.dx *= -1
    
    if (340 <= ball.xcor() <= 350) and ((paddle_B.ycor() - 50) <= ball.ycor() <= (paddle_B.ycor() + 50)):
        ball.dx *= -1