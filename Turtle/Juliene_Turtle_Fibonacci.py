import turtle
import math


def draw_spiral_plot(a, b):
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()
    x.pencolor("red")

    # Fibonacci Spiral Plot
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b


def draw_other_squares(square_a, square_b):
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        #Fibonacci
        temp = square_b
        square_b = square_b + square_a
        square_a = temp


def draw_first_square(b):
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)


def fiboPlot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    x.pencolor("blue")

    draw_first_square(b)

    #Fibonacci
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    draw_other_squares(square_a, square_b)

    draw_spiral_plot(a, b)


#Main
factor = 1
n = int(input('Enter the number of iterations (must be > 1): '))
# Plotting the Fibonacci Spiral Fractal
if n > 0:
    print("Fibonacci series for", n, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    fiboPlot(n)
    turtle.done()
else:
    print("Number of iterations must be > 0")