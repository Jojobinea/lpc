import turtle


def draw_triangle(x, y):
    tess.penup()
    tess.goto(x, y)
    tess.pendown()

    for i in range(3):
        tess.forward(100)
        tess.left(120)
        tess.forward(100)


wn = turtle.Screen()
tess = turtle.Turtle()
turtle.onscreenclick(draw_triangle, 1)
turtle.listen()

turtle.done()