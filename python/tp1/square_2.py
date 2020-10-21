import turtle

t = turtle.Turtle()


def draw_square(side):
    c = 4
    while c > 0:
        t.forward(side)
        t.left(90)
        c -= 1

    turtle.done()


side = int(input('Digite o tamanho do lado: '))

draw_square(side)
