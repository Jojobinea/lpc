import turtle
import os
import functools


# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


def draw_paddle(position):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(position, 0)

    return paddle


# draw paddle
paddles = [draw_paddle(-350), draw_paddle(350)]

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3.5
ball.dy = 3.5

# score
score_1 = 0
score_2 = 0

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def paddle_up(paddle):
    y = paddles[paddle].ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddles[paddle].sety(y)


def paddle_down(paddle):
    y = paddles[paddle].ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddles[paddle].sety(y)


def wall_score(score):
    score += 1
    hud.clear()
    hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
    os.system("afplay 258020_kodack_arcade-bleep-4sound.wav&")
    ball.goto(0, 0)
    ball.dx *= -1
    return score


# keyboard
screen.listen()
screen.onkeypress(functools.partial(paddle_up, 0), "w")
screen.onkeypress(functools.partial(paddle_down, 0), "s")
screen.onkeypress(functools.partial(paddle_up, 1), "Up")
screen.onkeypress(functools.partial(paddle_down, 1), "Down")


def collision_with_paddle(position, position_2, paddle):
    if position > ball.xcor() > position_2 and paddles[paddle].ycor() + 50 > ball.ycor() > paddles[0].ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")


def ball_movement():
    global score_1, score_2
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with the upper wall
    if ball.ycor() > 290:
        os.system("afplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1

    # collision with lower wall
    if ball.ycor() < -290:
        os.system("afplay bounce.wav&")
        ball.sety(-290)
        ball.dy *= -1

    # collision with left wall
    if ball.xcor() < -380:
        score_1 = wall_score(score_1)

    # collision with right wall
    if ball.xcor() > 380:
        score_2 = wall_score(score_2)

    # collision with the paddle 1
    collision_with_paddle(-330, -335, 0)

    # collision with the paddle 2
    collision_with_paddle(335, 330, 1)

    screen.ontimer(ball_movement, 2)


ball_movement()
screen.mainloop()
