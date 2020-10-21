import turtle

t = turtle.Turtle()


def draw_square(side):
    c = 4
    while c > 0:
        t.forward(side)
        t.left(90)
        c -= 1


def jump_square(side):
    t.forward(side - 10)
    t.left(90)
    t.penup()
    t.forward(10)
    t.pendown()


def draw(side):
    while side > 0:
        draw_square(side)
        jump_square(side)
        side -= 20


side = int(input('Tamanho do quadrado: '))

draw(side)


turtle.done()
